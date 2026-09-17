%global source0_hash ac7534163a09e21a5fa763e4e16dfc119bc84043f6e6a807aba666518f8df440

# openmpi dropped 32 bit support, thus also drop it
%ifarch %{ix86}
%bcond_with openmpi
%else
%bcond_without openmpi
%endif

%if 0%{?fedora} >= 33
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

%global _docdir_fmt %{name}

Name:           hpl
URL:            http://www.netlib.org/benchmark/hpl/
Version:        2.2
Release:        23%{?dist}
# Automatically converted from old format: BSD with advertising - review is highly recommended.
License:        LicenseRef-Callaway-BSD-with-advertising
Requires:       %{name}-common = %{version}-%{release}
BuildRequires:  mpich-devel
%if %{with openmpi}
BuildRequires:  openmpi-devel
%endif
BuildRequires:  %{blaslib}-devel
Summary:        A Portable Implementation of the High-Performance Linpack Benchmark
Source0:        http://www.netlib.org/benchmark/hpl/%{name}-%{version}.tar.gz
# setup/Make.Linux_PII_CBLAS_gm tuned for Fedora
Source1:        hpl-README.Fedora
Patch0:         hpl-2.1-fedora.patch

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
# Require explicitly for dir ownership and to guarantee the pickup of the right runtime
Requires: %{name}-common = %{version}-%{release}

%description openmpi
This package contains HPL compiled with openmpi.
%endif

%package mpich
Summary: HPL compiled against mpich
BuildRequires: mpich-devel
BuildRequires: make
# Require explicitly for dir ownership and to guarantee the pickup of the right runtime
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
# Have to do off-root builds to be able to build many versions at once

# To avoid replicated code define a build macro
# Cannot build in parallel (with _smp_mflags macro)
%global dobuild() \
cp setup/Make.Linux_PII_CBLAS_gm Make.$MPI_COMPILER \
make TOPdir="%{_builddir}/%{name}-%{version}" arch=$MPI_COMPILER ARCH=$MPI_COMPILER \\\
  LAlib=-l%{blaslib}

%if %{with openmpi}
# Build OpenMPI version
%{_openmpi_load}
%dobuild
%{_openmpi_unload}
%endif

# Build mpich version
%{_mpich_load}
%dobuild
%{_mpich_unload}

%install
%if %{with openmpi}
# Install OpenMPI version
%{_openmpi_load}
install -D -m 0755 bin/${MPI_COMPILER}/xhpl %{buildroot}${MPI_BIN}/xhpl${MPI_SUFFIX}
%{_openmpi_unload}
%endif

# Install MPICH version
%{_mpich_load}
install -D -m 0755 bin/${MPI_COMPILER}/xhpl %{buildroot}${MPI_BIN}/xhpl${MPI_SUFFIX}
%{_mpich_unload}

# Install HPL.dat
install -D -m 0644 testing/ptest/HPL.dat %{buildroot}%{_sysconfdir}/%{name}/HPL.dat

# Install docs
install -d -D -m 0755 %{buildroot}%{_docdir}/%{name}/html
install -p -D -m 0644 www/* %{buildroot}%{_docdir}/%{name}/html

# Install man pages
install -d -D -m 0755 %{buildroot}%{_mandir}/man3
install -p -D -m 0644 man/man3/* %{buildroot}%{_mandir}/man3

%check
%if %{with openmpi}
# Check openmpi implementation
%{_openmpi_load}
pushd bin/${MPI_COMPILER}
OMPI_MCA_rmaps_base_oversubscribe=1 mpirun -n 4 ./xhpl
popd
%{_openmpi_unload}
%endif

# Check mpich implementation
%{_mpich_load}
pushd bin/${MPI_COMPILER}
mpirun -n 4 ./xhpl
popd
%{_mpich_unload}

%files common
%exclude %{_docdir}/%{name}/html
%license COPYRIGHT
%doc BUGS HISTORY README TODO TUNING README.Fedora
%config(noreplace) %{_sysconfdir}/%{name}

%files doc
%doc %{_docdir}/%{name}/html
%{_mandir}/man3/*.3*

%if %{with openmpi}
%files openmpi
%{_libdir}/openmpi/bin/xhpl*
%endif

%files mpich
%{_libdir}/mpich/bin/xhpl*

%changelog
%autochangelog
