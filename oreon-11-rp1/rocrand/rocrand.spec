%global source0_hash 616c2f61a4e05d8f07e4f95a26c1f031e66092cbf45354fe64c62becc9dcb751
%bcond_with gitcommit
%if %{with gitcommit}
%global commit0 2584e35062ad9c2edb68d93c464cf157bc57e3b0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20250926
%endif
%global upstreamname rocRAND
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}/
%global pkg_suffix -%{rocm_release}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%endif
%if 0%{?suse_version}
%global rocrand_name librocrand1%{pkg_suffix}
%else
%global rocrand_name rocrand%{pkg_suffix}
%endif
%global toolchain rocm
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//' )
%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif
%bcond_with test
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif
%bcond_with doc
%bcond_with ninja
%if %{with ninja}
%global cmake_generator -G Ninja
%else
%global cmake_generator %{nil}
%endif
%global cmake_config \\\
  -DBUILD_TEST=%build_test \\\
  -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \\\
  -DCMAKE_BUILD_TYPE=%build_type \\\
  -DCMAKE_EXPORT_COMPILE_COMMANDS=%{build_compile_db} \\\
  -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \\\
  -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \\\
  -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \\\
  -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \\\
  -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \\\
  -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \\\
  -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \\\
  -DCMAKE_SKIP_RPATH=ON \\\
  -DROCM_SYMLINK_LIBS=OFF
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio
%global gpu_list %{rocm_gpu_list_default}
%global _gpu_list gfx1100
%bcond_with export
%if %{with export}
%global build_compile_db ON
%else
%global build_compile_db OFF
%endif
Name:           rocrand%{pkg_suffix}
%if %{with gitcommit}
Version:        git%{date0}.%{shortcommit0}
Release:        1%{?dist}
%else
Version:        %{rocm_version}
Release:        1%{?dist}
%endif
Summary:        ROCm random number generator
%if %{with gitcommit}
Url:            https://github.com/ROCm/rocm-libraries
%else
Url:            https://github.com/ROCm/rocRAND
%endif
License:        MIT AND BSD-3-Clause
%if %{with gitcommit}
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{toolchain}-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%else
%endif
%if %{with test} || %{with check}
%if 0%{?suse_version}
%else
%endif
%endif
%if %{with doc}
%endif
%if %{with ninja}
%if 0%{?suse_version}
%define __builder ninja
%endif
%endif
Provides:       rocrand%{pkg_suffix} = %{version}-%{release}
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  rocm-cmake-7.1
BuildRequires:  rocm-comgr-7.1-devel
BuildRequires:  rocm-compilersupport-7.1-macros
BuildRequires:  rocm-hip-7.1-devel
BuildRequires:  rocm-rpm-macros-7.1
BuildRequires:  rocm-rpm-macros-7.1-modules
BuildRequires:  rocm-runtime-7.1-devel
# /oreon:deps
%description
The rocRAND project provides functions that generate pseudo-random and
quasi-random numbers.

The rocRAND library is implemented in the HIP programming language and
optimized for AMD's latest discrete GPUs. It is designed to run on top of AMD's
Radeon Open Compute ROCm runtime, but it also works on CUDA enabled GPUs.

%if 0%{?suse_version}
%package -n %{rocrand_name}
Summary:        Shared libraries for %{name}
%description -n %{rocrand_name}
%{summary}

%ldconfig_scriptlets -n %{rocrand_name}
%endif

%package devel
Summary:        The rocRAND development package
Requires:       %{rocrand_name}%{?_isa} = %{version}-%{release}
%description devel
The rocRAND development package.

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{rocrand_name}%{?_isa} = %{version}-%{release}
%description test
%{summary}
%endif

%prep

%if %{with gitcommit}
%setup -q -n rocm-libraries-%{commit0}
cd projects/rocrand
%else
%autosetup -p1 -n %{upstreamname}-rocm-%{version}
%endif

# On Tumbleweed Q3,2025
# https://github.com/ROCm/rocm-libraries/issues/83
# /usr/include/gtest/internal/gtest-port.h:273:2: error: C++ versions less than C++17 are not supported.
# Convert the c++11's to c++17
sed -i -e 's@set(CMAKE_CXX_STANDARD 11)@set(CMAKE_CXX_STANDARD 17)@' {,test/{cpp_wrapper,package}/}CMakeLists.txt

%build

%if %{with gitcommit}
cd projects/rocrand
%endif
%cmake %{cmake_generator} %{cmake_config} \
       -DAMDGPU_TARGETS=%{gpu_list} \
%cmake_build
%install
%if %{with gitcommit}
cd projects/rocrand
%endif
%cmake_install
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocrand/LICENSE.md
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if 0%{?suse_version}
%files -f %{oreon_filedir}/main.list
%files -n rocrand-7.1-devel -f %{oreon_filedir}/rocrand-7.1-devel.list
%files -n rocrand-7.1-test -f %{oreon_filedir}/rocrand-7.1-test.list

%changelog

%autochangelog
%endif
