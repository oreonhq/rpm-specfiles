%global source0_hash 5630c24cdeb33b131612f7eb4b1a9934234754f9f388ff8617458d0be6f239a1
%ifarch s390 s390x
%bcond_with mpich
%else
%bcond_without mpich
%endif
%ifarch s390 s390x %{ix86}
%bcond_with openmpi
%else
%bcond_without openmpi
%endif
%if %{with mpich}
%global mpi_list %{?mpi_list} mpich
%endif
%if %{with openmpi}
%global mpi_list %{?mpi_list} openmpi
%endif
Name:           fftw
Version:        3.3.11
Release:        1%{?dist}
Summary:        A Fast Fourier Transform library
%define _lto_cflags %{nil}
License:        GPL-2.0-or-later AND MIT AND BSD-2-Clause
URL:            http://www.fftw.org
Source0:        http://www.fftw.org/fftw-%{version}.tar.gz
Patch1:         fix_autotools_build.patch
%global quad 0
%ifarch %{ix86} x86_64 ia64
%global quad 1
%endif
%global prec_names prec_name[0]=single;prec_name[1]=double;prec_name[2]=long;prec_name[3]=quad
%global nprec 3
%global nprec 4
%global nmpiprec 3
%if %{with mpich}
%endif
%if %{with openmpi}
%endif
%if %{with mpich} || %{with openmpi}
%endif
# oreon:deps
BuildRequires:  environment-modules
BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  mpich-devel
BuildRequires:  nss-myhostname
BuildRequires:  openmpi-devel
BuildRequires:  perl-interpreter
BuildRequires:  time
# /oreon:deps
%description
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

%package libs
Summary:        FFTW run-time library
Provides:       fftw3 = %{version}-%{release}
Obsoletes:      fftw-libs-threads < %{version}-%{release}
Obsoletes:      fftw-libs-openmp < %{version}-%{release}
Requires:       %{name}-libs-single%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs-double%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs-long%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs-quad%{?_isa} = %{version}-%{release}
%description libs
This is a dummy package package, pulling in the individual FFTW
run-time libraries.

%package devel
Summary:        Headers, libraries and docs for the FFTW library
Requires:       pkgconfig
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Provides:       fftw3-devel%{?_isa} = %{version}-%{release}
Provides:       fftw3-devel = %{version}-%{release}
%description devel
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

This package contains header files and development libraries needed to
develop programs using the FFTW fast Fourier transform library.

%package libs-double
Summary:        FFTW library, double precision
%description libs-double
This package contains the FFTW library compiled in double precision.

%package libs-single
Summary:        FFTW library, single precision
%description libs-single
This package contains the FFTW library compiled in single precision.

%package libs-long
Summary:        FFTW library, long double precision 
%description libs-long
This package contains the FFTW library compiled in long double
precision.

%package libs-quad
Summary:        FFTW library, quadruple
%description libs-quad
This package contains the FFTW library compiled in quadruple
precision.

%package        static
Summary:        Static versions of the FFTW libraries
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Provides:       fftw3-static%{?_isa} = %{version}-%{release}
Provides:       fftw3-static = %{version}-%{release}
%description static
The fftw-static package contains the statically linkable version of
the FFTW fast Fourier transform library.

%if %{with mpich}
%package mpich-libs
Summary:        FFTW MPICH run-time library
Provides:       fftw3-mpich = %{version}-%{release}
Requires:       %{name}-mpich-libs-single%{?_isa} = %{version}-%{release}
Requires:       %{name}-mpich-libs-double%{?_isa} = %{version}-%{release}
Requires:       %{name}-mpich-libs-long%{?_isa} = %{version}-%{release}
%description mpich-libs
This is a dummy package package, pulling in the individual FFTW
MPICH run-time libraries.

%package mpich-devel
Summary:        Headers, libraries and docs for the FFTW MPICH library
Requires:       mpich-devel
Requires:       pkgconfig
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-mpich-libs%{?_isa} = %{version}-%{release}
Provides:       fftw3-mpich-devel%{?_isa} = %{version}-%{release}
Provides:       fftw3-mpich-devel = %{version}-%{release}
%description mpich-devel
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

This package contains header files and development libraries needed to
develop programs using the FFTW fast Fourier transform library for MPICH.

%package mpich-libs-double
Summary:        FFTW MPICH library, double precision
Requires:       %{name}-libs-double%{?_isa} = %{version}-%{release}
%description mpich-libs-double
This package contains the FFTW MPICH library compiled in double precision.

%package mpich-libs-single
Summary:        FFTW MPICH library, single precision
Requires:       %{name}-libs-single%{?_isa} = %{version}-%{release}
%description mpich-libs-single
This package contains the FFTW MPICH library compiled in single precision.

