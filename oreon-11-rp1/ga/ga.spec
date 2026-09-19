%global source0_hash cbf15764bf9c04e47e7a798271c418f76b23f1857b23feb24b6cb3891a57fbf2

# Warning:
# Anyone editing this spec file please make sure the same spec file
# works on other fedora and epel releases, which are supported by this software.
# No quick Rawhide-only fixes will be allowed.

%if 0%{?fedora} >= 38
# openmpi segmentation fault on i686 bug #2142304
ExcludeArch: %{ix86}
%endif

%define mpich_name mpich

%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9
%global blaslib flexiblas
%else
%global blaslib openblas
%endif

Name:    ga
Version: 5.9.2
Release: 2%{?dist}
Summary: Global Arrays Toolkit
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
Source: https://github.com/GlobalArrays/ga/releases/download/v%{version}/ga-%{version}.tar.gz
URL: http://github.com/GlobalArrays/ga
ExclusiveArch: %{ix86} x86_64 %{arm} aarch64 ppc64le riscv64
BuildRequires: openmpi-devel, %{mpich_name}-devel, gcc-c++, gcc-gfortran
BuildRequires: %{blaslib}-devel, openssh-clients, dos2unix, perl

%define ga_desc_base \
The Global Arrays (GA) toolkit provides an efficient and portable \
"shared-memory" programming interface for distributed-memory \
computers. Each process in a MIMD parallel program can asynchronously \
access logical blocks of physically distributed dense multi- \
dimensional arrays, without need for explicit cooperation by other \
processes. Unlike other shared-memory environments, the GA model \
exposes to the programmer the non-uniform memory access (NUMA) \
characteristics of the high performance computers and acknowledges \
that access to a remote portion of the shared data is slower than to \
the local portion. The locality information for the shared data is \
available, and a direct access to the local portions of shared data \
is provided.

%description
%{ga_desc_base}
- Global Arrays Toolkit Base Package.

%package common
Summary: Global Arrays Common Files
BuildArch: noarch
%description common
%{ga_desc_base}
- Global Arrays Common Files.

%package mpich
Summary: Global Arrays Toolkit for MPICH
BuildRequires: scalapack-%{mpich_name}-devel
BuildRequires: %{blaslib}-devel
Requires: %{name}-common = %{version}
Provides: %{name}-mpich2 = %{version}-%{release}
Obsoletes: %{name}-mpich2 < %{version}-%{release}
%description mpich
%{ga_desc_base}
- Libraries against MPICH.
%package mpich-devel
Summary: Global Arrays Toolkit for MPICH Development
Requires: scalapack-%{mpich_name}-devel, %{mpich_name}-devel
Requires: %{blaslib}-devel, %{name}-common = %{version}, %{name}-mpich = %{version}
Provides: %{name}-mpich2-devel = %{version}-%{release}
Obsoletes: %{name}-mpich2-devel < %{version}-%{release}
%description mpich-devel
%{ga_desc_base}
- Development Software against MPICH.
%package mpich-static
Summary: Global Arrays Toolkit for MPICH Static Libraries
Requires: scalapack-%{mpich_name}-devel, %{mpich_name}-devel
Requires: %{blaslib}-devel, %{name}-common = %{version}, %{name}-mpich = %{version}
Provides: %{name}-mpich2-static = %{version}-%{release}
Obsoletes: %{name}-mpich2-static < %{version}-%{release}
%description mpich-static
%{ga_desc_base}
- Static Libraries against MPICH.
%ldconfig_scriptlets mpich

%package openmpi
Summary: Global Arrays Toolkit for OpenMPI
BuildRequires: scalapack-openmpi-devel
BuildRequires: %{blaslib}-devel
BuildRequires: make
Requires: %{name}-common = %{version}
%description openmpi
%{ga_desc_base}
- Libraries against OpenMPI.
%package openmpi-devel
Summary: Global Arrays Toolkit for OpenMPI Development
Requires: scalapack-openmpi-devel, openmpi-devel
Requires: %{blaslib}-devel, %{name}-common = %{version}, %{name}-openmpi = %{version}
%description openmpi-devel
%{ga_desc_base}
- Development Software against OpenMPI.
%package openmpi-static
Summary: Global Arrays Toolkit for OpenMPI Static Libraries
Requires: scalapack-openmpi-devel, openmpi-devel
Requires: %{blaslib}-devel, %{name}-common = %{version}, %{name}-openmpi = %{version}
%description openmpi-static
%{ga_desc_base}
- Static Libraries against OpenMPI.
%ldconfig_scriptlets openmpi

%define ga_version %{version}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -n %{name}-%{version}

pushd %{name}-%{ga_version}

popd
for i in mpich openmpi; do
  cp -a %{name}-%{ga_version} %{name}-%{version}-$i
done

