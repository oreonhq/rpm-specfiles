%global source0_hash cc304bebb6a3315a7bc55855d8cf24a38deeab3be619fc52ce9c632eedf1cf3f
%global rocm_release 7.1
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}
%global upstreamname rocm-smi-lib
%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}/
%global pkg_suffix -%{rocm_release}
%global pkg_skip_install_rpath FALSE
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_skip_install_rpath TRUE
%endif
%global pkg_name rocm-smi%{pkg_suffix}
%bcond_with test
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif
%bcond_with doc
Name:       %{pkg_name}
Version:    %{rocm_version}
Release:        1%{?dist}
Summary:        ROCm System Management Interface Library
License:    MIT AND NCSA
URL:        https://github.com/ROCm/rocm-systems
Source0:        https://github.com/ROCm/rocm-systems/releases/download/rocm-%{version}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz
ExclusiveArch:  x86_64 aarch64 ppc64le riscv64
%if %{with doc}
%endif
%if %{with test}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  libdrm-devel
# /oreon:deps
%description
The ROCm System Management Interface Library, or ROCm SMI library, is part of
the Radeon Open Compute ROCm software stack . It is a C library for Linux that
provides a user space interface for applications to monitor and control GPU
applications.

%package devel
Summary: ROCm SMI Library development files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libdrm-devel
%description devel
ROCm System Management Interface Library development files

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description test
%{summary}
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upstreamname} -p1

# Don't change default C FLAGS and CXX FLAGS:
sed -i '/CMAKE_C.*_FLAGS/d' CMakeLists.txt

# Fix script shebang
sed -i -e 's@env python3@python3@' python_smi_tools/*.py
sed -i -e 's@env python3@python3@' python_smi_tools/rsmiBindingsInit.py.in

# do not download gtest and install
# https://github.com/ROCm/rocm-systems/issues/1022
sed -i -e 's@FetchContent_MakeAvailable(googletest)@#FetchContent_MakeAvailable(googletest)@' tests/rocm_smi_test/CMakeLists.txt
sed -i -e 's@PUBLIC GTest::gtest_main@PUBLIC gtest_main gtest@' tests/rocm_smi_test/CMakeLists.txt
sed -i -e '/TARGETS gtest gtest_main/,+3d' tests/rocm_smi_test/CMakeLists.txt

# fix iomanip include
# https://github.com/ROCm/rocm-systems/issues/1021
sed -i '/#include <string.*/a#include <iomanip>' tests/rocm_smi_test/test_base.h

%build

%cmake \
    -DBUILD_TESTS=%{build_test} \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_SKIP_INSTALL_RPATH=%{pkg_skip_install_rpath} \
    -DSHARE_INSTALL_PREFIX=%{pkg_prefix}/share
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocm-smi-lib/LICENSE.md
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if 0%{?suse_version}
%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%endif
%files -f %{oreon_filedir}/main.list
%files -n rocm-smi-7.1-devel -f %{oreon_filedir}/rocm-smi-7.1-devel.list
%files -n rocm-smi-7.1-test -f %{oreon_filedir}/rocm-smi-7.1-test.list

%changelog

%autochangelog
