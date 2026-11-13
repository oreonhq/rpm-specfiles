# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash dd31f52ea1086513bb9df30f8fcee9b8918323ae067a3d5b78bc826a000712be
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-cffi
Version: 2.1.1
Release: 1%{?dist}
Summary: Foreign function interface for Python
License: MIT
URL: https://pypi.org/project/cffi/
Source0: https://files.pythonhosted.org/packages/9e/ef/008a1939e372c06329a3fce4279c02f328488f3526744906eeec3da7ad5f/cffi-2.1.1.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-pycparser
BuildRequires: libffi-devel
BuildRequires: gcc
Requires: python3
Requires: python3-pycparser

%description
Foreign function interface for Python

%prep
%oreon_sha256
%autosetup -n cffi-2.1.1

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib} python3 -c 'import cffi'

%files -f %{_builddir}/%{name}.files
