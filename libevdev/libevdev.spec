Name:           libevdev
Version:        1.13.6
Release:        2%{?dist}
Summary:        Kernel Evdev Device Wrapper Library

# SPDX
License:        MIT
URL:            http://www.freedesktop.org/wiki/Software/libevdev
Source0:        http://www.freedesktop.org/software/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  git-core
BuildRequires:  meson gcc
BuildRequires:  python3 python3-rpm-macros

%description
%{name} is a library to wrap kernel evdev devices and provide a proper API
to interact with those devices.

%package devel
Summary:        Kernel Evdev Device Wrapper Library Development Package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Kernel Evdev Device Wrapper Library Development Package.

%package utils
Summary:        Kernel Evdev Device Wrapper Library Utilities Package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description utils
Utilities to handle and/or debug evdev devices.

%prep
%autosetup -S git
# Replace whatever the source uses with the approved call
%py3_shebang_fix $(git grep -l  '#!/usr/bin/.*python3')

%build
%meson -Dtests=disabled -Ddocumentation=disabled -Dcoverity=false
%meson_build

%install
%meson_install

%ldconfig_scriptlets

%files
%doc COPYING
%{_libdir}/libevdev.so.*

%files devel
%dir %{_includedir}/libevdev-1.0/
%dir %{_includedir}/libevdev-1.0/libevdev
%{_includedir}/libevdev-1.0/libevdev/libevdev.h
%{_includedir}/libevdev-1.0/libevdev/libevdev-uinput.h
%{_libdir}/libevdev.so
%{_libdir}/pkgconfig/libevdev.pc
%{_mandir}/man3/libevdev.3*

%files utils
%{_bindir}/touchpad-edge-detector
%{_bindir}/mouse-dpi-tool
%{_bindir}/libevdev-tweak-device
%{_mandir}/man1/libevdev-tweak-device.1*
%{_mandir}/man1/touchpad-edge-detector.1*
%{_mandir}/man1/mouse-dpi-tool.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.13.6-2
- Prepare for Oreon 11 (RP1)
