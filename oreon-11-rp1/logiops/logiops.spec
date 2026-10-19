%global source0_hash c44b34765ca502a3cbbc2c711f5b85770042e1b176f818e03c705d69cab7554e
%global forgeurl https://github.com/PixlOne/logiops
Name:    logiops
Version: 0.3.5
Release:        1%{?dist}
Summary:        Unofficial driver for Logitech mice and keyboard
%forgemeta
License: GPL-3.0-or-later
URL:     %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:  logiops-use-ipcgull-shared-lib.patch
Requires:  ipcgull
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ipcgull-devel
BuildRequires:  libconfig-devel
BuildRequires:  libevdev-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  systemd-udev
# /oreon:deps
%description
This is an unofficial driver for Logitech mice and keyboard.

This is currently only compatible with HID++ >2.0 devices.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup
%patch -p1 0
rmdir src/ipcgull

%conf
%cmake

%build

%{cmake_build}
%install
%{cmake_install}
%oreon_autofiles main

%post

%systemd_post logid.service
%preun

%systemd_preun logid.service
%postun

%systemd_postun_with_restart logid.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
