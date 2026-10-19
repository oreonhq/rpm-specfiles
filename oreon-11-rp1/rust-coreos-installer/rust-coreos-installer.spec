%global source0_hash 4d80ee524bc98c032551354e42e80b2f7775684ba601a877211a0f6252796718
%global source1_hash 77a34d1e82e1b8ae3f530b5b23c366b37e566e51291855f48298b88a19b12922
%global source2_hash 14625a64aed36800511570d52759cdfad928021781873e82b94d86685f2e107b
%bcond_without check
%global cargo_install_lib 0
%global dracutlibdir %{_prefix}/lib/dracut
%global dracutcommit 1a0a13fe12508367fffb49fc102dc50932da41ce
%global dracutshortcommit %(c=%{dracutcommit}; echo ${c:0:7})
%global crate coreos-installer
Name:           rust-coreos-installer
Version:        0.26.0
Release:        1%{?dist}
Summary:        Installer for Fedora CoreOS and RHEL CoreOS
License:        Apache-2.0
URL:            https://crates.io/crates/coreos-installer
Source0:        https://static.crates.io/crates/coreos-installer/coreos-installer-%{version}.crate
Source1:        https://github.com/coreos/%{crate}/releases/download/v%{version}/%{crate}-%{version}-vendor.tar.gz
Source2:        https://github.com/coreos/coreos-installer-dracut/archive/%{dracutcommit}/coreos-installer-dracut-%{dracutshortcommit}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  gnupg2
BuildRequires:  libzstd-devel
BuildRequires:  rustc
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Installer for Fedora CoreOS and RHEL CoreOS
License:        Apache-2.0 AND BSD-3-Clause AND MIT AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (Unlicense OR MIT)
Requires:       gnupg
Requires:       kpartx
Requires:       systemd-udev
Requires:       util-linux
%ifarch s390x
Requires:       s390utils-core
%endif
Obsoletes:      coreos-installer-dracut < 0.0.1
%description -n %{crate}

%package     -n %{crate}-bootinfra
Summary:     %{crate} boot-time infrastructure for use on Fedora/RHEL CoreOS
License:        Apache-2.0 AND BSD-3-Clause AND MIT AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (Unlicense OR MIT)
Requires:    %{crate}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:    %{crate}-systemd = %{version}-%{release}
Obsoletes:   %{crate}-systemd <= 0.3.0-3
%description -n %{crate}-bootinfra
This subpackage contains boot-time infrastructure for Fedora CoreOS and
RHEL CoreOS.  It is not needed on other platforms.

%package     -n %{crate}-dracut
Summary:     Dracut module for running coreos-installer in the initrd in IoT/Edge
Requires:    %{crate} = %{version}-%{release}
%description -n %{crate}-dracut
This subpackage contains files and configuration to run coreos-installer
from the initramfs in IoT/Edge and is supported by the community.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -a 2 -p1
%oreon_vendor_cargo
%build

%cargo_build -f rdcore
%{cargo_license_summary -f rdcore}
%{cargo_license -f rdcore} > LICENSE.dependencies
%install
%cargo_install -f rdcore
install -D -m 0755 -t %{buildroot}%{dracutlibdir}/modules.d/50rdcore dracut/50rdcore/module-setup.sh
make install-scripts DESTDIR=%{buildroot}
make install-systemd DESTDIR=%{buildroot}
make install-man DESTDIR=%{buildroot}
make install-data DESTDIR=%{buildroot}
mv %{buildroot}%{_bindir}/rdcore %{buildroot}%{dracutlibdir}/modules.d/50rdcore/
%make_install -C coreos-installer-dracut-%{dracutcommit}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%cargo_test -f rdcore
%endif
%files -f %{oreon_filedir}/main.list
%files -n coreos-installer -f %{oreon_filedir}/coreos-installer.list
%files -n coreos-installer-bootinfra -f %{oreon_filedir}/coreos-installer-bootinfra.list
%files -n coreos-installer-dracut -f %{oreon_filedir}/coreos-installer-dracut.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.26.0-1
- Prepare for Oreon 11 (RP1)
