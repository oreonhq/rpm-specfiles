%global source0_hash 5a19eccca337da9e1cc629f2a223890af08987bc21771b9e860e28d823006be3
Name:           primecount
Version:        8.7
Release:        1%{?dist}
Summary:        Fast prime counting function implementation
License:        BSD-2-Clause AND (Zlib OR BSL-1.0)
URL:            https://github.com/kimwalisch/%{name}/
Source0:        https://github.com/kimwalisch/%{name}//archive/v%{version}/%{name}-%{version}.tar.gz
%ifarch %{ix86} x86_64 ia64 ppc64le
%endif
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libdivide-static
BuildRequires:  make
BuildRequires:  primesieve-devel
# /oreon:deps
%description
Primecount is a command-line program and C++ library that counts the
primes below an integer x<=10**31 using highly optimized implementations
of the combinatorial prime counting algorithms.

Primecount includes implementations of all important combinatorial prime
counting algorithms known up to this date all of which have been
parallelized using OpenMP.  Primecount contains the first ever open
source implementations of the Deleglise-Rivat algorithm and Xavier
Gourdon's algorithm (that works).  Primecount also features a novel load
balancer that is shared amongst all implementations and that scales up
to hundreds of CPU cores.  Primecount has already been used to compute
several world records e.g. pi(10**27)
(http://www.mersenneforum.org/showthread.php?t=20473) and
nth_prime(10**24) (https://oeis.org/A006988).

%package        libs
Summary:        C++ library for fast prime counting
%ldconfig_scriptlets
%description    libs
This package contains a C++ library for counting primes below an
integer.  See the primecount package for a command line interface.

%package        devel
Summary:        Headers and library links for libprimecount
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
This package contains files necessary to develop applications that use
libprimecount.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Unbundle libdivide
rm -f include/libdivide.h
ln -s %{_includedir}/libdivide.h include/libdivide.h

%build

%ifarch %{ix86} x86_64
export CFLAGS='%{build_cflags} -DLIBDIVIDE_SSE2'
export CXXFLAGS='%{build_cxxflags} -DLIBDIVIDE_SSE2'
%endif
%cmake -DBUILD_LIBPRIMESIEVE=OFF \
       -DBUILD_MANPAGE=ON \
       -DBUILD_SHARED_LIBS=ON \
       -DBUILD_STATIC_LIBS=OFF \
%ifarch %{ix86} x86_64
       -DWITH_FLOAT128=ON \
%endif
       -DBUILD_TESTS=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n primecount-libs -f %{oreon_filedir}/primecount-libs.list
%files -n primecount-devel -f %{oreon_filedir}/primecount-devel.list

%changelog

%autochangelog
