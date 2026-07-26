%global source0_hash none

Name:           scorep
Version:        9.4
Release:        3%{?dist}
Summary:        Scalable Performance Measurement Infrastructure for Parallel Codes
License:        BSD-3-Clause
URL:            http://www.vi-hps.org/projects/score-p/
Source0:        http://perftools.pages.jsc.fz-juelich.de/cicd/scorep/tags/scorep-%{version}/scorep-%{version}.tar.gz
# GCC plug-in: Adopt API changes in GCC 16 dev;
# https://gitlab.com/score-p/scorep/-/commit/469b1a129c19dd01e4aad40b6fd511e23a3d9cbd
Patch1:         gcc16.diff
BuildRequires:  make
BuildRequires:  gcc-gfortran
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  binutils-devel
BuildRequires:  chrpath
BuildRequires:  cube-libs-devel >= 4.9
BuildRequires:  ocl-icd-devel
BuildRequires:  opari2 >= 2.0.9
BuildRequires:  otf2-devel >= 3.1
BuildRequires:  papi-devel
BuildRequires:  gcc-plugin-devel
# Required for cubelib to build scorep-score against cubew
BuildRequires:  gcc-c++
BuildRequires:  llvm-devel
BuildRequires:  clang
BuildRequires:  clang-devel
BuildRequires:  automake libtool
BuildRequires:  libunwind-devel
BuildRequires:  gotcha-devel%{?_isa} >= 1.0.5
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       binutils-devel%{?_isa}
Requires:       cube-libs-devel%{?_isa} >= 4.9
Requires:       otf2-devel%{?_isa} >= 3.1
Requires:       papi-devel%{?_isa}
Requires:       ocl-icd-devel%{?_isa}
Requires:       opari2%{?_isa} >= 2.0.9
Requires:       gotcha-devel%{?_isa} >= 1.0.5
Requires:       libunwind-devel%{?_isa}
# s390 is missing papi and libunwind; 32-bit fails with configure
# "cannot determine instruction set" in v7.0.
ExcludeArch: s390 s390x armv7hl i686

%global with_mpich 1
%global with_openmpi 1

%if %{with_mpich}
%global mpi_list mpich
%endif
%if %{with_openmpi}
%global mpi_list %{?mpi_list} openmpi
%endif

%global oshmem 1
%ifarch ppc64le
# Currently no oshmem compilers on Fedora due to UCX bug -- not clear
# what better to test.
%if %{?fedora}0
%global oshmem 0
%endif
%endif

# Avoid missing symbol link errors in test
%undefine _ld_as_needed
# Avoid in test
#   /usr/bin/ld: pomp_tpd_: TLS reference in ./.libs/libscorep_adapter_opari2_openmp_event.so mismatches non-TLS reference in jacobi_omp_f90-jacobi.mod.o
%undefine _hardened_build

%global __requires_exclude_from ^%{_libdir}(/(openmpi|mpich)/lib)?/libscorep_.*|^%{_docdir}/.*$

%global desc \
The Score-P (Scalable Performance Measurement Infrastructure for\
Parallel Codes) measurement infrastructure is a highly scalable and\
easy-to-use tool suite for profiling and event trace recording of\
HPC applications.\
Reference DOI: 10.1007/978-3-642-31476-6_7

%description
%desc

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for %{name}

%package libs
Summary:        Score-P runtime libraries
# This is useful at runtime.
Requires:       %{name}-config%{?_isa} = %{version}-%{release}

%description libs
Score-P runtime libraries.

# This is relevant for Scalasca analysis, at least, without the libraries.
%package config
Summary:        Score-P configuration files

%description config
Score-P configuration files.

%if %{with_mpich}
%package mpich
Summary:        Scalable Performance Measurement Infrastructure for Parallel Codes for mpich
BuildRequires:  mpich-devel
Requires:       %{name}-mpich-libs%{?_isa} = %{version}-%{release}
Requires:       cube-libs-devel%{?_isa} >= 4.9
Requires:       otf2-devel%{?_isa} >= 3.1
Requires:       papi-devel%{?_isa}

%description mpich
%desc

This package was compiled with mpich.

%package mpich-libs
Summary:        Score-P mpich runtime libraries
Requires:       %{name}-mpich-config%{?_isa} = %{version}-%{release}

