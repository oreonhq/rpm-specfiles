%global source0_hash 38240eee1b29e2bde47ebb5d61160207dc68668a54cac62c076bb5032013b1eb

%bcond_with system_lapack
# Version of bundled lapack
%global lapackver 3.12.0

# DO NOT "CLEAN UP" OR MODIFY THIS SPEC FILE WITHOUT ASKING THE
# MAINTAINER FIRST!
#
# OpenBLAS is hand written assembler code and it has a limited number
# of supported architectures. Don't enable any new architectures /
# processors a) without checking that it is actually supported and b)
# without modifying the target flags.
#
# The same spec is also used on the EPEL branches, meaninng that some
# "obsoleted" features are still kept in the spec.

Name:           openblas
Version:        0.3.29
Release:        3%{?dist}
Summary:        An optimized BLAS library based on GotoBLAS2

License:        BSD-3-Clause
URL:            https://github.com/OpenMathLib/OpenBLAS
Source0:        https://github.com/OpenMathLib/OpenBLAS/archive/refs/tags/v0.3.29.tar.gz#/OpenBLAS-0.3.29.tar.gz

# Use system lapack
Patch0:         openblas-0.2.15-system_lapack.patch
# Drop extra p from threaded library name
Patch1:         openblas-0.2.5-libname.patch
# Don't use constructor priorities on too old architectures
Patch2:         openblas-0.2.15-constructor.patch
# Supply the proper flags to the test makefile
Patch3:         openblas-0.3.11-tests.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  perl-devel
BuildRequires:  multilib-rpm-config

# Rblas library is no longer necessary
%if 0%{?fedora} >= 31 || 0%{?rhel} >= 8
Obsoletes:      %{name}-Rblas < %{version}-%{release}
%endif

# Do we have execstack?
%if 0%{?rhel} == 7
%ifarch ppc64le aarch64
%global execstack 0
%else
%global execstack 1
%endif
%else
%global execstack 1
%endif
%if %{execstack}
BuildRequires:  /usr/bin/execstack
%endif

# LAPACK
%if %{with system_lapack}
%if 0%{?rhel} == 5 || 0%{?rhel} == 6
BuildRequires:  lapack-devel
%else
BuildRequires:  lapack-static
%endif
# Do we have LAPACKE? (Needs at least lapack 3.4.0)
%if 0%{?fedora}
%global lapacke 1
%else
%global lapacke 0
%endif

%else
# Use bundled LAPACK
%global lapacke 1
Provides:       bundled(lapack) = %{lapackver}
%endif

# Build 64-bit interface binaries?
%if 0%{?__isa_bits} == 64
%global build64 1
%bcond_without cpp_thread_check
%else
%global build64 0
%bcond_with cpp_thread_check
%endif

%if %{with system_lapack}
%if %build64
BuildRequires:  lapack64-static
%endif
%endif

# Upstream supports the package only on these architectures.
# Runtime processor detection is not available on other archs.
ExclusiveArch:  %{openblas_arches}

%global base_description \
OpenBLAS is an optimized BLAS library based on GotoBLAS2 1.13 BSD \
version. The project is supported by the Lab of Parallel Software and \
Computational Science, ISCAS. http://www.rdcps.ac.cn


%description
%{base_description}

%package serial
Summary:        An optimized BLAS library based on GotoBLAS2, serial version
Requires:       %{name} = %{version}-%{release}

%description serial
%{base_description}

This package contains the sequential library compiled with a 32-bit
integer interface.

%package openmp
Summary:        An optimized BLAS library based on GotoBLAS2, OpenMP version
Requires:       %{name} = %{version}-%{release}

%description openmp
%{base_description}

This package contains the library compiled with OpenMP support with
32-bit integer interface.

%package threads
Summary:        An optimized BLAS library based on GotoBLAS2, pthreads version
Requires:       %{name} = %{version}-%{release}

%description threads
%{base_description}

This package contains the library compiled with threading support and
a 32-bit integer interface.

%if %build64
%package serial64
Summary:        An optimized BLAS library based on GotoBLAS2, serial version
Requires:       %{name} = %{version}-%{release}

%description serial64
%{base_description}

This package contains the sequential library compiled with a 64-bit
integer interface.

%package openmp64
Summary:        An optimized BLAS library based on GotoBLAS2, OpenMP version
Requires:       %{name} = %{version}-%{release}

