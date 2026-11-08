# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 659f40c440e31ba865c52c818a33d3ba6a97349e3353f8b1985179cb2aa71ec5

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Name:    usbutils
Version:        019
Release:        1%{?dist}
Summary: Linux USB utilities
URL:     http://www.linux-usb.org/
License: GPL-2.0-or-later

Source0:        https://www.kernel.org/pub/linux/utils/usb/usbutils/usbutils-%{version}.tar.xz

# This adds usbreset binary to the package, but since upstream does not consider it stable, 
# let's not include it in the ELN. https://github.com/gregkh/usbutils/issues/222#issuecomment-2715192013
Patch0:        usbreset.patch

BuildRequires: meson
BuildRequires: gcc
BuildRequires: libusb1-devel
BuildRequires: systemd-devel
BuildRequires:  oreon-rpm-macros
Requires: hwdata

%description
This package contains utilities for inspecting devices connected to a
USB bus.

%prep
%oreon_sha256

%autosetup -p1

%build
%meson --sbindir=%{_sbindir} --datadir=%{_datadir}/hwdata
%meson_build

%install
%meson_install
rm -rf %{buildroot}/%{_libdir}/pkgconfig/usbutils.pc

%files
%license LICENSES/GPL*
%doc NEWS
%{_mandir}/*/*
%{_bindir}/*

