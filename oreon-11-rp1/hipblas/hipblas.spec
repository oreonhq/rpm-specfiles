%global source0_hash 719c27d839d2008be5c5ec270299d98aab820eaf6aee907b7fa12cecd0cea092
%bcond_with gitcommit
%if %{with gitcommit}
%global commit0 2584e35062ad9c2edb68d93c464cf157bc57e3b0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20250926
%endif
%global upstreamname hipBLAS
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
%global hipblas_name libhipblas3%{pkg_suffix}
%else
%global hipblas_name hipblas%{pkg_suffix}
%endif
%global toolchain rocm
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif
%bcond_with test
%if %{with test}
%global build_test ON
%global __brp_check_rpaths %{nil}
%global _smp_mflags -j1
%else
%global build_test OFF
%endif
%global build_fflags %{nil}
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio
Name:           hipblas%{pkg_suffix}
%if %{with gitcommit}
Version:        git%{date0}.%{shortcommit0}
Release:        1%{?dist}
%else
Version:        %{rocm_version}
Release:        1%{?dist}
%endif
Summary:        ROCm BLAS marshalling library
License:        MIT
%if %{with gitcommit}
Url:            https://github.com/ROCm/rocm-libraries
Source0:        https://github.com/ROCmSoftwarePlatform/%{upstreamname}/archive/refs/tags/%{pkg_module}.%{rocm_patch}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%else
Url:            https://github.com/ROCmSoftwarePlatform/%{upstreamname}
%endif
%if 0%{?suse_version}
%else
%endif
%if %{with test}
%if 0%{?suse_version}
%else
%endif
%endif
Provides:       hipblas%{pkg_suffix} = %{version}-%{release}
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  blas-static
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  gtest-devel
BuildRequires:  hipblas-common-devel
BuildRequires:  lapack-static
BuildRequires:  python3-pyyaml
BuildRequires:  rocblas-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocsolver-devel
# /oreon:deps
%description
hipBLAS is a Basic Linear Algebra Subprograms (BLAS) marshalling
library, with multiple supported backends. It sits between the
application and a 'worker' BLAS library, marshalling inputs into
the backend library and marshalling results back to the
application. hipBLAS exports an interface that does not require
the client to change, regardless of the chosen backend. Currently,
hipBLAS supports rocBLAS and cuBLAS as backends.

%if 0%{?suse_version}
%package -n %{hipblas_name}
Summary:        Shared libraries for %{name}
%description -n %{hipblas_name}
%{summary}

%ldconfig_scriptlets -n %{hipblas_name}
%endif

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{hipblas_name}%{?_isa} = %{version}-%{release}
Requires:       hipblas-common%{pkg_suffix}-devel
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
cd projects/hipblas
%else
%autosetup -p1 -n %{upstreamname}-rocm-%{version}
%endif

# This is a tarball, no .git to query
sed -i -e 's@find_package(Git REQUIRED)@#find_package(Git REQUIRED)@' library/CMakeLists.txt

%build

%if %{with gitcommit}
cd projects/hipblas
%endif
%cmake \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
    -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
    -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
    -DCMAKE_BUILD_TYPE=%build_type \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DCMAKE_SKIP_RPATH=ON \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DROCM_SYMLINK_LIBS=OFF \
    -DHIP_PLATFORM=amd \
    -DAMDGPU_TARGETS=%{rocm_gpu_list_default} \
    -DBUILD_CLIENTS_BENCHMARKS=%{build_test} \
    -DBUILD_CLIENTS_TESTS=%{build_test} \
    -DBUILD_CLIENTS_TESTS_OPENMP=OFF \
    -DBUILD_FORTRAN_CLIENTS=OFF \
    -DBLAS_LIBRARY=cblas
%cmake_build
%install
%if %{with gitcommit}
cd projects/hipblas
%endif
%cmake_install
rm -f %{buildroot}%{pkg_prefix}/share/doc/hipblas/LICENSE.md
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if 0%{?suse_version}
%files -f %{oreon_filedir}/main.list
%files -n hipblas-devel -f %{oreon_filedir}/hipblas-devel.list
%files -n hipblas-test -f %{oreon_filedir}/hipblas-test.list

%changelog

%autochangelog
%endif