%build
%define doBuild \
export LIBS="-lscalapack -l%{blaslib}" && \
export CFLAGS="%{optflags} -O1" && \
export CXXFLAGS="%{optflags} -O1" && \
export FFLAGS="%{optflags} -O1" && \
cd %{name}-%{version}-$MPI_COMPILER_NAME && \
%configure \\\
  --bindir=$MPI_BIN \\\
  --libdir=$MPI_LIB \\\
  --includedir=$MPI_INCLUDE \\\
  --with-scalapack4=-lscalapack \\\
  --with-blas4=-l%{blaslib} \\\
  --enable-shared \\\
  --enable-static \\\
  --enable-cxx \\\
  --enable-f77 \\\
  $GA_CONFIGURE_OPTIONS && \
%make_build && \
cd ..

export MPI_COMPILER_NAME=mpich
export GA_CONFIGURE_OPTIONS=""
%{_mpich_load}
%doBuild
%{_mpich_unload}

export MPI_COMPILER_NAME=openmpi
%{_openmpi_load}
%doBuild
%{_openmpi_unload}

%install
%define doInstall \
cd %{name}-%{version}-$MPI_COMPILER_NAME && \
%make_install && \
cd ..

rm -rf $RPM_BUILD_ROOT
export MPI_COMPILER_NAME=mpich
%{_mpich_load}
%doInstall
%{_mpich_unload}

export MPI_COMPILER_NAME=openmpi
%{_openmpi_load}
%doInstall
%{_openmpi_unload}

find %{buildroot} -type f -name "*.la" -exec rm -f {} \;

mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/sysctl.d
echo 'kernel.shmmax = 134217728' > $RPM_BUILD_ROOT/%{_sysconfdir}/sysctl.d/armci.conf
%define do_test 1
%check
%if %{?do_test}0
%if 0%{?rhel} != 6
%{_mpich_load}
cd %{name}-%{version}-mpich
make NPROCS=2 VERBOSE=1 check-ma check-travis
(make NPROCS=2 TESTS="global/testing/test.x global/testing/testc.x global/testing/testmatmult.x global/testing/patch.x global/testing/simple_groups_comm.x global/testing/elempatch.x" check-TESTS VERBOSE=1; EXIT=$? && cat ./test-suite.log && exit ${EXIT})
cd ..
%{_mpich_unload}
%endif
%{_openmpi_load}
cd %{name}-%{version}-openmpi
export OMPI_MCA_btl=^uct
export OMPI_MCA_btl_base_warn_component_unused=0
make NPROCS=2 VERBOSE=1 check-ma check-travis
(make NPROCS=2 TESTS="global/testing/test.x global/testing/testc.x global/testing/testmatmult.x global/testing/patch.x global/testing/simple_groups_comm.x global/testing/elempatch.x" check-TESTS VERBOSE=1; EXIT=$? && cat ./test-suite.log && exit ${EXIT})
cd ..
%{_openmpi_unload}
%endif

%files common
%doc %{name}-%{ga_version}/README.md %{name}-%{ga_version}/CHANGELOG.md
%doc %{name}-%{ga_version}/DISCLAIMER %{name}-%{ga_version}/LICENSE
%config(noreplace) %{_sysconfdir}/sysctl.d/armci.conf

%files mpich
%doc %{name}-%{ga_version}/DISCLAIMER %{name}-%{ga_version}/LICENSE
%{_libdir}/%{mpich_name}/lib/lib*.so.*
%{_libdir}/%{mpich_name}/bin/*.x
%files mpich-devel
%doc %{name}-%{ga_version}/DISCLAIMER %{name}-%{ga_version}/LICENSE
%{_libdir}/%{mpich_name}/lib/lib*.so
%{_includedir}/%{mpich_name}-%{_arch}/*
%{_libdir}/%{mpich_name}/bin/ga-config
%{_libdir}/%{mpich_name}/bin/armci-config
%{_libdir}/%{mpich_name}/bin/comex-config
%files mpich-static
%doc %{name}-%{ga_version}/DISCLAIMER %{name}-%{ga_version}/LICENSE
%{_libdir}/%{mpich_name}/lib/lib*.a

%files openmpi
%doc %{name}-%{ga_version}/DISCLAIMER %{name}-%{ga_version}/LICENSE
%{_libdir}/openmpi/lib/lib*.so.*
%{_libdir}/openmpi/bin/*.x
%files openmpi-devel
%doc %{name}-%{ga_version}/DISCLAIMER %{name}-%{ga_version}/LICENSE
%{_libdir}/openmpi/lib/lib*.so
%{_includedir}/openmpi-%{_arch}/*
%{_libdir}/openmpi/bin/ga-config
%{_libdir}/openmpi/bin/armci-config
%{_libdir}/openmpi/bin/comex-config
%files openmpi-static
%doc %{name}-%{ga_version}/DISCLAIMER %{name}-%{ga_version}/LICENSE
%{_libdir}/openmpi/lib/lib*.a

%changelog
%autochangelog
