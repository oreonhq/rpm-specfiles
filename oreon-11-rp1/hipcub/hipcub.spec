%global source0_hash 131c1168f0b690874f5bce2f20c37ce854d4de47487ad1ffd2d361445276c0b8
%bcond_with gitcommit
%if %{with gitcommit}
%global commit0 2584e35062ad9c2edb68d93c464cf157bc57e3b0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20250926
%endif
%global upstreamname hipCUB
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
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
%global debug_package %{nil}
%bcond_with test
%bcond check 1
%if %{with check} || %{with test}
%global build_test ON
%else
%global build_test OFF
%endif
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio
%global gpu_list %{rocm_gpu_list_default}
%global _gpu_list gfx1100
Name:           hipcub%{pkg_suffix}
%if %{with gitcommit}
Version:        git%{date0}.%{shortcommit0}
Release:        1%{?dist}
%else
Version:        %{rocm_version}
Release:        1%{?dist}
%endif
Summary:        ROCm port of CUDA CUB library
License:        MIT and BSD-3-Clause
%if %{with gitcommit}
Url:            https://github.com/ROCm/rocm-libraries
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%else
Url:            https://github.com/ROCm
%endif
%if %{with check} || %{with test}
%if 0%{?suse_version}
%else
%endif
%endif
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocminfo
BuildRequires:  rocprim-static
# /oreon:deps
%description
hipCUB is a thin wrapper library on top of rocPRIM or CUB. It enables developers
to port a project using the CUB library to the HIP layer to run on AMD hardware.
In the ROCm environment, hipCUB uses the rocPRIM library as the backend.

%package devel
Summary:        The %{upstreamname} development package
Provides:       %{name}-static = %{version}-%{release}
Requires:       rocprim%{pkg_suffix}-devel
%description devel
The %{upstreamname} development package.

%if %{with test}
%package test
Summary:        Self-tests for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
%description test
Precompiled self-tests for %{name}
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{with gitcommit}
%setup -q -n rocm-libraries-%{commit0}
cd projects/hipcub
%else
%autosetup -p1 -n %{upstreamname}-rocm-%{version}
%endif

#
# The ROCMExportTargetsHeaderOnly.cmake file
# generates a files that reference the install location of other files
# Make this change so they match
sed -i -e 's/ROCM_INSTALL_LIBDIR lib/ROCM_INSTALL_LIBDIR %{pkg_libdir}/' cmake/ROCMExportTargetsHeaderOnly.cmake

%build

%if %{with gitcommit}
cd projects/hipcub
%endif
%if %{with check}
gpu=`rocm_agent_enumerator | head -n 1`
%endif
%cmake \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
    -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
    -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DBUILD_TEST=%{build_test} \
%if %{with check}
    -DAMDGPU_TARGETS=${gpu} \
%else
    -DAMDGPU_TARGETS=${gpu_list} \
%endif
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DROCM_SYMLINK_LIBS=OFF
%cmake_build
%install
%if %{with gitcommit}
cd projects/hipcub
%endif
%cmake_install
rm -f %{buildroot}%{pkg_prefix}/share/doc/hipcub/LICENSE.txt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n hipcub-devel -f %{oreon_filedir}/hipcub-devel.list
%files -n hipcub-test -f %{oreon_filedir}/hipcub-test.list

%changelog

%autochangelog
