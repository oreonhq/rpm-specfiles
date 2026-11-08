# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d0c4c0adb77d0b10e33812ddaac23ecbd4434eea1b16d8a5ed068901870cdb7b
%global debug_package %{nil}

Name: java-srpm-macros
Version: 1
Release: 1%{?dist}
Summary: SRPM macros for Java packages
License: GPL-2.0-or-later
URL: https://openjdk.org/
BuildArch: noarch
Source0: macros.java-srpm
Requires: rpm

BuildRequires: oreon-rpm-macros

%description
SRPM macros for Java source packages.

%prep
%oreon_sha256

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
install -m 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.java-srpm

%files
%{_rpmmacrodir}/macros.java-srpm
