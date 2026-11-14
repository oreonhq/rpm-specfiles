# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2f29ef331735ce958efa4734873f084941970894c6090408b079c61b2e1c06d1
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-sphinxcontrib-applehelp
Version: 2.0.0
Release: 1%{?dist}
Summary: sphinxcontrib-applehelp is a Sphinx extension which outputs Apple h...
License: BSD License
URL: https://pypi.org/project/sphinxcontrib-applehelp/
Source0: https://files.pythonhosted.org/packages/ba/6e/b837e84a1a704953c62ef8776d45c3e8d759876b4a84fe14eba2859106fe/sphinxcontrib_applehelp-2.0.0.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-flit-core
Requires: python3

%description
sphinxcontrib-applehelp is a Sphinx extension which outputs Apple h...

%prep
%oreon_sha256
%autosetup -n sphinxcontrib_applehelp-2.0.0

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
python3 -c 'import sphinxcontrib.applehelp'

%files -f %{_builddir}/%{name}.files
