# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c98b376c2424642224d456b2f70c51402343e008c63d204634665e1a2a2835f5
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-calver
Version: 2025.10.20
Release: 1%{?dist}
Summary: Setuptools extension for CalVer package versions
License: MIT
URL: https://pypi.org/project/calver/
Source0: https://files.pythonhosted.org/packages/4a/96/0c57e3e228ffc54074867406b659b197678674f1f0bf600d114965289834/calver-2025.10.20.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-wheel
BuildRequires: python3-setuptools
Requires: python3

%description
Setuptools extension for CalVer package versions

%prep
%oreon_sha256
%autosetup -n calver-2025.10.20

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitearch} python3 -c 'import calver'

%files -f %{_builddir}/%{name}.files

%changelog
%autochangelog
