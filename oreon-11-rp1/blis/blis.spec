%global source0_hash 08bbebd77914a6d1a43874ae5ec2f54fe6a77cba745f2532df28361b0f1ad1b3

# Copyright (C) 2018  Dave love, University of Manchester
# Licence as for the package source

# The full tests are very time-consuming
%bcond_with fulltest

# We need to manipulate the built *.so.%%sover
%global sover .4.0.0
%global soshort .4

# Both these are necessary to avoid asm error
# error: bp cannot be used in ‘asm’ here
# Fixme: patch to localize this
%undefine _include_frame_pointers
%define _lto_cflags %{nil}

Name:		blis
Version:	2.0
Release:	5%{?dist}
Summary:	BLAS-like Library Instantiation Software Framework
License:	BSD-3-Clause
URL:		https://github.com/flame/blis
%if 0%{?commit}
Source0:	https://github.com/flame/blis/archive/%commit/%name-%shortcommit.tar.gz
%else
Source0:	https://github.com/flame/blis/archive/%version/%name-%version.tar.gz
%endif
Patch1:         0001-Update-Haswell-gemmsup-fix-for-gcc-16-and-later.-891.patch
BuildRequires:	perl
BuildRequires:	binutils gcc
BuildRequires:	python3-devel gcc-gfortran chrpath
BuildRequires:	make
# memkind is currently only relevant for KNL as far as I know, but
# might be relevant in future for other targets with HBM.  It should
# support other targets, but only x86_64 is packaged.
%ifarch x86_64
# removed from RHEL10
%if 0%{?el8}%{?el9}%{?fedora}
BuildRequires: memkind-devel
%endif
%endif

%global desc \
BLIS is a portable software framework for instantiating\
high-performance BLAS-like dense linear algebra libraries.  The\
framework was designed to isolate essential kernels of computation\
that, when optimized, immediately enable optimized implementations of\
most of its commonly used and computationally intensive operations.\
While BLIS exports a new BLAS-like API, it also includes a BLAS\
compatibility layer which gives application developers access to BLIS\
implementations via traditional BLAS routine calls.\
\
This packaging contains automatically-dispatched\
architecture-optimized kernels for some targets, notably recent x86_64.

%description
%desc

This is the serial version.

%package	devel
Summary:	Development files for %name
Requires:	%name%{?_isa} = %version-%release
Requires:	%name-openmp%{?_isa} = %version-%release
Requires:	%name-threads%{?_isa} = %version-%release
%if 0%{?__isa_bits} == 64
Requires:	%name-serial64%{?_isa} = %version-%release
Requires:	%name-openmp64%{?_isa} = %version-%release
Requires:	%name-threads64%{?_isa} = %version-%release
%endif

%description	devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package serial64
Summary:	BLAS-like Library Instantiation Software Framework - 64-bit

%description serial64
%desc

This is the serial version with a 64-bit integer interface.

%package openmp
Summary:	BLAS-like Library Instantiation Software Framework - OpenMP

%description openmp
%desc

This is the OpenMP-parallelized version.

%package openmp64
Summary:	BLAS-like Library Instantiation Software Framework - OpenMP, 64-bit

%description openmp64
%desc

This is the OpenMP-parallelized version with a 64-bit integer interface.

# A pthreads version is necessary for Python (numpy) according to
# Debian openblas.
%package threads
Summary:	BLAS-like Library Instantiation Software Framework - pthreads

%description threads
%desc

This is the pthreads-parallelized version.

%package threads64
Summary:	BLAS-like Library Instantiation Software Framework - pthreads, 64-bit

%description threads64
%desc

This is the pthreads-parallelized version with a 64-bit integer interface.

%package srpm-macros
Summary:	BLIS architecture macros
BuildArch:	noarch

%description srpm-macros
BLIS architecture macros.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q %{?commit: -n %name-%commit}
%patch -P1 -p1 -b .gcc16

%build
case %_arch in
x86_64) arch=x86_64 ;;
# a57 runs on all aarch64 and the optimized micro-kernel should be a
# better default than generic.
# Fixme:  Include my changes for arm and ppc micro-arch dispatch.
aarch64) arch=cortexa57 ;;
armv7hl) arch=cortexa9 ;;	# Similarly to aarch64
*) arch=generic ;;
esac

