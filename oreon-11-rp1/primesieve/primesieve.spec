%global source0_hash 7a418b9bacff174f1dedc3d517179e1dc62b7a1a9956d1b7c2585be8fd1cb3c9

Name:     primesieve
Version:  12.12
Release:  1%{?dist}
Summary:  Fast prime number generator
License:  LicenseRef-Callaway-BSD
URL:      https://github.com/kimwalisch/primesieve
Source0:  https://github.com/kimwalisch/primesieve/archive/v%{version}.tar.gz
Requires: primesieve-libs%{?_isa} = %{version}-%{release}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  cmake >= 3.9
BuildRequires:  asciidoc

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

%check
%ctest

%files -n primesieve
%doc README.md ChangeLog
%{_bindir}/primesieve
%{_mandir}/man1/primesieve.1*

%files -n primesieve-libs
%license COPYING
%{_libdir}/libprimesieve.so.12*

%files -n primesieve-devel
%doc doc/C_API.md doc/CPP_API.md
%{_libdir}/libprimesieve.so
%{_includedir}/primesieve.h
%{_includedir}/primesieve.hpp
%dir %{_includedir}/primesieve
%{_includedir}/primesieve/StorePrimes.hpp
%{_includedir}/primesieve/iterator.h
%{_includedir}/primesieve/iterator.hpp
%{_includedir}/primesieve/primesieve_error.hpp
%dir %{_libdir}/cmake/primesieve
%{_libdir}/cmake/primesieve/*.cmake
%{_libdir}/pkgconfig/primesieve.pc

%changelog
%autochangelog
