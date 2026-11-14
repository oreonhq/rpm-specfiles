# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash db2100058c50784c3d24984920ceefe61b951e915cb483ffafa116fdfc18cea2
%global source1_hash d05010279658d485b771ebec9692e83ebeb77ade914ea1d1e30598db34090585
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-vcsgraph
Version: 0.3.3
Release: 1%{?dist}
Summary: Graph algorithms for version control systems
License: MIT
URL: https://pypi.org/project/vcsgraph/
Source0: https://files.pythonhosted.org/packages/ee/03/5cdc1f74eff7a8532c1f28a789dddfa0984f5f392c08d67e96608c557639/vcsgraph-0.3.3.tar.gz
Source1: vcsgraph-0.3.3-vendor.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools-rust
BuildRequires: python3-wheel
BuildRequires: rust
BuildRequires: cargo
BuildRequires: gcc
Requires: python3

%description
Graph algorithms for version control systems

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -n vcsgraph-0.3.3
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
PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib} python3 -c 'import vcsgraph'

%files -f %{_builddir}/%{name}.files
