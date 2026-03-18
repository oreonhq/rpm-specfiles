%if %{defined rhel}
%bcond_with mpich
%else
# TODO check later if we can enable mpich on s390x
%ifarch s390 s390x
%bcond_with mpich
%else
%bcond_without mpich
%endif
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
Version:        3.3.10
Release:        17%{?dist}
Summary:        A Fast Fourier Transform library
# Generally, the code is under GPL but some headers are also under MIT or BSD:
License:        GPL-2.0-or-later AND MIT AND BSD-2-Clause
URL:            http://www.fftw.org
Source0:        http://www.fftw.org/fftw-%{version}.tar.gz
# https://github.com/FFTW/fftw3/pull/346
Patch1:         fix_autotools_build.patch

BuildRequires:  gcc-gfortran

%global quad 0
# Quad precision support only available with gcc >= 4.6 (Fedora >= 15)
# and only on these arches
%ifarch %{ix86} x86_64 ia64
%global quad 1
%endif

# Names of precisions to (maybe) build
%global prec_names prec_name[0]=single;prec_name[1]=double;prec_name[2]=long;prec_name[3]=quad
# Number of precisions to build; sometimes quad is not possible
%global nprec 3
%if %{quad}
%global nprec 4
%endif
# Number of precisions to build for MPI
%global nmpiprec 3

# For check phase
BuildRequires:  time
BuildRequires:  perl-interpreter
%if %{with mpich}
BuildRequires:  mpich-devel
BuildRequires:  nss-myhostname
%endif
%if %{with openmpi}
BuildRequires:  openmpi-devel
%endif
%if %{with mpich} || %{with openmpi}
BuildRequires:  environment-modules
%endif
BuildRequires:  make


%description
FFTW is a C subroutine library for computing the Discrete Fourier
Transform (DFT) in one or more dimensions, of both real and complex
data, and of arbitrary input size.

%package libs
Summary:        FFTW run-time library
Provides:       fftw3 = %{version}-%{release}
# Libs rearranged in 3.3.1-2
Obsoletes:      fftw-libs-threads < %{version}-%{release}
Obsoletes:      fftw-libs-openmp < %{version}-%{release}

# Pull in the actual libraries
Requires:       %{name}-libs-single%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs-double%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs-long%{?_isa} = %{version}-%{release}
%if %{quad}
Requires:       %{name}-libs-quad%{?_isa} = %{version}-%{release}
%endif

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

%if %{quad}
%package libs-quad
Summary:        FFTW library, quadruple

%description libs-quad
This package contains the FFTW library compiled in quadruple
precision.
%endif

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

# Pull in the actual libraries
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

# Pull in the actual libraries
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
%autosetup -p1

%build
%if %{with mpich} || %{with openmpi}
# Explicitly load shell support for the environment-modules package, used
# below via 'module' pseudo-command.
. /etc/profile.d/modules.sh
%endif

# Configure uses g77 by default, if present on system
export F77=gfortran

BASEFLAGS="--enable-shared --disable-dependency-tracking --enable-threads"
BASEFLAGS+=" --enable-openmp"

%prec_names

# Corresponding flags
prec_flags[0]=--enable-single
prec_flags[1]=--enable-double
prec_flags[2]=--enable-long-double
prec_flags[3]=--enable-quad-precision

%ifarch x86_64
# Enable SSE2 and AVX support for x86_64
for ((i=0; i<2; i++)) ; do
    prec_flags[i]+=" --enable-sse2 --enable-avx --enable-avx2"
done
%endif

%ifarch %{arm64}
# Compile support for NEON instructions
for ((i=0; i<2; i++)) ; do
    prec_flags[i]+=" --enable-neon"
done
BASEFLAGS+=" --enable-armv8-cntvct-el0"
%endif

%ifarch ppc ppc64
# Compile support for Altivec instructions; only supported for single precision
for ((i=0; i<1; i++)) ; do
    prec_flags[i]+=" --enable-altivec"
done
%endif

# Loop over precisions
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

# MPI Builds - this duplicates the non-mpi builds, but oh well
for mpi in %{?mpi_list} ; do
    module load mpi/${mpi}-%{_arch}
    # Loop over precisions - no quad precision support with MPI
    for((iprec=0;iprec<%{nmpiprec};iprec++)) ; do
        mkdir ${mpi}-${prec_name[iprec]}${ver_name[iver]}
        cd ${mpi}-${prec_name[iprec]}${ver_name[iver]}
        ln -s ../configure .
        # Force linking the _mpi.so libraries with the mpi libs.  This works because
        # we get rid of all of the non-mpi components of these builds
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
# Explicitly load shell support for the environment-modules package, used
# below via 'module' pseudo-command.
source /etc/profile.d/modules.sh
%endif

for((iprec=0;iprec<%{nprec};iprec++)) ; do
    %make_install -C ${prec_name[iprec]}
