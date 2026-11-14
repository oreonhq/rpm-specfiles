# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 411f5d96d445d1d73bb5d52133377b4248ec79db5c793ce7dbe59e074b4dd1ad
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-sphinxcontrib-devhelp
Version: 2.0.0
Release: 1%{?dist}
Summary: sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp d...
License: BSD License
URL: https://pypi.org/project/sphinxcontrib-devhelp/
Source0: https://files.pythonhosted.org/packages/f6/d2/5beee64d3e4e747f316bae86b55943f51e82bb86ecd325883ef65741e7da/sphinxcontrib_devhelp-2.0.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-flit-core
Requires: python3

%description
sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp d...

%prep
%oreon_sha256
%autosetup -n sphinxcontrib_devhelp-2.0.0

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import sphinxcontrib.devhelp'

%files -f %{_builddir}/%{name}.files
