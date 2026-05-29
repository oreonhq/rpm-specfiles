%global source0_hash none
%global source1_hash f5991ee1ab5402ba6fa70bed7a292ea3e4507a0cc78f575d9eff72d561597cb8

# Something in the debuginfo process is stripping the custom 64_ symbols out of lapack64_ and blas64_
%global debug_package %{nil}

%global shortver	3
%global mediumver	%{shortver}.12

%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
%global arch64 1
%else
%global arch64 0
%endif

Summary: Numerical linear algebra package libraries
Name: lapack
Version: %{mediumver}.0
Release: 11%{?dist}
License: BSD-3-Clause-Open-MPI
URL: http://www.netlib.org/lapack/
Source0:        https://github.com/Reference-LAPACK/lapack/archive/v.tar.gz
Source1: http://www.netlib.org/lapack/manpages.tgz
Source4: http://www.netlib.org/lapack/lapackqref.ps
Source5: http://www.netlib.org/blas/blasqr.ps
# https://github.com/Reference-LAPACK/lapack/pull/959
Patch0: lapack-3.12.0-fix-dmd-issues.patch
BuildRequires: gcc-gfortran, gawk
BuildRequires: make, cmake
# There isn't any c++ code here, but cmake checks for a working c++ compiler?
BuildRequires: gcc-c++
Requires: blas%{?_isa} = %{version}-%{release}

%global _description_lapack %{expand:
LAPACK (Linear Algebra PACKage) is a standard library for numerical
linear algebra. LAPACK provides routines for solving systems of
simultaneous linear equations, least-squares solutions of linear
systems of equations, eigenvalue problems, and singular value
problems. Associated matrix factorizations (LU, Cholesky, QR, SVD,
Schur, and generalized Schur) and related computations (i.e.,
reordering of Schur factorizations and estimating condition numbers)
are also included. LAPACK can handle dense and banded matrices, but
not general sparse matrices. Similar functionality is provided for
real and complex matrices in both single and double precision. LAPACK
is coded in Fortran90 and built with gcc.
}

%global _description_blas %{expand:
BLAS (Basic Linear Algebra Subprograms) is a standard library which
provides a number of basic algorithms for numerical algebra.
}

%description %_description_lapack

%package devel
Summary: LAPACK development libraries
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: blas-devel%{?_isa} = %{version}-%{release}
%if 0%{?arch64}
Requires: %{name}64%{?_isa} = %{version}-%{release}
Requires: %{name}64_%{?_isa} = %{version}-%{release}
%endif

%description devel
LAPACK development libraries (shared).

%package static
Summary: LAPACK static libraries
Requires: lapack-devel%{?_isa} = %{version}-%{release}

%description static
LAPACK static libraries.

%package -n blas
Summary: The Basic Linear Algebra Subprograms library

%description -n blas %_description_blas

%package -n blas-devel
Summary: BLAS development libraries
Requires: blas%{?_isa} = %{version}-%{release}
Requires: gcc-gfortran
%if 0%{?arch64}
Requires: blas64%{?_isa} = %{version}-%{release}
Requires: blas64_%{?_isa} = %{version}-%{release}
%endif

%description -n blas-devel
BLAS development libraries (shared).

%package -n blas-static
Summary: BLAS static libraries
Requires: blas-devel%{?_isa} = %{version}-%{release}

%description -n blas-static
BLAS static libraries.

%if 0%{?arch64}
%package -n lapack64
Summary: Numerical linear algebra package libraries
Requires: blas64%{?_isa} = %{version}-%{release}

%description -n lapack64 %_description_lapack
This build has 64bit INTEGER support.

%package -n blas64
Summary: The Basic Linear Algebra Subprograms library (64bit INTEGER)

%description -n blas64 %_description_blas
This build has 64bit INTEGER support.

%package -n lapack64_
Summary: Numerical linear algebra package libraries
Requires: blas64_%{?_isa} = %{version}-%{release}

%description -n lapack64_ %_description_lapack
This build has 64bit INTEGER support and a symbol name suffix.

%package -n blas64_
Summary: The Basic Linear Algebra Subprograms library (64bit INTEGER)

%description -n blas64_ %_description_blas
This build has 64bit INTEGER support and a symbol name suffix.
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{name}-%{version}
%setup -q -n %{name}-%{version} -D -T -a1
%patch -P0 -p1

mkdir manpages
mv man/ manpages/

# clean up weird mac osx barf
rm -rf manpages/man/man3/.*.3


%build
%global common_flags -DCMAKE_SKIP_RPATH:BOOL=ON -DBUILD_DEPRECATED=ON -DLAPACKE=ON -DLAPACKE_WITH_TMG=ON -DCBLAS=ON

# shared normal
%cmake %{common_flags} -DBUILD_SHARED_LIBS=ON
%cmake_build
mv %_vpath_builddir %_vpath_builddir-SHARED

