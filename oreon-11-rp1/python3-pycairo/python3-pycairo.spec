# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: LGPL-2.1-or-later OR MPL-1.1

%global source0_hash 3e69fff74fe64f5ba2dfa31f67c6bdf26413342574047437d2ac520d35e9a489

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-pycairo
Version: 1.29.2
Release: 1%{?dist}
Summary: Python bindings for cairo
License: LGPL-2.1-or-later OR MPL-1.1
URL: https://pycairo.readthedocs.io/
Source0: https://files.pythonhosted.org/packages/bb/5e/19ab2572981a996ce96b853a189d2dcced40506b67d9555a7568457abcf2/pycairo-%{version}.tar.gz
Provides: python3dist(pycairo) = %{version}
Provides: pkgconfig(py3cairo) = %{version}

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
BuildRequires: meson
BuildRequires: ninja-build
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-gobject)
Requires: python3
Requires: cairo

%description
Pycairo is a set of Python bindings for the cairo graphics library.

%prep
%oreon_sha256
%autosetup -n pycairo-%{version}

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import cairo'

%files -f %{_builddir}/%{name}.files

%changelog
%autochangelog
