%global source0_hash eda5d4b867ce95accfc74135f595a238fcd60f19cfc997f4950a5c74fbdd3ac1

Name:           primecount
Version:        8.1
Release:        9%{?dist}
Summary:        Fast prime counting function implementation

# BSD-2-Clause: the project as a whole
# Zlib OR BSL-1.0: due to including libdivide headers
License:        BSD-2-Clause AND (Zlib OR BSL-1.0)
URL:            https://github.com/kimwalisch/%{name}/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  asciidoc
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libdivide-static
%ifarch %{ix86} x86_64 ia64 ppc64le
BuildRequires:  libquadmath-devel
%endif
BuildRequires:  make
BuildRequires:  primesieve-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

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
# WITH_FLOAT128 should be ON only for architectures:
# - with a __float128 type that is different from long double
# - with libquadmath
# As of GCC 12:
# - All x86/x86_64 CPUs have __float128; it is different from long double
# - ppc64le has __float128; it is the same as long double
# - No other architecture has libquadmath
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

%check
%ctest

%files
%doc README.md
%{_bindir}/primecount
%{_mandir}/man1/primecount.1*

%files          libs
%license COPYING
%{_libdir}/libprimecount.so.8*

%files          devel
%doc ChangeLog doc/*.pdf doc/*.md
%{_includedir}/primecount.h
%{_includedir}/primecount.hpp
%{_libdir}/libprimecount.so
%dir %{_libdir}/cmake/primecount
%{_libdir}/cmake/primecount/*.cmake
%{_libdir}/pkgconfig/primecount.pc

%changelog
%autochangelog
