%global source0_hash 2fba3aeb970df06f95d465cc2dd5ba5096ec47966e26f2a4544a719e78d43e37
%global upstreamname MIVisionX
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
%global toolchain rocm
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//' )
%global _source_payload         w7T0.xzdio
%global _binary_payload         w7T0.xzdio
%global gpu_list %{rocm_gpu_list_default}
%global _gpu_list gfx1100
Name:           mivisionx%{pkg_suffix}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        AMD's computer vision toolkit
Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT AND Apache-2.0 AND MIT-Khronos-old AND GPL-3.0-or-later
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{upstreamname}-%{version}.tar.gz
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  half-devel
BuildRequires:  hipcc-7.1
BuildRequires:  libavcodec-free-devel
BuildRequires:  libavformat-free-devel
BuildRequires:  miopen-7.1-devel
BuildRequires:  opencv-devel
BuildRequires:  rocblas-7.1-devel
BuildRequires:  rocm-cmake-7.1
BuildRequires:  rocm-compilersupport-7.1-macros
BuildRequires:  rocm-hip-7.1-devel
BuildRequires:  rocm-omp-7.1-devel
BuildRequires:  rocm-rpm-macros-7.1
BuildRequires:  rocm-rpp-7.1-devel
BuildRequires:  rocm-runtime-7.1-devel
# /oreon:deps
%description
MIVisionX toolkit is a set of comprehensive computer vision
and machine intelligence libraries, utilities, and applications
bundled into a single toolkit. AMD MIVisionX delivers highly
optimized conformant open-source implementation of the Khronos
OpenVX™ and OpenVX™ Extensions along with Convolution Neural
Net Model Compiler & Optimizer supporting ONNX, and Khronos
NNEF™ exchange formats. The toolkit allows for rapid prototyping
and deployment of optimized computer vision and machine learning
inference workloads on a wide range of computer hardware,
including small embedded x86 CPUs, APUs, discrete GPUs, and
heterogeneous servers.

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}

%prep

%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# Remove some cruft
find . -type f -name '.gitignore' -delete
find . -type f -name '.DS_Store' -delete

# #include <half/half.hpp> -> <half.hpp>
for f in `find . -type f -name '*.hpp' -o -name '*.h' -o -name '*.cpp' `; do
    sed -i -e 's@#include <half/half.hpp>@#include <half.hpp>@' $f
done

# Fixup default ROCM_PATH
sed -i -e 's@/opt/rocm@%{pkg_prefix}@' CMakeLists.txt

# Make finding rpp required
sed -i -e 's@find_package(rpp 2.1.0 QUIET)@find_package(rpp 2.1.0 REQUIRED)@' amd_openvx_extensions/CMakeLists.txt

%build

%cmake \
    --debug-find-pkg=rpp \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DGPU_TARGETS=%{gpu_list} \
    -DMIGRAPHX=OFF \
    -DNEURAL_NET=OFF \
    -DHIP_PLATFORM=amd
%cmake_build
%install
%cmake_install
chrpath -r %{rocmllvm_libdir} %{buildroot}%{pkg_prefix}/%{pkg_libdir}/libvx_amd_custom.so.1.*.*
rm -f %{buildroot}%{pkg_prefix}/share/doc/mivisionx/LICENSE.txt
rm -f %{buildroot}%{pkg_prefix}/share/doc/mivisionx-asan/LICENSE.txt
rm -rf %{buildroot}%{pkg_prefix}/share/mivisionx/apps
rm -rf %{buildroot}%{pkg_prefix}/share/mivisionx/samples
rm -rf %{buildroot}%{pkg_prefix}/share/mivisionx/test
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mivisionx-7.1-devel -f %{oreon_filedir}/mivisionx-7.1-devel.list

%changelog

%autochangelog