# Hardening flags might be expected to affect performance, but appear
# not to.  With the f29 set and gcc 8 (but measured on EL6) for
# Haswell, a 5000×5000 DGEMM ran at 158295±565 MFLops with
# CFLAGS=$RPM_OPT_FLAGS and 158289±414 MFlops with no CFLAGS specified.
# Add back -O3, overridden by -O2 in RPM_OPT_FLAGS.
# -funsafe-math-optimizations vectorizes more, and passes tests
# <https://github.com/flame/blis/issues/259#issuecomment-463657085>
%global confflags --enable-debug=opt --disable-static --enable-shared --enable-verbose-make --enable-cblas
export CFLAGS="$RPM_OPT_FLAGS -O3 -funsafe-math-optimizations" LDFLAGS="%{?__global_ldflags}"
export PYTHON=%python3		# Needed by both configure and make

# It's not an autotools configure
./configure --prefix=$(pwd)/o %confflags -t openmp $arch
%make_build SOFLAGS="-shared -Wl,-soname=libbliso.so%sover"
make install

./configure --prefix=$(pwd)/p %confflags -t pthreads $arch
%make_build SOFLAGS="-shared -Wl,-soname=libblisp.so%sover"
make install

# Rename the libraries per soname and generate BLAS_compatible ones
mkdir -p blisblas{,o,p,64,o64,p64}
for d in o p; do
  cd $d/lib
  f=libblis.so%sover
  mv $f ${f/./$d.}
  ln -s libblis$d.so%sover libblis$d.so
  ln -s libblis$d.so%sover  libblis$d.so%soshort
  rm libblis.*
  cd ../..
  cc -shared -Wl,-soname=libblas.so.3 -L$(pwd)/$d/lib -lblis$d -o blisblas$d/libblas.so.3 $LDFLAGS
  ln -s libblas.so.3 blisblas$d/libblas.so
done

%if 0%{?__isa_bits} == 64

./configure --prefix=$(pwd)/64 %confflags -b 64 $arch
%make_build SOFLAGS="-shared -Wl,-soname=libblis64.so%sover"
make install

./configure --prefix=$(pwd)/o64 %confflags -b 64 -t openmp $arch
%make_build SOFLAGS="-shared -Wl,-soname=libbliso64.so%sover"
make install

./configure --prefix=$(pwd)/p64 %confflags -b 64 -t pthreads $arch
%make_build SOFLAGS="-shared -Wl,-soname=libblisp64.so%sover"
make install

for d in 64 o64 p64; do
  cd $d/lib
  f=libblis.so%sover
  mv $f ${f/./$d.}
  ln -s libblis$d.so%sover libblis$d.so
  ln -s libblis$d.so%sover libblis$d.so%soshort
  rm -f libblis.*
  cd ../..
  cc -shared -Wl,-soname=libblas64.so.3 -L$(pwd)/$d/lib -lblis$d -o blisblas$d/libblas64.so.3 $LDFLAGS
  ln -s libblas64.so.3 blisblas$d/libblas64.so
done

%endif

# done last for the benefit of check
./configure --prefix=$(pwd)/serial %confflags $arch
%make_build
make install
cc -shared -Wl,-soname=libblas.so.3 -L$(pwd)/serial/lib -lblis -o blisblas/libblas.so.3 $LDFLAGS
ln -s libblas.so.3 blisblas/libblas.so

%install
mkdir -p %buildroot%_libdir %buildroot%_includedir

