# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 928ae7e20211f3b6f3915a72f06a0cfd29ab9d24279dd6346b6b1a7146397d36
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-pyparsing
Version: 3.3.3
Release: 1%{?dist}
Summary: pyparsing - Classes and methods to define and execute parsing grammars
License: MIT
URL: https://pypi.org/project/pyparsing/
Source0: https://files.pythonhosted.org/packages/e4/11/b213bebff182584360cb8d17c72c1677fec5c5c228de439e63bcf8ab1c8f/pyparsing-3.3.3.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-flit-core
Requires: python3

%description
pyparsing - Classes and methods to define and execute parsing grammars

%prep
%oreon_sha256
%autosetup -n pyparsing-3.3.3

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import pyparsing'

%files -f %{_builddir}/%{name}.files