done

# MPI
for mpi in %{?mpi_list} ; do
    module load mpi/${mpi}-%{_arch}
    for((iprec=0;iprec<%{nmpiprec};iprec++)) ; do
        %make_install -C ${mpi}-${prec_name[iprec]}
        # Remove duplicated non-mpi libraries, binaries, and data
        find %{buildroot}%{_libdir}/${mpi}/lib -name libfftw\* -a \! -name \*_mpi.\* -delete
        rm -r %{buildroot}%{_libdir}/${mpi}/{bin,share}
    done
    module unload mpi/${mpi}-%{_arch}
done

rm -f %{buildroot}%{_infodir}/dir
find %{buildroot} -name \*.la -delete

%check
%prec_names
%if %{with mpich} || %{with openmpi}
# Explicitly load shell support for the environment-modules package, used
# below via 'module' pseudo-command.
. /etc/profile.d/modules.sh
%endif

bdir=$(pwd)
for((iprec=0;iprec<%{nprec};iprec++)) ; do
    export LD_LIBRARY_PATH=$bdir/${prec_name[iprec]}/.libs:$bdir/${prec_name[iprec]}/threads/.libs
    %make_build -C ${prec_name[iprec]} check
done

# MPI
# Allow oversubscription with openmpi
export OMPI_MCA_rmaps_base_oversubscribe=1
# For openmpi 5+
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
%if %{quad}
%ldconfig_scriptlets libs-quad
%endif

%files
%{_mandir}/man1/fftw*.1*
%{_bindir}/fftw*-wisdom*

%files libs

%files libs-single
%license COPYING COPYRIGHT
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/libfftw3f.so.*
%{_libdir}/libfftw3f_threads.so.*
%{_libdir}/libfftw3f_omp.so.*

%files libs-double
%license COPYING COPYRIGHT
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/libfftw3.so.*
%{_libdir}/libfftw3_threads.so.*
%{_libdir}/libfftw3_omp.so.*

%files libs-long
%license COPYING COPYRIGHT
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/libfftw3l.so.*
%{_libdir}/libfftw3l_threads.so.*
%{_libdir}/libfftw3l_omp.so.*

%if %{quad}
%files libs-quad
%license COPYING COPYRIGHT
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/libfftw3q.so.*
%{_libdir}/libfftw3q_threads.so.*
%{_libdir}/libfftw3q_omp.so.*
%endif

%files devel
%doc doc/FAQ/fftw-faq.html/
%doc %{_infodir}/fftw3.info*
%{_includedir}/fftw3*
%dir %{_libdir}/cmake/fftw3/
%{_libdir}/cmake/fftw3/*.cmake
%{_libdir}/pkgconfig/fftw3*.pc
%{_libdir}/libfftw3*.so

%files static
%{_libdir}/libfftw3*.a

%files doc
%doc doc/*.pdf doc/html/

%if %{with mpich}
%files mpich-libs

%files mpich-libs-single
%license COPYING COPYRIGHT
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/mpich/lib/libfftw3f_mpi.so.*

%files mpich-libs-double
%license COPYING COPYRIGHT
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/mpich/lib/libfftw3_mpi.so.*

%files mpich-libs-long
%license COPYING COPYRIGHT
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/mpich/lib/libfftw3l_mpi.so.*

%files mpich-devel
%doc doc/FAQ/fftw-faq.html/
%{_includedir}/mpich-%{_arch}
%dir %{_libdir}/mpich/lib/cmake/fftw3/
%{_libdir}/mpich/lib/cmake/fftw3/*.cmake
%{_libdir}/mpich/lib/pkgconfig/fftw3*.pc
%{_libdir}/mpich/lib/libfftw3*.so

%files mpich-static
%{_libdir}/mpich/lib/libfftw3*.a
%endif

%if %{with openmpi}
%files openmpi-libs

%files openmpi-libs-single
%license COPYING COPYRIGHT
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/openmpi/lib/libfftw3f_mpi.so.*

%files openmpi-libs-double
%license COPYING COPYRIGHT
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/openmpi/lib/libfftw3_mpi.so.*

%files openmpi-libs-long
%license COPYING COPYRIGHT
%doc AUTHORS ChangeLog NEWS README* TODO
%{_libdir}/openmpi/lib/libfftw3l_mpi.so.*

%files openmpi-devel
%doc doc/FAQ/fftw-faq.html/
%{_includedir}/openmpi-%{_arch}
%dir %{_libdir}/openmpi/lib/cmake/fftw3/
%{_libdir}/openmpi/lib/cmake/fftw3/*.cmake
%{_libdir}/openmpi/lib/pkgconfig/fftw3*.pc
%{_libdir}/openmpi/lib/libfftw3*.so

%files openmpi-static
%{_libdir}/openmpi/lib/libfftw3*.a
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3.10-17
- Prepare for Oreon 11 (RP1)