%description openmp64
%{base_description}

This package contains the library compiled with OpenMP support and
64-bit integer interface.

%package threads64
Summary:        An optimized BLAS library based on GotoBLAS2, pthreads version
Requires:       %{name} = %{version}-%{release}

%description threads64
%{base_description}

This package contains the library compiled with threading support and
64-bit integer interface.

%package serial64_
Summary:        An optimized BLAS library based on GotoBLAS2, serial version
Requires:       %{name} = %{version}-%{release}

%description serial64_
%{base_description}

This package contains the sequential library compiled with a 64-bit
integer interface and a symbol name suffix.

%package openmp64_
Summary:        An optimized BLAS library based on GotoBLAS2, OpenMP version
Requires:       %{name} = %{version}-%{release}

%description openmp64_
%{base_description}

This package contains the library compiled with OpenMP support and
64-bit integer interface and a symbol name suffix.

%package threads64_
Summary:        An optimized BLAS library based on GotoBLAS2, pthreads version
Requires:       %{name} = %{version}-%{release}

%description threads64_
%{base_description}

This package contains the library compiled with threading support and
64-bit integer interface and a symbol name suffix.
%endif


%package devel
Summary:        Development headers and libraries for OpenBLAS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-serial%{?_isa} = %{version}-%{release}
Requires:       %{name}-openmp%{?_isa} = %{version}-%{release}
Requires:       %{name}-threads%{?_isa} = %{version}-%{release}
%if %build64
Requires:       %{name}-openmp64%{?_isa} = %{version}-%{release}
Requires:       %{name}-threads64%{?_isa} = %{version}-%{release}
Requires:       %{name}-serial64%{?_isa} = %{version}-%{release}
Requires:       %{name}-openmp64_%{?_isa} = %{version}-%{release}
Requires:       %{name}-threads64_%{?_isa} = %{version}-%{release}
Requires:       %{name}-serial64_%{?_isa} = %{version}-%{release}
%endif
Requires:       %{name}-srpm-macros

%description devel
%{base_description}

This package contains the development headers and libraries.

%package static
Summary:        Static version of OpenBLAS
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
%{base_description}

This package contains the static libraries.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -T

# Untar source
tar zxf %{SOURCE0}
cd OpenBLAS-%{version}
%if %{with system_lapack}
%patch 0 -p1 -b .system_lapack
%endif
%patch 1 -p1 -b .libname
%if 0%{?rhel} == 5
%patch 2 -p1 -b .constructor
%endif
%patch 3 -p1 -b .tests

# Fix source permissions
find -name \*.f -exec chmod 644 {} \;

%if %{with system_lapack}
# Get rid of bundled LAPACK sources
rm -rf lapack-netlib
%endif

# Make serial, threaded and OpenMP versions; as well as 64-bit versions
cd ..
cp -ar OpenBLAS-%{version} openmp
cp -ar OpenBLAS-%{version} threaded
%if %build64
for d in {serial,threaded,openmp}64{,_}; do
    cp -ar OpenBLAS-%{version} $d
done
%endif
mv OpenBLAS-%{version} serial

%if %{with system_lapack}
# Setup 32-bit interface LAPACK
mkdir netliblapack
cd netliblapack
ar x %{_libdir}/liblapack_pic.a
# Get rid of duplicate functions. See list in Makefile of lapack directory
for f in laswp getf2 getrf potf2 potrf lauu2 lauum trti2 trtri getrs; do
    \rm {c,d,s,z}$f.o
done

# LAPACKE
%if %{lapacke}
ar x %{_libdir}/liblapacke.a
%endif

# Create makefile
echo "TOPDIR = .." > Makefile
echo "include ../Makefile.system" >> Makefile
echo "COMMONOBJS = \\" >> Makefile
for i in *.o; do
 echo "$i \\" >> Makefile
done
echo -e "\n\ninclude \$(TOPDIR)/Makefile.tail" >> Makefile

%if %{lapacke}
# Copy include files
cp -a %{_includedir}/lapacke .
%endif
cd ..

# Copy in place
for d in serial threaded openmp; do
    cp -pr netliblapack $d
done
rm -rf netliblapack


