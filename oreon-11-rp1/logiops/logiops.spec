%global source0_hash c44b34765ca502a3cbbc2c711f5b85770042e1b176f818e03c705d69cab7554e

%global forgeurl https://github.com/PixlOne/logiops

Name:    logiops
Version: 0.3.5
Release: 6%{?dist}
Summary: Unofficial driver for Logitech mice and keyboard
%forgemeta

License: GPL-3.0-or-later
URL:     %{forgeurl}

Source0:  %{forgesource}

# Change from static to dynamic lib
Patch0:  logiops-use-ipcgull-shared-lib.patch

Requires:  ipcgull

BuildRequires:  cmake
BuildRequires:  systemd-devel
BuildRequires:  systemd-udev
BuildRequires:  systemd-rpm-macros
BuildRequires:  libconfig-devel
BuildRequires:  libevdev-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ipcgull-devel

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

%post
%systemd_post logid.service

%preun
%systemd_preun logid.service

%postun
%systemd_postun_with_restart logid.service

%files
%{_bindir}/logid
%{_unitdir}/logid.service
%{_datadir}/dbus-1/system.d/pizza.pixl.LogiOps.conf
%license LICENSE
%doc README.md
%doc TESTED.md
%doc logid.example.cfg

%changelog
%autochangelog
