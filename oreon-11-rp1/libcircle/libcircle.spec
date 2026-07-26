%global source0_hash fd8bc6e4dcc6fdec9d2a3d1c78a4060948ae4f11f0b278792610d6c05d53e14c

Name:    libcircle
Version: 0.3
Release: 21%{?dist}

Source: https://github.com/hpc/libcircle/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL: http://hpc.github.io/libcircle/
Summary: A library used to distribute workloads
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
ExcludeArch:    %{ix86}

BuildRequires:  check-devel
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
A simple interface for processing workloads using an automatically
distributed global queue.

%package openmpi
Summary:        Libcircle Open MPI libraries
BuildRequires:  openmpi-devel

%description openmpi
A simple interface for processing workloads using an automatically
distributed global queue.

libcircle compiled with Open MPI

%package mpich
Summary:        Libcircle MPICH libraries
BuildRequires:  mpich-devel
BuildRequires: make

%description mpich
A simple interface for processing workloads using an automatically
distributed global queue.

libcircle compiled with MPICH

%package doc
Summary:        Documuation for libcircle
BuildArch:      noarch

%description doc
A simple interface for processing workloads using an automatically
distributed global queue.

This package contain documenation for libcircle

%package openmpi-devel
Summary:    Development headers and libraries for Open MPI libcircle
Requires:   %{name}-openmpi%{?_isa} = %{version}-%{release}

%description openmpi-devel
A simple interface for processing workloads using an automatically
distributed global queue.

This package contains development headers and libraries for Open 
MPI ibcircle

%package mpich-devel
Summary:    Development headers and libraries for MPICH libcircle
Requires:   %{name}-mpich%{?_isa} = %{version}-%{release}

%description mpich-devel
A simple interface for processing workloads using an automatically
distributed global queue.

This package contains development headers and libraries for
MPICH ibcircle

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
./autogen.sh

%build
mkdir openmpi mpich
%global _configure ../configure

pushd openmpi
%{_openmpi_load}
%configure --enable-doxygen --enable-tests --disable-static --libdir="${MPI_LIB}" --includedir="${MPI_INCLUDE}"
%make_build
%{_openmpi_unload}
popd

pushd mpich
%{_mpich_load}
%configure --enable-tests --disable-static --libdir="${MPI_LIB}" --includedir="${MPI_INCLUDE}"
%make_build
%{_mpich_unload}
popd

%install
%make_install -C openmpi
%make_install -C mpich
rm %{buildroot}%{_libdir}/*mpi*/lib/*.la

cd openmpi
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -r doc/html/* %{buildroot}%{_docdir}/%{name}

%check
%ifarch s390x %arm
export CK_TIMEOUT_MULTIPLIER=10
%endif
%{_openmpi_load}
make -C openmpi check || { cat openmpi/tests/test-suite.log && exit 1; }
%{_openmpi_unload}
%{_mpich_load}
make -C mpich check || { cat mpich/tests/test-suite.log && exit 1; }
%{_mpich_unload}

%files openmpi
%license COPYING AUTHORS
%{_libdir}/openmpi*/lib/%{name}.so.*

%files mpich
%license COPYING AUTHORS
%{_libdir}/mpich*/lib/%{name}.so.*

%files openmpi-devel
%{_libdir}/openmpi*/lib/%{name}.so
%{_libdir}/openmpi*/lib/pkgconfig/%{name}.pc
%{_includedir}/openmpi*/%{name}.h

%files mpich-devel
%{_libdir}/mpich*/lib/%{name}.so
%{_libdir}/mpich*/lib/pkgconfig/%{name}.pc
%{_includedir}/mpich*/%{name}.h

%doc
%{_docdir}/%{name}

%changelog
%autochangelog