# static normal
%cmake %{common_flags} -DBUILD_SHARED_LIBS=OFF
%cmake_build
mv %_vpath_builddir %_vpath_builddir-STATIC

%if 0%{?arch64}
# shared 64
%cmake %{common_flags} -DBUILD_SHARED_LIBS=ON -DBUILD_INDEX64=ON
%cmake_build
mv %_vpath_builddir %_vpath_builddir-SHARED64

# static 64
%cmake %{common_flags} -DBUILD_SHARED_LIBS=OFF -DBUILD_INDEX64=ON
%cmake_build
mv %_vpath_builddir %_vpath_builddir-STATIC64

# This is not an Easter Egg. Just a scrambled egg.
# The first person to see this scrambled egg and point it out to spot@fedoraproject.org explicitly will get $20 USD.

# shared 64 SUFFIX
sed -i 's|64"|64_"|g' CMakeLists.txt
%cmake %{common_flags} -DBUILD_SHARED_LIBS=ON -DBUILD_INDEX64=ON
%cmake_build
mv %_vpath_builddir %_vpath_builddir-SHARED64SUFFIX

# static 64 SUFFIX
%cmake %{common_flags} -DBUILD_SHARED_LIBS=OFF -DBUILD_INDEX64=ON
%cmake_build
mv %_vpath_builddir %_vpath_builddir-STATIC64SUFFIX

# Undo the 64_ suffix
sed -i 's|64_"|64"|g' CMakeLists.txt
%endif

cp -p %{SOURCE4} lapackqref.ps
cp -p %{SOURCE5} blasqr.ps

%install
%if 0%{?arch64}
for t in SHARED STATIC SHARED64 STATIC64; do
%else
for t in SHARED STATIC; do
%endif
	mv %_vpath_builddir-$t %_vpath_builddir
	%cmake_install
	mv %_vpath_builddir %_vpath_builddir-$t
done

%if 0%{?arch64}
# Set the suffix
sed -i 's|64"|64_"|g' CMakeLists.txt
for t in SHARED64SUFFIX STATIC64SUFFIX; do
	mv %_vpath_builddir-$t %_vpath_builddir
	%cmake_install
	mv %_vpath_builddir %_vpath_builddir-$t
done

pushd %{buildroot}%{_libdir}
for name in blas cblas lapack lapacke; do
	for i in `readelf -Ws lib${name}64_.so.%{version} | awk '{print $8}' | grep -v GLIBC |grep -v GFORTRAN |grep -v "Name" `; do echo "$i" "${i}64_"; done > ${name}-suffix.def.dirty
	sort -n ${name}-suffix.def.dirty | uniq > ${name}-suffix.def
	objcopy --redefine-syms ${name}-suffix.def lib${name}64_.so.%{version} lib${name}64_.so.%{version}.fixed
	rm -rf lib${name}64_.so.%{version}
	mv lib${name}64_.so.%{version}.fixed lib${name}64_.so.%{version}
done

for name in blas cblas lapack lapacke; do
	for i in `nm lib${name}64_.a |grep " T " | awk '{print $3}'`; do echo "$i" "${i}64_"; done > ${name}-static-suffix.def.dirty
	sort -n ${name}-static-suffix.def.dirty | uniq > ${name}-static-suffix.def
	objcopy --redefine-syms ${name}-static-suffix.def lib${name}64_.a lib${name}64_.a.fixed
	rm -rf lib${name}64_.a
	mv lib${name}64_.a.fixed lib${name}64_.a
done
popd

