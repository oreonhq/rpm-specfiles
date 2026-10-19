%global source0_hash 928c2f18d350a91443fe8024ad01ce2c6009e9c551e0a73e797fc567f119137d
Summary:        A high-performance implementation of MPI
Name:           mpich
Version:        5.0.2
Release:        1%{?dist}
License:        mpich2
URL:            https://www.mpich.org/
Source0:        https://www.mpich.org/static/downloads/%{version}/%{name}-%{version}.tar.gz
Source1:        mpich.macros
Source3:        mpich.pth.py3
Patch:          0001-pkgconf-remove-optimization-and-link-flags-from-pkgc.patch
Patch:          0002-pkgconf-also-drop-rpath-flags-from-pkgconf-file.patch
Patch:          0003-Drop-build-flags-e.g.-specs.-and-lto-from-mpi-wrappe.patch
Patch:          0004-Make-mpich.module-useful.patch
Patch:          mpich-aclocal_cc-implicit-int.patch
Patch:          mpich-json-configure-__thread.patch
%ifarch aarch64 ppc64le x86_64 riscv64
%endif
Provides:       bundled(yaksa) = 0.2
%ifarch %{valgrind_arches}
%endif
Provides:       mpi
Provides:       mpich2 = %{version}
Obsoletes:      mpich2 < 3.0
Requires:       environment(modules)
Requires:       (python(abi) = %{python3_version} if python3)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  hwloc-devel
BuildRequires:  libfabric-devel
BuildRequires:  libnl3-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  numactl-devel
BuildRequires:  perl(lib)
BuildRequires:  python3-devel
BuildRequires:  rpm-mpi-hooks
# /oreon:deps
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
Provides:       mpich2-autoload = 3.0.1
Obsoletes:      mpich2-autoload < 3.0
%description autoload
This package contains profile files that make mpich automatically loaded.

%package devel
Summary:        Development files for mpich
Provides:       %{name}-devel-static = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Requires:       gcc-gfortran
Requires:       rpm-mpi-hooks
Requires:       redhat-rpm-config
Provides:       mpich2-devel = 3.0.1
Obsoletes:      mpich2-devel < 3.0
%description devel
Contains development headers and libraries for mpich

%package doc
Summary:        Documentations and examples for mpich
BuildArch:      noarch
Requires:       %{name}-devel = %{version}-%{release}
Provides:       mpich2-doc = 3.0.1
Obsoletes:      mpich2-doc < 3.0
%description doc
Contains documentations, examples and man-pages for mpich

%package -n python3-mpich
Summary:        mpich support for Python 3
Requires:       %{name} = %{version}-%{release}
Requires:       python(abi) = %{python3_version}
%description -n python3-mpich
mpich support for Python 3.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
CONFIGURE_OPTS=(
        --with-custom-version-string=%{version}-%{release}
        --enable-sharedlibs=gcc
        --enable-shared
        --enable-static=no
        --enable-lib-depend
        --disable-rpath
        --disable-silent-rules
        --disable-dependency-tracking
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
)
%configure "${CONFIGURE_OPTS[@]}"               \
  FFLAGS="$FFLAGS -fallow-argument-mismatch"    \
  FCFLAGS="$FCFLAGS -fallow-argument-mismatch"
sed -r -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -r -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
sed -i -e 's| -shared | -Wl,--as-needed\0|g' libtool
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
%oreon_autofiles python3-mpich usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check VERBOSE=1 \
%ifarch ppc64le
|| :
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n mpich-autoload -f %{oreon_filedir}/mpich-autoload.list
%files -n mpich-devel -f %{oreon_filedir}/mpich-devel.list
%files -n mpich-doc -f %{oreon_filedir}/mpich-doc.list
%files -n python3-mpich -f %{oreon_filedir}/python3-mpich.list

%changelog

%autochangelog
