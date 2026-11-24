# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 57423cf87d09b7d084f420b55b737fe654c33339b06df77945620d97795c6ac4
%global source1_hash 0d20b7ab35aa08a408142439d0e8e36c4a7bc3597503dbc0167821d078955634
%global source2_hash a38721cd3c4e8b60f93d6ee1af0eb8462f50ab20bf6c1d605822e6adf2353c5c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%define srcname dbus_python

Name:    dbus-python
Version: 1.5.1
Release:        %{autorelease}
Summary: D-Bus Python Bindings

License: MIT
URL:     http://www.freedesktop.org/wiki/Software/DBusBindings/
Source0: http://dbus.freedesktop.org/releases/dbus-python/%{srcname}-%{version}.tar.gz
Source1: http://dbus.freedesktop.org/releases/dbus-python/%{srcname}-%{version}.tar.gz.asc
Source2: gpgkey-7A073AD1AE694FA25BFF62E5235C099D3EB33076.gpg

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: openpgpverify
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: dbus-x11
BuildRequires: python3-gobject

BuildRequires: meson

%global _description\
D-Bus python bindings for use with python programs.

%description %_description

%package -n python3-dbus
Summary: D-Bus bindings for python3
%{?python_provide:%python_provide python3-dbus}
BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(setuptools-scm)
BuildRequires: python3dist(pip)
BuildRequires: python3dist(ninja)
BuildRequires: make

%description -n python3-dbus
%{summary}.

%package devel
Summary: Libraries and headers for dbus-python

%description devel
Headers and static libraries for hooking up custom mainloops to the dbus python
bindings.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%{openpgpverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{srcname}-%{version}

%build
%meson
%meson_build

%install
%meson_install
%py3_install

%check
%meson_test

%files -n python3-dbus
%doc NEWS
%license COPYING
%{python3_sitearch}/*.so
%{python3_sitearch}/dbus/
%{python3_sitearch}/dbus_python*egg-info

%files devel
%doc README doc/API_CHANGES.txt doc/tutorial.txt
%{_includedir}/dbus-1.0/dbus/dbus-python.h
%{_libdir}/pkgconfig/dbus-python.pc

%changelog
%autochangelog
