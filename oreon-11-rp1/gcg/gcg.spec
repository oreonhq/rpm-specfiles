%global source0_hash e3e86aa8269ba55639e1e5fd4c5ad075ea97de494da1d698af07bfe83e63f0da
%global giturl  https://github.com/scipopt/gcg
Name:           gcg
Version:        4.0.2
Release:        1%{?dist}
Summary:        Branch-and-price and column generation
License:        Apache-2.0
URL:            https://gcg.or.rwth-aachen.de/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-nauty-pkgconfig.patch
Patch:          %{name}-gsl-flexiblas.patch
ExcludeArch:    %{ix86}
Requires:       libgcg%{?_isa} = %{version}-%{release}
%global _desc %{expand:GCG: Generic Column Generation
Welcome to what is currently one of the only available open-source solvers for
mixed integer programming (MIP) that applies a comprehensive and expandable
Branch-Price-and-Cut framework.  By making use of detection algorithms, GCG is
able to apply Dantzig-Wolfe reformulation and Benders decomposition to solve
(potentially) structured MIPs faster.  It builds upon SCIP and thus allows for
total control of the solution process and the access of detailed information
down to the guts of the solver.}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(gtest)
BuildRequires:  cmake(scip)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(flexiblas)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(highs)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libcliquer)
BuildRequires:  pkgconfig(libnauty)
# /oreon:deps
%description
%_desc

This package contains a command-line tool to access GCG functionality.

%package -n     libgcg
Summary:        Library for branch-and-price and column generation
%description -n libgcg
%_desc

This package contains a library interface to GCG functionality.

%package -n     libgcg-devel
Summary:        Headers and library links for libgcg
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libgcg%{?_isa} = %{version}-%{release}
%description -n libgcg-devel
This package contains headers and library links for developing applications
that use libgcg.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
# Remove the prebuilt hmetis executable
rm hmetis

# Disable unwanted rpaths
sed -e '/INSTALL_RPATH_USE_LINK_PATH/s/TRUE/FALSE/' \
    -e '/INSTALL_RPATH.*CMAKE_INSTALL_PREFIX/d' \
    -i src/CMakeLists.txt

%build

export CFLAGS='%{build_cflags} -DNDEBUG'
export CXXFLAGS='%{build_cxxflags} -DNDEBUG'
%cmake -DHIGHS:BOOL=ON -DOPENMP:BOOL=ON
%cmake_build
%install
%cmake_install
rm -fr %{buildroot}%{_datadir}/licenses/%{name}
%oreon_autofiles libgcg usr/*/lib*.so.*
%oreon_autofiles libgcg-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%ctest
%files -f %{oreon_filedir}/main.list
%files -n libgcg -f %{oreon_filedir}/libgcg.list
%files -n libgcg-devel -f %{oreon_filedir}/libgcg-devel.list

%changelog

%autochangelog
