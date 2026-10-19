%global source0_hash f4568ebec5332ef686d9a8a456169ba22b5a8c18027fa9a14b13c9b4cc447dc3
Name:           mpibash
Version:        1.5
Release:        1%{?dist}
Summary:        Parallel scripting right from the Bourne-Again Shell
License:        GPL-3.0-or-later
Url:            https://github.com/lanl/MPI-Bash
Source0:        https://github.com/lanl/MPI-Bash/releases/download/v%{version}/mpibash-%{version}.tar.gz
ExcludeArch:    %{ix86}
%global __requires_exclude ^%{_libdir}/.*/bin/.*
# oreon:deps
BuildRequires:  bash-devel
BuildRequires:  libcircle-mpich-devel
BuildRequires:  libcircle-openmpi-devel
BuildRequires:  make
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel
# /oreon:deps
%description

%package openmpi
Summary:        Mpibash Open MPI binaries and libraries
BuildRequires:  openmpi-devel
BuildRequires:  libcircle-openmpi-devel
%description openmpi

mpibash compiled with Open MPI, package incl. binaries and libraries.

%package mpich
Summary:        Mpibash MPICH binaries and libraries
BuildRequires:  mpich-devel
BuildRequires:  libcircle-mpich-devel
%description mpich

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
%oreon_prep
%build

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
sed -i '1s@/usr/bin/env bash@/bin/bash@' %{buildroot}/%{_libdir}/*mpi*/bin/mpibash*
sed -i '1s@/usr/bin/env mpibash@%{_libdir}/openmpi/bin/mpibash_openmpi@' %{buildroot}/%{_libdir}/openmpi/lib/share/%{name}/examples/* %{buildroot}/%{_libdir}/openmpi/bin/m*
sed -i '1s@/usr/bin/env mpibash@%{_libdir}/mpich/bin/mpibash_mpich@' %{buildroot}/%{_libdir}/mpich/lib/share/%{name}/examples/* %{buildroot}/%{_libdir}/mpich/bin/m*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mpibash-openmpi -f %{oreon_filedir}/mpibash-openmpi.list
%files -n mpibash-mpich -f %{oreon_filedir}/mpibash-mpich.list
%files -n mpibash-openmpi-examples -f %{oreon_filedir}/mpibash-openmpi-examples.list
%files -n mpibash-mpich-examples -f %{oreon_filedir}/mpibash-mpich-examples.list

%changelog

%autochangelog
