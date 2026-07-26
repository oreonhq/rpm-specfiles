%global source0_hash a8b536ddeb0f173b9273941da3513a6919f7916b07532e16a050a9d224b7ef02

# Warning:
# Anyone editing this spec file please make sure the same spec file
# works on other fedora and epel releases, which are supported by this software.
# No quick Rawhide-only fixes will be allowed.

%if 0%{?el6} || 0%{?el7}
elk-5.2.14 requires libxc 3 or newer
%quit
%endif

# missing on el6
%{?!_fmoddir: %global _fmoddir %{_libdir}/gfortran/modules}

%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9
%global extra_gfortran_flags -fallow-argument-mismatch
%else
%global extra_gfortran_flags %{nil}
%endif

%if 0%{?el6}
# el6/ppc64 Error: No Package found for mpich-devel
ExclusiveArch:          x86_64 %{ix86}
%else
%if 0%{?fedora} >= 40
ExclusiveArch:          x86_64 aarch64 %{arm} %{power64}
%else
ExclusiveArch:          x86_64 %{ix86} aarch64 %{arm} %{power64}
%endif
%endif

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global BLASLAPACK flexiblas
%else
%global BLASLAPACK openblas
%endif
%global FFTW -L%{_libdir} -lfftw3 -lfftw3f
%if 0%{?fedora} >= 25 || 0%{?rhel} >= 9
%global LIBXC -L%{_libdir} -lxc -lxcf03
%else
%global LIBXC -L%{_libdir} -lxc
%endif

Name:			elk
Version:		9.2.12
Release:		8%{?dist}
Summary:		An all-electron full-potential linearised augmented-plane wave code

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:		GPL-3.0-or-later
URL:			http://elk.sourceforge.net/
Source0:		https://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tgz

# Patch for libxc 7 compatibility: standard Fortran interface has been called libxcf03 since libxc 3
Patch0:                 elk-9.2.12-libxc7.patch

BuildRequires:		patch
BuildRequires:		time

BuildRequires:		gcc-gfortran
BuildRequires:		%{BLASLAPACK}-devel
# Use openblas-serial instead of openblas-openmp, but it's unavailable on centos stream
# due to https://bugzilla.redhat.com/show_bug.cgi?id=2182460, so use a workaround of export OMP_NUM_THREADS=1
# https://github.com/edoapra/fedpkg/issues/10#issuecomment-731855285
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
BuildRequires:		flexiblas-openblas-openmp
Requires:		flexiblas-openblas-openmp
%endif

BuildRequires:		fftw3-devel
BuildRequires:		libxc-devel

Requires:		%{name}-species = %{version}-%{release}

%global desc_base \
An all-electron full-potential linearised augmented-plane wave (FP-LAPW) code\
with many advanced features. Written originally at\
Karl-Franzens-Universität Graz as a milestone of the EXCITING EU Research and\
Training Network, the code is designed to be as simple as possible so that new\
developments in the field of density functional theory (DFT) can be added\
quickly and reliably.

%description
%{desc_base}

%package openmpi
Summary:		%{name} - openmpi version
BuildRequires:		openmpi-devel
Requires:		%{name}-species = %{version}-%{release}

%description openmpi
%{desc_base}

This package contains the openmpi version.

%package mpich
Summary:		%{name} - mpich version
BuildRequires:		mpich-devel
BuildRequires: make
Requires:		%{name}-species = %{version}-%{release}

%description mpich
%{desc_base}

This package contains the mpich version.

%package species
Summary:		%{name} - species files
Requires:		%{name}-common = %{version}-%{release}
BuildArch:		noarch

%description species
%{desc_base}

This package contains the species files.

%package common
Summary:		%{name} - common files

%description common
%{desc_base}

This package contains the common binaries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
%patch 0 -p 1 -b .libxc7

%if 0%{?fedora} >= 41
# Libxc 7 split off the functionals into a different module
sed -i 's|use xc_f03_lib_m|use xc_f03_lib_m\nuse xc_f03_funcs_m|g' src/libxcifc.f90
%endif

