%global source0_hash ef786edc203daec76475825640b3af247bd08e31fc52217e5ce8f76107b4bb05
%global abiver  3
Name:           date
Version:        3.0.5
Release:        1%{?dist}
Summary:        Date and time library based on the C++11/14/17 <chrono> header
License:        MIT
URL:            https://github.com/HowardHinnant/date
Source0:        https://github.com/HowardHinnant/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         output-date-pc-for-pkg-config.patch
Patch1:         date-macro.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  tzdata
# /oreon:deps
%description

# only timezone libary has binary part
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
%description    devel

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 %{?date:-n %{name}-%{commit}}
# remove broken tests
# fails due to gcc std::locale bugs (gcc#86976, HowardHinnant/date#388)
rm -f test/date_test/parse.pass.cpp
# fails in fedora-rawhide-i386 due to missing timezone configuration
rm -f test/tz_test/zoned_time_deduction.pass.cpp
# one more test that depends on localtime. we don't even install this header
rm -rf test/solar_hijri_test/

%build

%cmake \
    -DBUILD_TZ_LIB=ON     \
    -DUSE_SYSTEM_TZ_DB=ON \
    -DENABLE_DATE_TESTING=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles libdate-tz usr/*/lib*.so.*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

true
%files -f %{oreon_filedir}/main.list
%files -n libdate-tz -f %{oreon_filedir}/libdate-tz.list

%changelog

%autochangelog
