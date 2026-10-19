%global source0_hash b7c70e754c23f8bef5843ac02b82f9dc1707a653c867474123e635951305af88
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%ifarch %{x86_64} %{power64}
%global quadmath 1
%else
%global quadmath 0
%endif
%bcond bootstrap 0
%global giturl  https://github.com/scipopt/papilo/
Name:           papilo
Version:        3.0.1
Release:        1%{?dist}
Summary:        Parallel presolve for integer and linear optimization
License:        Apache-2.0 AND BSL-1.0 AND Zlib AND MIT
URL:            https://www.scipopt.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-unbundle.patch
Patch:          %{name}-shared.patch
Patch:          %{name}-vector-bounds.patch
ExcludeArch:    %{ix86}
%if %{without bootstrap}
%endif
Requires:       libpapilo%{?_isa} = %{version}-%{release}
%global _desc %{expand:PaPILO provides parallel presolve routines for (mixed integer) linear
programming problems.  The routines are implemented using templates which
allows switching to higher precision or rational arithmetic using the boost
multiprecision package.}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  catch-devel
BuildRequires:  cmake
BuildRequires:  cmake(scip)
BuildRequires:  cmake(soplex)
BuildRequires:  cmake(tbb)
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  libatomic
BuildRequires:  lusol-devel
BuildRequires:  pdqsort-static
BuildRequires:  pkgconfig(gmp)
# /oreon:deps
%description
%_desc

%package     -n libpapilo
Summary:        Library interface to PaPILO
Provides:       bundled(fmt) = 7.1.3
%description -n libpapilo
%_desc

This package provides a library interface to the PaPILO functionality.

%package     -n libpapilo-devel
Summary:        Headers and library links for libpapilo
Requires:       libpapilo%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}
Requires:       lusol-devel%{?_isa}
Requires:       pdqsort-static
Requires:       tbb-devel%{?_isa}
%description -n libpapilo-devel
%_desc

This package contains headers and library links to develop applications that
use libpapilo.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
# Ensure none of the bundled code but fmt can be used
rm -fr src/papilo/external/{catch,lusol,pdqsort,ska}

%build

%cmake -DQUADMATH:BOOL=%{?quadmath:ON}%{!?quadmath:OFF}
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_mandir}/man1
export LD_LIBRARY_PATH=$PWD/%{_vpath_builddir}
cd %{_vpath_builddir}/bin
help2man -N -h '' --version-string %{version} \
  -n 'parallel presolve for integer and linear optimization' ./papilo > \
  %{buildroot}%{_mandir}/man1/papilo.1
cd -
sed -i 's,\./\(papilo\),\1,' %{buildroot}%{_mandir}/man1/papilo.1
rm -fr %{buildroot}%{_defaultlicensedir}
%oreon_autofiles libpapilo usr/*/lib*.so.*
%oreon_autofiles libpapilo-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n libpapilo -f %{oreon_filedir}/libpapilo.list
%files -n libpapilo-devel -f %{oreon_filedir}/libpapilo-devel.list

%changelog

%autochangelog
