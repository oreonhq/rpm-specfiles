# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1620739f04e36a2c779f1a131a2dfd49b2fd07351bf1968ced074365933abc7a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-sphinxcontrib-jquery
Version: 4.1
Release: 1%{?dist}
Summary: Extension to include jQuery on newer Sphinx releases
License: BSD License
URL: https://pypi.org/project/sphinxcontrib-jquery/
Source0: https://files.pythonhosted.org/packages/de/f3/aa67467e051df70a6330fe7770894b3e4f09436dea6881ae0b4f3d87cad8/sphinxcontrib-jquery-4.1.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-flit-core
Requires: python3
Requires: python3-sphinx

%description
Extension to include jQuery on newer Sphinx releases

%prep
%oreon_sha256
%autosetup -n sphinxcontrib-jquery-4.1

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import sphinxcontrib.jquery'

%files -f %{_builddir}/%{name}.files
