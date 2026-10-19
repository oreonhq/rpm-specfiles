%global source0_hash ef5c5015e91c4fef6797c4961c400d18e1ae8191a8d1eae6e3512823dd2ff2a8
Name:           quickemu
Version:        4.9.9
Release:        1%{?dist}
Summary:        Quickly create and run optimized Windows, macOS and Linux virtual machines
License:        MIT
URL:            https://github.com/quickemu-project/quickemu
Source0:        https://github.com/%{name}-project/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       bash
Requires:       coreutils
Requires:       curl
Requires:       edk2-tools
Requires:       genisoimage
Requires:       grep
Requires:       jq
Requires:       mesa-demos
Requires:       pciutils
Requires:       procps
Requires:       python3
Requires:       qemu
Requires:       sed
Requires:       socat
Requires:       spice-gtk-tools
Requires:       swtpm
Requires:       unzip
Requires:       usbutils
Requires:       util-linux
Requires:       xdg-user-dirs
Requires:       xrandr
# oreon:deps

# /oreon:deps
%description
Quickly create and run optimized Windows, macOS and Linux virtual machines

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%install
install -Dpm755 chunkcheck %{buildroot}%{_bindir}/chunkcheck
install -Dpm755 quickemu %{buildroot}%{_bindir}/quickemu
install -Dpm755 quickget %{buildroot}%{_bindir}/quickget
install -Dpm755 quickreport %{buildroot}%{_bindir}/quickreport
install -Dpm644 docs/quickemu_conf.5 %{buildroot}%{_mandir}/man5/quickemu_conf.5
install -Dpm644 docs/quickemu.1 %{buildroot}%{_mandir}/man1/quickemu.1
install -Dpm644 docs/quickget.1 %{buildroot}%{_mandir}/man1/quickget.1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