# Setup 64-bit interface LAPACK
%if %build64
mkdir netliblapack64
cd netliblapack64
ar x %{_libdir}/liblapack64_pic.a
# Get rid of duplicate functions. See list in Makefile of lapack directory
for f in laswp getf2 getrf potf2 potrf lauu2 lauum trti2 trtri getrs; do
    \rm {c,d,s,z}$f.o
done

# LAPACKE, no 64-bit interface
%if %{lapacke}
ar x %{_libdir}/liblapacke.a
%endif

# Create makefile
echo "TOPDIR = .." > Makefile
echo "include ../Makefile.system" >> Makefile
echo "COMMONOBJS = \\" >> Makefile
for i in *.o; do
    echo "$i \\" >> Makefile
done
echo -e "\n\ninclude \$(TOPDIR)/Makefile.tail" >> Makefile

%if %{lapacke}
# Copy include files
cp -a %{_includedir}/lapacke .
%endif
cd ..

# Copy in place
for d in {serial,threaded,openmp}64{,_}; do
    cp -pr netliblapack64 $d/netliblapack
done
rm -rf netliblapack64
%endif
%endif

%build
# openblas fails to build with LTO due to undefined symbols.  These could
# well be the result of the assembly code used in this package
%define _lto_cflags %{nil}
%if !%{lapacke}
LAPACKE="NO_LAPACKE=1"
%endif

# Maximum possible amount of processors
NMAX="NUM_THREADS=128"

%ifarch %{ix86} x86_64
TARGET="TARGET=CORE2 DYNAMIC_ARCH=1 DYNAMIC_OLDER=1"

# Compability for old versions of GCC
%if 0%{?rhel} == 5
export AVX="NO_AVX=1 NO_AVX2=1"
%endif
%if 0%{?rhel} == 6
export AVX="NO_AVX2=1"
%endif

%endif
%ifarch armv7hl
# ARM v7 still doesn't have runtime cpu detection...
TARGET="TARGET=ARMV7 DYNAMIC_ARCH=0"
%endif
%ifarch ppc64
TARGET="TARGET=POWER6 DYNAMIC_ARCH=1 DYNAMIC_OLDER=1"
%endif
%ifarch ppc64p7
TARGET="TARGET=POWER7 DYNAMIC_ARCH=1 DYNAMIC_OLDER=1"
%endif
%ifarch ppc64le
TARGET="TARGET=POWER8 DYNAMIC_ARCH=1 DYNAMIC_OLDER=1"
%endif
%ifarch aarch64
TARGET="TARGET=ARMV8 DYNAMIC_ARCH=1 DYNAMIC_OLDER=1"
%endif
%ifarch s390x
TARGET="TARGET=ZARCH_GENERIC DYNAMIC_ARCH=1 DYNAMIC_OLDER=1"
%endif
%ifarch riscv64
TARGET="TARGET=RISCV64_GENERIC DYNAMIC_ARCH=0"
%endif

%if 0%{?rhel} == 5
# Gfortran too old to recognize -frecursive
COMMON="%{optflags} -fPIC"
FCOMMON="%{optflags} -fPIC"
%else
COMMON="%{optflags} -fPIC"
FCOMMON="%{optflags} -fPIC -frecursive"
%endif
# Use Fedora linker flags
export LDFLAGS="%{__global_ldflags}"

# Declare some necessary build flags
COMMON="%{optflags} -fPIC"
FCOMMON="$COMMON -frecursive"
make -C serial     $TARGET USE_THREAD=0 USE_LOCKING=1 USE_OPENMP=0 FC=gfortran CC=gcc COMMON_OPT="$COMMON" FCOMMON_OPT="$FCOMMON" $NMAX LIBPREFIX="libopenblas"      $AVX $LAPACKE INTERFACE64=0
make -C threaded   $TARGET USE_THREAD=1 USE_OPENMP=0 FC=gfortran CC=gcc COMMON_OPT="$COMMON" FCOMMON_OPT="$FCOMMON" $NMAX LIBPREFIX="libopenblasp"     $AVX $LAPACKE INTERFACE64=0

