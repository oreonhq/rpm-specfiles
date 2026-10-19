%global source0_hash 2523439ad448608e6e5167b69a0c5d721db2e30d5943188a9ca9f21baa0dd0a9
Name:		lis
Version:	2.1.11
Release:        1%{?dist}
Summary:        A library for solving linear equations and eigenvalue problems
License:	BSD
URL:		http://www.ssisc.org/lis/index.en.html
Source0:        http://www.ssisc.org/lis/dl/lis-%{version}.zip
Patch0:		lis-1.5.60-optflags.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  chrpath
BuildRequires:  gcc-gfortran
BuildRequires:  make
# /oreon:deps
%description
Lis, a Library of Iterative Solvers for linear systems, is a scalable parallel
library for solving systems of linear equations and standard eigenvalue
problems with real sparse matrices using iterative methods.

%package bin
Summary:	lis executables
%description bin
This package contains binaries shipped with the lis library.

%package devel
Summary:	Development headers and library for lis
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
Lis, a Library of Iterative Solvers for linear systems, is a scalable parallel
library for solving systems of linear equations and standard eigenvalue
problems with real sparse matrices using iterative methods.

This package contains the development headers and library.

%package doc
Summary:	Developer documentation for lis
BuildArch:  noarch
%description doc
Lis, a Library of Iterative Solvers for linear systems, is a scalable parallel
library for solving systems of linear equations and standard eigenvalue
problems with real sparse matrices using iterative methods.

This package contains the developer documentation for lis.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0 -b .optflags

%build

export CC=gcc
autoconf --force
mkdir -p omp
pushd omp
%global _configure ../configure
%configure --disable-static --enable-shared \
    --enable-saamg \
    --enable-quad --disable-rpath
make %{?_smp_mflags}
popd
%install
make -C omp install DESTDIR=%{buildroot}
chrpath --delete %{buildroot}%{_bindir}/*
rm %{buildroot}%{_libdir}/liblis.la
rm -rf %{buildroot}%{_datadir}/examples
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lis-bin -f %{oreon_filedir}/lis-bin.list
%files -n lis-devel -f %{oreon_filedir}/lis-devel.list
%files -n lis-doc -f %{oreon_filedir}/lis-doc.list

%changelog

%autochangelog
