%global source0_hash 84a47f7c4231b9efdf4d4f631a2cae2bdd9adeaabc088261d15af040143ed112
%global _incmpidir %{_includedir}/openmpi-%{_arch}
%global _libmpidir %{_libdir}/openmpi/lib
%global _incmpichdir %{_includedir}/mpich-%{_arch}
%global _libmpichdir %{_libdir}/mpich/lib
%global soname_version 5.7
%undefine _ld_as_needed
%global with_openmpi 1
%global with_openmpi_check 1
%ifnarch s390x
%global with_mpich_check 1
%else
%global with_mpich_check 0
%endif
%global with_mpich 1
%global with_openmpi 1
%global with_openmpi_check 1
%ifnarch s390x
%global with_mpich_check 1
%else
%global with_mpich_check 0
%endif
%global with_mpich 1
%if 0%{?fedora} || 0%{?rhel} >= 9 || 0%{?oreon}
%global build_fflags %{build_fflags} -fallow-argument-mismatch
%endif
Name: MUMPS
Version: %{soname_version}.3
Release:        1%{?dist}
Summary:        A MUltifrontal Massively Parallel sparse direct Solver
License: CECILL-C
URL: https://mumps-solver.org
Source0:        https://mumps-solver.org/%{name}_%{version}.tar.gz
Source1: %{name}-Makefile.par.inc
Source2: %{name}-Makefile.seq.inc
Patch0: %{name}-examples-mpilibs.patch
Patch1: %{name}-shared-pord.patch
Patch2: %{name}-shared.patch
Patch3: %{name}-shared-seq.patch
Requires:      %{name}-common = %{version}-%{release}
Obsoletes: %{name}-openmp < 0:5.4.0-1
# oreon:deps
BuildRequires:  blacs-mpich-devel
BuildRequires:  blacs-openmpi-devel
BuildRequires:  gcc
BuildRequires:  gcc-gfortran
BuildRequires:  hwloc-devel
BuildRequires:  make
BuildRequires:  metis-devel
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel
BuildRequires:  openssh-clients
BuildRequires:  pkgconfig(flexiblas)
BuildRequires:  ptscotch-mpich-devel
BuildRequires:  ptscotch-mpich-devel-parmetis
BuildRequires:  ptscotch-openmpi-devel
BuildRequires:  ptscotch-openmpi-devel-parmetis
BuildRequires:  rpm-mpi-hooks
BuildRequires:  scalapack-mpich-devel
BuildRequires:  scalapack-openmpi-devel
BuildRequires:  scotch-devel
BuildRequires:  scotch-devel-metis
# /oreon:deps
%description
MUMPS implements a direct solver for large sparse linear systems, with a
particular focus on symmetric positive definite matrices.  It can
operate on distributed matrices e.g. over a cluster.  It has Fortran and
C interfaces, and can interface with ordering tools such as Scotch.

%package devel
Summary: The MUMPS headers and development-related files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gcc-gfortran%{?_isa}
Requires: %{name}-srpm-macros = %{version}-%{release}
Obsoletes: %{name}-openmp-devel < 0:5.4.0-1
%description devel
Shared links and header files.
This package contains dummy MPI header file 
including symbols used by MUMPS.

%package examples
Summary: The MUMPS common illustrative test programs
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
This package contains common illustrative
test programs about how MUMPS can be used.

%package common
Summary: Documentation files for MUMPS
BuildArch: noarch
%description common
This package contains common documentation files for MUMPS.

%package srpm-macros
Summary: Additional RPM macros for MUMPS
BuildArch: noarch
%description srpm-macros
Additional RPM macros for MUMPS.

########################################################
%if 0%{?with_openmpi}
%package openmpi
Summary: MUMPS libraries compiled against openmpi
BuildRequires: openmpi-devel
BuildRequires: blacs-openmpi-devel
BuildRequires: scalapack-openmpi-devel
BuildRequires: ptscotch-openmpi-devel >= 7.0.1
BuildRequires: ptscotch-openmpi-devel-parmetis >= 7.0.1
Requires: %{name}-common = %{version}-%{release}
Requires: openmpi%{?_isa}
Requires: scalapack-openmpi%{?_isa}
Requires: ptscotch-openmpi%{?_isa} >= 7.0.1
%description openmpi
MUMPS libraries compiled against openmpi.

