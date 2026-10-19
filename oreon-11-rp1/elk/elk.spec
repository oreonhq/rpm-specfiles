%global source0_hash dbb1f94bc14fd3247080ac3e56ee28d5d8f65ef364bdd4bef2e0d63b8d81fa56
%if 0%{?el6} || 0%{?el7}
elk-5.2.14 requires libxc 3 or newer
%quit
%endif
%{?!_fmoddir: %global _fmoddir %{_libdir}/gfortran/modules}
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%global extra_gfortran_flags -fallow-argument-mismatch
%else
%global extra_gfortran_flags %{nil}
%endif
%if 0%{?el6}
ExclusiveArch:          x86_64 %{ix86}
%else
ExclusiveArch:          x86_64 %{ix86} aarch64 %{arm} %{power64}
%endif
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%global BLASLAPACK flexiblas
%else
%global BLASLAPACK openblas
%endif
%global FFTW -L%{_libdir} -lfftw3 -lfftw3f
%if 0%{?fedora} >= 25 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%global LIBXC -L%{_libdir} -lxc -lxcf03
%else
%global LIBXC -L%{_libdir} -lxc
%endif
Name:			elk
Version:		11.0.2
Release:        1%{?dist}
Summary:        An all-electron full-potential linearised augmented-plane wave code
License:		GPL-3.0-or-later
URL:			http://elk.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tgz
Patch0:                 elk-9.2.12-libxc7.patch
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
Requires:		flexiblas-openblas-openmp
%endif
Requires:		%{name}-species = %{version}-%{release}
%global desc_base \
An all-electron full-potential linearised augmented-plane wave (FP-LAPW) code\
with many advanced features. Written originally at\
Karl-Franzens-Universität Graz as a milestone of the EXCITING EU Research and\
Training Network, the code is designed to be as simple as possible so that new\
developments in the field of density functional theory (DFT) can be added\
quickly and reliably.
# oreon:deps
BuildRequires:  fftw3-devel
BuildRequires:  flexiblas-devel
BuildRequires:  flexiblas-openblas-openmp
BuildRequires:  gcc-gfortran
BuildRequires:  libxc-devel
BuildRequires:  make
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel
BuildRequires:  patch
BuildRequires:  time
# /oreon:deps
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

mv src src.orig
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
cp -rp src.orig src
%{_openmpi_load}
%dobuild
%{_openmpi_unload}
rm -rf src
cp -rp src.orig src
%{_mpich_load}
%dobuild
%{_mpich_unload}
%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
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
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 %{name} elk-eos elk-spacegroup $RPM_BUILD_ROOT%{_bindir}
%{_openmpi_load}
%doinstall
%{_openmpi_unload}
%{_mpich_load}
%doinstall
%{_mpich_unload}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rp species $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rp make.inc* $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -rp tests tests-libxc examples $RPM_BUILD_ROOT%{_datadir}/%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export NPROC=2 # test on X cores
export OMP_NUM_THREADS=1
mv tests-libxc tests-libxc.orig
mv tests tests.orig
export TIMEOUT_OPTS='--preserve-status --kill-after 10 7200'
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
ELK_EXECUTABLE="../../%{name}" MPI_SUFFIX=_openmp %docheck
%{_openmpi_load}
ELK_EXECUTABLE="mpiexec -np ${NPROC} ../../%{name}$MPI_SUFFIX" %docheck
%{_openmpi_unload}
%{_mpich_load}
ELK_EXECUTABLE="mpiexec -np ${NPROC} ../../%{name}$MPI_SUFFIX" %docheck
%{_mpich_unload}
mv tests-libxc.orig tests-libxc
mv tests.orig tests
%files -f %{oreon_filedir}/main.list
%files -n elk-openmpi -f %{oreon_filedir}/elk-openmpi.list
%files -n elk-mpich -f %{oreon_filedir}/elk-mpich.list
%files -n elk-species -f %{oreon_filedir}/elk-species.list
%files -n elk-common -f %{oreon_filedir}/elk-common.list

%changelog

%autochangelog
