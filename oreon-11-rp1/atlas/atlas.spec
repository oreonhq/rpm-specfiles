%global source0_hash 2688eb733a6c5f78a18ef32144039adcd62fabce66f2eb51dd59dde806a6d2b7
%global source12_hash none

%define enable_native_atlas 0
%global build_type_safety_c 0

Name:           atlas
Version:        3.10.3
%if "%{?enable_native_atlas}" != "0"
%define dist .native
%endif
Release:        32%{?dist}
Summary:        Automatically Tuned Linear Algebra Software

License:        BSD-3-Clause
URL:            http://math-atlas.sourceforge.net/
Source0:        https://downloads.sourceforge.net/math-atlas/%{name}%{version}.tar.bz2
Source2:        README.dist
# arch lapack refs from ubuntu/debian atlas packaging
Source12:        https://archive.ubuntu.com/ubuntu/pool/universe/a/atlas/atlas_3.10.3-13ubuntu1.debian.tar.xz
# Properly pass -melf_* to the linker with -Wl, fixes FTBFS bug 817552
# https://sourceforge.net/tracker/?func=detail&atid=379484&aid=3555789&group_id=23725
Patch1:        atlas-melf.patch
Patch2:        atlas-throttling.patch

#credits Lukas Slebodnik
Patch3:        atlas-shared_libraries.patch

Patch4:        atlas-genparse.patch

# Unbundle LAPACK (BZ #1181369)
Patch5:        atlas.3.10.1-unbundle.patch
Patch6:        atlas-gcc10.patch


#patches dealing with z{13,14,15}, provided by IBM
Patch7:        0001-Avoid-c99-standard-compiler.patch
Patch8:        0002-Fix-rpath-link-command-line-options.patch
Patch9:        0003-Fix-SIMD-support-on-IBM-z13.patch
Patch10:        0004-Read-L1-data-cache-size-from-sysconf-if-possible.patch
Patch11:        0005-Optimizations-for-IBM-z13.patch
Patch12:        0006-Add-IBM-z14-support.patch
Patch13:        0007-Enable-cross-compile.patch
Patch14:        0008-Add-IBM-z15-support.patch



Patch15:        atlas-fgrep.patch
#Covscan
Patch101:        atlas-getri.patch

BuildRequires: make
BuildRequires:  gcc-gfortran, lapack-static, gcc

%ifarch x86_64
Obsoletes:      atlas-sse3 < 3.10.3-1
%endif

%ifarch %{ix86}
Obsoletes:      atlas-3dnow < 3.10.3-1
Obsoletes:      atlas-sse < 3.10.3-1
Obsoletes:      atlas-sse2 < 3.10.3-1
Obsoletes:      atlas-sse3 < 3.10.3-1
%endif

%ifarch s390 s390x
Obsoletes:      atlas-z10 < 3.10.3-11
Obsoletes:      atlas-z196 < 3.10.3-11
%endif


