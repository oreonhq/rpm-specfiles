# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2eb3688fc52244330c4837f0e446122b9726da777a3f301fe3b0c73f92202036
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:		python-libevdev
Version:	0.13.1
Release:	1%{?dist}
Summary:	Python bindings to the libevdev evdev device wrapper library

License:	MIT
URL:		https://pypi.python.org/pypi/libevdev/
Source0:	https://gitlab.freedesktop.org/libevdev/python-libevdev/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

%description
%{name} provides the Python bindings to the libevdev evdev device
wrapper library. These bindings provide a pythonic API to access evdev
devices and create uinput devices.

%package -n	python3-libevdev
Summary:	Python bindings to the libevdev evdev device wrapper library

BuildRequires: oreon-rpm-macros
BuildRequires:	python3-devel
BuildRequires:	python3dist(hatchling)
Requires:	libevdev

%{?python_provide:%python_provide python3-libevdev}

%description -n	python3-libevdev
%{name} provides the Python bindings to the libevdev evdev device
wrapper library. These bindings provide a pythonic API to access evdev
devices and create uinput devices.

%generate_buildrequires
%pyproject_buildrequires

%prep
%oreon_sha256
%autosetup -n %{name}-%{version} -p1

%build
%pyproject_wheel

%install
%pyproject_install

%files -n	python3-libevdev
%license COPYING
%{python3_sitelib}/libevdev/
%{python3_sitelib}/libevdev-%{version}.dist-info

%changelog
%autochangelog
