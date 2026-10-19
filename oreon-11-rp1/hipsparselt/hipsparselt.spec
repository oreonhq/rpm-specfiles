%global source1_hash 9cd33f96768361c551cb580f1080def10561142d47a027f074b46ba24010010f
%global source0_hash 31047a7187c128cf85fdbd822ba057ab1f9ae2f5ceceb230ca428042a96e24d4
%if 0%{?suse_version}
%{?sle15_python_module_pythons}
%{?!python_module:%define python_module() python3-%{**}}
%else
%define python_exec python3
%define python_expand python3
%endif
%bcond_with gitcommit
%if %{with gitcommit}
%global commit0 2584e35062ad9c2edb68d93c464cf157bc57e3b0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20250926
%endif
%global upstreamname hipSPARSELt
%global rocm_release 7.1
%global rocm_patch 1
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
%global hipsparselt_name libhipsparselt0
%else
%global hipsparselt_name hipsparselt
%endif
%global hipblaslt_commit 7c0ea90bd75ec971502a9232373f8ae7484a5cfa
%global hipblaslt_scommit %(c=%{hipblaslt_commit}; echo ${c:0:7})
%global toolchain rocm
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
%bcond_with test
%if %{with test}
%global __brp_check_rpaths %{nil}
%global build_test ON
%else
%global build_test OFF
%endif
%global build_fflags %{nil}
%global tensile_version 4.33.0
%global tensile_verbose 1
%global gpu_list %{rocm_gpu_list_hipblaslt}
%global _gpu_list "gfx1100"
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio
%bcond_with ninja
%if %{with ninja}
%global cmake_generator -G Ninja
%else
%global cmake_generator %{nil}
%endif
%bcond_with nanobind
Name:           %{hipsparselt_name}
%if %{with gitcommit}
Version:        git%{date0}.%{shortcommit0}
Release:        1%{?dist}
%else
Version:        %{rocm_version}
Release:        1%{?dist}
%endif
Summary:        A SPARSE marshaling library
License:        MIT
%if %{with gitcommit}
Url:            https://github.com/ROCm/rocm-libraries
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%else
Url:            https://github.com/ROCm/%{upstreamname}
%endif
Source1:        https://github.com/ROCm/hipBLASLt/archive/%{hipblaslt_commit}/hipBLASLt-%{hipblaslt_scommit}.tar.gz
Source2:        0001-hipblaslt-tensilelite-remove-yappi-dependency.patch
Source3:        0001-hipblaslt-tensilelite-use-fedora-paths.patch
Source4:        0001-hipblaslt-find-origami-package.patch
Source5:        0001-hipblaslt-tensilelite-use-nanobind-tarball.patch
%global nanobind_version 2.9.2
%global nanobind_giturl https://github.com/wjakob/nanobind
Source10:       %{nanobind_giturl}/archive/v%{nanobind_version}/nanobind-%{nanobind_version}.tar.gz
%global robinmap_version 1.3.0
%global robinmap_giturl https://github.com/Tessil/robin-map
Source11:       %{robinmap_giturl}/archive/v%{robinmap_version}/robin-map-%{robinmap_version}.tar.gz
%if %{with ninja}
%endif
%if 0%{?suse_version}
%global tensile_library_format yaml
%global tensile_verbose 2
%else
%if %{with nanobind}
%endif
%global tensile_library_format msgpack
%global tensile_verbose 1
%endif
%if %{with test}
%endif
Provides:       hipsparselt%{pkg_suffix} = %{version}-%{release}
Provides:       bundled(python-tensile) = %{tensile_version}
%if %{without nanobind}
Provides:       bundled(nanobind) = %{nanobind_version}
Provides:       bundled(robin-map) = %{robinmap_version}
%endif
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  hipcc
BuildRequires:  hipsparse-devel
BuildRequires:  libzstd-devel
BuildRequires:  msgpack-devel
BuildRequires:  ninja-build
BuildRequires:  python3-devel
BuildRequires:  python3dist(joblib)
BuildRequires:  python3dist(msgpack)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(setuptools)
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-llvm-devel
BuildRequires:  rocm-omp-devel
BuildRequires:  rocm-origami-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-smi-devel
BuildRequires:  rocminfo
BuildRequires:  rocsparse-devel
BuildRequires:  roctracer-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
hipSPARSELt is a SPARSE marshaling library, with multiple
supported backends. It sits between the application and a
'worker' SPARSE library, marshaling inputs into the backend
library and marshaling results back to the application.
hipSPARSELt exports an interface that does not require the
client to change, regardless of the chosen backend. Currently,
hipSPARSELt supports the rocSPARSELt backend.

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       hipsparselt%{pkg_suffix}-devel = %{version}-%{release}
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
cd projects/hipsparselt
%else
%autosetup -p1 -n %{upstreamname}-rocm-%{version}
%endif

tar xf %{SOURCE1}
mv hipBLASLt-%{hipblaslt_commit} hipBLASLt
cd hipBLASLt

patch -p1 < %{SOURCE2}
patch -p1 < %{SOURCE3}
patch -p1 < %{SOURCE4}
patch -p1 < %{SOURCE5}

# Use PATH to find where TensileGetPath and other tensile bins are
sed -i -e 's@${Tensile_PREFIX}/bin/TensileGetPath@TensileGetPath@g'            tensilelite/Tensile/cmake/TensileConfig.cmake