%description
The ATLAS (Automatically Tuned Linear Algebra Software) project is an
ongoing research effort f(ocusing on applying empirical techniques in
order to provide portable performance. At present, it provides C and
Fortran77 interfaces to a portably efficient BLAS implementation, as
well as a few routines from LAPACK.

The performance improvements in ATLAS are obtained largely via
compile-time optimizations and tend to be specific to a given hardware
configuration. In order to package ATLAS some compromises
are necessary so that good performance can be obtained on a variety
of hardware. This set of ATLAS binary packages is therefore not
necessarily optimal for any specific hardware configuration.  However,
the source package can be used to compile customized ATLAS packages;
see the documentation for information.

%package devel
Summary:        Development libraries for ATLAS
Requires:       %{name} = %{version}-%{release}
Obsoletes:	%name-header <= %version-%release
Requires(posttrans):	/usr/sbin/alternatives
Requires(postun):	/usr/sbin/alternatives

%ifarch x86_64
Obsoletes:      atlas-sse3-devel < 3.10.3-1
%endif

%ifarch %{ix86}
Obsoletes:      atlas-3dnow-devel < 3.10.3-1
Obsoletes:      atlas-sse-devel < 3.10.3-1
Obsoletes:      atlas-sse2-devel < 3.10.3-1
Obsoletes:      atlas-sse3-devel < 3.10.3-1
%endif

%ifarch s390 s390x
Obsoletes:      atlas-z10-devel < 3.10.3-11
Obsoletes:      atlas-z196-devel < 3.10.3-11
%endif

%description devel
This package contains headers for development with ATLAS
(Automatically Tuned Linear Algebra Software).

%package static
Summary:        Static libraries for ATLAS
Requires:       %{name}-devel = %{version}-%{release}
Requires(posttrans):	/usr/sbin/alternatives
Requires(postun):	/usr/sbin/alternatives

%ifarch x86_64
Obsoletes:      atlas-sse3-static < 3.10.3-1
%endif

%ifarch %{ix86}
Obsoletes:      atlas-3dnow-static < 3.10.3-1
Obsoletes:      atlas-sse-static < 3.10.3-1
Obsoletes:      atlas-sse2-static < 3.10.3-1
Obsoletes:      atlas-sse3-static < 3.10.3-1
%endif

%ifarch s390 s390x
Obsoletes:      atlas-z10-static < 3.10.3-11
Obsoletes:      atlas-z196-static  < 3.10.3-11
%endif

%description static
This package contains static version of ATLAS (Automatically Tuned
Linear Algebra Software).


%define types base

%if "%{?enable_native_atlas}" == "0"
############## Subpackages for architecture extensions #################
#
%ifarch x86_64
%define types base corei2

%package corei2-static
Summary:        ATLAS libraries for Corei2 (Ivy/Sandy bridge) CPUs

%description corei2-static
This package contains the ATLAS (Automatically Tuned Linear Algebra
Software) static libraries compiled with optimizations for the Corei2 (Ivy/Sandy bridge)
CPUs. The base ATLAS builds for the x86_64 architecture are made for the hammer64 CPUs.

%package corei2
Summary:        ATLAS libraries for Corei2 (Ivy/Sandy bridge) CPUs

%description corei2
This package contains the ATLAS (Automatically Tuned Linear Algebra
Software) libraries compiled with optimizations for the Corei2 (Ivy/Sandy bridge)
CPUs. The base ATLAS builds for the x86_64 architecture are made for the hammer64 CPUs.

%package corei2-devel
Summary:        Development libraries for ATLAS for Corei2 (Ivy/Sandy bridge) CPUs
Requires:       %{name}-corei2 = %{version}-%{release}
Obsoletes:	%name-header <= %version-%release
Requires(posttrans):	/usr/sbin/alternatives
Requires(postun):	/usr/sbin/alternatives

%description corei2-devel
This package contains shared and static versions of the ATLAS
(Automatically Tuned Linear Algebra Software) libraries compiled with
optimizations for the corei2 (Ivy/Sandy bridge) CPUs.
%endif

%ifarch %{ix86}
%define types base

%endif

%ifarch s390 s390x
%define types base z14 z15

%package z14
Summary:        ATLAS libraries for z14
Group:          System Environment/Libraries

%description z14
This package contains ATLAS (Automatically Tuned Linear Algebra Software)
shared libraries compiled with optimizations for the z14 CPUs.

%package z14-devel
Summary:        Development libraries for ATLAS for z14
Group:          Development/Libraries
Requires:       %{name}-z14 = %{version}-%{release}
Obsoletes:	%name-header <= %version-%release
Requires(posttrans):	chkconfig
Requires(postun):	chkconfig

%description z14-devel
This package contains shared and static versions of the ATLAS
(Automatically Tuned Linear Algebra Software) libraries compiled with
optimizations for the z14 CPUs.

%package z14-static
Summary:        Static libraries for ATLAS for z14
Group:          Development/Libraries
Requires:       %{name}-z14-devel = %{version}-%{release}
Requires(posttrans):	chkconfig
Requires(postun):	chkconfig

%description z14-static
This package contains the ATLAS (Automatically Tuned Linear Algebra
Software) static libraries compiled with optimizations for the z14
CPUs.


%package z15
Summary:        ATLAS libraries for z15
Group:          System Environment/Libraries

%description z15
This package contains ATLAS (Automatically Tuned Linear Algebra Software)
shared libraries compiled with optimizations for the z15 CPUs.

%package z15-devel
Summary:        Development libraries for ATLAS for z15
Group:          Development/Libraries
Requires:       %{name}-z15 = %{version}-%{release}
Obsoletes:	%name-header <= %version-%release
Requires(posttrans):	chkconfig
Requires(postun):	chkconfig

%description z15-devel
This package contains shared and static versions of the ATLAS
(Automatically Tuned Linear Algebra Software) libraries compiled with
optimizations for the z15 CPUs.

%package z15-static
Summary:        Static libraries for ATLAS for z15
Group:          Development/Libraries
Requires:       %{name}-z15-devel = %{version}-%{release}
Requires(posttrans):	chkconfig
Requires(postun):	chkconfig

%description z15-static
This package contains the ATLAS (Automatically Tuned Linear Algebra
Software) static libraries compiled with optimizations for the z15
CPUs.
%endif


%ifarch ppc64
%define types base power7 power8

%package power8
Summary:        ATLAS libraries for Power 8

%description power8
This package contains ATLAS (Automatically Tuned Linear Algebra Software)
shared libraries compiled with optimizations for the Power 8 CPUs. 
The base ATLAS builds for the ppc64 architecture are made for Power 5 CPUs.

%package power8-devel
Summary:        Development libraries for ATLAS for Power 8
Requires:       %{name}-power8 = %{version}-%{release}
Obsoletes:	%name-header <= %version-%release
Requires(posttrans):	/usr/sbin/alternatives
Requires(postun):	/usr/sbin/alternatives

%description power8-devel
This package contains shared and static versions of the ATLAS
(Automatically Tuned Linear Algebra Software) libraries compiled with
optimizations for the Power 8 CPUs.

%package power8-static
Summary:        Static libraries for ATLAS for Power 8
Requires:       %{name}-power8-devel = %{version}-%{release}
Requires(posttrans):	/usr/sbin/alternatives
Requires(postun):	/usr/sbin/alternatives

%description power8-static
This package contains the ATLAS (Automatically Tuned Linear Algebra
Software) static libraries compiled with optimizations for the Power 8
CPUs. The base ATLAS builds for the ppc64 architecture are made for the Power 5 CPUs.

%package power7
Summary:        ATLAS libraries for Power 7

%description power7
This package contains ATLAS (Automatically Tuned Linear Algebra Software)
shared libraries compiled with optimizations for the Power 7 CPUs. 
The base ATLAS builds for the ppc64 architecture are made for Power 5 CPUs.

%package power7-devel
Summary:        Development libraries for ATLAS for Power 7
Requires:       %{name}-power7 = %{version}-%{release}
Obsoletes:	%name-header <= %version-%release
Requires(posttrans):	/usr/sbin/alternatives
Requires(postun):	/usr/sbin/alternatives

%description power7-devel
This package contains shared and static versions of the ATLAS
(Automatically Tuned Linear Algebra Software) libraries compiled with
optimizations for the Power 7 CPUs.

%package power7-static
Summary:        Static libraries for ATLAS for Power 7
Requires:       %{name}-power7-devel = %{version}-%{release}
Requires(posttrans):	/usr/sbin/alternatives
Requires(postun):	/usr/sbin/alternatives

%description power7-static
This package contains the ATLAS (Automatically Tuned Linear Algebra
Software) static libraries compiled with optimizations for the Power 7
CPUs. The base ATLAS builds for the ppc64 architecture are made for the Power 5 CPUs.

%endif
#end of enable_native_atlas if
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source12_hash}" = "none" || { f="%{SOURCE12}"; test -f "$f" || { echo "oreon: missing Source12 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source12_hash}" || { echo "oreon: Source12 hash mismatch" >&2; exit 1; }; }
%setup -q -n ATLAS