%package openmpi-devel
Summary: The MUMPS headers and development-related files
BuildRequires: openmpi-devel
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires: gcc-gfortran%{?_isa}
Requires: %{name}-srpm-macros = %{version}-%{release}
%description openmpi-devel
Shared links, header files for MUMPS.

%package openmpi-examples
Summary: The MUMPS OpenMPI common illustrative test programs
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires: openmpi
%description openmpi-examples
This package contains common illustrative
test programs about how MUMPS-openmpi can be used.
%endif
##########################################################

########################################################
%if 0%{?with_mpich}
%package mpich
Summary: MUMPS libraries compiled against MPICH
BuildRequires: mpich-devel
BuildRequires: blacs-mpich-devel
BuildRequires: scalapack-mpich-devel
BuildRequires: ptscotch-mpich-devel >= 7.0.1
BuildRequires: ptscotch-mpich-devel-parmetis >= 7.0.1
Requires: %{name}-common = %{version}-%{release}
Requires: mpich%{?_isa}
Requires: scalapack-mpich%{?_isa}
Requires: ptscotch-mpich%{?_isa} >= 7.0.1
%description mpich
MUMPS libraries compiled against MPICH.

%package mpich-devel
Summary: The MUMPS headers and development-related files
BuildRequires: mpich-devel
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
Requires: %{name}-srpm-macros = %{version}-%{release}
%description mpich-devel
Shared links, header files for MUMPS.

%package mpich-examples
Summary: The MUMPS MPICH common illustrative test programs
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
Requires: gcc-gfortran%{?_isa}
Requires: mpich
%description mpich-examples
This package contains common illustrative
test programs about how MUMPS-mpich can be used.
%endif
##########################################################

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}_%{version}

%patch -P 0 -p1 -b .examples-mpilibs
%patch -P 1 -p1 -b .shared-pord
%patch -P 2 -p1 -b .shared

mv examples/README examples/README-examples

%build

rm -f Makefile.inc
%if 0%{?with_openmpi}
%{_openmpi_load}
cp -f %{SOURCE1} Makefile.inc
sed -e 's|@@FFLAGS@@|%{build_fflags} -fPIC -Dscotch -Dmetis -Dptscotch -DWITHOUT_PTHREAD -DINTSIZE32 -I${MPI_FORTRAN_MOD_DIR}|g' -i Makefile.inc
sed -e 's|@@CFLAGS@@|%{build_cflags} -fPIC -Dscotch -Dmetis -Dptscotch -DWITHOUT_PTHREAD -DINTSIZE32|g' -i Makefile.inc
sed -e 's|@@LDFLAGS@@|%{__global_ldflags}|g' -i Makefile.inc
sed -e 's|@@MPICLIB@@|-lmpi|g' -i Makefile.inc
MUMPS_MPI=openmpi
MUMPS_INCDIR=-I$MPI_INCLUDE
LMETISDIR=%{_libdir}
LMETIS="-lmetis -L$MPI_LIB -lptscotchparmetis"
IMETIS=-I%{_includedir}
SCOTCHDIR=$MPI_LIB
ISCOTCH=-I$MPI_INCLUDE/scotch
LSCOTCH=" -L$MPI_LIB -lesmumps -lscotch -lscotcherr -lptesmumps -lptscotch -lptscotcherr"
IPORD=" -I$PWD/PORD/include/"
LPORD=" -L$PWD/PORD/lib -lpord"
FPIC_OPT=-fPIC
export MPIBLACSLIBS=""
export MPI_COMPILER_NAME=openmpi
export LD_LIBRARY_PATH="$MPI_LIB:%{_libdir}"
export LDFLAGS="%{__global_ldflags}"
mkdir -p %{name}-%{version}-$MPI_COMPILER_NAME/lib
mkdir -p %{name}-%{version}-$MPI_COMPILER_NAME/examples
mkdir -p %{name}-%{version}-$MPI_COMPILER_NAME/modules
export LIBBLAS="-L%{_libdir} -lflexiblas"
export INCBLAS=-I%{_includedir}/flexiblas
make all \
 SONAME_VERSION=%{soname_version} \
 CC=$MPI_BIN/mpicc \
 FC=$MPI_BIN/mpif77 \
 FL=$MPI_BIN/mpif77 \
 MUMPS_MPI="$MUMPS_MPI" \
 MUMPS_INCDIR="$MUMPS_INCDIR $INCBLAS" \
 MUMPS_LIBF77="${LIBBLAS} -L$MPI_LIB -Wl,-rpath -Wl,$MPI_LIB %{mpic_libs} $MPIFORTRANSLIB -lscalapack $MPIBLACSLIBS" \
 LMETISDIR="$LMETISDIR" LMETIS="$LMETIS" IMETIS="$IMETIS" \
 SCOTCHDIR=$SCOTCHDIR \
 ISCOTCH=$ISCOTCH \
 LSCOTCH="$LSCOTCH" \
 IPORD="$IPORD" \
 LPORD="$LPORD" \
 OPTL="%{__global_ldflags}"
