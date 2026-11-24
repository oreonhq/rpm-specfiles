# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash cd7e129868320cc2d033afa920e31202dfe0b8066a5b66661900ccc0f197dfed

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           openblas
Version:        0.3.34
Release:        1%{?dist}
Summary:        Optimized BLAS and LAPACK
License:        BSD-3-Clause
URL:            https://www.openblas.net
Source0:        https://github.com/OpenMathLib/OpenBLAS/releases/download/v%{version}/OpenBLAS-%{version}.tar.gz

BuildRequires:  oreon-rpm-macros
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  flang

%description
OpenBLAS is an optimized BLAS library based on GotoBLAS2, with LAPACK.

%package devel
Summary:        Development files for OpenBLAS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       pkgconfig(openblas) = %{version}-%{release}

%description devel
Headers, cmake files, and the pkg-config file for OpenBLAS.

%prep
%oreon_sha256
%autosetup -n OpenBLAS-%{version}

%build
FFLAGS=$(printf '%s\n' "$FFLAGS" | sed \
  -e 's/-fplugin=[^ ]*//g' \
  -e 's/-grecord-gcc-switches//g' \
  -e 's/-fexceptions//g' \
  -e 's/-Wp,-U_FORTIFY_SOURCE,-D_FORTIFY_SOURCE=[0-9]*//g' \
  -e 's/-Wp,-D_GLIBCXX_ASSERTIONS//g' \
  -e 's/-pipe//g' \
  -e 's/-fstack-protector-strong//g' \
  -e 's/-fasynchronous-unwind-tables//g' \
  -e 's/-fstack-clash-protection//g' \
  -e 's/-fcf-protection\(=[^ ]*\)\{0,1\}//g' \
  -e 's/-mtls-dialect=[^ ]*//g' \
  -e 's/-mno-omit-leaf-frame-pointer//g' \
  -e 's/-mbranch-protection=[^ ]*//g' \
  -e 's/-mbackchain//g' \
  -e 's/-mfpmath=[^ ]*//g' \
  -e 's/-mstackrealign//g' \
  -e 's/-msse2//g' \
  -e 's/-I[^ ]*gfortran\/modules//g')
FCFLAGS="$FFLAGS"
LDFLAGS=$(printf '%s\n' "$LDFLAGS" | sed \
  -e 's/--config=[^ ]*oreon-hardened-clang-ld.cfg//g')
export FFLAGS FCFLAGS LDFLAGS

%cmake \
  -DCMAKE_Fortran_COMPILER=flang \
  -DBUILD_SHARED_LIBS=ON \
  -DBUILD_STATIC_LIBS=OFF \
  -DBUILD_TESTING=ON \
%ifarch x86_64 aarch64 ppc64le
  -DDYNAMIC_ARCH=ON \
%endif
%ifarch x86_64 %{ix86}
  -DTARGET=GENERIC \
%endif
%ifarch aarch64
  -DTARGET=ARMV8 \
%endif
%ifarch %{arm}
  -DTARGET=ARMV7 \
%endif
%ifarch ppc64le
  -DTARGET=POWER8 \
%endif
%ifarch ppc64
  -DTARGET=PPC970MP \
%endif
%ifarch riscv64
  -DTARGET=RISCV64_GENERIC \
%endif
%ifarch s390x
  -DTARGET=ZARCH_GENERIC \
%endif
%ifarch %{ix86}
  -DBINARY=32 \
%else
  -DBINARY=64 \
%endif
  -DNO_AFFINITY=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%{_libdir}/libopenblas.so.0
%{_libdir}/libopenblas.so.0.*

%files devel
%{_includedir}/openblas/
%{_libdir}/libopenblas.so
%{_libdir}/pkgconfig/openblas.pc
%{_libdir}/cmake/OpenBLAS/

%changelog
%autochangelog