# USE_THREAD determines use of SMP, not of pthreads
COMMON="%{optflags} -fPIC -fopenmp -pthread"
FCOMMON="$COMMON -frecursive"
make -C openmp     $TARGET USE_THREAD=1 USE_OPENMP=1 FC=gfortran CC=gcc COMMON_OPT="$COMMON" FCOMMON_OPT="$FCOMMON" $NMAX LIBPREFIX="libopenblaso"     $AVX $LAPACKE INTERFACE64=0 %{with cpp_thread_check:CPP_THREAD_SAFETY_TEST=1}
make -C openmp     $TARGET USE_THREAD=1 USE_OPENMP=1 FC=gfortran CC=gcc COMMON_OPT="$COMMON" FCOMMON_OPT="$FCOMMON" $NMAX LIBPREFIX="libopenblaso"     $AVX $LAPACKE INTERFACE64=0 %{with cpp_thread_check:CPP_THREAD_SAFETY_TEST=1} lapack-test

%if %build64
COMMON="%{optflags} -fPIC"
FCOMMON="$COMMON -frecursive -fdefault-integer-8"
make -C serial64   $TARGET USE_THREAD=0 USE_LOCKING=1 USE_OPENMP=0 FC=gfortran CC=gcc COMMON_OPT="$COMMON" FCOMMON_OPT="$FCOMMON" $NMAX LIBPREFIX="libopenblas64"    $AVX $LAPACKE INTERFACE64=1
make -C threaded64 $TARGET USE_THREAD=1 USE_OPENMP=0 FC=gfortran CC=gcc COMMON_OPT="$COMMON" FCOMMON_OPT="$FCOMMON" $NMAX LIBPREFIX="libopenblasp64"   $AVX $LAPACKE INTERFACE64=1

COMMON="%{optflags} -fPIC -fopenmp -pthread"
FCOMMON="$COMMON -frecursive -fdefault-integer-8"
make -C openmp64   $TARGET USE_THREAD=1 USE_OPENMP=1 FC=gfortran CC=gcc COMMON_OPT="$COMMON" FCOMMON_OPT="$FCOMMON" $NMAX LIBPREFIX="libopenblaso64"   $AVX $LAPACKE INTERFACE64=1 CPP_THREAD_SAFETY_TEST=1

COMMON="%{optflags} -fPIC"
FCOMMON="$COMMON -frecursive  -fdefault-integer-8"
make -C serial64_   $TARGET USE_THREAD=0 USE_LOCKING=1 USE_OPENMP=0 FC=gfortran CC=gcc COMMON_OPT="$COMMON" FCOMMON_OPT="$FCOMMON" $NMAX LIBPREFIX="libopenblas64_"  $AVX $LAPACKE INTERFACE64=1 SYMBOLSUFFIX=64_
make -C threaded64_ $TARGET USE_THREAD=1 USE_OPENMP=0 FC=gfortran CC=gcc COMMON_OPT="$COMMON" FCOMMON_OPT="$FCOMMON" $NMAX LIBPREFIX="libopenblasp64_" $AVX $LAPACKE INTERFACE64=1 SYMBOLSUFFIX=64_

COMMON="%{optflags} -fPIC -fopenmp -pthread"
FCOMMON="$COMMON -frecursive -fdefault-integer-8"
make -C openmp64_   $TARGET USE_THREAD=1 USE_OPENMP=1 FC=gfortran CC=gcc COMMON_OPT="$COMMON" FCOMMON_OPT="$FCOMMON" $NMAX LIBPREFIX="libopenblaso64_" $AVX $LAPACKE INTERFACE64=1 SYMBOLSUFFIX=64_ CPP_THREAD_SAFETY_TEST=1
%endif

%install
rm -rf %{buildroot}
# Install serial library and headers
make -C serial USE_THREAD=0 PREFIX=%{buildroot} OPENBLAS_LIBRARY_DIR=%{buildroot}%{_libdir} OPENBLAS_INCLUDE_DIR=%{buildroot}%{_includedir}/%name OPENBLAS_BINARY_DIR=%{buildroot}%{_bindir} OPENBLAS_CMAKE_DIR=%{buildroot}%{_libdir}/cmake install

# Copy lapacke include files
%if %{with system_lapack} && %{lapacke}
cp -a %{_includedir}/lapacke %{buildroot}%{_includedir}/%{name}
%endif

# Fix i686-x86_64 multilib difference
%multilib_fix_c_header --file %{_includedir}/openblas/openblas_config.h

