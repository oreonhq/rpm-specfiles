# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 141eb04d3432ef09dbbbd010400291909717bcc0d55e0e34b9573dfeb757b8bc
%global debug_package %{nil}

Name: cmake-srpm-macros
Version: 4.2.3
Release: 1%{?dist}
Summary: SRPM macros for cmake packages
License: BSD-3-Clause
URL: https://cmake.org/
BuildArch: noarch
Source0: macros.aaa-cmake-srpm
Requires: rpm

BuildRequires: oreon-rpm-macros

%description
SRPM macros that mark cmake packages before the main cmake macros load.

%prep
%oreon_sha256

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.aaa-cmake-srpm

%files
%{_rpmmacrodir}/macros.aaa-cmake-srpm
