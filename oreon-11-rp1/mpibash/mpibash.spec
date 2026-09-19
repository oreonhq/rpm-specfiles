%global source0_hash f4568ebec5332ef686d9a8a456169ba22b5a8c18027fa9a14b13c9b4cc447dc3

Name:           mpibash
Version:        1.5
Release:        2%{?dist}
Summary:        Parallel scripting right from the Bourne-Again Shell
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
Url:            https://github.com/lanl/MPI-Bash
Source0:        https://github.com/lanl/MPI-Bash/releases/download/v%{version}/mpibash-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  bash-devel >= 4.4
ExcludeArch:    %{ix86}

# Prevent generation of a file dependency on ourselves
# https://bugzilla.redhat.com/show_bug.cgi?id=2229948
%global __requires_exclude ^%{_libdir}/.*/bin/.*

%global _description %{expand:
This package makes it possible to parallelize bash scripts which run a set of
Linux commands independently over a large number of input files. Because mpibash
includes various MPI functions for data transfer and synchronization, it is not
limited to parallel workloads, but can incorporate phased operations where all
workers must finish operation X before any worker is allowed to begin
operation Y.}

%description %_description

%package openmpi
Summary:        Mpibash Open MPI binaries and libraries
BuildRequires:  openmpi-devel
BuildRequires:  libcircle-openmpi-devel

%description openmpi  %_description

mpibash compiled with Open MPI, package incl. binaries and libraries.

%package mpich
Summary:        Mpibash MPICH binaries and libraries
BuildRequires:  mpich-devel
BuildRequires:  libcircle-mpich-devel

%description mpich  %_description

mpibash compiled with MPICH, package incl. binaries and libraries.

%package openmpi-examples
Summary:        Example Scripts for Open MPI %{name}
Requires:       %{name}-openmpi = %{version}

%description openmpi-examples
MPI-Bash makes it possible to parallelize Bash scripts which run a set of
Linux commands independently over a large number of input files.

This package contains example scripts for mpibash compiled with Open MPI.

%package mpich-examples
Summary:        Example Scripts for MPICH %{name}
Requires:       %{name}-mpich = %{version}

%description mpich-examples
MPI-Bash makes it possible to parallelize Bash scripts which run a set of
Linux commands independently over a large number of input files.

This package contains example scripts for mpibash compiled with MPICH.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# workaround for build issue with gcc-15 + bash-4.2, https://github.com/lanl/MPI-Bash/issues/20
%if 0%{?fedora} == 42
export CFLAGS="%{optflags} -std=gnu17"
%endif

mkdir openmpi mpich
%global _configure ../configure

pushd openmpi
%{_openmpi_load}
%configure --with-bashdir=/usr/include/bash --docdir=${MPI_LIB}/share/%{name} --with-plugindir=${MPI_LIB}/%{name}/ --bindir=${MPI_BIN} --mandir=${MPI_MAN} --program-suffix=${MPI_SUFFIX} CC=mpicc
%make_build
%{_openmpi_unload}
popd

pushd mpich
%{_mpich_load}
%configure --with-bashdir=/usr/include/bash --docdir=${MPI_LIB}/share/%{name} --with-plugindir=${MPI_LIB}/%{name}/ --bindir=${MPI_BIN} --mandir=${MPI_MAN} --program-suffix=${MPI_SUFFIX} CC=mpicc
%make_build
%{_mpich_unload}
popd

%install
%make_install -C openmpi
%make_install -C mpich
# Fix shebang
sed -i '1s@/usr/bin/env bash@/bin/bash@' %{buildroot}/%{_libdir}/*mpi*/bin/mpibash*
sed -i '1s@/usr/bin/env mpibash@%{_libdir}/openmpi/bin/mpibash_openmpi@' %{buildroot}/%{_libdir}/openmpi/lib/share/%{name}/examples/* %{buildroot}/%{_libdir}/openmpi/bin/m*
sed -i '1s@/usr/bin/env mpibash@%{_libdir}/mpich/bin/mpibash_mpich@' %{buildroot}/%{_libdir}/mpich/lib/share/%{name}/examples/* %{buildroot}/%{_libdir}/mpich/bin/m*

%files openmpi
%{_libdir}/openmpi/bin/m*
%{_mandir}/openmpi*/man1/m*
%{_libdir}/openmpi/lib/%{name}

%files openmpi-examples
%{_libdir}/openmpi/lib/share/%{name}/examples

%files mpich
%{_libdir}/mpich/bin/m*
%{_mandir}/mpich*/man1/m*
%{_libdir}/mpich/lib/%{name}

%files mpich-examples
%{_libdir}/mpich/lib/share/%{name}/examples

%changelog
%autochangelog