%description mpich-libs
Score-P mpich runtime libraries.

%package mpich-config
Summary:        Score-P mpich configuration files

%description mpich-config
Score-P mpich configuration files.
%endif

%if %{with_openmpi}
%package openmpi
Summary:        Scalable Performance Measurement Infrastructure for Parallel Codes for openmpi
BuildRequires:  openmpi-devel
Requires:       %{name}-openmpi-libs%{?_isa} = %{version}-%{release}
Requires:       cube-libs-devel%{?_isa} >= 4.9
Requires:       otf2-devel%{?_isa} >= 3.1
Requires:       papi-devel%{?_isa}

%description openmpi
%desc

This package was compiled with openmpi.

%package openmpi-libs
Summary:        Score-P openmpi runtime libraries
Requires:       %{name}-openmpi-config%{?_isa} = %{version}-%{release}

%description openmpi-libs
Score-P openmpi runtime libraries.

%package openmpi-config
Summary:        Score-P openmpi configuration files

%description openmpi-config
Score-P openmpi configuration files.
%endif

%prep
%setup -q
%patch -P1 -p1 -b .gcc16
# Bundled libs in vendor/
rm -rf vendor/{opari2,otf2,cubew,cubelib}
mkdir bin
# configure expects llvm-config
ln -s %_bindir/llvm-config-%__isa_bits bin/llvm-config
pushd build-gcc-plugin
autoreconf
popd

%build
# This package uses -Wl,-wrap to wrap calls at link time.  This is incompatible
# with LTO.
# Disable LTO
%define _lto_cflags %{nil}

%global _configure ../configure
# Fixme: --disable-silent-rules or V=1 doesn't work in all parts of the build
%global configure_opts --enable-shared --disable-static --disable-silent-rules --with-libunwind=yes

cp /usr/lib/rpm/redhat/config.{sub,guess} build-config/

# Build serial version
mkdir serial
cd serial
%configure %{configure_opts} --without-mpi --without-shmem
find -name Makefile -exec sed -r -i 's,-L%{_libdir}/?( |$),,g;s,-L/usr/lib/../%{_lib} ,,g' {} \;

%make_build V=1
cd -

# Build MPI versions
for mpi in %{mpi_list}
do
  mkdir $mpi
  cd $mpi
  module load mpi/$mpi-%{_arch}
  %configure %{configure_opts} \
    --libdir=%{_libdir}/$mpi/lib \
    --bindir=%{_libdir}/$mpi/bin \
    --sbindir=%{_libdir}/$mpi/sbin \
    --datadir=%{_libdir}/$mpi/share \
    --includedir=%{_includedir}/$mpi-%{_arch} \
    --mandir=%{_libdir}/$mpi/share/man
  find -name Makefile -exec sed -r -i 's,-L%{_libdir}/?( |$),,g;s,-L/usr/lib/../%{_lib} ,,g' {} \;
  sed -i -e 's/HARDCODE_INTO_LIBS"]="1"/HARDCODE_INTO_LIBS"]="0"/' \
      -e "s/hardcode_into_libs='yes'/hardcode_into_libs='no'/" \
      build-backend/config.status
  # See serial version
  %make_build V=1
  module purge
  cd -
done

%install
%make_install -C serial

for mpi in %{mpi_list}
do
  module load mpi/$mpi-%{_arch}
  %make_install -C $mpi
  module purge
done
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -delete

