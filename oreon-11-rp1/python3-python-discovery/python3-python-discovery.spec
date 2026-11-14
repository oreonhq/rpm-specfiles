# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 86279f5d2728bc067de28b7ddc571be2eacc2ae0e7048f8629d2481a0f8848a2
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-python-discovery
Version: 1.9.5
Release: 1%{?dist}
Summary: Discover Python interpreters
License: MIT
URL: https://pypi.org/project/python-discovery/
Source0: https://files.pythonhosted.org/packages/68/55/70b46fae646bc6f5cb5e82569949d925cff1c7b5ce20ec4a11e0d977f8c6/python_discovery-1.9.5.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-hatchling
BuildRequires: python3-hatch-vcs
BuildRequires: python3-hatch-fancy-pypi-readme
Requires: python3

%description
Discover Python interpreters

%prep
%oreon_sha256
%autosetup -n python_discovery-1.9.5

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import python_discovery'

%files -f %{_builddir}/%{name}.files
