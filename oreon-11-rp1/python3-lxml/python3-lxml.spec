# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 45222d94ddd511536f3b2f7d9deae3b2339b4ce0f075f1ca25703b07cad9dd21
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-lxml
Version: 6.1.3
Release: 1%{?dist}
Summary: Python bindings for libxml2 and libxslt
License: BSD-3-Clause
URL: https://lxml.de/
Source0: https://files.pythonhosted.org/packages/23/ad/28ecd7cb894d172f3c9c80a075eeeb2017ac62e3632cee05a5f9493547eb/lxml-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-cython
BuildRequires: python3-cython
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
Requires: python3

%description
lxml is the Python XML library yelp-tools imports.

%prep
%oreon_sha256
%autosetup -n lxml-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --skip-build --root %{buildroot}

%check
PYTHONPATH=$(echo build/lib.*) python3 -c 'import lxml.etree, lxml.html'

%files
%license LICENSE.txt
%{python3_sitearch}/lxml/
%{python3_sitearch}/lxml-*.egg-info
