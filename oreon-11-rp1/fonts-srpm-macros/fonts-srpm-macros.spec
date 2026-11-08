# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5317afc1e41570ca6412f18309030b9de6547aae10f80a7c90f78b46a2b5f24d
%global debug_package %{nil}

Name: fonts-srpm-macros
Version: 5.0.0
Release: 2%{?dist}
Summary: SRPM macros for font packages
License: MIT
URL: https://pagure.io/fonts-rpm-macros
BuildArch: noarch
Source0: macros.fonts-srpm
Source1: fonts.lua
Source2: LICENSE.txt
Requires: oreon-rpm-config
Requires: forge-srpm-macros

BuildRequires: oreon-rpm-macros

%description
SRPM macros for packaging fonts.

%prep
%oreon_sha256
cp %{SOURCE2} .

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
mkdir -p %{buildroot}%{_rpmluadir}/oreon/srpm
install -m 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.fonts-srpm
install -m 644 %{SOURCE1} %{buildroot}%{_rpmluadir}/oreon/srpm/fonts.lua

%files
%license LICENSE.txt
%{_rpmmacrodir}/macros.fonts-srpm
%{_rpmluadir}/oreon/srpm/fonts.lua
