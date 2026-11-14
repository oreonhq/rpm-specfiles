# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash a0d403f3122aae24d34d2682665e505925bba7a6d3246da482b7a2a9cdcea8fe
%global source1_hash f3010798c5ac64f961325f598b46bba06c174274cf168900ce922c82ab757f15
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: python3-fastbencode
Version: 0.3.12
Release: 1%{?dist}
Summary: Implementation of bencode with optional fast Rust extensions
License: MIT
URL: https://pypi.org/project/fastbencode/
Source0: https://files.pythonhosted.org/packages/ac/be/21ea2218a70d634a32cd1c8be2c11624cfcfeaeec14016f04187a394f6b1/fastbencode-0.3.12.tar.gz
Source1: fastbencode-0.3.12-vendor.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-build
BuildRequires: python3-installer
BuildRequires: python3-setuptools
BuildRequires: python3-setuptools-rust
BuildRequires: rust
BuildRequires: cargo
BuildRequires: gcc
Requires: python3

%description
Implementation of bencode with optional fast Rust extensions

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -n fastbencode-0.3.12
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
PYTHONPATH=%{buildroot}%{python3_sitearch}:%{buildroot}%{python3_sitelib} python3 -c 'import fastbencode'

%files -f %{_builddir}/%{name}.files

%changelog
%autochangelog
