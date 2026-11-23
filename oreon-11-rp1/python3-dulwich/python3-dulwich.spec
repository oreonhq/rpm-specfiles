# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5d3939f64883e6799614cab708ef4ee9ef415dd6dcad47527cdbb0eea43bf3a2
%global source1_hash 3354926c7325eecc7e57262ca1dfdf522c1765e27c9667c3130baac620f56cea
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-dulwich
Version: 1.2.21
Release: 1%{?dist}
Summary: Python Git Library
License: Apache-2.0 OR GPL-2.0-or-later
URL: https://pypi.org/project/dulwich/
Source0: https://files.pythonhosted.org/packages/01/d1/01adf1db003374db4c2a70f7bae757ddfc39a33d9fb5ab765522b4d339e6/dulwich-1.2.21.tar.gz
Source1: dulwich-1.2.21-vendor.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools-rust
BuildRequires: rust
BuildRequires: cargo
BuildRequires: gcc
BuildRequires: python3-urllib3
Requires: python3
Requires: python3-urllib3

%description
Python Git Library

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -n dulwich-1.2.21
tar -xf %{SOURCE1}
%oreon_cargo_prep vendor

%build
export CARGO_HOME=%{_builddir}/cargo-home
mkdir -p "$CARGO_HOME"
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib} python3 -c 'import dulwich._objects, dulwich._pack, dulwich._diff_tree'

%files -f %{_builddir}/%{name}.files

%changelog
%autochangelog
