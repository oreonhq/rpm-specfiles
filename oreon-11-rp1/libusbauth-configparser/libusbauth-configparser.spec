%global source0_hash 592b867902fb59ced63fa10f1be2921ff703d231d35f30350288a60a12ca5b8e

#
# spec file for package libusbauth-configparser
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017-2018 Stefan Koch <stefan.koch10@gmail.com>
# Copyright (c) 2015 SUSE LLC. All Rights Reserved.
# Author: Stefan Koch <skoch@suse.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           libusbauth-configparser
Version:        1.0.5
Summary:        Library for USB Firewall including flex/bison parser
URL:            https://github.com/kochstefan/usbauth-all/tree/master/libusbauth-configparser
Source:         https://github.com/kochstefan/usbauth-all/archive/v%{version}.tar.gz

Release:        10%{?dist}
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2

BuildRequires:  pkgconfig(libudev)
BuildRequires:  gcc
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool

%description
Library to read usbauth config file into data structures

%package devel
Summary:        Development part of library for USB Firewall including flex/bison parser
Requires:       libusbauth-configparser%{?_isa} = %{version}-%{release}

%description devel
Development part of library to read usbauth config file into data structures

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n usbauth-all-%{version} -p1

%build
pushd %{name}/
autoreconf -f -i
%configure
%make_build
popd

%install
pushd %{name}/
%make_install
popd

%files
%license %{name}/COPYING
%doc %{name}/README
%_libdir/lib*.so.1*

%files devel
%license %{name}/COPYING
%doc %{name}/README
%doc %_mandir/*/*
%_includedir/*
%_libdir/lib*.so
%_libdir/pkgconfig/*

%ldconfig_post

%ldconfig_postun

%changelog
%autochangelog
