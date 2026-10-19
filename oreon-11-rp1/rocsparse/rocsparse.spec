%global source0_hash cdad45e7b23e91a9107e512d9205ef58dcdfaea506b6e5fce3701a2b6e96952c
%bcond_with gitcommit
%if %{with gitcommit}
%global commit0 2584e35062ad9c2edb68d93c464cf157bc57e3b0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20250926
%endif
%global upstreamname rocSPARSE
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix -%{rocm_release}
%global pkg_module rocm%{pkg_suffix}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%endif
%if 0%{?suse_version}
%global rocsparse_name librocsparse1%{pkg_suffix}
%else
%global rocsparse_name rocsparse%{pkg_suffix}
%endif
%global toolchain rocm
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RELEASE
%endif
%bcond_without compress
%if %{with compress}
%global build_compress ON
%else
%global build_compress OFF
%endif
%bcond_with test
%if %{with test}
%global build_test ON
%global __brp_check_rpaths %{nil}
%else
%global build_test OFF
%endif
%bcond check 1
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio
%bcond_with ninja
%if %{with ninja}
%global cmake_generator -G Ninja
%else
%global cmake_generator %{nil}
%endif
%global cmake_config \\\
  -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \\\
  -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \\\
  -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \\\
  -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \\\
  -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \\\
  -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \\\
  -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \\\
  -DCMAKE_BUILD_TYPE=%build_type \\\
  -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \\\
  -DCMAKE_SKIP_RPATH=ON \\\
  -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \\\
  -DROCM_SYMLINK_LIBS=OFF \\\
  -DHIP_PLATFORM=amd \\\
  -DBUILD_WITH_OFFLOAD_COMPRESS=%{build_compress} \\\
  -DBUILD_CLIENTS_BENCHMARKS=%{build_test} \\\
  -DBUILD_CLIENTS_TESTS=%{build_test} \\\
  -DBUILD_CLIENTS_TESTS_OPENMP=OFF \\\
  -DBUILD_FORTRAN_CLIENTS=OFF
%global gpu_list %{rocm_gpu_list_default}
%global _gpu_list gfx1100
Name:           rocsparse%{pkg_suffix}
%if %{with gitcommit}
Version:        git%{date0}.%{shortcommit0}
Release:        1%{?dist}
%else
Version:        %{rocm_version}
Release:        1%{?dist}
%endif
Summary:        SPARSE implementation for ROCm
License:        MIT
%if %{with gitcommit}
Url:            https://github.com/ROCm/rocm-libraries
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%else
Url:            https://github.com/ROCm/%{upstreamname}
%endif
%if %{with compress}
%endif
%if %{with test}
%if 0%{?suse_version}
%else
%endif
%endif
%if %{with ninja}
%if 0%{?suse_version}
%define __builder ninja
%endif
%endif
Provides:       rocsparse%{pkg_suffix} = %{version}-%{release}
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  gtest-devel
BuildRequires:  libomp-devel
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  rocblas-7.1-devel
BuildRequires:  rocm-cmake-7.1
BuildRequires:  rocm-comgr-7.1-devel
BuildRequires:  rocm-compilersupport-7.1-macros
BuildRequires:  rocm-hip-7.1-devel
BuildRequires:  rocm-rpm-macros-7.1
BuildRequires:  rocm-runtime-7.1-devel
BuildRequires:  rocprim-7.1-static
# /oreon:deps
%description
rocSPARSE exposes a common interface that provides Basic
Linear Algebra Subroutines for sparse computation
implemented on top of AMD's Radeon Open eCosystem Platform
ROCm runtime and toolchains. rocSPARSE is created using
the HIP programming language and optimized for AMD's
latest discrete GPUs.

%if 0%{?suse_version}
%package -n %{rocsparse_name}
Summary:        Shared libraries for %{name}
%description -n %{rocsparse_name}
%{summary}

%ldconfig_scriptlets -n %{rocsparse_name}
%endif

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{rocsparse_name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description test
%{summary}
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{with gitcommit}
%setup -q -n rocm-libraries-%{commit0}
cd projects/rocsparse
%else
%autosetup -p1 -n %{upstreamname}-rocm-%{version}
%endif

# On Tumbleweed Q3,2025
# /usr/include/gtest/internal/gtest-port.h:273:2: error: C++ versions less than C++17 are not supported.
# Convert the c++14 to c++17
sed -i -e 's@set(CMAKE_CXX_STANDARD 14)@set(CMAKE_CXX_STANDARD 17)@' {,clients/}CMakeLists.txt

%build

%if %{with gitcommit}
cd projects/rocsparse
%endif
%cmake %{cmake_generator} %{cmake_config} \
    -DGPU_TARGETS=%{gpu_list} \
%if %{with test}
    -DCMAKE_MATRICES_DIR=%{_builddir}/rocsparse-test-matrices/
%endif
%cmake_build
%install
%if %{with gitcommit}
cd projects/rocsparse
%endif
%cmake_install
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocsparse/LICENSE.md
%if %{with test}
mkdir -p %{buildroot}/%{pkg_prefix}/share/rocsparse/matrices
install -pm 644 %{_builddir}/rocsparse-test-matrices/* %{buildroot}/%{pkg_prefix}/share/rocsparse/matrices
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

%if %{with test}
%if %{with check}
%if 0%{?suse_version}
export LD_LIBRARY_PATH=%{__builddir}/library:$LD_LIBRARY_PATH
%{__builddir}/clients/staging/rocsparse-test
%else
export LD_LIBRARY_PATH=%{_vpath_builddir}/library:$LD_LIBRARY_PATH
%{_vpath_builddir}/clients/staging/rocsparse-test
%endif
%endif
%endif
%if 0%{?suse_version}
%files -f %{oreon_filedir}/main.list
%files -n rocsparse-7.1-devel -f %{oreon_filedir}/rocsparse-7.1-devel.list
%files -n rocsparse-7.1-test -f %{oreon_filedir}/rocsparse-7.1-test.list

%changelog

%autochangelog
%endif