# Strip rpath
chrpath -d %{buildroot}%{_libdir}/*.so.* %{buildroot}%{_bindir}/scorep-score
chrpath -d %{buildroot}%{_libexecdir}/scorep/scorep-library-wrapper-generator

# Fixme: I haven't figured out how to get this re-built with the final
# build-gcc-plugin result; kludge it for now.
find %{buildroot} -name scorep.summary | xargs sed -i -e "s|\
no, missing plug-in headers, please install|\
yes, using the C++ compiler and -I$(%_bindir/gcc -print-file-name=plugin/include)|"

%ldconfig_scriptlets libs

%check
%if %{with_openmpi}
%_openmpi_load
OMPI_MCA_rmaps_base_oversubscribe=1 \
make -C openmpi check V=1
%else
make -C serial check V=1
%endif

%files
%license COPYING
#%doc AUTHORS CITATION.cff ChangeLog README.md THANKS OPEN_ISSUES
%doc AUTHORS README.md THANKS
%{_bindir}/scorep
%{_bindir}/scorep-backend-info
%{_bindir}/scorep-g++
%{_bindir}/scorep-gcc
%{_bindir}/scorep-gfortran
%{_bindir}/scorep-info
%{_bindir}/scorep-score
%{_bindir}/scorep-wrapper
%{_bindir}/scorep-preload-init
%{_bindir}/scorep-libwrap-init
%{_libdir}/scorep/
%{_includedir}/scorep/
# Are the libtools in here necessary (different from vanilla)?
%{_libexecdir}/scorep
# Files required by scorep-info
%{_defaultdocdir}/scorep/ChangeLog
%{_defaultdocdir}/scorep/COPYING
%{_defaultdocdir}/scorep/OPEN_ISSUES
%{_defaultdocdir}/scorep/CITATION.cff

%files doc
%license COPYING
%{_defaultdocdir}/scorep/examples/
%{_defaultdocdir}/scorep/html/
%{_defaultdocdir}/scorep/pdf/
%{_defaultdocdir}/scorep/profile/
%{_defaultdocdir}/scorep/tags/

%files libs
%license COPYING
%{_libdir}/libscorep_*.so*

%files config
%license COPYING
%{_bindir}/scorep-config
%{_datadir}/scorep/

%if %{with_mpich}
%files mpich
%license COPYING
%doc AUTHORS CITATION.cff ChangeLog README.md THANKS OPEN_ISSUES
%{_libdir}/mpich/bin/scorep
%{_libdir}/mpich/bin/scorep-backend-info
%{_libdir}/mpich/bin/scorep-g++
%{_libdir}/mpich/bin/scorep-gcc
%{_libdir}/mpich/bin/scorep-gfortran
%{_libdir}/mpich/bin/scorep-info
%{_libdir}/mpich/bin/scorep-mpicc
%{_libdir}/mpich/bin/scorep-mpicxx
%{_libdir}/mpich/bin/scorep-mpif77
%{_libdir}/mpich/bin/scorep-mpif90
%{_libdir}/mpich/bin/scorep-score
%{_libdir}/mpich/bin/scorep-wrapper
%{_libdir}/mpich/bin/scorep-preload-init
%{_libdir}/mpich/bin/scorep-libwrap-init
%{_libdir}/mpich/lib/scorep/
%{_includedir}/mpich-%{_arch}/scorep/

%files mpich-libs
%license COPYING
%{_libdir}/mpich/lib/*.so*

%files mpich-config
%license COPYING
%{_libdir}/mpich/bin/scorep-config
%{_libdir}/mpich/share/scorep
%endif

%if %{with_openmpi}
%files openmpi
%license COPYING
%doc AUTHORS CITATION.cff ChangeLog README.md THANKS OPEN_ISSUES
%{_libdir}/openmpi/bin/scorep
%{_libdir}/openmpi/bin/scorep-backend-info
%{_libdir}/openmpi/bin/scorep-g++
%{_libdir}/openmpi/bin/scorep-gcc
%{_libdir}/openmpi/bin/scorep-gfortran
%{_libdir}/openmpi/bin/scorep-info
%{_libdir}/openmpi/bin/scorep-mpicc
%{_libdir}/openmpi/bin/scorep-mpicxx
%{_libdir}/openmpi/bin/scorep-mpif77
%{_libdir}/openmpi/bin/scorep-mpif90
%if %{oshmem}
%{_libdir}/openmpi/bin/scorep-oshcc
%{_libdir}/openmpi/bin/scorep-oshcxx
%{_libdir}/openmpi/bin/scorep-oshfort
%endif
%{_libdir}/openmpi/bin/scorep-score
%{_libdir}/openmpi/bin/scorep-wrapper
%{_libdir}/openmpi/bin/scorep-preload-init
%{_libdir}/openmpi/bin/scorep-libwrap-init
%{_libdir}/openmpi/lib/scorep/
%{_includedir}/openmpi-%{_arch}/scorep/

%files openmpi-libs
%license COPYING
%{_libdir}/openmpi/lib/*.so*

%files openmpi-config
%license COPYING
%{_libdir}/openmpi/bin/scorep-config
%{_libdir}/openmpi/share/scorep
%endif

%changelog
%autochangelog
