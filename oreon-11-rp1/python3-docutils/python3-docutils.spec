# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4db53b1fde9abecbb74d91230d32ab626d94f6badfc575d6db9194a49df29968
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-docutils
Version: 0.22.4
Release: 1%{?dist}
Summary: Docutils -- Python Documentation Utilities
License: BSD License
URL: https://pypi.org/project/docutils/
Source0: https://files.pythonhosted.org/packages/ae/b6/03bb70946330e88ffec97aefd3ea75ba575cb2e762061e0e62a213befee8/docutils-0.22.4.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-flit-core
Requires: python3

%description
Docutils -- Python Documentation Utilities

%prep
%oreon_sha256
%autosetup -n docutils-0.22.4

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import docutils'

%files -f %{_builddir}/%{name}.files
