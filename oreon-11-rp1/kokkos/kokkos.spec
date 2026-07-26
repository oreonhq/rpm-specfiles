%global source0_hash a81826ac0a167933d13506bc2a986fb5517038df9abb780fe9bb2c1d4e80803b

%if 0%{?rhel} < 9
# Needed for EPEL8
%undefine __cmake_in_source_build
%endif

# For ROCm
%if 0%{?fedora}
%ifarch x86_64
%bcond_without rocm
%endif
%endif

%if %{with rocm}
# Kokkos only builds one gpu at a time, so need to loop over them
# $gpu will be evaluated in the loops below
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${gpu:-normal}

# For testing gpus, depends on having a gpu
%bcond_with rocm_test
%if %{with rocm_test}
# Only build the for the gpu you are testing
%global gpu_test gfx1100
%global kokkos_gpu_list %{gpu_test}
%global build_rocm_test ON
%else
# kokkos only supports some GPUs, of these pick the important ones
%global kokkos_gpu_list gfx942 gfx90a gfx1100
%global build_rocm_test OFF
%endif

# hippc is clang based, the toolchain is gcc, remove the gcc options that are not supported on clang
%global rocm_cxxflags %(echo %{optflags} | sed -E 's/-specs=[^ ]+//g; s/-Wno-complain-wrong-lang//g; s/-fexceptions//g; s/-fstack-clash-protection//g; s/-fcf-protection//g; s/-ffat-lto-objects//g; s/-Xarch_host//g; s/-mtls-dialect=[^ ]+//g; s/-flto=auto//g; s/-grecord-gcc-switches/-frecord-command-line/g; s/-Wp,-U_FORTIFY_SOURCE,-D_FORTIFY_SOURCE=3//g; s/-Wp,-D_GLIBCXX_ASSERTIONS//g; s/-mno-omit-leaf-frame-pointer//g; s/[[:space:]]+/ /g')
%endif

Name:           kokkos
Version:        4.7.02
%global         sover 4.7
Release:        1%{?dist}
Summary:        Kokkos C++ Performance Portability Programming
# no support for 32-bit archs https://github.com/kokkos/kokkos/issues/2312
ExcludeArch: i686 armv7hl

License:        Apache-2.0 WITH LLVM-exception
URL:            https://github.com/kokkos/kokkos
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.16
BuildRequires:  hwloc-devel
%if 0%{?rhel} == 9
%global gts_version 13
BuildRequires: gcc-toolset-%{gts_version}
%endif
%if %{with rocm}
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-rpm-macros-modules
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocprim-devel
BuildRequires:  rocthrust-devel
Requires:       rocm-rpm-macros-modules
%endif

%global kokkos_desc \
Kokkos Core implements a programming model in C++ for writing performance \
portable applications targeting all major HPC platforms. For that purpose \
it provides abstractions for both parallel execution of code and data \
management.  Kokkos is designed to target complex node architectures with \
N-level memory hierarchies and multiple types of execution resources. It \
currently can use OpenMP, Pthreads and CUDA as backend programming models.

%description
%{kokkos_desc}

%package devel
Summary:        Development package for  %{name} packages
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       hwloc-devel
%description devel
%{kokkos_desc}

This package contains the development files of %{name}.

%package -n %{name}-rocm
Summary:        %{name} ROCm package
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}-rocm
%{summary}

%package -n %{name}-rocm-devel
Summary:        %{name} ROCm development package
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description -n %{name}-rocm-devel
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build

%{?el9:. /opt/rh/gcc-toolset-%{gts_version}/enable}
%cmake \
  -DKokkos_ENABLE_TESTS=On \
%ifarch ppc64le
  -DKokkos_ARCH_POWER8=ON \
%endif
  -DCMAKE_INSTALL_INCLUDEDIR=include/kokkos \
  -DKokkos_ENABLE_AGGRESSIVE_VECTORIZATION=ON \
  -DKokkos_ENABLE_DEPRECATED_CODE=ON \
  -DKokkos_ENABLE_OPENMP=ON \
  -DKokkos_ENABLE_SERIAL=ON \
  -DKokkos_ENABLE_HWLOC=ON \
  -DKokkos_ENABLE_HIP=OFF \
  %{nil}
%cmake_build

%if %{with rocm}
rocm_clang=`hipconfig -l`/clang++
for gpu in %{kokkos_gpu_list}
do
    module load rocm/$gpu
    ugpu=${gpu^^}
    %cmake \
	   -DCMAKE_CXX_COMPILER=${rocm_clang} \
	   -DCMAKE_CXX_FLAGS="%{rocm_cxxflags}" \
	   -DCMAKE_CXX_STANDARD=17 \
	   -DCMAKE_INSTALL_BINDIR=$ROCM_BIN \
	   -DCMAKE_INSTALL_INCLUDEDIR=%{_libdir}/rocm/${gpu}/include/kokkos \
	   -DCMAKE_INSTALL_LIBDIR=$ROCM_LIB \
	   -DKokkos_ARCH_AMD_${ugpu}=ON \
	   -DKokkos_ENABLE_AGGRESSIVE_VECTORIZATION=ON \
	   -DKokkos_ENABLE_DEPRECATED_CODE=ON \
	   -DKokkos_ENABLE_HIP=ON \
	   -DKokkos_ENABLE_HWLOC=ON \
	   -DKokkos_ENABLE_OPENMP=OFF \
	   -DKokkos_ENABLE_SERIAL=ON \
	   -DKokkos_ENABLE_TESTS=%{build_rocm_test}

    %cmake_build
    module purge
done
%endif

%install

%cmake_install

%if %{with rocm}
for gpu in %{kokkos_gpu_list}
do
    %cmake_install
done
%endif

%check
# https://github.com/kokkos/kokkos/issues/2959 - unstable test
%ifarch s390x
%global testargs --exclude-regex KokkosCore_UnitTest_StackTraceTest
%endif
%ctest %{?testargs} --timeout 6000

%if %{with rocm_test}
gpu=%{gpu_test}
module load rocm/$gpu
%ctest %{?testargs} --timeout 6000
module purge
%endif

%files
%doc README.md
%license LICENSE
%{_libdir}/libkokkos*.so.%{sover}*

%files devel
%{_includedir}/kokkos
%{_libdir}/libkokkos*.so
%{_libdir}/cmake/Kokkos
%{_bindir}/nvcc_wrapper
%{_bindir}/hpcbind
%{_bindir}/kokkos_launch_compiler

%if %{with rocm}
%files -n %{name}-rocm
%{_libdir}/rocm/gfx*/lib/libkokkos*.so.%{sover}*

%files -n %{name}-rocm-devel
%{_libdir}/rocm/gfx*/lib/libkokkos*.so
%{_libdir}/rocm/gfx*/lib/cmake/Kokkos
%{_libdir}/rocm/gfx*/bin/nvcc_wrapper
%{_libdir}/rocm/gfx*/bin/hpcbind
%{_libdir}/rocm/gfx*/bin/kokkos_launch_compiler
%{_libdir}/rocm/gfx*/include/kokkos
%endif

%changelog
%autochangelog
