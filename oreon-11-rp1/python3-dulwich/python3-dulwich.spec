# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5d3939f64883e6799614cab708ef4ee9ef415dd6dcad47527cdbb0eea43bf3a2
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-dulwich
Version: 1.2.21
Release: 1%{?dist}
Summary: Python Git Library
License: MIT
URL: https://pypi.org/project/dulwich/
Source0: https://files.pythonhosted.org/packages/01/d1/01adf1db003374db4c2a70f7bae757ddfc39a33d9fb5ab765522b4d339e6/dulwich-1.2.21.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: gcc
BuildRequires: python3-urllib3
Requires: python3
Requires: python3-urllib3

%description
Python Git Library

%prep
%oreon_sha256
%autosetup -n dulwich-1.2.21

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import dulwich'

%files -f %{_builddir}/%{name}.files
