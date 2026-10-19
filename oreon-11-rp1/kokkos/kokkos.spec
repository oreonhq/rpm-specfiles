%global source0_hash d6557aaef39302282a15f9c770433d1fcdf4e961dfd6d9ed726b9d0d0f546b9f
%if %{with rocm}
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${gpu:-normal}
%bcond_with rocm_test
%if %{with rocm_test}
%global gpu_test gfx1100
%global kokkos_gpu_list %{gpu_test}
%global build_rocm_test ON
%else
%global kokkos_gpu_list gfx942 gfx90a gfx1100
%global build_rocm_test OFF
%endif
%global rocm_cxxflags %(echo %{optflags} | sed -E 's/-specs=[^ ]+//g; s/-Wno-complain-wrong-lang//g; s/-fexceptions//g; s/-fstack-clash-protection//g; s/-fcf-protection//g; s/-ffat-lto-objects//g; s/-Xarch_host//g; s/-mtls-dialect=[^ ]+//g; s/-flto=auto//g; s/-grecord-gcc-switches/-frecord-command-line/g; s/-Wp,-U_FORTIFY_SOURCE,-D_FORTIFY_SOURCE=3//g; s/-Wp,-D_GLIBCXX_ASSERTIONS//g; s/-mno-omit-leaf-frame-pointer//g; s/[[:space:]]+/ /g')
%endif
Name:           kokkos
Version:        5.2.2
%global         sover 5.2
Release:        1%{?dist}
Summary:        Kokkos C++ Performance Portability Programming
ExcludeArch: i686 armv7hl
License:        Apache-2.0 WITH LLVM-exception
URL:            https://github.com/kokkos/kokkos
Source0:        https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
%if %{with rocm}
Requires:       rocm-rpm-macros-modules
%endif
%global kokkos_desc \
Kokkos Core implements a programming model in C++ for writing performance \
portable applications targeting all major HPC platforms. For that purpose \
it provides abstractions for both parallel execution of code and data \
management.  Kokkos is designed to target complex node architectures with \
N-level memory hierarchies and multiple types of execution resources. It \
currently can use OpenMP, Pthreads and CUDA as backend programming models.
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hwloc-devel
# /oreon:deps
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
%oreon_prep
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%check

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
%files -f %{oreon_filedir}/main.list
%files -n kokkos-devel -f %{oreon_filedir}/kokkos-devel.list
%files -n kokkos-rocm -f %{oreon_filedir}/kokkos-rocm.list
%files -n kokkos-rocm-devel -f %{oreon_filedir}/kokkos-rocm-devel.list

%changelog

%autochangelog
