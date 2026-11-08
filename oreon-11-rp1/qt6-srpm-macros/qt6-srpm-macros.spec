# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 18c694cfdec2629081064aec81364bd4a62c6a4225532fc5fc93aba36fa86f1a
%global debug_package %{nil}

Name: qt6-srpm-macros
Version: 6.10.3
Release: 1%{?dist}
Summary: SRPM macros for Qt6 packages
License: GPL-3.0-only
URL: https://www.qt.io/
BuildArch: noarch
Source0: macros.qt6-srpm

BuildRequires: oreon-rpm-macros

%description
SRPM macros for packages that build against Qt6.

%prep
%oreon_sha256

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.qt6-srpm

%files
%{_rpmmacrodir}/macros.qt6-srpm
