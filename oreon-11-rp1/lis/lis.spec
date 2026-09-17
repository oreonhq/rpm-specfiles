%global source0_hash a674d645013e99f9239e95358f524836b074c2c285885d5a68155bb4e6e6c1a6

Name:		lis
Version:	2.0.21
Release:	13%{?dist}
Summary:	A library for solving linear equations and eigenvalue problems
License:	BSD
URL:		http://www.ssisc.org/lis/index.en.html
Source0:	http://www.ssisc.org/lis/dl/lis-%{version}.zip
# Disable use of -O3 -fomit-frame-pointer
Patch0:		lis-1.5.60-optflags.patch

BuildRequires:	autoconf
BuildRequires:	chrpath
BuildRequires:	gcc-gfortran
BuildRequires: make

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

# Get rid of RPATHs
# https://fedoraproject.org/wiki/Packaging:Guidelines#Beware_of_Rpath
chrpath --delete %{buildroot}%{_bindir}/*

# Get rid of .la file
rm %{buildroot}%{_libdir}/liblis.la

# .. and examples
rm -rf %{buildroot}%{_datadir}/examples

%ldconfig_scriptlets

%files
%doc AUTHORS
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_libdir}/liblis.so.*

%files bin
%{_bindir}/esolve
%{_bindir}/gesolve
%{_bindir}/esolver
%{_bindir}/gesolver
%{_bindir}/lsolve
%{_bindir}/spmvtest?
%{_bindir}/spmvtest?b
%{_bindir}/hpcg_kernel
%{_bindir}/hpcg_spmvtest
%{_mandir}/man1/esolve.1.*
%{_mandir}/man1/gesolve.1.*
%{_mandir}/man1/esolver.1.*
%{_mandir}/man1/gesolver.1.*
%{_mandir}/man1/lsolve.1.*
%{_mandir}/man1/spmvtest?.1.*
%{_mandir}/man1/spmvtest?b.1.*
%{_mandir}/man1/hpcg_kernel.1.*
%{_mandir}/man1/hpcg_spmvtest.1.*

%files devel
%{_includedir}/lis.h
%{_includedir}/lis_config.h
%{_includedir}/lisf.h
%{_libdir}/liblis.so

%files doc
%doc doc/*.pdf
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_mandir}/man3/lis*.3.*
%{_mandir}/man3/lis*.3f.*

%changelog
%autochangelog
