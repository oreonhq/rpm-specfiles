%global source1_hash a0c0a78684da2d26ee883ccc632c8f51a4b00cfd3915707f9675cc8c0cf96483
%global source0_hash ef2ef3a6468e9dc47061afa91d862870c08cbdb7a6c883880d11eb168427bba9
%global upstreamname ROCmValidationSuite
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_llvm_prefix %{_libdir}/rocm/rocm-%{rocm_release}/llvm
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix -%{rocm_release}
%global pkg_module rocm%{pkg_suffix}
%else
%global pkg_libdir %{_lib}
%global pkg_llvm_prefix %{_libdir}/rocm/llvm
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%endif
%global toolchain rocm
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fcf-protection//' -e 's/-fcf-protection//' -e 's/-ffat-lto-objects//' -e 's/-flto=thin//' -e 's/-mtls-dialect=gnu2//')
%global _lto_cflags %{nil}
%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif
Name:           rocm-validation-suite%{pkg_suffix}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        ROCm Validation Suite (rvs)
Url:            https://github.com/ROCm/ROCmValidationSuite
License:        MIT AND NCSA
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%global mxdata_commit 12c016dc694139317feb2e23c59028fde70beaf4
%global mxdata_scommit %(c=%{mxdata_commit}; echo ${c:0:7})
Source1:        https://github.com/ROCm/mxDataGenerator/archive/%{mxdata_commit}/mxDataGenerator-%{mxdata_scommit}.tar.gz
Patch1:         0001-rocm-validation-suite-do-not-download-mxDataGenerato.patch
ExclusiveArch: x86_64
# oreon:deps
BuildRequires:  amdsmi-7.1-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hipblas-common-7.1-devel
BuildRequires:  hipblaslt-7.1-devel
BuildRequires:  hiprand-7.1-devel
BuildRequires:  ninja-build
BuildRequires:  pciutils-devel
BuildRequires:  rocblas-7.1-devel
BuildRequires:  rocm-cmake-7.1
BuildRequires:  rocm-comgr-7.1-devel
BuildRequires:  rocm-compilersupport-7.1-macros
BuildRequires:  rocm-hip-7.1-devel
BuildRequires:  rocm-omp-7.1-devel
BuildRequires:  rocm-rpm-macros-7.1
BuildRequires:  rocm-runtime-7.1-devel
BuildRequires:  rocm-smi-7.1-devel
BuildRequires:  yaml-cpp-devel
# /oreon:deps
%description
The ROCm Validation Suite (RVS) is a system validation and
diagnostics tool for monitoring, stress testing, detecting
and troubleshooting issues that affects the functionality
and performance of AMD GPU(s) operating in a
high-performance/AI/ML computing environment. RVS is enabled
using the ROCm software stack on a compatible software and
hardware platform.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upstreamname}-rocm-%{version} -p1

# mxDataGenerator
tar xf %{SOURCE1}
mv mxDataGenerator-* mxDataGenerator
cp -p mxDataGenerator/LICENSE.md mxDataGenerator/LICENSE.mxDataGenerator.md

# disable rpath
# Fixes these related issues on build
# ERROR   0010: file '/opt/rocm/usr/lib64/librvslib.so.0.0.0' contains an empty runpath in [:/..]
sed -i -e 's@set(CMAKE_SHARED_LINKER_FLAGS_INIT@#set(CMAKE_SHARED_LINKER_FLAGS_INIT@' CMakeLists.txt
sed -i -e 's@set(CMAKE_EXE_LINKER_FLAGS_INIT@#set(CMAKE_EXE_LINKER_FLAGS_INIT@' CMakeLists.txt

# fix opt/rocm things
sed -i -e 's@set(ROCM_PATH "/opt/rocm"@set(ROCM_PATH "%{pkg_prefix}"@' CMakeLists.txt
sed -i -e 's@set(CMAKE_INSTALL_PREFIX "/opt/rocm"@#set(CMAKE_INSTALL_PREFIX "/opt/rocm"@' CMakeLists.txt

# lib64 vs lib
# https://github.com/ROCm/ROCmValidationSuite/issues/985
sed -i -e 's@HSA_PATH}/lib@HSA_PATH}/%{pkg_libdir}@' CMakeLists.txt
sed -i -e 's@ROCBLAS_INC_DIR}/../lib@ROCBLAS_INC_DIR}/../%{pkg_libdir}@' CMakeLists.txt
sed -i -e 's@HIPBLASLT_INC_DIR}/../lib@HIPBLASLT_INC_DIR}/../%{pkg_libdir}@' CMakeLists.txt
sed -i -e 's@hiprand_INCLUDE_DIR}/../lib@hiprand_INCLUDE_DIR}/../%{pkg_libdir}@' CMakeLists.txt
sed -i -e 's@rocrand_INCLUDE_DIR}/../lib@rocrand_INCLUDE_DIR}/../%{pkg_libdir}@' CMakeLists.txt
# and with the dlopen
sed -i -e 's@../lib/rvs/@../%{pkg_libdir}/rvs/@' rvs/src/rvsmodule.cpp

