%global source0_hash 4c223ad15482126f239a9e827a46c8f1bef602d1798235ea19dad9097d6cfb11

#
# Copyright Fedora Project Authors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

%bcond_with gitcommit
%if %{with gitcommit}
%global commit0 2584e35062ad9c2edb68d93c464cf157bc57e3b0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20250926
%endif

%global upstreamname rocprim
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

# Compiler is hipcc, which is clang based:
%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')

%bcond_with test
# Option to build test subpackage
# enable building of tests if check or test are enabled
%if %{with test}
%global build_test ON
%else
%global build_test OFF
# there is no debug package, this just headers
%global debug_package %{nil}
%endif

# For documentation
%bcond_with doc

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

%global gpu_list %{rocm_gpu_list_default}
%global _gpu_list gfx1100

Name:           rocprim%{pkg_suffix}
%if %{with gitcommit}
Version:        git%{date0}.%{shortcommit0}
Release:        2%{?dist}
%else
Version:        %{rocm_version}
Release:        3%{?dist}
%endif
Summary:        ROCm parallel primatives

License:        MIT AND BSD-3-Clause

%if %{with gitcommit}
URL:            https://github.com/ROCm/rocm-libraries
Source0:        %{url}/archive/%{commit0}/rocm-libraries-%{shortcommit0}.tar.gz
%else
URL:            https://github.com/ROCm/rocm-libraries
Source0:        %{url}/releases/download/rocm-%{version}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%endif

# ROCm only working on x86_64
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-runtime%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}

%if %{with doc}
BuildRequires:  doxygen
BuildRequires:  python3dist(marshalparser)
%endif

%if %{with test}
%if 0%{?suse_version}
BuildRequires:  gtest
%else
BuildRequires:  gtest-devel
%endif
BuildRequires:  rocminfo%{pkg_suffix}
%endif

%description
The rocPRIM is a header-only library providing HIP parallel primitives
for developing performant GPU-accelerated code on AMD ROCm platform.

%package devel
Summary:        ROCm parallel primatives
Provides:       rocprim%{pkg_suffix}-static = %{version}-%{release}

# the devel subpackage is only headers and cmake infra
BuildArch: noarch

%description devel
The rocPRIM is a header-only library providing HIP parallel primitives
for developing performant GPU-accelerated code on AMD ROCm platform.

%if %{with test}
%package test
Summary:        upstream tests for ROCm parallel primatives
Provides:       rocprim%{pkg_suffix}-test = %{version}-%{release}
Requires:       rocprim%{pkg_suffix}-devel
Requires:       gtest

%description test
tests for the rocPRIM package
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{with gitcommit}
%setup -q -n rocm-libraries-%{commit0}
cd projects/rocprim
%else
%autosetup -n %{upstreamname} -p1
%endif

# In file included from rocPRIM-rocm-6.4.2/test/rocprim/test_texture_cache_iterator.cpp:26: 
# ../rocprim/include/rocprim/iterator/texture_cache_iterator.hpp:231:13: error:
#   'tex1Dfetch<int, nullptr>' is unavailable: The image/texture API not supported on the device
# Remove fail to build test
sed -i -e 's@add_rocprim_test("rocprim.texture_cache_iterator"@#add_rocprim_test("rocprim.texture_cache_iterator"@' test/rocprim/CMakeLists.txt
grep texture_cach test/rocprim/CMakeLists.txt

%build
%if %{with gitcommit}
cd projects/rocprim
%endif

%cmake \
    -DBUILD_TEST=%{build_test} \
    -DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
    -DCMAKE_BUILD_TYPE=%build_type \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=share \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
    -DGPU_TARGETS=%{gpu_list} \
    -DROCM_SYMLINK_LIBS=OFF

%cmake_build

%install
%if %{with gitcommit}
cd projects/rocprim
%endif

%cmake_install

rm -f %{buildroot}%{pkg_prefix}/share/doc/rocprim/LICENSE.md

%if %{with test}
# force the cmake test file to use absolute paths for its referenced binaries
sed -i -e 's@\.\.@\/usr\/bin@' %{buildroot}%{pkg_prefix}/bin/rocprim/CTestTestfile.cmake
%endif

%files devel
%if %{with gitcommit}
%doc projects/rocprim/README.md
%license projects/rocprim/LICENSE.md
%license projects/rocprim/NOTICES.txt
%else
%doc README.md
%license LICENSE.md
%license NOTICES.txt
%endif
%{pkg_prefix}/include/rocprim/
%{pkg_prefix}/share/cmake/rocprim/

%if %{with test}
%files test
%{pkg_prefix}/bin/test*
%{pkg_prefix}/share/libtest*
%{pkg_prefix}/bin/rocprim/
%endif

%changelog
%autochangelog
