# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash e07bbc54a0d798fe6010a12398422e62a8bfbba95c394fd0956ef58cb4d3e260
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-snowballstemmer
Version: 3.1.1
Release: 1%{?dist}
Summary: This package provides 36 stemmers for 34 languages generated from S...
License: BSD-3-Clause
URL: https://pypi.org/project/snowballstemmer/
Source0: https://files.pythonhosted.org/packages/43/f8/0a71edf031f03c40db17503cb8ca78a69a171254e568e7db241b0ab57ea1/snowballstemmer-3.1.1.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-wheel
BuildRequires: python3-setuptools
Requires: python3

%description
This package provides 36 stemmers for 34 languages generated from S...

%prep
%oreon_sha256
%autosetup -n snowballstemmer-3.1.1

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitelib}:%{buildroot}%{python3_sitearch} python3 -c 'import snowballstemmer'

%files -f %{_builddir}/%{name}.files

%changelog
%autochangelog
