%global source0_hash e2a1c711dc8ebc418e21195833814cb2f84b878b90a2774365f0166402308e08
%global blaslib openblas
Name:		qrupdate
Version:	1.1.2
Release:        35%{?dist}
Summary:        A Fortran library for fast updates of QR and Cholesky decompositions
License:	GPL-3.0-or-later
URL:		http://qrupdate.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  openblas-devel
# /oreon:deps
%description
qrupdate is a Fortran library for fast updates of QR and Cholesky
decompositions. 

%package devel
Summary:	Development libraries for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	%{blaslib}-devel%{?_isa}
%description devel
This package contains the development libraries for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# Modify install location
sed -i 's|$(PREFIX)/lib/|$(DESTDIR)%{_libdir}/|g' src/Makefile

%build

%make_build solib FC=gfortran FFLAGS="%{optflags} -fimplicit-none -funroll-loops -fallow-argument-mismatch $LDFLAGS" BLAS="-l%{blaslib}" LAPACK=
%install
make install-shlib LIBDIR=%{_libdir} PREFIX="%{buildroot}"
chmod 755 %{buildroot}%{_libdir}/libqrupdate.*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make test FC=gfortran FFLAGS="%{optflags} -fimplicit-none -funroll-loops -fallow-argument-mismatch $LDFLAGS" BLAS="-l%{blaslib}" LAPACK=
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n qrupdate-devel -f %{oreon_filedir}/qrupdate-devel.list

%changelog

%autochangelog