%package mpich-libs-long
Summary:        FFTW MPICH library, long double precision 
Requires:       %{name}-libs-long%{?_isa} = %{version}-%{release}
%description mpich-libs-long
This package contains the FFTW MPICH library compiled in long double
precision.

%package        mpich-static
Summary:        Static versions of the FFTW MPICH libraries
Requires:       %{name}-mpich-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-static%{?_isa} = %{version}-%{release}
Provides:       fftw3-mpich-static%{?_isa} = %{version}-%{release}
Provides:       fftw3-mpich-static = %{version}-%{release}
%description mpich-static
The fftw-mpich-static package contains the statically linkable version of
the FFTW fast Fourier transform library for MPICh.
%endif

%if %{with openmpi}
%package openmpi-libs
Summary:        FFTW OpenMPI run-time library
Provides:       fftw3-openmpi = %{version}-%{release}
Requires:       %{name}-openmpi-libs-single%{?_isa} = %{version}-%{release}
Requires:       %{name}-openmpi-libs-double%{?_isa} = %{version}-%{release}
Requires:       %{name}-openmpi-libs-long%{?_isa} = %{version}-%{release}
%description openmpi-libs
This is a dummy package package, pulling in the individual FFTW
OpenMPI run-time libraries.

%package openmpi-devel
Summary:        Headers, libraries and docs for the FFTW OpenMPI library
Requires:       openmpi-devel
Requires:       pkgconfig
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-openmpi-libs%{?_isa} = %{version}-%{release}
Provides:       fftw3-openmpi-devel%{?_isa} = %{version}-%{release}
Provides:       fftw3-openmpi-devel = %{version}-%{release}
%description openmpi-devel
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

This package contains header files and development libraries needed to
develop programs using the FFTW fast Fourier transform library for OpenMPI.

%package openmpi-libs-double
Summary:        FFTW OpenMPI library, double precision
Requires:       %{name}-libs-double%{?_isa} = %{version}-%{release}
%description openmpi-libs-double
This package contains the FFTW OpenMPI library compiled in double precision.

%package openmpi-libs-single
Summary:        FFTW OpenMPI library, single precision
Requires:       %{name}-libs-single%{?_isa} = %{version}-%{release}
%description openmpi-libs-single
This package contains the FFTW OpenMPI library compiled in single precision.

%package openmpi-libs-long
Summary:        FFTW OpenMPI library, long double precision 
Requires:       %{name}-libs-long%{?_isa} = %{version}-%{release}
%description openmpi-libs-long
This package contains the FFTW OpenMPI library compiled in long double
precision.

%package        openmpi-static
Summary:        Static versions of the FFTW OpenMPI libraries
Requires:       %{name}-openmpi-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-static%{?_isa} = %{version}-%{release}
Provides:       fftw3-openmpi-static%{?_isa} = %{version}-%{release}
Provides:       fftw3-openmpi-static = %{version}-%{release}
%description openmpi-static
The fftw-openmpi-static package contains the statically linkable version of
the FFTW fast Fourier transform library for MPICh.
%endif

%package doc
Summary:        FFTW library manual
BuildArch:      noarch
%description doc
This package contains the manual for the FFTW fast Fourier transform
library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%if %{with mpich} || %{with openmpi}
. /etc/profile.d/modules.sh
%endif
export F77=gfortran
BASEFLAGS="--enable-shared --disable-dependency-tracking --enable-threads"
BASEFLAGS+=" --enable-openmp"
%prec_names
prec_flags[0]=--enable-single
prec_flags[1]=--enable-double
prec_flags[2]=--enable-long-double
prec_flags[3]=--enable-quad-precision
%ifarch x86_64
for ((i=0; i<2; i++)) ; do
    prec_flags[i]+=" --enable-sse2 --enable-avx --enable-avx2"
done
%endif
%ifarch %{arm64}
for ((i=0; i<2; i++)) ; do
    prec_flags[i]+=" --enable-neon"
done
BASEFLAGS+=" --enable-armv8-cntvct-el0"
%endif
%ifarch ppc ppc64
for ((i=0; i<1; i++)) ; do
    prec_flags[i]+=" --enable-altivec"
done
%endif
for ((iprec=0; iprec<%{nprec}; iprec++)) ; do
    mkdir ${prec_name[iprec]}${ver_name[iver]}
    cd ${prec_name[iprec]}${ver_name[iver]}
    ln -s ../configure .
    %{configure} ${BASEFLAGS} ${prec_flags[iprec]}
    sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
    sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
    %make_build
    cd ..
