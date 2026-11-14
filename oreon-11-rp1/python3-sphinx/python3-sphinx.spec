# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 90470459f3cab15d9dfed146c71cf77694b0445df17b2e0e69059cb9f7fc9ee4
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-sphinx
Version: 9.2.0
Release: 1%{?dist}
Summary: Python documentation generator
License: MIT
URL: https://pypi.org/project/sphinx/
Source0: https://files.pythonhosted.org/packages/64/d4/413466f0be8b1cb0e3e43893a148b96d7462d0923d82b4166b21afc5f30c/sphinx-9.2.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-flit-core
BuildRequires: python3-sphinxcontrib-applehelp
BuildRequires: python3-sphinxcontrib-devhelp
BuildRequires: python3-sphinxcontrib-htmlhelp
BuildRequires: python3-sphinxcontrib-jsmath
BuildRequires: python3-sphinxcontrib-qthelp
BuildRequires: python3-sphinxcontrib-serializinghtml
BuildRequires: python3-jinja2
BuildRequires: python3-pygments
BuildRequires: python3-docutils
BuildRequires: python3-snowballstemmer
BuildRequires: python3-babel
BuildRequires: python3-alabaster
BuildRequires: python3-imagesize
BuildRequires: python3-requests
BuildRequires: python3-roman-numerals
BuildRequires: python3-packaging
Requires: python3
Requires: python3-sphinxcontrib-applehelp
Requires: python3-sphinxcontrib-devhelp
Requires: python3-sphinxcontrib-htmlhelp
Requires: python3-sphinxcontrib-jsmath
Requires: python3-sphinxcontrib-qthelp
Requires: python3-sphinxcontrib-serializinghtml
Requires: python3-jinja2
Requires: python3-pygments
Requires: python3-docutils
Requires: python3-snowballstemmer
Requires: python3-babel
Requires: python3-alabaster
Requires: python3-imagesize
Requires: python3-requests
Requires: python3-roman-numerals
Requires: python3-packaging

%description
Python documentation generator

%prep
%oreon_sha256
%autosetup -n sphinx-9.2.0

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import sphinx'

%files -f %{_builddir}/%{name}.files
