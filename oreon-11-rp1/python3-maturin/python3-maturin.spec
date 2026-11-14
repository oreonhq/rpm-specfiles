# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 13e69ca12542999d8c5467131de72a49bb76e4c284b9a45c5783df7c0fcb3a8a
%global source1_hash 960c7c9feca8695c74f016780e0206e17f83f362878d5ce154dabcf384f35c09
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-maturin
Version: 1.16.0
Release: 1%{?dist}
Summary: Build and publish crates with pyo3
License: Apache-2.0 OR MIT
URL: https://pypi.org/project/maturin/
Source0: https://files.pythonhosted.org/packages/bd/71/eb078174335ff30bde1be2ad54fb6256db4b160eb3efa81163fa30f8c814/maturin-1.16.0.tar.gz
Source1: maturin-1.16.0-vendor.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools-rust
BuildRequires: rust
BuildRequires: cargo
Requires: python3

%description
Build and publish crates with pyo3

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -n maturin-1.16.0
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
PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib} python3 -c 'import maturin'

%files -f %{_builddir}/%{name}.files

%changelog
%autochangelog