%patch 1 -p1
%patch 2 -p1
%patch 3 -p2
%patch 4 -p1
%patch 5 -p1
%patch 6 -p1

%patch 7 -p1
%patch 8 -p1
%patch 10 -p1

%ifarch s390x s390
%patch 9 -p1
%patch 11 -p1
%patch 12 -p1
%patch 13 -p1
%patch 14 -p1
%endif

%patch 15 -p1
%patch 101 -p1

cp %{SOURCE2} doc
tar -xJf %{SOURCE12} debian/archdefs
find debian/archdefs -type f \( -name '*.tgz' -o -name '*.tar.bz2' \) -exec cp -t CONFIG/ARCHS/ {} +
rm -rf debian

%ifarch %{arm}
sed -i -e 's,-mfloat-abi=softfp,-mfloat-abi=hard,' CONFIG/src/atlcomp.txt
%endif

sed -i -e 's,MYFLAGS =,MYFLAGS = -fpermissive,' CONFIG/src/Makefile
# Generate lapack library
mkdir lapacklib
cd lapacklib
ar x %{_libdir}/liblapack_pic.a
# Remove functions that have ATLAS implementations
rm -f cgelqf.f.o cgels.f.o cgeqlf.f.o cgeqrf.f.o cgerqf.f.o cgesv.f.o cgetrf.f.o cgetri.f.o cgetrs.f.o clarfb.f.o clarft.f.o clauum.f.o cposv.f.o cpotrf.f.o cpotri.f.o cpotrs.f.o ctrtri.f.o dgelqf.f.o dgels.f.o dgeqlf.f.o dgeqrf.f.o dgerqf.f.o dgesv.f.o dgetrf.f.o dgetri.f.o dgetrs.f.o dlamch.f.o dlarfb.f.o dlarft.f.o dlauum.f.o dposv.f.o dpotrf.f.o dpotri.f.o dpotrs.f.o dtrtri.f.o ieeeck.f.o ilaenv.f.o lsame.f.o sgelqf.f.o sgels.f.o sgeqlf.f.o sgeqrf.f.o sgerqf.f.o sgesv.f.o sgetrf.f.o sgetri.f.o sgetrs.f.o slamch.f.o slarfb.f.o slarft.f.o slauum.f.o sposv.f.o spotrf.f.o spotri.f.o spotrs.f.o strtri.f.o xerbla.f.o zgelqf.f.o zgels.f.o zgeqlf.f.o zgeqrf.f.o zgerqf.f.o zgesv.f.o zgetrf.f.o zgetri.f.o zgetrs.f.o zlarfb.f.o zlarft.f.o zlauum.f.o zposv.f.o zpotrf.f.o zpotri.f.o zpotrs.f.o ztrtri.f.o 
# Create new library
ar rcs ../liblapack_pic_pruned.a *.o
cd ..


