# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 56e05531ee8994124eeb498d0e6a5e1c3b9d4fccbecdf555fe266631368fb55f
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global abiver  3

Name:           date
Version:        3.0.4
Release:        1%{?dist}
Summary:        Date and time library based on the C++11/14/17 <chrono> header

License:        MIT
URL:            https://github.com/HowardHinnant/date
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         output-date-pc-for-pkg-config.patch
Patch1:         date-macro.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  cmake >= 3.7
BuildRequires:  tzdata

%global _description %{expand:
This is actually several separate C++11/C++14/C++17 libraries:
 - "date.h" is a header-only library which builds upon <chrono>.
   It adds some new duration types, and new time_point types. It
   also adds "field" types such as year_month_day which is a
   struct {year, month, day}. And it provides convenient means
   to convert between the "field" types and the time_point types.
 - "tz.h" / "tz.cpp" are a timezone library built on top of the
   "date.h" library. This timezone library is a complete parser
   of the IANA timezone database. It provides for an easy way to
   access all of the data in this database, using the types from
   "date.h" and <chrono>. The IANA database also includes data
   on leap seconds, and this library provides utilities to compute
   with that information as well.
Slightly modified versions of "date.h" and "tz.h" were voted into
the C++20 standard.}

%description %{_description}

%package -n     libdate-tz
Summary:        Timezone library built on top of the date library
Requires:       tzdata

%description -n libdate-tz
Timezone library built on top of the date library. This timezone library
is a complete parser of the IANA timezone database. It provides for
an easy way to access all of the data in this database, using the types
from "date.h" and <chrono>. The IANA database also includes data on leap
seconds, and this library provides utilities to compute with that
information as well.

%package        devel
Summary:        Date and time library based on the C++11/14/17 <chrono> header
Requires:       libdate-tz%{?_isa} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}

%description    devel %{_description}

%prep
%oreon_sha256
%autosetup -p1 %{?date:-n %{name}-%{commit}}
rm -f test/date_test/parse.pass.cpp
rm -f test/tz_test/zoned_time_deduction.pass.cpp
rm -rf test/solar_hijri_test/

%build
%cmake \
    -DBUILD_TZ_LIB=ON     \
    -DUSE_SYSTEM_TZ_DB=ON \
    -DENABLE_DATE_TESTING=ON
%cmake_build

%install
%cmake_install

%check
export CTEST_OUTPUT_ON_FAILURE=ON
%cmake_build -t testit

%files -n libdate-tz
%license LICENSE.txt
%{_libdir}/libdate-tz.so.%{abiver}*

%files devel
%license LICENSE.txt
%doc README.md
%{_includedir}/%{name}/
%{_libdir}/libdate-tz.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
