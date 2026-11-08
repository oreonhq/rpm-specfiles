# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 3c3fb388829b2c879b597d5fc1bf1ce1bcc999c97ac0bb5045a513e792fb9ffe
%global debug_package %{nil}

Name: lua-srpm-macros
Version: 1
Release: 2%{?dist}
Summary: SRPM macros for Lua packages
License: MIT
URL: https://www.lua.org/
BuildArch: noarch
Source0: macros.lua-srpm
Source1: LICENSE
Requires: rpm

BuildRequires: oreon-rpm-macros

%description
SRPM macros for Lua source packages.

%prep
%oreon_sha256
cp %{SOURCE1} .

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.lua-srpm

%files
%license LICENSE
%{_rpmmacrodir}/macros.lua-srpm
