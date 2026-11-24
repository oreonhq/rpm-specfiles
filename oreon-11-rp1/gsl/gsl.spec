# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 6a99eeed15632c6354895b1dd542ed5a855c0f15d9ad1326c6fe2b2c9e423190
%global source1_hash 4e48a4bb62ae9ec40185d52b3691a963c9dac6a317290eb80985cdbadcdf4476
%global source2_hash 754dbbaf2640bb8bc4fc3166918b9ba0f99ae438f5a6888e0ac8a082020eb9d6
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary: The GNU Scientific Library for numerical analysis
Name: gsl
Version: 2.8
Release: 1%{?dist}
URL: https://www.gnu.org/software/gsl/
VCS: git://git.savannah.gnu.org/gsl.git
License: GPL-3.0-or-later
Source0: https://ftp.gnu.org/gnu/gsl/%{name}-%{version}.tar.gz
Source1: https://ftp.gnu.org/gnu/gsl/%{name}-%{version}.tar.gz.sig
Source2: https://www.gnu.org/software/gsl/key/gsl_key.txt
Patch0: gsl-1.10-lib64.patch
Patch1: gsl-tol.patch
Patch2: gsl-test.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gnupg2
BuildRequires: pkgconfig
BuildRequires: make

%description
The GNU Scientific Library (GSL) is a collection of routines for
numerical analysis, written in C.

%package devel
Summary: Libraries and the header files for GSL development
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The gsl-devel package contains the header files necessary for 
developing programs using the GSL (GNU Scientific Library).

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -
%setup -q
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%patch -P0 -p1 -b .lib64
%patch -P1 -p1 -b .tol
%patch -P2 -p1 -b .test

%build
%ifarch aarch64 ppc64 ppc64le s390 s390x x86_64 riscv64
export CFLAGS="%{optflags} -ffp-contract=off"
%endif
%configure --disable-silent-rules --disable-static
%make_build

%check
make check || ( cat */test-suite.log && exit 1 )

%install
%make_install
rm -rf %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/*.la

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%{_bindir}/gsl-histogram
%{_bindir}/gsl-randist
%{_libdir}/libgsl.so.28*
%{_libdir}/libgslcblas.so.0*
%{_mandir}/man1/gsl-histogram.1*
%{_mandir}/man1/gsl-randist.1*

%files devel
%{_bindir}/gsl-config
%{_libdir}/libgsl.so
%{_libdir}/libgslcblas.so
%{_libdir}/pkgconfig/gsl.pc
%{_mandir}/man1/gsl-config.1*
%{_mandir}/man3/gsl.3*
%{_infodir}/gsl-ref.info*
%{_datadir}/aclocal/gsl.m4
%{_includedir}/gsl/

%changelog
%autochangelog