# Fix name of libraries: runtime CPU detection has none
suffix=""
# but archs that don't have it do have one
%ifarch armv7hl
suffix="_armv7"
%endif
%ifarch riscv64
suffix="_riscv64_generic"
%endif
slibname=`basename %{buildroot}%{_libdir}/libopenblas${suffix}-*.so .so`
mv %{buildroot}%{_libdir}/${slibname}.a %{buildroot}%{_libdir}/lib%{name}.a
if [[ "$suffix" != "" ]]; then
   sname=$(echo $slibname | sed "s|$suffix||g")
   mv %{buildroot}%{_libdir}/${slibname}.so %{buildroot}%{_libdir}/${sname}.so
else
   sname=${slibname}
fi

# Install the OpenMP library
olibname=`echo ${slibname} | sed "s|lib%{name}|lib%{name}o|g"`
install -D -p -m 644 openmp/${olibname}.a %{buildroot}%{_libdir}/lib%{name}o.a
if [[ "$suffix" != "" ]]; then
   oname=$(echo $olibname | sed "s|$suffix||g")
else
   oname=${olibname}
fi
install -D -p -m 755 openmp/${olibname}.so %{buildroot}%{_libdir}/${oname}.so

# Install the threaded library
plibname=`echo ${slibname} | sed "s|lib%{name}|lib%{name}p|g"`
install -D -p -m 644 threaded/${plibname}.a %{buildroot}%{_libdir}/lib%{name}p.a
if [[ "$suffix" != "" ]]; then
   pname=$(echo $plibname | sed "s|$suffix||g")
else
   pname=${plibname}
fi
install -D -p -m 755 threaded/${plibname}.so %{buildroot}%{_libdir}/${pname}.so

# Install the 64-bit interface libraries
%if %build64
slibname64=`echo ${slibname} | sed "s|lib%{name}|lib%{name}64|g"`
install -D -p -m 644 serial64/${slibname64}.a %{buildroot}%{_libdir}/lib%{name}64.a
slibname64_=`echo ${slibname} | sed "s|lib%{name}|lib%{name}64_|g"`
install -D -p -m 644 serial64_/${slibname64_}.a %{buildroot}%{_libdir}/lib%{name}64_.a

if [[ "$suffix" != "" ]]; then
   sname64=$(echo ${slibname64} | sed "s|$suffix||g")
   sname64_=$(echo ${slibname64_} | sed "s|$suffix||g")
else
   sname64=${slibname64}
   sname64_=${slibname64_}
fi
install -D -p -m 755 serial64/${slibname64}.so %{buildroot}%{_libdir}/${sname64}.so
install -D -p -m 755 serial64_/${slibname64_}.so %{buildroot}%{_libdir}/${sname64_}.so

olibname64=`echo ${slibname} | sed "s|lib%{name}|lib%{name}o64|g"`
install -D -p -m 644 openmp64/${olibname64}.a %{buildroot}%{_libdir}/lib%{name}o64.a
olibname64_=`echo ${slibname} | sed "s|lib%{name}|lib%{name}o64_|g"`
install -D -p -m 644 openmp64_/${olibname64_}.a %{buildroot}%{_libdir}/lib%{name}o64_.a

if [[ "$suffix" != "" ]]; then
   oname64=$(echo ${olibname64} | sed "s|$suffix||g")
   oname64_=$(echo ${olibname64_} | sed "s|$suffix||g")
else
   oname64=${olibname64}
   oname64_=${olibname64_}
fi
install -D -p -m 755 openmp64/${olibname64}.so %{buildroot}%{_libdir}/${oname64}.so
install -D -p -m 755 openmp64_/${olibname64_}.so %{buildroot}%{_libdir}/${oname64_}.so

plibname64=`echo ${slibname} | sed "s|lib%{name}|lib%{name}p64|g"`
install -D -p -m 644 threaded64/${plibname64}.a %{buildroot}%{_libdir}/lib%{name}p64.a
plibname64_=`echo ${slibname} | sed "s|lib%{name}|lib%{name}p64_|g"`
install -D -p -m 644 threaded64_/${plibname64_}.a %{buildroot}%{_libdir}/lib%{name}p64_.a

if [[ "$suffix" != "" ]]; then
   pname64=$(echo $plibname64 | sed "s|$suffix||g")
   pname64_=$(echo $plibname64_ | sed "s|$suffix||g")
else
   pname64=${plibname64}
   pname64_=${plibname64_}
