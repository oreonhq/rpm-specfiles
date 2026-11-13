# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1252ce3a102372ca6f86eb968e16f9014c4ba511c5c37d95a7f023e2ca6e5c25
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-packageurl
Version: 0.17.6
Release: 1%{?dist}
Summary: Python parser for package URLs
License: MIT
URL: https://pypi.org/project/packageurl-python/
Source0: https://files.pythonhosted.org/packages/f5/d6/3b5a4e3cfaef7a53869a26ceb034d1ff5e5c27c814ce77260a96d50ab7bb/packageurl_python-0.17.6.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-wheel
Requires: python3

%description
Python parser for package URLs

%prep
%oreon_sha256
%autosetup -n packageurl_python-0.17.6

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitearch} python3 -c 'import packageurl'

%files -f %{_builddir}/%{name}.files
