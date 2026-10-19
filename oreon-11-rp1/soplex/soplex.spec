%global source0_hash f989f650e0d489f4e84037af2a50b1d0928f62ab79179ef566111d9197c2b6c8
%ifarch %{x86_64} %{power64}
%global quadmath 1
%else
%global quadmath 0
%endif
%global giturl  https://github.com/scipopt/soplex
Name:           soplex
Version:        8.0.3
Release:        1%{?dist}
Summary:        Sequential object-oriented simplex
License:        Apache-2.0 AND MIT
URL:            https://soplex.zib.de/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-shared.patch
Patch:          %{name}-unbundle-zstr.patch
ExcludeArch:    %{ix86}
Requires:       libsoplex%{?_isa} = %{version}-%{release}
%global _desc %{expand:
SoPlex is an optimization package for solving linear programming problems
(LPs) based on an advanced implementation of the primal and dual revised
simplex algorithm.  It provides special support for the exact solution of LPs
with rational input data.  It can be used as a standalone solver reading MPS
or LP format files via a command line interface as well as embedded into other
programs via a C++ class library.  The main features of SoPlex are:
- presolving, scaling, exploitation of sparsity, hot-starting from any regular
  basis,
- column- and row-oriented form of the simplex algorithm,
- an object-oriented software design written in C++,
- a compile-time option to use 80bit extended ("quad") precision for
  numerically difficult LPs,
- an LP iterative refinement procedure to compute high-precision solution, and
- routines for an exact rational LU factorization and continued fraction
  approximations in order to compute exact solutions.
SoPlex has been used in numerous research and industry projects and is the
standard LP solver linked to the mixed-integer nonlinear programming and
constraint integer programming solver SCIP.}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(papilo)
BuildRequires:  cmake(tbb)
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  ninja-build
BuildRequires:  php-cli
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  python3
BuildRequires:  zstr-static
# /oreon:deps
%description
%_desc

This package contains a command-line tool to access SoPlex functionality.

%package -n     libsoplex
Summary:        Library for sequential object-oriented simplex
Provides:       bundled(fmt) = 7.1.3
%description -n libsoplex
%_desc

This package contains a library interface to SoPlex functionality.

%package -n     libsoplex-devel
Summary:        Headers and library links for libsoplex
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libsoplex%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}
Requires:       gmp-devel%{?_isa}
Requires:       libpapilo-devel%{?_isa}
Requires:       mpfr-devel%{?_isa}
Requires:       zstr-devel
%description -n libsoplex-devel
This package contains headers and library links for developing applications
that use libsoplex.

%package -n     libsoplex-doc
License:        Apache-2.0 AND GPL-1.0-or-later AND MIT
Summary:        API documentation for libsoplex
BuildArch:      noarch
%description -n libsoplex-doc
API documentation for libsoplex.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
# We want to know about overflow errors, as the compiler can do surprising
# things if we don't fix them!
sed -i 's/ -Wno-strict-overflow//' CMakeLists.txt Makefile

# Turn off HTML timestamps for repeatable builds
sed -i '/HTML_TIMESTAMP/s/YES/NO/' doc/soplex.dxy

# Ensure the bundled copy of zstr is not used
rm -fr src/soplex/external/zstr

%build

%cmake \
  -DMPFR:BOOL=ON \
  -DPAPILO:BOOL=ON \
  -DQUADMATH:BOOL=%{?quadmath:ON}%{!?quadmath:OFF}
%cmake_build
cd doc
../%{_vpath_builddir}/bin/soplex --saveset=parameters.set
cd inc
python3 parser.py --linkext html
php localfaq.php > faq.inc
cd ..
doxygen soplex.dxy
cd ..
%install
%cmake_install
rm -fr %{buildroot}%{_defaultlicensedir}
sed -i 's/papilo;/papilo-core;/' \
    %{buildroot}%{_libdir}/cmake/soplex/soplex-targets.cmake
%oreon_autofiles libsoplex usr/*/lib*.so.*
%oreon_autofiles libsoplex-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libsoplex-doc usr/*/lib*.so.*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest
%files -f %{oreon_filedir}/main.list
%files -n libsoplex -f %{oreon_filedir}/libsoplex.list
%files -n libsoplex-devel -f %{oreon_filedir}/libsoplex-devel.list
%files -n libsoplex-doc -f %{oreon_filedir}/libsoplex-doc.list

%changelog

%autochangelog
