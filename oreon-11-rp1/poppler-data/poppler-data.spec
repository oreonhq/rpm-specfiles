# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c835b640a40ce357e1b83666aabd95edffa24ddddd49b8daff63adb851cdab74

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: poppler-data
Version: 0.4.12
Release: 1%{?dist}
Summary: Encoding files for poppler
License: Adobe-2006 AND GPL-2.0-or-later AND MIT
URL: https://poppler.freedesktop.org/
Source0: https://poppler.freedesktop.org/poppler-data-%{version}.tar.gz

BuildRequires: oreon-rpm-macros >= 1-14
BuildRequires: cmake

Provides: pkgconfig(poppler-data) = %{version}

%description
CMap, Unicode and encoding data used by poppler when it reads PDF files.

%prep
%oreon_sha256
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%check
test -s %{buildroot}%{_datadir}/poppler/cMap/Adobe-CNS1/Adobe-CNS1-0
test -s %{buildroot}%{_datadir}/poppler/unicodeMap/ISO-8859-7
grep -q '^poppler_datadir=' %{buildroot}%{_datadir}/pkgconfig/poppler-data.pc

%files
%license COPYING COPYING.adobe COPYING.gpl2
%{_datadir}/poppler/
%{_datadir}/pkgconfig/poppler-data.pc

%changelog
%autochangelog
