# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash e0e45989e821bef6aa9ae15c7d583ab5e055f7406c4b3624e49e06d24e90375a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-cython
Version: 3.3.1
Release: 1%{?dist}
Summary: The Cython compiler for writing C extensions in the Python language.
License: Apache-2.0
URL: https://pypi.org/project/cython/
Source0: https://files.pythonhosted.org/packages/99/ca/18e324972e5cac914816fdd7bb03e19a455b90039c277a538f7781b50c85/cython-3.3.1.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-wheel
BuildRequires: python3-setuptools
BuildRequires: gcc
Requires: python3

%description
The Cython compiler for writing C extensions in the Python language.

%prep
%oreon_sha256
%autosetup -n cython-3.3.1

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitearch} python3 -c 'import Cython'

%files -f %{_builddir}/%{name}.files
