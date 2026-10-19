%global source0_hash eea7f2fbdcaacbf1097f62f9e4fb50ffd238cec3085b67d384ab0a419274e1da
Name:           usbtop
Version:        1.0
Release:        1%{?dist}
Summary:        Utility to show USB bandwidth
License:        BSD-3-Clause
URL:            https://github.com/aguinet/usbtop
Source0:        https://github.com/aguinet/%{name}/archive/release-%{version}/%{name}-%{version}.tar.gz
Patch:          0001-CMake-4-compatibility.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
usbtop is a top-like utility that shows an estimated instantaneous bandwidth on
USB buses and devices.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n usbtop-release-%{version}
rm -rf third-party

%build

%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build
%install
%cmake_install
install -d %{buildroot}%{_modulesloaddir}
echo usbmon > %{buildroot}%{_modulesloaddir}/usbtop.conf
%if "%{_sbindir}" == "%{_bindir}"
mv -v %{buildroot}/usr/sbin %{buildroot}%{_bindir}
%oreon_autofiles main
%endif
%post

modprobe usbmon &> /dev/null || :
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
