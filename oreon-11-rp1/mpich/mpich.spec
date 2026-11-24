# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 928c2f18d350a91443fe8024ad01ce2c6009e9c551e0a73e797fc567f119137d
%global source1_hash c40ceff8dafeab533e9bf31bb1dbeb15f97d7d99fc49c06a1852c7ab4ec533f1
%global source3_hash 2acaeda51628ea81b01876497dc4c84fe056317391262cab92e9dd40b0721e74
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global somajor 12
%global mpi_abi_somajor 1

Summary:        A high-performance implementation of MPI
Name:           mpich
Version:        5.0.2
Release:        %{autorelease}
License:        mpich2
URL:            https://www.mpich.org/

Source0:        https://www.mpich.org/static/downloads/%{version}/%{name}-%{version}.tar.gz
Source1:        mpich.macros
Source3:        mpich.pth.py3

Patch:          0001-pkgconf-drop-linker-flags.patch
Patch:          0002-Make-mpich.module-useful.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires:  make
BuildRequires:  gcc-gfortran
BuildRequires:  hwloc-devel >= 2.0
%if ! (0%{?rhel} >= 10)
%ifarch x86_64
BuildRequires:  libpsm2-devel
%endif
%endif
BuildRequires:  libfabric-devel
BuildRequires:  libnl3-devel
BuildRequires:  libuuid-devel
BuildRequires:  numactl-devel
%ifarch aarch64 ppc64le x86_64 riscv64
BuildRequires:  ucx-devel
%endif
%if ! 0%{?rhel}
BuildRequires:  yaksa-devel
%else
Provides:       bundled(yaksa) = 0.2
%endif
BuildRequires:  perl(lib)
%ifarch %{valgrind_arches}
BuildRequires:  valgrind-devel
%endif
BuildRequires:  python3-devel
BuildRequires:  rpm-mpi-hooks
Provides:       mpi
Requires:       environment(modules)

Requires:       (python(abi) = %{python3_version} if python3)

%description
MPICH is a high-performance and widely portable implementation of the Message
Passing Interface (MPI) standard (MPI-1, MPI-2 and MPI-3). The goals of MPICH
are: (1) to provide an MPI implementation that efficiently supports different
computation and communication platforms including commodity clusters (desktop
systems, shared-memory systems, multicore architectures), high-speed networks
(10 Gigabit Ethernet, InfiniBand, Myrinet, Quadrics) and proprietary high-end
computing systems (Blue Gene, Cray) and (2) to enable cutting-edge research in
MPI through an easy-to-extend modular framework for other derived
implementations.

The mpich binaries in this RPM packages were configured to use the default
process manager (Hydra) using the default device (ch3). The ch3 device
was configured with support for the nemesis channel that allows for
shared-memory and TCP/IP sockets based communication.

This build also include support for using the 'module environment' to select
which MPI implementation to use when multiple implementations are installed.
If you want MPICH support to be automatically loaded, you need to install the
mpich-autoload package.

%package autoload
Summary:        Load mpich automatically into profile
Requires:       mpich = %{version}-%{release}

%description autoload
This package contains profile files that make mpich automatically loaded.

%package devel
Summary:        Development files for mpich
Provides:       %{name}-devel-static = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Requires:       gcc-gfortran
Requires:       rpm-mpi-hooks
Requires:       oreon-rpm-config

%description devel
Contains development headers and libraries for mpich

%package doc
Summary:        Documentations and examples for mpich
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Contains documentations, examples and man-pages for mpich

%package -n python3-mpich
Summary:        mpich support for Python 3
Requires:       %{name} = %{version}-%{release}
Requires:       python(abi) = %{python3_version}

%description -n python3-mpich
mpich support for Python 3.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
echo '%{source3_hash}  %{SOURCE3}' | sha256sum -c -
%autosetup -p1

%conf
CONFIGURE_OPTS=(
        --with-custom-version-string=%{version}-%{release}
        --enable-mpi-abi
        --enable-shared
        --enable-static=no
        --disable-silent-rules
        --disable-dependency-tracking
        --with-wrapper-dl-type=none
        --with-gnu-ld
        --with-pm=hydra:gforker
        --includedir=%{_includedir}/%{name}-%{_arch}
        --bindir=%{_libdir}/%{name}/bin
        --libdir=%{_libdir}/%{name}/lib
        --datadir=%{_datadir}/%{name}
        --mandir=%{_mandir}/%{name}-%{_arch}
        --docdir=%{_datadir}/%{name}/doc
        --htmldir=%{_datadir}/%{name}/doc
        --with-hwloc
        --with-libfabric
%ifarch aarch64 ppc64le x86_64 riscv64
        --with-ucx
%endif
%if ! 0%{?rhel}
        --with-yaksa
%endif
)

%configure "${CONFIGURE_OPTS[@]}"               \
  FFLAGS="$FFLAGS -fallow-argument-mismatch"    \
  FCFLAGS="$FCFLAGS -fallow-argument-mismatch"

sed -r -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -r -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