%build
p=$(pwd)
%undefine _strict_symbol_defs_build
%ifarch %{arm}
%global mode %{nil}
%else
%global mode -b %{__isa_bits}
%endif

%define arg_options %{nil}
%define flags %{nil}
%define threads_option "-t 2"

#Target architectures for the 'base' versions
%ifarch s390x
%define flags %{nil}
%define base_options "-A IBMz12 -V 1"
#%define base_options "-A IBMz13 -V 8 -Si archdef 2"
%endif

%ifarch x86_64
%define flags %{nil}
%define base_options "-A HAMMER -V 896"
%endif

%ifarch %ix86
%define flags %{nil}
%define base_options "-A PIII -V 512"
%endif

%ifarch ppc
%define flags %{nil}
%define base_options "-A POWER5 -V 1"
%endif

%ifarch ppc64
%define flags %{nil}
%define base_options "-A POWER5 -V 1"
%endif

%ifarch ppc64le
%define flags %{nil}
%define base_options "-A POWER8 -V 1"
%endif

%ifarch %{arm}
%define flags "-DATL_ARM_HARDFP=1"
%define base_options "-A ARMa7 -V 1"
%endif

%ifarch aarch64
%define flags %{nil}
%define base_options "-A ARM64a53 -V 1"
%endif

