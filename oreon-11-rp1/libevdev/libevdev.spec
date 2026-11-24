# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5a0966c7110648665983848bad696c7acba614a2160d2865d535397101007332
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libevdev
Version:        1.14.0
Release:        1%{?dist}
Summary:        Kernel Evdev Device Wrapper Library

License:        MIT
URL:            http://www.freedesktop.org/wiki/Software/libevdev
Source0:        https://www.freedesktop.org/software/%{name}/%{name}-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  python3
BuildRequires:  python3-rpm-macros

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
%oreon_sha256
%autosetup -S git
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
%autochangelog
