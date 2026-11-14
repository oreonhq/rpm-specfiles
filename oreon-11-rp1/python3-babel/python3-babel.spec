# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b80b99a14bd085fcacfa15c9165f651fbb3406e66cc603abf11c5750937c992d
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-babel
Version: 2.18.0
Release: 1%{?dist}
Summary: Internationalization utilities
License: BSD-3-Clause
URL: https://pypi.org/project/babel/
Source0: https://files.pythonhosted.org/packages/7d/b2/51899539b6ceeeb420d40ed3cd4b7a40519404f9baf3d4ac99dc413a834b/babel-2.18.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-wheel
BuildRequires: python3-setuptools
Requires: python3

%description
Internationalization utilities

%prep
%oreon_sha256
%autosetup -n babel-2.18.0

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitearch} python3 -c 'import babel'

%files -f %{_builddir}/%{name}.files

%changelog
%autochangelog