cp -a {serial,o,p}/lib/* %buildroot%_libdir
mv serial/include/blis %buildroot%_includedir
for d in o p; do
  cp -a $d/include/blis %buildroot%_includedir/blis$d
done
%if 0%{?__isa_bits} == 64
cp -a {64,o64,p64}/lib/* %buildroot%_libdir
for d in 64 o64 p64; do
  cp -a $d/include/blis %buildroot%_includedir/blis$d
done
%endif
# Needed for debuginfo processing
chmod +x %buildroot%_libdir/*.so.*
cp -a blisblas* %buildroot%_libdir
# This is quite large.
gzip CHANGELOG
chrpath -d %buildroot%_libdir/*.so.*

cat <<EOF >README.Fedora
Fedora BLIS packaging
---------------------

Similarly to the OpenBLAS packaging, as well as the serial library
(libblis), there are versions named with suffix "o" using OpenMP, and
suffix "p" using pthreads.  Also, on 64-bit targets, there are
versions built with 64-bit integer interfaces, which have suffix "64".
Thus "libblaso64" is built for 64-bit integers and OpenMP
parallelization.  The cblas interface is included in each version.

For the BLAS interface, BLIS and OpenBLAS are expected to have similar
performance where they are optimized for the same micro-architectures,
but do show some performance differences in either direction.  BLIS
supports AVX512 on KNL and SKX, which OpenBLAS currently doesn't, and
will be more than twice as fast on such systems, which are the main
targets for this packaging.  BLIS' non-BLAS interface is obviously a
potential advantage generally, but it isn't currently used by any
Fedora packages.

There are shared library shims in %_libdir/blisblas* for each version
that provide sonames libblas.so.3 or libblas64.so.3 and so may be
linked dynamically instead of the reference libblas.  You can use an
ldconfig file so that this will be done automatically if the blis or
blis64 packages are installed, which will usually be a lot faster than
the reference version.  Otherwise, setting
LD_LIBRARY_PATH=%_libdir/blisblaso, say, will cause a binary
dynamically linked against libblas to run with the OpenMP BLIS version
instead, to allow multiple threads to be used.  The shims could be
extended to substitute the atlas and openblas libraries, but those can
be overridden by running with LD_PRELOAD=%_libdir/libblis.so%sover in
the environment.

Runtime dispatch on the micro-architecture is currently only available
on x86_64.  aarch64 will use cortexa57 instructions.  Other
architectures use the "generic" target, so OpenBLAS will be faster on
any of them that it supports (arm, power64, ix86, and s390x in Fedora).

The blis-srpm-macros package defines RPM macro %blis_opt_arches for
the architectures with optimized implementations in case the list is
extended in future.

EOF

%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
mkdir -p %buildroot%macrosdir
cat <<EOF >%buildroot%macrosdir/macros.blis-srpm
# Architectures for for BLIS has an optimized implementation
%blis_opt_arches x86_64 aarch64
EOF

%check
# A quick check which tests the Fortran BLAS interface with gfortran,
# unlike the "test" or "check" targets.
# Fixme: check a 64-bit version where relevant
gfortran -o dblat blastest/src/fortran/dblat3.f -Lblisblas -Lserial/lib -lblas -lblis
LD_LIBRARY_PATH=$(pwd)/serial/lib:$(pwd)/blisblas ./dblat <<+ || { cat dblat3.summ && false; }
'dblat3.summ'
6
'dblat3.snap'
-1
F
T
T
16.0
7
0 1 2 3 7 31 63
3
0.0 1.0 0.7
3
0.0 1.0 1.3
DGEMM  T
DSYMM  F
+

export LD_LIBRARY_PATH=`pwd`/serial/lib
%if %{with fulltest}
%make_build test
%else
%make_build check
%endif

%ldconfig_scriptlets
%ldconfig_scriptlets openmp
%ldconfig_scriptlets serial64
%ldconfig_scriptlets openmp64
%ldconfig_scriptlets threads
%ldconfig_scriptlets threads64

%global docs CHANGELOG.gz CREDITS README.md README.Fedora

%files
%doc %docs
%license LICENSE
%{_libdir}/libblis.so%{soshort}*
%{_libdir}/blisblas

%files openmp
%doc %docs
%license LICENSE
%{_libdir}/libbliso.so%{soshort}*
%{_libdir}/blisblaso

%files threads
%doc %docs
%license LICENSE
%{_libdir}/libblisp.so%{soshort}*
%{_libdir}/blisblasp

%if 0%{?__isa_bits} == 64

%files serial64
%doc %docs
%license LICENSE
%{_libdir}/libblis64.so%{soshort}*
%{_libdir}/blisblas64

%files openmp64
%doc %docs
%license LICENSE
%{_libdir}/libbliso64.so%{soshort}*
%{_libdir}/blisblaso64

%files threads64
%doc %docs
%license LICENSE
%{_libdir}/libblisp64.so%{soshort}*
%{_libdir}/blisblasp64

%endif

%files devel
%doc examples
%{_includedir}/*
%{_libdir}/libblis*.so

%files srpm-macros
%{macrosdir}/macros.blis-srpm

%changelog
%autochangelog
