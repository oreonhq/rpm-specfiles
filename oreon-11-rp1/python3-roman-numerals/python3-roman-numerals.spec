# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1af8b147eb1405d5839e78aeb93131690495fe9da5c91856cb33ad55a7f1e5b2
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-roman-numerals
Version: 4.1.0
Release: 1%{?dist}
Summary: Manipulate well-formed Roman numerals
License: MIT
URL: https://pypi.org/project/roman-numerals/
Source0: https://files.pythonhosted.org/packages/ae/f9/41dc953bbeb056c17d5f7a519f50fdf010bd0553be2d630bc69d1e022703/roman_numerals-4.1.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-flit-core
Requires: python3

%description
Manipulate well-formed Roman numerals

%prep
%oreon_sha256
%autosetup -n roman_numerals-4.1.0

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import roman_numerals'

%files -f %{_builddir}/%{name}.files
