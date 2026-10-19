%global source0_hash 8b41df21ec01e76ac0c85dc8cc05079ddbf3b2e046e6ecc14c16960b8473ad10
%bcond_with gitcommit
%if %{with gitcommit}
%global commit0 2584e35062ad9c2edb68d93c464cf157bc57e3b0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20250926
%endif
%global upstreamname rocthrust
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
%global toolchain rocm
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
%global debug_package %{nil}
%bcond check 1
%if %{with check}
%global build_test ON
%else
%global build_test OFF
%endif
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio
Name:           rocthrust%{pkg_suffix}
%if %{with gitcommit}
Version:        git%{date0}.%{shortcommit0}
Release:        1%{?dist}
%else
Version:        %{rocm_version}
Release:        1%{?dist}
%endif
Summary:        ROCm Thrust libary
%if 0%{?suse_version}
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND MIT
%else
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND MIT AND LicenseRef-Fedora-Public-Domain
%endif
%if %{with gitcommit}
URL:            https://github.com/ROCm/rocm-libraries
Source0:        https://github.com/ROCm/%{toolchain}-%{pkg_libdir}raries/releases/download/%{pkg_module}.%{rocm_patch}/%{upstreamname}.tar.gz#/%{name}.%{rocm_patch}.tar.gz
%else
URL:            https://github.com/ROCm/rocm-libraries
%endif
%if %{with check}
%if 0%{?suse_version}
%else
%endif
%endif
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  rocm-cmake-7.1
BuildRequires:  rocm-comgr-7.1-devel
BuildRequires:  rocm-compilersupport-7.1-macros
BuildRequires:  rocm-hip-7.1-devel
BuildRequires:  rocm-rpm-macros-7.1
BuildRequires:  rocm-runtime-7.1-devel
BuildRequires:  rocminfo
BuildRequires:  rocprim-7.1-static
# /oreon:deps
%description
Thrust is a parallel algorithm library. This library has been
ported to HIP/ROCm platform, which uses the rocPRIM library.

%package devel
Summary:        The %{upstreamname} development package
Provides:       %{name}-static = %{version}-%{release}
%description devel
The %{upstreamname} development package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{with gitcommit}
%setup -q -n rocm-libraries-%{commit0}
cd projects/rocthrust
%else
%autosetup -n %{upstreamname} -p1
%endif

#
# The ROCMExportTargetsHeaderOnly.cmake file
# generates a files that reference the install location of other files
# Make this change so they match
sed -i -e 's/ROCM_INSTALL_LIBDIR lib/ROCM_INSTALL_LIBDIR %{pkg_libdir}/' cmake/ROCMExportTargetsHeaderOnly.cmake

%build

%if %{with gitcommit}
cd projects/rocthrust
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
%endif
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DROCM_SYMLINK_LIBS=OFF
%cmake_build
%install
%if %{with gitcommit}
cd projects/rocthrust
%endif
%cmake_install
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocthrust/LICENSE
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%if %{with check}
%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n rocthrust-7.1-devel -f %{oreon_filedir}/rocthrust-7.1-devel.list

%changelog

%autochangelog
