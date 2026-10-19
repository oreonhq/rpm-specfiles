%global source0_hash 32c5c17d22330e6f2337b681aded51637fb6008d3f0eb7c277b163fadd612830
%ifarch %{ix86}
%bcond_with openmpi
%else
%bcond_without openmpi
%endif
%global blaslib openblas
%global _docdir_fmt %{name}
Name:           hpl
URL:            http://www.netlib.org/benchmark/hpl/
Version:        2.3
Release:        1%{?dist}
License:        LicenseRef-Callaway-BSD-with-advertising
Requires:       %{name}-common = %{version}-%{release}
%if %{with openmpi}
%endif
Summary:        A Portable Implementation of the High-Performance Linpack Benchmark
Source0:        http://www.netlib.org/benchmark/hpl/%{name}-%{version}.tar.gz
Source1:        hpl-README.Fedora
Patch0:         hpl-2.1-fedora.patch
# oreon:deps
BuildRequires:  make
BuildRequires:  mpich-devel
BuildRequires:  openblas-devel
BuildRequires:  openmpi-devel
# /oreon:deps
%description
HPL is a software package that solves a (random) dense linear system in
double precision (64 bits) arithmetic on distributed-memory computers.
It can thus be regarded as a portable as well as freely available
implementation of the High Performance Computing Linpack Benchmark.

%package common
Summary: HPL common files
BuildArch: noarch
%description common
HPL common files

%package doc
Summary: HPL documentation
Requires: %{name}-common = %{version}-%{release}
BuildArch: noarch
%description doc
HPL documentation.

%if %{with openmpi}
%package openmpi
Summary: HPL compiled against openmpi
Requires: %{name}-common = %{version}-%{release}
%description openmpi
This package contains HPL compiled with openmpi.
%endif

%package mpich
Summary: HPL compiled against mpich
BuildRequires: mpich-devel
BuildRequires: make
Requires: %{name}-common = %{version}-%{release}
%description mpich
This package contains HPL compiled with mpich.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .fedora

cp %{SOURCE1} README.Fedora

# Remove executable mode from sources
find . -type f -perm /111 -exec chmod a-x {} \;

# Patch docs to point to upstream sources
sed -i "s|\"hpl-%{version}.tar.gz\"|\"http://www.netlib.org/benchmark/hpl/hpl-%{version}.tar.gz\"|g" www/*.html

%build

%global dobuild() \
cp setup/Make.Linux_PII_CBLAS_gm Make.$MPI_COMPILER \
make TOPdir="%{_builddir}/%{name}-%{version}" arch=$MPI_COMPILER ARCH=$MPI_COMPILER \\\
  LAlib=-l%{blaslib}
%if %{with openmpi}
%{_openmpi_load}
%dobuild
%{_openmpi_unload}
%endif
%{_mpich_load}
%dobuild
%{_mpich_unload}
%install
%if %{with openmpi}
%{_openmpi_load}
install -D -m 0755 bin/${MPI_COMPILER}/xhpl %{buildroot}${MPI_BIN}/xhpl${MPI_SUFFIX}
%{_openmpi_unload}
%endif
%{_mpich_load}
install -D -m 0755 bin/${MPI_COMPILER}/xhpl %{buildroot}${MPI_BIN}/xhpl${MPI_SUFFIX}
%{_mpich_unload}
install -D -m 0644 testing/ptest/HPL.dat %{buildroot}%{_sysconfdir}/%{name}/HPL.dat
install -d -D -m 0755 %{buildroot}%{_docdir}/%{name}/html
install -p -D -m 0644 www/* %{buildroot}%{_docdir}/%{name}/html
install -d -D -m 0755 %{buildroot}%{_mandir}/man3
install -p -D -m 0644 man/man3/* %{buildroot}%{_mandir}/man3
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with openmpi}
%{_openmpi_load}
pushd bin/${MPI_COMPILER}
OMPI_MCA_rmaps_base_oversubscribe=1 mpirun -n 4 ./xhpl
popd
%{_openmpi_unload}
%endif
%{_mpich_load}
pushd bin/${MPI_COMPILER}
mpirun -n 4 ./xhpl
popd
%{_mpich_unload}
%files -f %{oreon_filedir}/main.list
%files -n hpl-common -f %{oreon_filedir}/hpl-common.list
%files -n hpl-doc -f %{oreon_filedir}/hpl-doc.list
%files -n hpl-openmpi -f %{oreon_filedir}/hpl-openmpi.list
%files -n hpl-mpich -f %{oreon_filedir}/hpl-mpich.list

%changelog

%autochangelog
