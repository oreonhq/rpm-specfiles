# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 73ac416376dd65c737594ab4b1037b0823390239f33672f1ee1e30725dcef4e9
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: python-mallard-ducktype
Version: 1.0.2
Release: 1%{?dist}
Summary: Convert Ducktype markup to Mallard XML
License: MIT
URL: https://github.com/projectmallard/mallard-ducktype
Source0: https://github.com/projectmallard/mallard-ducktype/archive/refs/tags/%{version}.tar.gz
Patch0: mallard-no-pkg-resources.patch
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3
BuildRequires: python3-rpm-macros
BuildRequires: python3-setuptools
Requires: python3

%description
ducktype turns Mallard Ducktype files into XML. dbus design docs use it.

%prep
%oreon_sha256
%autosetup -n mallard-ducktype-%{version} -p1

%build
python3 setup.py build

%install
python3 setup.py install --skip-build --root %{buildroot}

%check
cd tests
bash ./runtests

%files
%license COPYING
%{_bindir}/ducktype
%{python3_sitelib}/mallard/
%{python3_sitelib}/mallard_ducktype*
