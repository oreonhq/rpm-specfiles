%global source0_hash c3bd27e74f0769fe46ea5067e05001f909dc83f01000a22e04e6a0e3d6f4dfc8
%bcond_with gitcommit
%if %{with gitcommit}
%global commit0 2584e35062ad9c2edb68d93c464cf157bc57e3b0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20250926
%endif
%global upstreamname hipRAND
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
%global hiprand_name libhiprand1%{pkg_suffix}
%else
%global hiprand_name hiprand%{pkg_suffix}
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
%else
%global build_test OFF
%endif
%bcond check 1
%bcond_with doc
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio
Name:           %{hiprand_name}
%if %{with gitcommit}
Version:        git%{date0}.%{shortcommit0}
Release:        1%{?dist}
%else
Version:        %{rocm_version}
Release:        1%{?dist}
%endif
Summary:        HIP random number generator
License:        MIT AND BSD-3-Clause
%if %{with gitcommit}
Url:            https://github.com/ROCm/rocm-libraries
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%else
Url:            https://github.com/ROCm/%{upstreamname}
%endif
%if %{with test}
%if 0%{?suse_version}
%else
%endif
%endif
%if %{with doc}
%endif
Provides:       hiprand%{pkg_suffix} = %{version}-%{release}
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
BuildRequires:  rocrand-devel
# /oreon:deps
%description
hipRAND is a RAND marshalling library, with multiple supported backends. It
sits between the application and the backend RAND library, marshalling inputs
into the backend and results back to the application. hipRAND exports an
interface that does not require the client to change, regardless of the chosen
backend. Currently, hipRAND supports either rocRAND or cuRAND.

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%package devel
Summary:        The hipRAND development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       rocrand%{pkg_suffix}-devel
Provides:       hiprand%{pkg_suffix}-devel = %{version}-%{release}
%description devel
The hipRAND development package.

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
cd projects/hiprand
%else
%autosetup -p1 -n %{upstreamname}-rocm-%{version}
%endif

#Remove RPATH:
sed -i '/INSTALL_RPATH/d' CMakeLists.txt

# On Tumbleweed Q2,2025
# /usr/include/gtest/internal/gtest-port.h:279:2: error: C++ versions less than C++14 are not supported.
#   279 | #error C++ versions less than C++14 are not supported.
# https://github.com/ROCm/hipRAND/issues/222
# Convert the c++11's to c++14
sed -i -e 's@set(CMAKE_CXX_STANDARD 11)@set(CMAKE_CXX_STANDARD 14)@' {,test/package/}CMakeLists.txt

%build

%if %{with gitcommit}
cd projects/hiprand
%endif
%cmake \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
    -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
    -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DCMAKE_SKIP_RPATH=ON \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
    -DAMDGPU_TARGETS=%{rocm_gpu_list_default} \
    -DBUILD_TEST=%{build_test} \
    -DROCM_SYMLINK_LIBS=OFF
%cmake_build
%install
%if %{with gitcommit}
cd projects/hiprand
%endif
%cmake_install
rm -f %{buildroot}%{pkg_prefix}/share/doc/hiprand/LICENSE.md
rm -f %{buildroot}%{pkg_prefix}/bin/hipRAND/CTestTestfile.cmake
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with test}
%if %{with check}
%if 0%{?suse_version}
export LD_LIBRARY_PATH=$PWD/build/library:$LD_LIBRARY_PATH
%endif
%ctest
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n hiprand-devel -f %{oreon_filedir}/hiprand-devel.list
%files -n hiprand-test -f %{oreon_filedir}/hiprand-test.list

%changelog

%autochangelog