# create common make.inc.common
# default serial fortran
echo "SRC_MPI = mpi_stub.f90" > make.inc.common
echo "F90 = gfortran -fopenmp %{extra_gfortran_flags}" >> make.inc.common
echo "F77 = gfortran -fopenmp %{extra_gfortran_flags}" >> make.inc.common
echo "F90_OPTS = -I%{_fmoddir} %{optflags}" >> make.inc.common
echo "F77_OPTS = \$(F90_OPTS)" >> make.inc.common
echo "AR = ar" >> make.inc.common
# Use stub routines which Elk can call when libraries are not available
echo "SRC_MKL = mkl_stub.f90" >> make.inc.common
echo "SRC_BLIS = blis_stub.f90" >> make.inc.common
echo "SRC_W90S = w90_stub.f90" >> make.inc.common
# enable blas/fftw/libxc dynamic linking
echo "F90_LIB = -L%{_libdir} -l%{BLASLAPACK} %{FFTW}" >> make.inc.common
echo "SRC_FFT = zfftifc_fftw.f90 cfftifc_fftw.f90" >> make.inc.common
echo "LIB_LIBXC = %LIBXC" >> make.inc.common
echo "SRC_LIBXC = libxcifc.f90" >> make.inc.common

# remove bundling of BLAS/LAPACK/FFTW/LIBXC/ERF
sed -i "s/blas lapack fft elk/elk/" src/Makefile
sed -i "s/erf.f90//" src/Makefile
sed -i "s/,erf//" src/stheta_mp.f90
# remove bundled sources
rm -rf src/LAPACK src/BLAS src/fftlib
rm -f src/libxc_funcs.f90 src/libxc.f90 src/libxcf90.f90
rm -f src/erf.f90

%build
# Have to do off-root builds to be able to build many versions at once
mv src src.orig

# To avoid replicated code define a macro
%global dobuild() \
cp -p make.inc.common make.inc&& \
%{__sed} -i "s|F90 =.*|F90 = mpif90 -fopenmp %{extra_gfortran_flags}|" make.inc&& \
%{__sed} -i "s|F77 =.*|F77 = mpif77 -fopenmp %{extra_gfortran_flags}|" make.inc&& \
%{__sed} -i "s|F90_OPTS =|F90_OPTS = -I\${MPI_FORTRAN_MOD_DIR}|" make.inc&& \
echo "SRC_MPI =" >> make.inc&&\
cat make.inc&& \
cp -p make.inc make.inc$MPI_SUFFIX&& \
%{__make}&& \
mv src/%{name} %{name}$MPI_SUFFIX&& \
%{__make} clean

# build serial/openmp version
export MPI_SUFFIX=_openmp
cp -rp src.orig src
cp -p make.inc.common make.inc&& \
cat make.inc&& \
cp -p make.inc make.inc$MPI_SUFFIX&& \
%{__make}&& \
mv src/%{name} .&& \
mv src/eos/eos elk-eos&& \
mv src/spacegroup/spacegroup elk-spacegroup&& \
%{__make} clean&& \
rm -rf src

# build openmpi version
cp -rp src.orig src
%{_openmpi_load}
%dobuild
%{_openmpi_unload}
rm -rf src

cp -rp src.orig src
# build mpich version
%{_mpich_load}
%dobuild
%{_mpich_unload}
# leave last src build for debuginfo

%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}