%{_openmpi_unload}
cp -pr lib/* %{name}-%{version}-$MPI_COMPILER_NAME/lib
cp -pr examples/* %{name}-%{version}-$MPI_COMPILER_NAME/examples
rm -rf lib/*
cp -a include %{name}-%{version}-$MPI_COMPILER_NAME/
cp -pr src/*.mod %{name}-%{version}-$MPI_COMPILER_NAME/modules
make clean
%endif
%if 0%{?with_mpich}
rm -f Makefile.inc
cp -f %{SOURCE1} Makefile.inc
sed -e 's| -DBLR_MT||g' -i Makefile.inc
%{_mpich_load}
%global mpif77_cflags %(env PKG_CONFIG_PATH=%{_libmpichdir}/pkgconfig pkg-config --cflags mpich)
%global mpif77_libs %(env PKG_CONFIG_PATH=%{_libmpichdir}/pkgconfig pkg-config --libs mpich)
%global mpifort_cflags %(env PKG_CONFIG_PATH=%{_libmpichdir}/pkgconfig pkg-config --cflags mpich)
%global mpifort_libs %(env PKG_CONFIG_PATH=%{_libmpichdir}/pkgconfig pkg-config --libs mpich)
%global mpich_libs %(env PKG_CONFIG_PATH=%{_libmpichdir}/pkgconfig pkg-config --libs mpich)
sed -e 's|@@FFLAGS@@|%{build_fflags} -fPIC -Dscotch -Dmetis -Dptscotch -DWITHOUT_PTHREAD -DINTSIZE32 -I${MPI_FORTRAN_MOD_DIR}|g' -i Makefile.inc
sed -e 's|@@LDFLAGS@@|%{__global_ldflags}|g' -i Makefile.inc
sed -e 's|@@CFLAGS@@|%{build_cflags} -fPIC -Dscotch -Dmetis -Dptscotch -DWITHOUT_PTHREAD -DINTSIZE32|g' -i Makefile.inc
sed -e 's|@@MPICLIB@@|-lmpich|g' -i Makefile.inc
sed -e 's|@@MPIFORTRANLIB@@|%{mpifort_libs}|g' -i Makefile.inc
MUMPS_MPI=mpich
MUMPS_INCDIR=-I$MPI_INCLUDE
LMETISDIR=$MPI_LIB
LMETIS="-lmetis -L$MPI_LIB -lptscotchparmetis"
IMETIS=-I%{_includedir}
SCOTCHDIR=$MPI_LIB
ISCOTCH=-I$MPI_INCLUDE/scotch
LSCOTCH="-L$MPI_LIB -lesmumps -lscotch -lscotcherr -lptesmumps -lptscotch -lptscotcherr"
export IPORD=" -I$PWD/PORD/include/"
export LPORD=" -L$PWD/PORD/lib -lpord"
FPIC_OPT=-fPIC
export MPIBLACSLIBS=""
export MPI_COMPILER_NAME=mpich
export LD_LIBRARY_PATH=$MPI_LIB:%{_libdir}
export LDFLAGS="%{__global_ldflags}"
mkdir -p %{name}-%{version}-$MPI_COMPILER_NAME/lib
mkdir -p %{name}-%{version}-$MPI_COMPILER_NAME/examples
mkdir -p %{name}-%{version}-$MPI_COMPILER_NAME/modules
export LIBBLAS="-L%{_libdir} -lflexiblas"
export INCBLAS=-I%{_includedir}/flexiblas
make all \
 SONAME_VERSION=%{soname_version} \
 CC=$MPI_BIN/mpicc \
 FC=$MPI_BIN/mpif77 \
 FL=$MPI_BIN/mpif77 \
 MUMPS_MPI="$MUMPS_MPI" \
 MUMPS_INCDIR="$MUMPS_INCDIR $INCBLAS" \
 MUMPS_LIBF77="${LIBBLAS} -L$MPI_LIB %{mpich_libs} $MPIFORTRANSLIB -lscalapack $MPIBLACSLIBS" \
 LMETISDIR="$LMETISDIR" LMETIS="$LMETIS" IMETIS="$IMETIS" \
 SCOTCHDIR=$SCOTCHDIR \
 ISCOTCH=$ISCOTCH \
 LSCOTCH="$LSCOTCH" \
 IPORD="$IPORD" \
 LPORD="$LPORD" \
 OPTL="%{__global_ldflags}"
%{_mpich_unload}
cp -pr lib/* %{name}-%{version}-$MPI_COMPILER_NAME/lib
cp -pr examples/* %{name}-%{version}-$MPI_COMPILER_NAME/examples
cp -a include %{name}-%{version}-$MPI_COMPILER_NAME/
rm -rf lib/*
cp -pr src/*.mod %{name}-%{version}-$MPI_COMPILER_NAME/modules
make clean
%endif
patch -p1 < %{PATCH3}
rm -f Makefile.inc
cp -f %{SOURCE2} Makefile.inc
sed -e 's| -DBLR_MT||g' -i Makefile.inc
sed -e 's|@@FFLAGS@@|%{build_fflags} -fPIC -Dscotch -Dmetis -DWITHOUT_PTHREAD -DINTSIZE32|g' -i Makefile.inc
sed -e 's|@@LDFLAGS@@|%{__global_ldflags}|g' -i Makefile.inc
sed -e 's|@@CFLAGS@@|%{build_cflags} -fPIC -Dscotch -Dmetis -DWITHOUT_PTHREAD -DINTSIZE32|g' -i Makefile.inc
mkdir -p %{name}-%{version}/lib
mkdir -p %{name}-%{version}/examples
mkdir -p %{name}-%{version}/modules
IPORD=" -I$PWD/PORD/include/"
LPORD=" -L$PWD/PORD/lib -lpord"
FPIC_OPT=-fPIC
export LIBBLAS="-L%{_libdir} -lflexiblas"
export INCBLAS=-I%{_includedir}/flexiblas
export LDFLAGS="%{__global_ldflags}"
make all \
 SONAME_VERSION=%{soname_version} \
 CC=gcc \
 FC=gfortran \
 FL=gfortran \
 MUMPS_LIBF77="${LIBBLAS}" \
 LIBBLAS="${LIBBLAS}" \
 LIBOTHERS=" -lpthread" \
 LIBSEQ="-L../libseq -lmpiseq" \
 INCSEQ="-I../libseq $INCBLAS" \
 LMETISDIR=%{_libdir} \
 IMETIS=-I%{_includedir} \
 LMETIS="-L%{_libdir} -lmetis -lscotchmetis" \
 SCOTCHDIR=%{_prefix} \
 ISCOTCH=-I%{_includedir}/scotch \
 LSCOTCH=" -L%{_libdir} -lesmumps -lscotch -lscotcherr" \
 IPORD="$IPORD" \
 LPORD="$LPORD" \
 OPTL="%{__global_ldflags}"
make -C examples
cp -pr lib/* %{name}-%{version}/lib
cp -pr examples/* %{name}-%{version}/examples
cp -a include %{name}-%{version}/
rm -rf lib/*
cp -pr src/*.mod %{name}-%{version}/modules
make clean
iconv -f iso8859-1 -t utf-8 README > README-t && mv README-t README
%check

pushd %{name}-%{version}/examples
LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir} \
 ./ssimpletest < input_simpletest_real
LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir} \
 ./dsimpletest < input_simpletest_real
LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir} \
 ./csimpletest < input_simpletest_cmplx
LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir} \
 ./zsimpletest < input_simpletest_cmplx
LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir} \
 ./c_example
popd
%if 0%{?with_openmpi_check}
%{_openmpi_load}
pushd %{name}-%{version}-openmpi/examples
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT$MPI_LIB
./ssimpletest < input_simpletest_real
./dsimpletest < input_simpletest_real
./csimpletest < input_simpletest_cmplx
./zsimpletest < input_simpletest_cmplx
mpirun -np 3 ./c_example
popd
%{_openmpi_unload}
%endif
%if 0%{?with_mpich_check}
%{_mpich_load}
pushd %{name}-%{version}-mpich/examples
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT$MPI_LIB
./ssimpletest < input_simpletest_real
./dsimpletest < input_simpletest_real
./csimpletest < input_simpletest_cmplx
./zsimpletest < input_simpletest_cmplx
mpirun -np 3 ./c_example
popd
%{_mpich_unload}
%endif
%install
%if 0%{?with_openmpi}
%{_openmpi_load}
mkdir -p $RPM_BUILD_ROOT$MPI_LIB
mkdir -p $RPM_BUILD_ROOT%{_libdir}/openmpi/%{name}-%{version}-examples
mkdir -p $RPM_BUILD_ROOT$MPI_INCLUDE
mkdir -p $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}-%{version}
install -cpm 755 %{name}-%{version}-openmpi/lib/lib*-*.so $RPM_BUILD_ROOT$MPI_LIB
install -cpm 755 %{name}-%{version}-openmpi/lib/libmumps_common.so $RPM_BUILD_ROOT$MPI_LIB
install -cpm 755 %{name}-%{version}-openmpi/lib/lib*mumps.so $RPM_BUILD_ROOT$MPI_LIB
install -cpm 755 %{name}-%{version}-openmpi/lib/lib*mumps-%{soname_version}.so $RPM_BUILD_ROOT$MPI_LIB
install -cpm 755 %{name}-%{version}-openmpi/lib/libpord-%{soname_version}.so $RPM_BUILD_ROOT$MPI_LIB
install -cpm 755 %{name}-%{version}-openmpi/lib/libpord.so $RPM_BUILD_ROOT$MPI_LIB
ln -sf libsmumps-%{soname_version}.so $RPM_BUILD_ROOT$MPI_LIB/libsmumps.so
ln -sf libcmumps-%{soname_version}.so $RPM_BUILD_ROOT$MPI_LIB/libcmumps.so
ln -sf libzmumps-%{soname_version}.so $RPM_BUILD_ROOT$MPI_LIB/libzmumps.so
ln -sf libdmumps-%{soname_version}.so $RPM_BUILD_ROOT$MPI_LIB/libdmumps.so
ln -sf libmumps_common-%{soname_version}.so $RPM_BUILD_ROOT$MPI_LIB/libmumps_common.so
ln -sf libpord-%{soname_version}.so $RPM_BUILD_ROOT$MPI_LIB/libpord.so
install -cpm 755 %{name}-%{version}-openmpi/examples/?simpletest $RPM_BUILD_ROOT%{_libdir}/openmpi/%{name}-%{version}-examples
install -cpm 755 %{name}-%{version}-openmpi/examples/input_* $RPM_BUILD_ROOT%{_libdir}/openmpi/%{name}-%{version}-examples
install -cpm 755 %{name}-%{version}-openmpi/examples/README-* $RPM_BUILD_ROOT%{_libdir}/openmpi/%{name}-%{version}-examples
install -cpm 644 %{name}-%{version}-openmpi/include/*.h $RPM_BUILD_ROOT$MPI_INCLUDE
install -cpm 644 PORD/include/* $RPM_BUILD_ROOT$MPI_INCLUDE
install -cpm 644 %{name}-%{version}-openmpi/modules/* $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}-%{version}/
%{_openmpi_unload}
%endif
%if 0%{?with_mpich}
%{_mpich_load}
mkdir -p $RPM_BUILD_ROOT$MPI_LIB
mkdir -p $RPM_BUILD_ROOT%{_libdir}/mpich/%{name}-%{version}-examples
mkdir -p $RPM_BUILD_ROOT$MPI_INCLUDE
mkdir -p $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}-%{version}
install -cpm 755 %{name}-%{version}-mpich/lib/lib*-*.so $RPM_BUILD_ROOT$MPI_LIB
install -cpm 755 %{name}-%{version}-mpich/lib/libmumps_common.so $RPM_BUILD_ROOT$MPI_LIB
install -cpm 755 %{name}-%{version}-mpich/lib/lib*mumps.so $RPM_BUILD_ROOT$MPI_LIB
install -cpm 755 %{name}-%{version}-mpich/lib/lib*mumps-%{soname_version}.so $RPM_BUILD_ROOT$MPI_LIB
install -cpm 755 %{name}-%{version}-mpich/lib/libpord-%{soname_version}.so $RPM_BUILD_ROOT$MPI_LIB
install -cpm 755 %{name}-%{version}-mpich/lib/libpord.so $RPM_BUILD_ROOT$MPI_LIB
ln -sf libsmumps-%{soname_version}.so $RPM_BUILD_ROOT$MPI_LIB/libsmumps.so
ln -sf libcmumps-%{soname_version}.so $RPM_BUILD_ROOT$MPI_LIB/libcmumps.so
ln -sf libzmumps-%{soname_version}.so $RPM_BUILD_ROOT$MPI_LIB/libzmumps.so
ln -sf libdmumps-%{soname_version}.so $RPM_BUILD_ROOT$MPI_LIB/libdmumps.so
ln -sf libmumps_common-%{soname_version}.so $RPM_BUILD_ROOT$MPI_LIB/libmumps_common.so
ln -sf libpord-%{soname_version}.so $RPM_BUILD_ROOT$MPI_LIB/libpord.so
install -cpm 755 %{name}-%{version}-mpich/examples/?simpletest $RPM_BUILD_ROOT%{_libdir}/mpich/%{name}-%{version}-examples
install -cpm 755 %{name}-%{version}-mpich/examples/input_* $RPM_BUILD_ROOT%{_libdir}/mpich/%{name}-%{version}-examples
install -cpm 755 %{name}-%{version}-mpich/examples/README-* $RPM_BUILD_ROOT%{_libdir}/mpich/%{name}-%{version}-examples
install -cpm 644 %{name}-%{version}-mpich/include/*.h $RPM_BUILD_ROOT$MPI_INCLUDE
install -cpm 644 PORD/include/* $RPM_BUILD_ROOT$MPI_INCLUDE
install -cpm 644 %{name}-%{version}-mpich/modules/* $RPM_BUILD_ROOT$MPI_FORTRAN_MOD_DIR/%{name}-%{version}/
%{_mpich_unload}
%endif
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}-%{version}/examples
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_fmoddir}/%{name}-%{version}
install -cpm 755 %{name}-%{version}/lib/lib*-*.so $RPM_BUILD_ROOT%{_libdir}/
ln -sf libsmumps-%{soname_version}.so $RPM_BUILD_ROOT%{_libdir}/libsmumps.so
ln -sf libcmumps-%{soname_version}.so $RPM_BUILD_ROOT%{_libdir}/libcmumps.so
ln -sf libzmumps-%{soname_version}.so $RPM_BUILD_ROOT%{_libdir}/libzmumps.so
ln -sf libdmumps-%{soname_version}.so $RPM_BUILD_ROOT%{_libdir}/libdmumps.so
ln -sf libmumps_common-%{soname_version}.so $RPM_BUILD_ROOT%{_libdir}/libmumps_common.so
ln -sf libpord-%{soname_version}.so $RPM_BUILD_ROOT%{_libdir}/libpord.so
ln -sf libmpiseq-%{soname_version}.so $RPM_BUILD_ROOT%{_libdir}/libmpiseq.so
install -cpm 755 %{name}-%{version}/examples/?simpletest $RPM_BUILD_ROOT%{_libexecdir}/%{name}-%{version}/examples
install -cpm 755 %{name}-%{version}/examples/input_* $RPM_BUILD_ROOT%{_libexecdir}/%{name}-%{version}/examples
install -cpm 755 %{name}-%{version}/examples/README-* $RPM_BUILD_ROOT%{_libexecdir}/%{name}-%{version}/examples
install -cpm 644 %{name}-%{version}/modules/* $RPM_BUILD_ROOT%{_fmoddir}/%{name}-%{version}/
install -cpm 644 %{name}-%{version}/include/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}
install -cpm 644 libseq/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}
install -cpm 644 PORD/include/* $RPM_BUILD_ROOT%{_includedir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_rpmmacrodir}
cat > $RPM_BUILD_ROOT%{_rpmmacrodir}/macros.MUMPS <<EOF
%%_MUMPS_version %{version}
EOF
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if 0%{?with_openmpi}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