fi
install -D -p -m 755 threaded64/${plibname64}.so %{buildroot}%{_libdir}/${pname64}.so
install -D -p -m 755 threaded64_/${plibname64_}.so %{buildroot}%{_libdir}/${pname64_}.so
%endif

# Fix symlinks
pushd %{buildroot}%{_libdir}
# Serial libraries
ln -sf ${sname}.so lib%{name}.so
ln -sf ${sname}.so lib%{name}.so.0
# OpenMP libraries
ln -sf ${oname}.so lib%{name}o.so
ln -sf ${oname}.so lib%{name}o.so.0
# Threaded libraries
ln -sf ${pname}.so lib%{name}p.so
ln -sf ${pname}.so lib%{name}p.so.0

%if %build64
# Serial libraries
ln -sf ${sname64}.so lib%{name}64.so
ln -sf ${sname64}.so lib%{name}64.so.0
ln -sf ${sname64_}.so lib%{name}64_.so
ln -sf ${sname64_}.so lib%{name}64_.so.0
# OpenMP libraries
ln -sf ${oname64}.so lib%{name}o64.so
ln -sf ${oname64}.so lib%{name}o64.so.0
ln -sf ${oname64_}.so lib%{name}o64_.so
ln -sf ${oname64_}.so lib%{name}o64_.so.0
# Threaded libraries
ln -sf ${pname64}.so lib%{name}p64.so
ln -sf ${pname64}.so lib%{name}p64.so.0
ln -sf ${pname64_}.so lib%{name}p64_.so
ln -sf ${pname64_}.so lib%{name}p64_.so.0
%endif

%if %{execstack}
# Get rid of executable stacks
for lib in %{buildroot}%{_libdir}/libopenblas*.so; do
 execstack -c $lib
done
%endif

# Get rid of generated CMake config
rm -rf %{buildroot}%{_libdir}/cmake
# Get rid of generated pkgconfig
rm -rf %{buildroot}%{_libdir}/pkgconfig

%ldconfig_scriptlets

%ldconfig_scriptlets openmp

%ldconfig_scriptlets threads

%if %build64
%ldconfig_scriptlets openmp64
%ldconfig_scriptlets openmp64_

%ldconfig_scriptlets serial64
%ldconfig_scriptlets serial64_

%ldconfig_scriptlets threads64
%ldconfig_scriptlets threads64_
%endif

%files
%license serial/LICENSE
%doc serial/Changelog.txt serial/GotoBLAS* 

%files serial
%{_libdir}/lib%{name}-*.so
%{_libdir}/lib%{name}.so.*

%files openmp
%{_libdir}/lib%{name}o-*.so
%{_libdir}/lib%{name}o.so.*

%files threads
%{_libdir}/lib%{name}p-*.so
%{_libdir}/lib%{name}p.so.*

%if %build64
%files serial64
%{_libdir}/lib%{name}64-*.so
%{_libdir}/lib%{name}64.so.*

%files openmp64
%{_libdir}/lib%{name}o64-*.so
%{_libdir}/lib%{name}o64.so.*

%files threads64
%{_libdir}/lib%{name}p64-*.so
%{_libdir}/lib%{name}p64.so.*

%files serial64_
%{_libdir}/lib%{name}64_-*.so
%{_libdir}/lib%{name}64_.so.*

%files openmp64_
%{_libdir}/lib%{name}o64_-*.so
%{_libdir}/lib%{name}o64_.so.*

%files threads64_
%{_libdir}/lib%{name}p64_-*.so
%{_libdir}/lib%{name}p64_.so.*
%endif

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}o.so
%{_libdir}/lib%{name}p.so
%if %build64
%{_libdir}/lib%{name}64.so
%{_libdir}/lib%{name}o64.so
%{_libdir}/lib%{name}p64.so
%{_libdir}/lib%{name}64_.so
%{_libdir}/lib%{name}o64_.so
%{_libdir}/lib%{name}p64_.so
%endif

%files static
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}o.a
%{_libdir}/lib%{name}p.a
%if %build64
%{_libdir}/lib%{name}64.a
%{_libdir}/lib%{name}o64.a
%{_libdir}/lib%{name}p64.a
%{_libdir}/lib%{name}64_.a
%{_libdir}/lib%{name}o64_.a
%{_libdir}/lib%{name}p64_.a
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.29-3
- Prepare for Oreon 11 (RP1)