done
for mpi in %{?mpi_list} ; do
    module load mpi/${mpi}-%{_arch}
    for((iprec=0;iprec<%{nmpiprec};iprec++)) ; do
        mkdir ${mpi}-${prec_name[iprec]}${ver_name[iver]}
        cd ${mpi}-${prec_name[iprec]}${ver_name[iver]}
        ln -s ../configure .
        export CC=mpicc
        if [ $mpi = "openmpi" ]; then
            export MPIRUN="mpirun --oversubscribe"
        fi
        %{configure} ${BASEFLAGS} ${prec_flags[iprec]} \
            --enable-mpi \
            --libdir=%{_libdir}/$mpi/lib \
            --bindir=%{_libdir}/$mpi/bin \
            --sbindir=%{_libdir}/$mpi/sbin \
            --includedir=%{_includedir}/$mpi-%{_arch} \
            --mandir=%{_libdir}/$mpi/share/man
        %make_build
        cd ..
    done
    module unload mpi/${mpi}-%{_arch}
done
%install
%prec_names
%if %{with mpich} || %{with openmpi}
source /etc/profile.d/modules.sh
%endif
for((iprec=0;iprec<%{nprec};iprec++)) ; do
    %make_install -C ${prec_name[iprec]}
done
for mpi in %{?mpi_list} ; do
    module load mpi/${mpi}-%{_arch}
    for((iprec=0;iprec<%{nmpiprec};iprec++)) ; do
        %make_install -C ${mpi}-${prec_name[iprec]}
        find %{buildroot}%{_libdir}/${mpi}/lib -name libfftw\* -a \! -name \*_mpi.\* -delete
        rm -r %{buildroot}%{_libdir}/${mpi}/{bin,share}
    done
    module unload mpi/${mpi}-%{_arch}
done
rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -name \*.la -delete
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%prec_names
%if %{with mpich} || %{with openmpi}
. /etc/profile.d/modules.sh
%endif
bdir=$(pwd)
for((iprec=0;iprec<%{nprec};iprec++)) ; do
    export LD_LIBRARY_PATH=$bdir/${prec_name[iprec]}/.libs:$bdir/${prec_name[iprec]}/threads/.libs
    %make_build -C ${prec_name[iprec]} check
done
export OMPI_MCA_rmaps_base_oversubscribe=1
export PRTE_MCA_rmaps_default_mapping_policy=:oversubscribe
for mpi in %{?mpi_list} ; do
    module load mpi/${mpi}-%{_arch}
    for((iprec=0;iprec<%{nmpiprec};iprec++)) ; do
        export LD_LIBRARY_PATH=$bdir/${prec_name[iprec]}/.libs:$bdir/${prec_name[iprec]}/threads/.libs
        %make_build -C ${mpi}-${prec_name[iprec]}/mpi check
    done
    module unload mpi/${mpi}-%{_arch}
done
%ldconfig_scriptlets libs-single
%ldconfig_scriptlets libs-double
%ldconfig_scriptlets libs-long
%ldconfig_scriptlets libs-quad
%files -f %{oreon_filedir}/main.list
%files -n fftw-libs -f %{oreon_filedir}/fftw-libs.list
%files -n fftw-devel -f %{oreon_filedir}/fftw-devel.list
%files -n fftw-libs-double -f %{oreon_filedir}/fftw-libs-double.list
%files -n fftw-libs-single -f %{oreon_filedir}/fftw-libs-single.list
%files -n fftw-libs-long -f %{oreon_filedir}/fftw-libs-long.list
%files -n fftw-libs-quad -f %{oreon_filedir}/fftw-libs-quad.list
%files -n fftw-static -f %{oreon_filedir}/fftw-static.list
%files -n fftw-mpich-libs -f %{oreon_filedir}/fftw-mpich-libs.list
%files -n fftw-mpich-devel -f %{oreon_filedir}/fftw-mpich-devel.list
%files -n fftw-mpich-libs-double -f %{oreon_filedir}/fftw-mpich-libs-double.list
%files -n fftw-mpich-libs-single -f %{oreon_filedir}/fftw-mpich-libs-single.list
%files -n fftw-mpich-libs-long -f %{oreon_filedir}/fftw-mpich-libs-long.list
%files -n fftw-mpich-static -f %{oreon_filedir}/fftw-mpich-static.list
%files -n fftw-openmpi-libs -f %{oreon_filedir}/fftw-openmpi-libs.list
%files -n fftw-openmpi-devel -f %{oreon_filedir}/fftw-openmpi-devel.list
%files -n fftw-openmpi-libs-double -f %{oreon_filedir}/fftw-openmpi-libs-double.list
%files -n fftw-openmpi-libs-single -f %{oreon_filedir}/fftw-openmpi-libs-single.list
%files -n fftw-openmpi-libs-long -f %{oreon_filedir}/fftw-openmpi-libs-long.list
%files -n fftw-openmpi-static -f %{oreon_filedir}/fftw-openmpi-static.list
%files -n fftw-doc -f %{oreon_filedir}/fftw-doc.list

%changelog

%autochangelog
