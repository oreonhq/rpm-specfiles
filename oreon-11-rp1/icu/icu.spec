# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f06bcab72736ee9d55689033b8198a178562354128cf38edb2afc2e67e3fd931

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: icu
Version: 78.3
Release: 1%{?dist}
Summary: International Components for Unicode tools
License: Unicode-DFS-2016 AND BSD-2-Clause AND BSD-3-Clause AND NAIST-2003
URL: https://icu.unicode.org/
Source0: https://github.com/unicode-org/icu/archive/refs/tags/release-%{version}.tar.gz#/icu-release-%{version}.tar.gz
Source1: metaZones.txt
Source2: timezoneTypes.txt
Source3: windowsZones.txt
Source4: zoneinfo64.txt
Source10: icu-config.sh
Patch4: gennorm2-man.patch
Patch5: icuinfo-man.patch
Patch6: 3496.patch

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: autoconf
BuildRequires: python3
BuildRequires: make

Requires: libicu%{?_isa} = %{version}-%{release}

%description
ICU tools for Unicode and globalization support.

%package -n libicu
Summary: ICU shared libraries

%description -n libicu
Shared libraries for ICU.

%package -n libicu-devel
Summary: Development files for ICU
Requires: libicu%{?_isa} = %{version}-%{release}
Provides: libicu-devel%{?_isa} = %{version}-%{release}
Provides: pkgconfig(icu-i18n) = %{version}
Provides: pkgconfig(icu-uc) = %{version}
Provides: pkgconfig(icu-io) = %{version}

%description -n libicu-devel
Headers and libraries for developing with ICU.

%prep
%oreon_sha256
%autosetup -p1 -n icu-release-%{version}
cp -v -f %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} source/data/misc/

%build
cd source
%configure --disable-samples --enable-shared --disable-static
%make_build

%install
cd source
%make_install
install -D -m 755 %{SOURCE10} %{buildroot}%{_bindir}/icu-config
rm -f %{buildroot}%{_libdir}/*.la

%check
cd source
%make_build check

%files
%{_bindir}/derb
%{_bindir}/genbrk
%{_bindir}/gencfu
%{_bindir}/gencnval
%{_bindir}/gendict
%{_bindir}/genrb
%{_bindir}/icu-config
%{_bindir}/icuexportdata
%{_bindir}/icuinfo
%{_bindir}/makeconv
%{_bindir}/pkgdata
%{_bindir}/uconv
%{_sbindir}/icupkg
%{_mandir}/man1/*
%{_mandir}/man8/*

%files -n libicu
%license LICENSE
%{_libdir}/libicu*.so.*
%{_datadir}/icu/

%files -n libicu-devel
%{_includedir}/unicode/
%{_libdir}/libicu*.so
%{_libdir}/pkgconfig/icu-*.pc
%{_libdir}/icu/

%changelog
%autochangelog