%if "%{?enable_native_atlas}" != "0"
%define	threads_option %{nil}
%define base_options %{nil}
%define flags %{nil}
%endif

for type in %{types}; do
	if [ "$type" = "base" ]; then
		libname=atlas
		arg_options=%{base_options}
		thread_options=%{threads_option}
		%define pr_base %(echo $((%{__isa_bits}+0)))
	else
		libname=atlas-${type}
		if [ "$type" = "corei2" ]; then
			thread_options="-t 4"
			arg_options="-A Corei2 -V 896"
			%define pr_corei2 %(echo $((%{__isa_bits}+2)))
		elif [ "$type" = "corei1" ]; then
			arg_options="-A Corei1 -V 896"
			%define pr_corei1 %(echo $((%{__isa_bits}+2)))
		elif [ "$type" = "z14" ]; then
			  thread_options="-t 4"
			  arg_options="-A IBMz14 -V 4 -Si archdef 2"
			  %define pr_z14 %(echo $((%{__isa_bits}+2)))
		elif [ "$type" = "z15" ]; then
			  thread_options="-t 4"
			  arg_options="-A IBMz15 -V 4 -Si archdef 2"
			  %define pr_z15 %(echo $((%{__isa_bits}+4)))
		elif [ "$type" = "power7" ]; then
			thread_options="-t 4"
			arg_options="-A POWER7 -V 1"
			%define pr_power7 %(echo $((%{__isa_bits}+2)))
		elif [ "$type" = "power8" ]; then
			thread_options="-t 4"
			arg_options="-A POWER8 -V 1"
			%define pr_power8 %(echo $((%{__isa_bits}+4)))
		fi
	fi
	mkdir -p %{_arch}_${type}
	pushd %{_arch}_${type}
	../configure  %{mode} $thread_options $arg_options -v 2 -D c -DWALL -F xc ' '  -Fa alg '%{flags} -D_FORTIFY_SOURCE=2 -g -Wa,--noexecstack,--generate-missing-build-notes=yes -fpermissive -fstack-protector-strong -fstack-clash-protection -fPIC -fplugin=annobin -Wl,-z,now' \
	--prefix=%{buildroot}%{_prefix}			\
	--incdir=%{buildroot}%{_includedir}		\
	--libdir=%{buildroot}%{_libdir}/${libname}
	#--with-netlib-lapack-tarfile=%%{SOURCE10}

	#matches both SLAPACK and SSLAPACK
	sed -i "s#SLAPACKlib.*#SLAPACKlib = ${p}/liblapack_pic_pruned.a#" Make.inc
	cat Make.inc
%if "%{?enable_native_atlas}" == "0"

%ifarch ppc64
	#Use big endian
	sed -i 's#ARCH = POWER564LE#ARCH = POWER564#' Make.inc
	sed -i 's#ARCH = POWER764LE#ARCH = POWER764#' Make.inc
	sed -i 's#ARCH = POWER864LE#ARCH = POWER864#' Make.inc
%endif

%endif

	make build
	cd lib
	make shared
	make ptshared
	popd
done

