%global source0_hash 8558429ce8db0aff88ba6bd7ef8cf12169f0fe87df4800b851003ca43db0a86b
%global source1_hash 9b72cef6c65f9c8a5fd7c69e5280da335de98585e428655125739a160bb98ba8
%bcond_without check
%global dracutmodulesdir %(pkg-config --variable=dracutmodulesdir dracut || echo '/usr/lib/dracut/modules.d')
%global crate afterburn
Name:           rust-afterburn
Version:        5.11.0
Release:        1%{?dist}
Summary:        Simple cloud provider agent
License:        Apache-2.0
URL:            https://crates.io/crates/afterburn
Source0:        https://crates.io/api/v1/crates/afterburn/5.11.0/download#/afterburn-5.11.0.crate
Source1:        https://github.com/coreos/%{crate}/releases/download/v%{version}/%{crate}-%{version}-vendor.tar.gz
Source2:        90-afterburn-authorized-keys-file.conf
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(dracut)
BuildRequires:  rustc
BuildRequires:  systemd
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Simple cloud provider agent
License:        Apache-2.0 AND 0BSD AND BSD-3-Clause AND MIT AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (MPL-2.0 OR MIT OR Apache-2.0) AND (Unlicense OR MIT) AND Zlib
%{?systemd_requires}
%description -n %{crate}

%post        -n %{crate}

%systemd_post afterburn.service
%systemd_post afterburn-checkin.service
%systemd_post afterburn-firstboot-checkin.service
%systemd_post afterburn-sshkeys@.service
%preun       -n %{crate}

%systemd_preun afterburn.service
%systemd_preun afterburn-checkin.service
%systemd_preun afterburn-firstboot-checkin.service
%systemd_preun afterburn-sshkeys@.service
%postun      -n %{crate}

%systemd_postun afterburn.service
%systemd_postun afterburn-checkin.service
%systemd_postun afterburn-firstboot-checkin.service
%systemd_postun afterburn-sshkeys@.service
%package     -n %{crate}-dracut
Summary:        Dracut modules for afterburn
BuildRequires:  pkgconfig(dracut)
Requires:       %{crate}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       dracut
Requires:       dracut-network
%description -n %{crate}-dracut
Dracut module that enables afterburn and corresponding services
to run in the initramfs on boot.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version_no_tilde} -p1
sed -e 's,@DEFAULT_INSTANCE@,core,' < \
systemd/afterburn-sshkeys@.service.in > \
systemd/afterburn-sshkeys@.service
%oreon_vendor_cargo
%build

%cargo_build
%{?cargo_license_summary}
%{?cargo_license} > LICENSE.dependencies
%install
%cargo_install
install -Dpm0644 -t %{buildroot}%{_unitdir} \
  systemd/*.service systemd/*.target
mkdir -p %{buildroot}%{dracutmodulesdir}
cp -a dracut/* %{buildroot}%{dracutmodulesdir}
install -d -p %{buildroot}%{_sysconfdir}/ssh/sshd_config.d/
install -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/ssh/sshd_config.d/90-afterburn-authorized-keys-file.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n afterburn -f %{oreon_filedir}/afterburn.list
%files -n afterburn-dracut -f %{oreon_filedir}/afterburn-dracut.list

%changelog

%autochangelog
