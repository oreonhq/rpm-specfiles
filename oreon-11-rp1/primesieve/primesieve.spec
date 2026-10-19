%global source0_hash acaafd94cc30dbeef4808e682d0cb096c05d25f74eda5bacecefd323f697833f
Name:     primesieve
Version:  12.15
Release:        1%{?dist}
Summary:        Fast prime number generator
License:  LicenseRef-Callaway-BSD
URL:      https://github.com/kimwalisch/primesieve
Source0:        https://github.com/kimwalisch/primesieve/archive/v%{version}.tar.gz
Requires: primesieve-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
primesieve is a program that generates primes using a highly optimized
sieve of Eratosthenes implementation. primesieve can generate primes
and prime k-tuplets up to 2^64.

%package -n primesieve-libs
Summary: C/C++ library for generating prime numbers
%description -n primesieve-libs
This package contains the shared runtime library for primesieve.

%package -n primesieve-devel
Summary: Development files for the primesieve library
Requires: primesieve-libs%{?_isa} = %{version}-%{release}
%description -n primesieve-devel
This package contains the C/C++ header files and the configuration
files for developing applications that use the primesieve library.
It also contains the API documentation of the library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

%build

%cmake -DBUILD_STATIC_LIBS=OFF -DBUILD_TESTS=ON -DBUILD_MANPAGE=ON
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets -n primesieve-libs
%oreon_autofiles primesieve-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles primesieve-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n primesieve-libs -f %{oreon_filedir}/primesieve-libs.list
%files -n primesieve-devel -f %{oreon_filedir}/primesieve-devel.list

%changelog

%autochangelog
