# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash fd8269e4a03f801cc22b9e0fdf9b34cf39b90b799620badd8416041356d972af
%global debug_package %{nil}

Name: pyproject-srpm-macros
Version: 1.24.0
Release: 2%{?dist}
Summary: SRPM macros for pyproject packages
License: MIT
URL: https://github.com/rpm-software-management/pyproject-rpm-macros
BuildArch: noarch
Source0: macros.aaa-pyproject-srpm
Source1: LICENSE
Requires: (pyproject-rpm-macros >= 1.24.0 if pyproject-rpm-macros)
Requires: (rpm-build >= 4.14.90 if rpm-build)

BuildRequires: oreon-rpm-macros

%description
SRPM macros that load before the rest of the pyproject macros.

%prep
%oreon_sha256
cp %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.aaa-pyproject-srpm

%files
%license LICENSE
%{_rpmmacrodir}/macros.aaa-pyproject-srpm