%install
for type in %{types}; do
	pushd %{_arch}_${type}
	make DESTDIR=%{buildroot} install
        mv %{buildroot}%{_includedir}/atlas %{buildroot}%{_includedir}/atlas-%{_arch}-${type}
        mv %{buildroot}%{_includedir}/clapack.h %{buildroot}%{_includedir}/atlas-%{_arch}-${type}/clapack.h
        mv %{buildroot}%{_includedir}/cblas.h %{buildroot}%{_includedir}/atlas-%{_arch}-${type}/cblas.h
	if [ "$type" = "base" ]; then
		cp -pr lib/*.so* %{buildroot}%{_libdir}/atlas/
		rm -f %{buildroot}%{_libdir}/atlas/*.a
		cp -pr lib/libcblas.a lib/libatlas.a lib/libf77blas.a lib/liblapack.a %{buildroot}%{_libdir}/atlas/
	else
		cp -pr lib/*.so* %{buildroot}%{_libdir}/atlas-${type}/
		rm -f %{buildroot}%{_libdir}/atlas-${type}/*.a
		cp -pr lib/libcblas.a lib/libatlas.a lib/libf77blas.a lib/liblapack.a %{buildroot}%{_libdir}/atlas-${type}/
	fi
	popd

	mkdir -p %{buildroot}/etc/ld.so.conf.d
	if [ "$type" = "base" ]; then
		echo "%{_libdir}/atlas"		\
		> %{buildroot}/etc/ld.so.conf.d/atlas-%{_arch}.conf
	else
		echo "%{_libdir}/atlas-${type}"	\
		> %{buildroot}/etc/ld.so.conf.d/atlas-%{_arch}-${type}.conf
	fi
done

#create pkgconfig file
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
cat > $RPM_BUILD_ROOT%{_libdir}/pkgconfig/atlas.pc << DATA
Name: %{name}
Version: %{version}
Description: %{summary}
Cflags: -I%{_includedir}/atlas/
Libs: -L%{_libdir}/atlas/ -lsatlas
DATA


mkdir -p %{buildroot}%{_includedir}/atlas


%check
for type in %{types}; do
	if [ "$type" = "z14" ] || [ "$type" = "z15" ]; then
	    # skip the tests (may fail due to illegal instructions).
		  echo "Skipping tests for the $type subpackage"
	else
	    pushd %{_arch}_${type}
	    make check ptcheck
	    popd
  fi
done
#%endif

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%posttrans devel
/usr/sbin/alternatives	--install %{_includedir}/atlas atlas-inc 	\
		%{_includedir}/atlas-%{_arch}-base %{pr_base}

%postun devel
if [ $1 -ge 0 ] ; then
/usr/sbin/alternatives --remove atlas-inc %{_includedir}/atlas-%{_arch}-base
fi

%if "%{?enable_native_atlas}" == "0"
%ifarch x86_64

%post -n atlas-corei2 -p /sbin/ldconfig

%postun -n atlas-corei2 -p /sbin/ldconfig

%posttrans corei2-devel
	/usr/sbin/alternatives	--install %{_includedir}/atlas atlas-inc 	\
		%{_includedir}/atlas-%{_arch}-corei2  %{pr_corei2}

%postun corei2-devel
if [ $1 -ge 0 ] ; then
	/usr/sbin/alternatives --remove atlas-inc %{_includedir}/atlas-%{_arch}-corei2
fi

%endif

%ifarch %{ix86}
# No arch specific packages
%endif

%ifarch s390 s390x

%post -n atlas-z14 -p /sbin/ldconfig

%postun -n atlas-z14 -p /sbin/ldconfig

%posttrans z14-devel
/usr/sbin/alternatives	--install %{_includedir}/atlas atlas-inc 	\
						    %{_includedir}/atlas-%{_arch}-z14  %{pr_z14}

%postun z14-devel
if [ $1 -ge 0 ] ; then
		/usr/sbin/alternatives --remove atlas-inc %{_includedir}/atlas-%{_arch}-z14
fi

%post -n atlas-z15 -p /sbin/ldconfig

%postun -n atlas-z15 -p /sbin/ldconfig

%posttrans z15-devel
/usr/sbin/alternatives	--install %{_includedir}/atlas atlas-inc 	\
					  %{_includedir}/atlas-%{_arch}-z15  %{pr_z15}

%postun z15-devel
if [ $1 -ge 0 ] ; then
		/usr/sbin/alternatives --remove atlas-inc %{_includedir}/atlas-%{_arch}-z15
fi

%endif

%ifarch ppc64

%post -n atlas-power7 -p /sbin/ldconfig

%postun -n atlas-power7 -p /sbin/ldconfig

%posttrans power7-devel
	/usr/sbin/alternatives	--install %{_includedir}/atlas atlas-inc 	\
		%{_includedir}/atlas-%{_arch}-power7  %{pr_power7}

%postun power7-devel
if [ $1 -ge 0 ] ; then
	/usr/sbin/alternatives --remove atlas-inc %{_includedir}/atlas-%{_arch}-power7
fi

%post -n atlas-ppc8 -p /sbin/ldconfig

%postun -n atlas-ppc8 -p /sbin/ldconfig

%posttrans ppc8-devel
	/usr/sbin/alternatives	--install %{_includedir}/atlas atlas-inc 	\
		%{_includedir}/atlas-%{_arch}-ppc8  %{pr_ppc8}

%postun ppc8-devel
if [ $1 -ge 0 ] ; then
	/usr/sbin/alternatives --remove atlas-inc %{_includedir}/atlas-%{_arch}-ppc8
fi

%endif
#enable_native_atlas
%endif
%files
%doc doc/README.dist
%dir %{_libdir}/atlas
%{_libdir}/atlas/*.so.*
%config(noreplace) /etc/ld.so.conf.d/atlas-%{_arch}.conf

%files devel
%doc doc
%{_libdir}/atlas/*.so
%{_includedir}/atlas-%{_arch}-base/
%ghost %{_includedir}/atlas
%{_libdir}/pkgconfig/atlas.pc

%files static
%{_libdir}/atlas/*.a

%if "%{?enable_native_atlas}" == "0"

%ifarch x86_64

%files corei2
%doc doc/README.dist
%dir %{_libdir}/atlas-corei2
%{_libdir}/atlas-corei2/*.so.*
%config(noreplace) /etc/ld.so.conf.d/atlas-%{_arch}-corei2.conf

%files corei2-devel
%doc doc
%{_libdir}/atlas-corei2/*.so
%{_includedir}/atlas-%{_arch}-corei2/
%ghost %{_includedir}/atlas

%files corei2-static
%{_libdir}/atlas-corei2/*.a
%endif

%ifarch ppc64


%files power8
%doc doc/README.dist
%dir %{_libdir}/atlas-power8
%{_libdir}/atlas-power8/*.so.*
%config(noreplace) /etc/ld.so.conf.d/atlas-%{_arch}-power8.conf

%files power8-devel
%doc doc
%{_libdir}/atlas-power8/*.so
%{_includedir}/atlas-%{_arch}-power8/
%ghost %{_includedir}/atlas

%files power8-static
%{_libdir}/atlas-power8/*.a

%files power7
%doc doc/README.dist
%dir %{_libdir}/atlas-power7
%{_libdir}/atlas-power7/*.so.*
%config(noreplace) /etc/ld.so.conf.d/atlas-%{_arch}-power7.conf

%files power7-devel
%doc doc
%{_libdir}/atlas-power7/*.so
%{_includedir}/atlas-%{_arch}-power7/
%ghost %{_includedir}/atlas

%files power7-static
%{_libdir}/atlas-power7/*.a
%endif

%ifarch s390 s390x

%files z14
%doc doc/README.dist
%dir %{_libdir}/atlas-z14
%{_libdir}/atlas-z14/*.so.*
%config(noreplace) /etc/ld.so.conf.d/atlas-%{_arch}-z14.conf

%files z14-devel
%doc doc
%{_libdir}/atlas-z14/*.so
%{_includedir}/atlas-%{_arch}-z14/
%ghost %{_includedir}/atlas

%files z14-static
%{_libdir}/atlas-z14/*.a


%files z15
%doc doc/README.dist
%dir %{_libdir}/atlas-z15
%{_libdir}/atlas-z15/*.so.*
%config(noreplace) /etc/ld.so.conf.d/atlas-%{_arch}-z15.conf

%files z15-devel
%doc doc
%{_libdir}/atlas-z15/*.so
%{_includedir}/atlas-%{_arch}-z15/
%ghost %{_includedir}/atlas

%files z15-static
%{_libdir}/atlas-z15/*.a

%endif


#enable_native_atlas if
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.10.3-32
- Import