# Make sure hip/hip_runtime.h is found
sed -i -e 's@-x hip @-I%{pkg_prefix}/include -x hip @' device-library/matrix-transform/CMakeLists.txt
sed -i -e 's@"-D__HIP_HCC_COMPAT_MODE__=1"@"-D__HIP_HCC_COMPAT_MODE__=1","-I%{pkg_prefix}/include"@' tensilelite/Tensile/Toolchain/Component.py

%if %{with nanobind}
# Disable download of nanobind
sed -i -e 's@FetchContent_MakeAvailable(nanobind)@find_package(nanobind)@' tensilelite/rocisa/CMakeLists.txt
%else
# Use bundled nanobind
tar xf %{SOURCE10}
mv nanobind-* nanobind
cd nanobind
tar xf %{SOURCE11}
cp -r robin-map-*/* ext/robin_map/
cd ..
tar czf nanobind.tar.gz nanobind
%endif

cd ..

# Prevent the virtualenv install from cmake
sed -i -e 's@virtualenv_install@#virtualenv_install@' CMakeLists.txt

# Unforce the setting of libdir
# https://github.com/ROCm/hipSPARSELt/issues/256
sed -i -e 's@set(CMAKE_INSTALL_LIBDIR@#set(CMAKE_INSTALL_LIBDIR@' CMakeLists.txt

# change looking for cblas to flexiblas
sed -i -e 's@find_package( cblas REQUIRED CONFIG )@#find_package( cblas REQUIRED CONFIG )@' clients/CMakeLists.txt
sed -i -e 's@set( BLAS_LIBRARY "blas" )@set( BLAS_LIBRARY "flexiblas" )@' clients/CMakeLists.txt
sed -i -e 's@lapack cblas@flexiblas@' clients/gtest/CMakeLists.txt

# We are building from a tarball, not a git repo
sed -i -e 's@find_package(Git REQUIRED)@#find_package(Git REQUIRED)@' hipBLASLt/cmake/dependencies.cmake
sed -i -e 's@find_package(Git REQUIRED)@#find_package(Git REQUIRED)@' cmake/Dependencies.cmake

%build

%if %{with gitcommit}
cd projects/hipsparselt
%endif
HIPBLASLT_PATH=$PWD/hipBLASLt
cd hipBLASLt
sed -i -e 's@option(HIPBLASLT_ENABLE_OPENMP "Use OpenMP to improve performance." ON)@option(HIPBLASLT_ENABLE_OPENMP "Use OpenMP to improve performance." OFF)@' CMakeLists.txt
cd tensilelite
TL=$PWD
python3 setup.py install --root $TL
cd ../..
export PATH=%{pkg_prefix}/bin:%{rocmllvm_bindir}:$PATH
CLANG_PATH=`hipconfig --hipclangpath`
ROCM_CLANG=${CLANG_PATH}/clang
RESOURCE_DIR=`${ROCM_CLANG} -print-resource-dir`
export DEVICE_LIB_PATH=${RESOURCE_DIR}/amdgcn/bitcode
export TENSILE_ROCM_ASSEMBLER_PATH=${CLANG_PATH}/clang++
export TENSILE_ROCM_OFFLOAD_BUNDLER_PATH=${CLANG_PATH}/clang-offload-bundler
export PATH=${TL}/%{_bindir}:$PATH
export PYTHONPATH=${TL}%{python3_sitelib}:$PYTHONPATH
export Tensile_DIR=${TL}%{python3_sitelib}/Tensile
%cmake %{cmake_generator} \
       -DGPU_TARGETS=%{gpu_list} \
       -DBLAS_INCLUDE_DIR=%{_includedir}/flexiblas \
       -DBUILD_CLIENTS_TESTS=%{build_test} \
       -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
       -DBUILD_VERBOSE=ON \
       -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DCMAKE_C_COMPILER=%{rocmllvm_bindir}/amdclang \
       -DCMAKE_CXX_COMPILER=%{rocmllvm_bindir}/amdclang++ \
       -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
       -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
       -DCMAKE_PREFIX_PATH=%{python3_sitelib}/nanobind \
       -DCMAKE_Fortran_COMPILER=gfortran \
       -DCMAKE_VERBOSE_MAKEFILE=ON \
       -DHIP_PLATFORM=amd \
       -DHIPSPARSELT_HIPBLASLT_PATH=${HIPBLASLT_PATH} \
       -DROCM_SYMLINK_LIBS=OFF \
       -DTensile_LIBRARY_FORMAT=%{tensile_library_format} \
       -DTensile_TEST_LOCAL_PATH=${TL} \
       -DTensile_VERBOSE=%{tensile_verbose} \
       -DVIRTUALENV_BIN_DIR=%{_bindir} \
       -DVIRTUALENV_SITE_PATH=${TL}%{python3_sitelib} \
       %{nil}
%cmake_build
%install
%if %{with gitcommit}
cd projects/hipsparselt
%endif
%cmake_install
rm -f %{buildroot}%{pkg_prefix}/share/doc/hipsparselt/LICENSE.md
%{rocmllvm_bindir}/llvm-strip %{buildroot}%{pkg_prefix}/%{pkg_libdir}/hipsparselt/library/Kernels*.hsaco
chmod a+x %{buildroot}%{pkg_prefix}/%{pkg_libdir}/hipsparselt/library/Kernels*.hsaco
%if %{with test}
chrpath -r %{rocmllvm_libdir} %{buildroot}%{pkg_prefix}/bin/hipsparselt-test
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n hipsparselt-devel -f %{oreon_filedir}/hipsparselt-devel.list
%files -n hipsparselt-test -f %{oreon_filedir}/hipsparselt-test.list

%changelog

%autochangelog