# To avoid replicated code define a macro
%global doinstall() \
mkdir -p $RPM_BUILD_ROOT/$MPI_BIN&& \
install -p -m 755 %{name}$MPI_SUFFIX $RPM_BUILD_ROOT/$MPI_BIN/%{name}_binary$MPI_SUFFIX&& \
echo '#!/bin/bash' >  $RPM_BUILD_ROOT/$MPI_BIN/%{name}$MPI_SUFFIX&& \
echo 'export FLEXIBLAS=openblas-openmp' >>  $RPM_BUILD_ROOT/$MPI_BIN/%{name}$MPI_SUFFIX&& \
echo 'export OMP_NUM_THREADS=1' >>  $RPM_BUILD_ROOT/$MPI_BIN/%{name}$MPI_SUFFIX&& \
echo -n "%{name}_binary$MPI_SUFFIX " >>  $RPM_BUILD_ROOT/$MPI_BIN/%{name}$MPI_SUFFIX&& \
echo '"$@"' >>  $RPM_BUILD_ROOT/$MPI_BIN/%{name}$MPI_SUFFIX&& \
chmod 755  $RPM_BUILD_ROOT/$MPI_BIN/%{name}$MPI_SUFFIX&& \
cat $RPM_BUILD_ROOT/$MPI_BIN/%{name}$MPI_SUFFIX

# install serial version
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 %{name} elk-eos elk-spacegroup $RPM_BUILD_ROOT%{_bindir}

# install openmpi version
%{_openmpi_load}
%doinstall
%{_openmpi_unload}

# install mpich version
%{_mpich_load}
%doinstall
%{_mpich_unload}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}

# don't copy utilities - they trigger dependency on perl, python ...
cp -rp species $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rp make.inc* $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rp tests tests-libxc examples $RPM_BUILD_ROOT%{_datadir}/%{name}

%check

export NPROC=2 # test on X cores
export OMP_NUM_THREADS=1

# save tests
mv tests-libxc tests-libxc.orig
mv tests tests.orig

export TIMEOUT_OPTS='--preserve-status --kill-after 10 7200'

# To avoid replicated code define a macro
%global docheck() \
cp -rp tests-libxc.orig tests-libxc&& \
cp -rp tests.orig tests&& \
sed -i "s#mpirun -n 4 ../../src/elk#$ELK_EXECUTABLE#g" tests/test-mpi.sh&& \
sed -i "/Failed/ a \ \ \ \ cat test.log" tests/test-mpi.sh&& \
timeout ${TIMEOUT_OPTS} time %{__make} test-libxc-mpi 2>&1 | tee test-libxc-mpi.${NPROC}$MPI_SUFFIX.log&& \
rm -rf tests tests-libxc&& \
cp -rp tests.orig tests&& \
sed -i "s#mpirun -n 4 ../../src/elk#$ELK_EXECUTABLE#g" tests/test-mpi.sh&& \
sed -i "/Failed/ a \ \ \ \ cat test.log" tests/test-mpi.sh&& \
timeout ${TIMEOUT_OPTS} time %{__make} test-mpi 2>&1 | tee test-mpi.${NPROC}$MPI_SUFFIX.log&& \
rm -rf tests

# check serial version
ELK_EXECUTABLE="../../%{name}" MPI_SUFFIX=_openmp %docheck

# check openmpi version
%{_openmpi_load}
ELK_EXECUTABLE="mpiexec -np ${NPROC} ../../%{name}$MPI_SUFFIX" %docheck
%{_openmpi_unload}

# this will fail for mpich2 on el6 - mpd would need to be started ...
# check mpich version
%{_mpich_load}
ELK_EXECUTABLE="mpiexec -np ${NPROC} ../../%{name}$MPI_SUFFIX" %docheck
%{_mpich_unload}

# restore tests
mv tests-libxc.orig tests-libxc
mv tests.orig tests

%files
%{_bindir}/%{name}

%files common
%doc COPYING README
%{_bindir}/elk-eos
%{_bindir}/elk-spacegroup
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/species

%files species
%{_datadir}/%{name}/species

%files openmpi
%{_libdir}/openmpi%{?_opt_cc_suffix}/bin/%{name}_binary_openmpi
%{_libdir}/openmpi%{?_opt_cc_suffix}/bin/%{name}_openmpi

%files mpich
%{_libdir}/mpich%{?_opt_cc_suffix}/bin/%{name}_binary_mpich
%{_libdir}/mpich%{?_opt_cc_suffix}/bin/%{name}_mpich

%changelog
%autochangelog