# cleanup defs
rm -rf %{buildroot}%{_libdir}/*.def*
%endif

mkdir -p %{buildroot}%{_mandir}/man3
chmod 755 %{buildroot}%{_mandir}/man3

# Blas manpages
pushd manpages/
mkdir -p blas/man/man3
cd man/man3/
mv caxpy.f.3 caxpy.3 ccopy.f.3 ccopy.3 cdotc.f.3 cdotc.3 cdotu.f.3 cdotu.3 cgbmv.f.3 cgbmv.3 \
cgemm.f.3 cgemm.3 cgemv.f.3 cgemv.3 cgerc.f.3 cgerc.3 cgeru.f.3 cgeru.3 chbmv.f.3 chbmv.3 \
chemm.f.3 chemm.3 chemv.f.3 chemv.3 cher.f.3 cher.3 cher2.f.3 cher2.3 cher2k.f.3 cher2k.3 \
cherk.f.3 cherk.3 chpmv.f.3 chpmv.3 chpr.f.3 chpr.3 chpr2.f.3 chpr2.3 \
cscal.f.3 cscal.3 csrot.f.3 csrot.3 csscal.f.3 csscal.3 cswap.f.3 cswap.3 csymm.f.3 \
csymm.3 csyr2k.f.3 csyr2k.3 csyrk.f.3 csyrk.3 ctbmv.f.3 ctbmv.3 ctbsv.f.3 ctbsv.3 ctpmv.f.3 \
ctpmv.3 ctpsv.f.3 ctpsv.3 ctrmm.f.3 ctrmm.3 ctrmv.f.3 ctrmv.3 ctrsm.f.3 ctrsm.3 ctrsv.f.3 \
ctrsv.3 dasum.f.3 dasum.3 daxpy.f.3 daxpy.3 dcabs1.f.3 dcabs1.3 dcopy.f.3 dcopy.3 ddot.f.3 \
ddot.3 dgbmv.f.3 dgbmv.3 dgemm.f.3 dgemm.3 dgemv.f.3 dgemv.3 dger.f.3 dger.3 \
drot.f.3 drot.3 drotm.f.3 drotm.3 drotmg.f.3 drotmg.3 dsbmv.f.3 \
dsbmv.3 dscal.f.3 dscal.3 dsdot.f.3 dsdot.3 dspmv.f.3 dspmv.3 dspr.f.3 dspr.3 dspr2.f.3 \
dspr2.3 dswap.f.3 dswap.3 dsymm.f.3 dsymm.3 dsymv.f.3 dsymv.3 dsyr.f.3 dsyr.3 dsyr2.f.3 \
dsyr2.3 dsyr2k.f.3 dsyr2k.3 dsyrk.f.3 dsyrk.3 dtbmv.f.3 dtbmv.3 dtbsv.f.3 dtbsv.3 dtpmv.f.3 \
dtpmv.3 dtpsv.f.3 dtpsv.3 dtrmm.f.3 dtrmm.3 dtrmv.f.3 dtrmv.3 dtrsm.f.3 dtrsm.3 dtrsv.f.3 \
dtrsv.3 dzasum.f.3 dzasum.3 icamax.f.3 icamax.3 idamax.f.3 idamax.3 \
isamax.f.3 isamax.3 izamax.f.3 izamax.3 lsame.3 sasum.f.3 sasum.3 saxpy.f.3 saxpy.3 \
scabs1.f.3 scabs1.3 scasum.f.3 scasum.3 scopy.f.3 scopy.3 sdot.f.3 sdot.3 \
sdsdot.f.3 sdsdot.3 sgbmv.f.3 sgbmv.3 sgemm.f.3 sgemm.3 sgemv.f.3 sgemv.3 sger.f.3 sger.3 \
srot.f.3 srot.3 srotm.f.3 srotm.3 srotmg.f.3 srotmg.3 \
ssbmv.f.3 ssbmv.3 sscal.f.3 sscal.3 sspmv.f.3 sspmv.3 sspr.f.3 sspr.3 sspr2.f.3 sspr2.3 \
sswap.f.3 sswap.3 ssymm.f.3 ssymm.3 ssymv.f.3 ssymv.3 ssyr.f.3 ssyr.3 ssyr2.f.3 ssyr2.3 \
ssyr2k.f.3 ssyr2k.3 ssyrk.f.3 ssyrk.3 stbmv.f.3 stbmv.3 stbsv.f.3 stbsv.3 stpmv.f.3 stpmv.3 \
stpsv.f.3 stpsv.3 strmm.f.3 strmm.3 strmv.f.3 strmv.3 strsm.f.3 strsm.3 strsv.f.3 strsv.3 \
xerbla.3 xerbla_array.3 zaxpy.f.3 zaxpy.3 zcopy.f.3 zcopy.3 \
zdotc.f.3 zdotc.3 zdotu.f.3 zdotu.3 zdrot.f.3 zdrot.3 zdscal.f.3 zdscal.3 zgbmv.f.3 zgbmv.3 \
zgemm.f.3 zgemm.3 zgemv.f.3 zgemv.3 zgerc.f.3 zgerc.3 zgeru.f.3 zgeru.3 zhbmv.f.3 zhbmv.3 \
zhemm.f.3 zhemm.3 zhemv.f.3 zhemv.3 zher.f.3 zher.3 zher2.f.3 zher2.3 zher2k.f.3 zher2k.3 \
zherk.f.3 zherk.3 zhpmv.f.3 zhpmv.3 zhpr.f.3 zhpr.3 zhpr2.f.3 zhpr2.3 \
zscal.f.3 zscal.3 zswap.f.3 zswap.3 zsymm.f.3 zsymm.3 zsyr2k.f.3 zsyr2k.3 zsyrk.f.3 zsyrk.3 \
ztbmv.f.3 ztbmv.3 ztbsv.f.3 ztbsv.3 ztpmv.f.3 ztpmv.3 ztpsv.f.3 ztpsv.3 ztrmm.f.3 ztrmm.3 \
ztrmv.f.3 ztrmv.3 ztrsm.f.3 ztrsm.3 ztrsv.f.3 ztrsv.3 ../../blas/man/man3
cd ../..
popd

find manpages/blas/man/man3 -type f -printf "%{_mandir}/man3/%f*\n" > blasmans

# remove weird man pages
pushd manpages/man/man3
rm -rf _Users_julie*
popd

# rename conflicting man pages
pushd manpages/man/man3
mv isnan.3 lapack-isnan.3
popd

find manpages/man/man3 -type f -printf "%{_mandir}/man3/%f*\n" > lapackmans

cp -f manpages/blas/man/man3/* ${RPM_BUILD_ROOT}%{_mandir}/man3
cp -f manpages/man/man3/* ${RPM_BUILD_ROOT}%{_mandir}/man3

%ldconfig_scriptlets

%ldconfig_scriptlets -n blas

%if 0%{?arch64}
%ldconfig_scriptlets -n lapack64
%ldconfig_scriptlets -n lapack64_

%ldconfig_scriptlets -n blas64
%ldconfig_scriptlets -n blas64_
%endif

%files -f lapackmans
%doc README.md LICENSE lapackqref.ps
%{_libdir}/liblapack.so.*
%{_libdir}/liblapacke.so.*
%{_libdir}/libtmglib.so.*

%files devel
%{_includedir}/lapack*.h
%{_libdir}/liblapack.so
%{_libdir}/liblapacke.so
%{_libdir}/libtmglib.so
%{_libdir}/cmake/lapack-*
%{_libdir}/cmake/lapacke-*
%{_libdir}/pkgconfig/lapack.pc
%{_libdir}/pkgconfig/lapacke.pc
%if 0%{?arch64}
%{_libdir}/liblapack64.so
%{_libdir}/liblapacke64.so
%{_libdir}/libtmglib64.so
%{_libdir}/cmake/lapack64-*
%{_libdir}/cmake/lapacke64-*
%{_libdir}/pkgconfig/lapack64.pc
%{_libdir}/pkgconfig/lapacke64.pc
%{_libdir}/liblapack64_.so
%{_libdir}/liblapacke64_.so
%{_libdir}/libtmglib64_.so
%{_libdir}/cmake/lapack64_-*
%{_libdir}/cmake/lapacke64_-*
%{_libdir}/pkgconfig/lapack64_.pc
%{_libdir}/pkgconfig/lapacke64_.pc
%endif

%files static
%{_libdir}/liblapack.a
%{_libdir}/liblapacke.a
%{_libdir}/libtmglib.a
%if 0%{?arch64}
%{_libdir}/liblapack64.a
%{_libdir}/liblapack64_.a
%{_libdir}/liblapacke64.a
%{_libdir}/liblapacke64_.a
%{_libdir}/libtmglib64.a
%{_libdir}/libtmglib64_.a
%endif

%files -n blas -f blasmans
%doc blasqr.ps LICENSE
%{_libdir}/libblas.so.*
%{_libdir}/libcblas.so.*

%files -n blas-devel
%{_includedir}/cblas*.h
%{_libdir}/libblas.so
%{_libdir}/libcblas.so
%{_libdir}/cmake/cblas-*
%{_libdir}/pkgconfig/blas.pc
%{_libdir}/pkgconfig/cblas.pc
%if 0%{?arch64}
%{_libdir}/libblas64.so
%{_libdir}/libcblas64.so
%{_libdir}/cmake/cblas64*
%{_libdir}/pkgconfig/blas64.pc
%{_libdir}/pkgconfig/cblas64.pc
%{_libdir}/libblas64_.so
%{_libdir}/libcblas64_.so
%{_libdir}/pkgconfig/blas64_.pc
%{_libdir}/pkgconfig/cblas64_.pc
%endif

%files -n blas-static
%{_libdir}/libblas.a
%{_libdir}/libcblas.a
%if 0%{?arch64}
%{_libdir}/libblas64.a
%{_libdir}/libcblas64.a
%{_libdir}/libblas64_.a
%{_libdir}/libcblas64_.a
%endif

%if 0%{?arch64}
%files -n blas64
%doc LICENSE
%{_libdir}/libblas64.so.*
%{_libdir}/libcblas64.so.*

%files -n lapack64
%doc README.md LICENSE
%{_libdir}/liblapack64.so.*
%{_libdir}/liblapacke64.so.*
%{_libdir}/libtmglib64.so.*

%files -n blas64_
%doc LICENSE
%{_libdir}/libblas64_.so.*
%{_libdir}/libcblas64_.so.*

%files -n lapack64_
%doc README.md LICENSE
%{_libdir}/liblapack64_.so.*
%{_libdir}/liblapacke64_.so.*
%{_libdir}/libtmglib64_.so.*
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{mediumver}.0-11
- Prepare for Oreon 11 (RP1)