sed -i -e 's| -shared | -Wl,--as-needed\0|g' libtool

%build
%make_build VERBOSE=1

%install
%make_install

mkdir -p %{buildroot}%{_fmoddir}/%{name}
mv  %{buildroot}%{_includedir}/%{name}-*/*.mod %{buildroot}%{_fmoddir}/%{name}/
sed -r -i 's|^modincdir=.*|modincdir=%{_fmoddir}/%{name}|' %{buildroot}%{_libdir}/%{name}/bin/mpifort

mkdir -p %{buildroot}%{_datadir}/modulefiles/mpi
sed -r 's|%{_bindir}|%{_libdir}/%{name}/bin|;
        s|@LIBDIR@|%{_libdir}/%{name}|;
        s|@MPINAME@|%{name}|;
        s|@py2sitearch@|%{python2_sitearch}|;
        s|@py3sitearch@|%{python3_sitearch}|;
        s|@ARCH@|%{_arch}|;
        s|@fortranmoddir@|%{_fmoddir}|;
     ' \
     <src/packaging/envmods/mpich.module \
     >%{buildroot}%{_datadir}/modulefiles/mpi/%{name}-%{_arch}

mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat >%{buildroot}%{_sysconfdir}/profile.d/mpich-%{_arch}.sh <<EOF
module load mpi/%{name}-%{_arch}
EOF
cp -p %{buildroot}%{_sysconfdir}/profile.d/mpich-%{_arch}.{sh,csh}

install -pDm0644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/macros.d/macros.%{name}

mkdir -p %{buildroot}%{python3_sitearch}/%{name}
install -pDm0644 %{SOURCE3} %{buildroot}%{python3_sitearch}/%{name}.pth

mkdir -p %{buildroot}%{_libdir}/%{name}/lib/cmake/

mkdir -p %{buildroot}%{_libdir}/%{name}/lib/cmake
mkdir -p %{buildroot}%{_libdir}/%{name}/include

find %{buildroot} -type f -name "*.la" -delete

rm %{buildroot}%{_libdir}/%{name}/bin/parkill

%check
make check VERBOSE=1 \
%ifarch ppc64le
|| :
%endif

%ldconfig_scriptlets

%files
%license COPYRIGHT
%config(noreplace) %{_sysconfdir}/mpixxx_opts.conf
%doc CHANGES README README.envvar
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/lib
%dir %{_libdir}/%{name}/bin
%dir %{_libdir}/%{name}/lib/cmake
%dir %{_libdir}/%{name}/include
%dir %{_fmoddir}/mpich
%{_libdir}/%{name}/lib/libmpi.so.%{somajor}{,.*}
%{_libdir}/%{name}/lib/libmpicxx.so.%{somajor}{,.*}
%{_libdir}/%{name}/lib/libmpifort.so.%{somajor}{,.*}
%{_libdir}/%{name}/lib/libmpi_abi.so.%{mpi_abi_somajor}{,.*}
%{_libdir}/%{name}/bin/hydra*
%{_libdir}/%{name}/bin/mpichversion
%{_libdir}/%{name}/bin/mpiexec*
%{_libdir}/%{name}/bin/mpirun
%{_libdir}/%{name}/bin/mpivars
%dir %{_mandir}/%{name}-%{_arch}
%doc %{_mandir}/%{name}-%{_arch}/man1/
%{_datadir}/modulefiles/mpi/

%files autoload
%{_sysconfdir}/profile.d/mpich-%{_arch}.*

%files devel
%{_includedir}/%{name}-%{_arch}/
%{_libdir}/%{name}/lib/pkgconfig/
%{_libdir}/%{name}/lib/cmake/
%{_libdir}/%{name}/lib/libmpi.so
%{_libdir}/%{name}/lib/libmpicxx.so
%{_libdir}/%{name}/lib/libmpifort.so
%{_libdir}/%{name}/lib/libmpi_abi.so
%{_libdir}/%{name}/lib/libmpich.so
%{_libdir}/%{name}/lib/libmpichcxx.so
%{_libdir}/%{name}/lib/libmpichf90.so
%{_libdir}/%{name}/lib/libfmpich.so
%{_libdir}/%{name}/lib/libmpl.so
%{_libdir}/%{name}/lib/libopa.so
%{_libdir}/%{name}/bin/mpicc
%{_libdir}/%{name}/bin/mpicc_abi
%{_libdir}/%{name}/bin/mpic++
%{_libdir}/%{name}/bin/mpicxx
%{_libdir}/%{name}/bin/mpicxx_abi
%{_libdir}/%{name}/bin/mpif77
%{_libdir}/%{name}/bin/mpif90
%{_libdir}/%{name}/bin/mpifort
%{_fmoddir}/%{name}/
%{_rpmconfigdir}/macros.d/macros.%{name}
%{_mandir}/%{name}-%{_arch}/man3/

%files doc
%dir %{_datadir}/%{name}
%doc %{_datadir}/%{name}/doc/

%files -n python3-mpich
%dir %{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}.pth

%changelog
%autochangelog