# rvs_lib_path
sed -i -e 's@DRVS_LIB_PATH="${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR}/rvs"@DRVS_LIB_PATH="%{pkg_prefix}/%{pkg_libdir}/rvs"@' CMakeLists.txt

# disable use of CPACK_PACKAGING_INSTALL_PREFIX
# https://github.com/ROCm/ROCmValidationSuite/issues/984
sed -i -e 's@DESTINATION ${CPACK_PACKAGING_INSTALL_PREFIX}/@DESTINATION @g' CMakeLists.txt
sed -i -e 's@INSTALL_DESTINATION ${CPACK_PACKAGING_INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR}/cmake/rvs@INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake/rvs@' CMakeLists.txt
sed -i -e 's@${CPACK_PACKAGING_INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR}/cmake/rvs@${CMAKE_INSTALL_LIBDIR}/cmake/rvs@' CMakeLists.txt
find -type f -name CMakeLists.txt -print0 | xargs -0 sed -i -e 's@DESTINATION ${CPACK_PACKAGING_INSTALL_PREFIX}/@DESTINATION @g'

# Hardcoded gpus
# Has 803,1030,900,906,908,942,950,1100,1101,1200,1201
# Need to remove 803
sed -i -e 's@--offload-arch=gfx803@@' CMakeLists.txt
# Need to add 1031,1035,1036,1102,1103,1150,1151,1152,1153
sed -i -e 's@--offload-arch=gfx1030@--offload-arch=gfx1030 --offload-arch=gfx1031 --offload-arch=gfx1035 --offload-arch=gfx1036 --offload-arch=gfx1102 --offload-arch=gfx1103 --offload-arch=gfx1150 --offload-arch=gfx1151 --offload-arch=gfx1152 --offload-arch=gfx1153@' CMakeLists.txt

# disable git usage on tarballs
sed -i -e 's@GIT NAMES git@GIT NAMES git-not-going-to-find-me@' cmake_modules/utils.cmake

# fix link of librvslib
sed -i -e '/add_library/a target_link_libraries(${RVS_TARGET} -lrocm_smi64 -lhipblaslt -lhiprand -lrocrand -lrocblas -lyaml-cpp -lpci -lamd_smi -lamdhip64 -lhsa-runtime64 -lomp)' rvslib/CMakeLists.txt
# Now the library path
sed -i -e 's@-lrocm_smi64 @-L%{pkg_prefix}/%{pkg_libdir} -lrocm_smi64 @' rvslib/CMakeLists.txt

# for finding omp.h
sed -i -e 's@${YAML_CPP_INCLUDE_DIR}@${YAML_CPP_INCLUDE_DIR} "%{pkg_llvm_prefix}/include" @' rvs/CMakeLists.txt
sed -i -e 's@${YAML_CPP_INCLUDE_DIR}@${YAML_CPP_INCLUDE_DIR} "%{pkg_llvm_prefix}/include" @' rvslib/CMakeLists.txt

%build

%cmake -G Ninja \
       -DAMDGPU_TARGETS=%{rocm_gpu_list_default} \
       -DCMAKE_BUILD_TYPE=%{build_type} \
       -DCMAKE_C_COMPILER=%{rocmllvm_bindir}/amdclang \
       -DCMAKE_CXX_COMPILER=%{rocmllvm_bindir}/amdclang++ \
       -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
       -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
       -DHIP_PLATFORM=amd \
       -DMXDATAGENERATOR_INC_DIR=${PWD}/mxDataGenerator/lib/include \
       -DRVS_BUILD_TESTS=FALSE
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocm-validation-suite/LICENSE
rm -rf %{buildroot}%{pkg_prefix}/include
rm -rf %{buildroot}%{pkg_prefix}/%{pkg_libdir}/cmake
rm %{buildroot}%{pkg_prefix}/%{pkg_libdir}/librvslib.so{,.0}
L="libbabel libgm libgpup libgst libiet libmem libpbqt libpeqt libperf libpebb libpesm librcqt libsmqt libtst"
for l in $L; do
    if [ -f $l.so ]; then
	rm %{buildroot}%{pkg_prefix}/%{pkg_libdir}/rvs/$l.so{,.0}
	mv %{buildroot}%{pkg_prefix}/%{pkg_libdir}/rvs/$l.so.0.0.0 %{buildroot}%{pkg_prefix}/%{pkg_libdir}/rvs/$l.so
    fi
done
%fdupes %{buildroot}%{pkg_prefix}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
