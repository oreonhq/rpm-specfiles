%global source1_hash afbf20de8d26089d6f76d28815b6d66390c125e652cbf7b89026a19697ab519e
%global source0_hash 9c7fa992ed88c535d5beed3dc9c57ba2082805fb404d048e2fa2cdd309c15d7e
%bcond check 0
%global with_bundled 1
%global crate zincati
Name:           rust-zincati
Version:        0.0.32
Release:        1%{?dist}
Summary:        Update agent for Fedora CoreOS
License:        Apache-2.0
URL:            https://crates.io/crates/zincati
Source0:        https://static.crates.io/crates/zincati/zincati-%{version}.crate
Source1:        https://github.com/coreos/%{crate}/releases/download/v%{version}/%{crate}-%{version}-vendor.tar.gz
%if ! 0%{?with_bundled}
%endif
ExcludeArch:    armv7hl i686
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  glib2-devel
BuildRequires:  ostree-devel
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Update agent for Fedora CoreOS
License:        Apache-2.0 AND BSD-3-Clause AND MIT AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR BSD-2-Clause) AND (MIT OR Apache-2.0 OR Zlib) AND (Unlicense OR MIT)
Requires:       polkit
%description -n %{crate}

%post        -n %{crate}

%systemd_post zincati.service
%preun       -n %{crate}

%systemd_preun zincati.service
%postun      -n %{crate}

%systemd_postun_with_restart zincati.service
%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%if 0%{?with_bundled}
%autosetup -N -n %{crate}-%{version} -a1
%else
%autosetup -N -n %{crate}-%{version}
%endif
%autopatch -p1
%if ! 0%{?with_bundled}
%oreon_vendor_cargo
%build

%cargo_build
%{?cargo_license_summary}
%{?cargo_license} > LICENSE.dependencies
%if 0%{?with_bundled}
%{cargo_vendor_manifest}
%endif
%install
%cargo_install
mkdir -p %{buildroot}%{_libexecdir}
mv %{buildroot}%{_bindir}/zincati %{buildroot}%{_libexecdir}/zincati
install -Dpm0755 -t %{buildroot}%{_bindir} dist/bin/zincati-update-now
install -Dpm0644 -t %{buildroot}%{_prefix}/lib/%{crate}/config.d \
  dist/config.d/*.toml
mkdir -p %{buildroot}%{_sysconfdir}/%{crate}/config.d
install -Dpm0644 -t %{buildroot}%{_unitdir} \
  dist/systemd/system/*.service
install -Dpm0644 -t %{buildroot}%{_sysusersdir} \
  dist/sysusers.d/*.conf
install -Dpm0644 -t %{buildroot}%{_tmpfilesdir} \
  dist/tmpfiles.d/*.conf
install -Dpm0644 -t %{buildroot}%{_datadir}/polkit-1/rules.d \
  dist/polkit-1/rules.d/*.rules
install -Dpm0644 -t %{buildroot}%{_datadir}/polkit-1/actions \
  dist/polkit-1/actions/org.coreos.zincati.*
install -Dpm0644 -t %{buildroot}%{_datadir}/dbus-1/system.d \
  dist/dbus-1/system.d/*.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n zincati -f %{oreon_filedir}/zincati.list

%changelog

%autochangelog
%endif
