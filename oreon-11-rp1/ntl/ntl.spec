%global source0_hash bc0ef9aceb075a6a0673ac8d8f47d5f8458c72fe806e4468fbd5d3daff056182
Name:           ntl
Version:        11.6.0
Release:        1%{?dist}
Summary:        High-performance algorithms for vectors, matrices, and polynomials
License:        LGPL-2.1-or-later AND BSD-2-Clause
URL:            https://libntl.org/
VCS:            git:https://github.com/libntl/ntl.git
Source0:        https://libntl.org/%{name}-%{version}.tar.gz
Patch:          %{name}-loadtime-cpu.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gf2x-devel
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl-interpreter
# /oreon:deps
%description
NTL is a high-performance, portable C++ library providing data structures and
algorithms for arbitrary length integers; for vectors, matrices, and
polynomials over the integers and over finite fields; and for arbitrary
precision floating point arithmetic.

NTL provides high quality implementations of state-of-the-art algorithms for:
* arbitrary length integer arithmetic and arbitrary precision floating point
  arithmetic;
* polynomial arithmetic over the integers and finite fields including basic
  arithmetic, polynomial factorization, irreducibility testing, computation
  of minimal polynomials, traces, norms, and more;
* lattice basis reduction, including very robust and fast implementations of
  Schnorr-Euchner, block Korkin-Zolotarev reduction, and the new
  Schnorr-Horner pruning heuristic for block Korkin-Zolotarev;
* basic linear algebra over the integers, finite fields, and arbitrary
  precision floating point numbers.

%package devel 
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel 
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Remove an unused file with an unacceptable license (CC-BY-3.0)
rm src/GetTime0.cpp

%build

cd src
./configure \
  CXX="${CXX-g++}" \
  CXXFLAGS='%{build_cxxflags} -fPIC' \
  LDFLAGS='%{build_ldflags}' \
  DOCDIR=%{_docdir} \
  ENABLE_RPATH=off \
  LIBDIR=%{_libdir} \
  NATIVE=off \
  NTL_GF2X_LIB=on \
  NTL_STD_CXX14=on \
%ifarch %{x86_64}
  NTL_LOADTIME_CPU=on \
  TUNE=x86 \
%else
  TUNE=generic \
%endif
  PKGDIR=%{_libdir}/pkgconfig \
  SHARED=on \
  SYS_PREFIX=%{_prefix}
cd -
make -C src V=1
%install
make -C src install \
  DESTDIR=%{buildroot} \
  PREFIX=%{_prefix} \
  DOCDIR=%{_docdir} \
  INCLUDEDIR=%{_includedir} \
  LIBDIR=%{_libdir} 
rm -rfv %{buildroot}%{_docdir}/NTL
rm -fv  %{buildroot}%{_libdir}/libntl.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make -C src check
%files -f %{oreon_filedir}/main.list
%files -n ntl-devel -f %{oreon_filedir}/ntl-devel.list

%changelog

%autochangelog
