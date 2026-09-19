%global source0_hash 8b41df21ec01e76ac0c85dc8cc05079ddbf3b2e046e6ecc14c16960b8473ad10

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

# Compiler is hipcc, which is clang based:
%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
# there is no debug package
%global debug_package %{nil}

# Option to test suite for testing on real HW:
%bcond check 1
%if %{with check}
%global build_test ON
%else
%global build_test OFF
%endif

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio"	xz level 7 using %%{getncpus} threads
# Threaded compression reduces the build time.
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

Name:           rocthrust%{pkg_suffix}
%if %{with gitcommit}
Version:        git%{date0}.%{shortcommit0}
Release:        2%{?dist}
%else
Version:        %{rocm_version}
Release:        3%{?dist}
%endif
Summary:        ROCm Thrust libary

%if 0%{?suse_version}
# https://en.opensuse.org/openSUSE:Accepted_licences
# Uses 'Public Domain' but this is not a spdx tag and hangs up the SLE 15.7 autochecker
# The license should also include Public Domain
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND MIT
%else
# https://docs.fedoraproject.org/en-US/legal/allowed-licenses/
# Uses 'LicenseRef-Fedora-Public-Domain'
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND MIT AND LicenseRef-Fedora-Public-Domain
%endif
# All files are Apache 2.0 with some exceptions:
# ./cmake contains only files under MIT
# ./internal/benchmark/*.py are dual licensed Apache 2.0 and Boost 1.0
# ./thrust/ contain some headers files that are Boost 1.0 licensed
# ./thrust/ contain some headers that are dual Apache 2.0 and Boost 1.0
# ./thrust/cmake/FindTBB.cmake is public domain
# ./thrust/detail/allocator/allocator_traits.h is dual Apache 2.0 and MIT
# ./thrust/detail/complex contains BSD 2 clause licensed headers

%if %{with gitcommit}
URL:            https://github.com/ROCm/rocm-libraries
Source0:        %{url}/archive/%{commit0}/rocm-libraries-%{shortcommit0}.tar.gz
%else
URL:            https://github.com/ROCm/rocm-libraries
Source0:        %{url}/releases/download/rocm-%{version}/%{upstreamname}.tar.gz#/%{upstreamname}-%{version}.tar.gz
%endif

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocprim%{pkg_suffix}-static
BuildRequires:  rocm-runtime%{pkg_suffix}-devel
BuildRequires:  rocm-rpm-macros%{pkg_suffix}

%if %{with check}
%if 0%{?suse_version}
BuildRequires:  gtest
%else
BuildRequires:  gtest-devel
%endif
BuildRequires:  rocminfo
%endif

# Only headers, cmake infra, noarch confuses libdir
# BuildArch: noarch
# Only x86_64 works right now:
ExclusiveArch:  x86_64

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
# Building all the gpu's does not make sense
# Build only the first one, this only works well with rpmbuild.
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

# Extra license
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocthrust/LICENSE

%check
%if %{with check}
%ctest
%endif

%files devel
%if %{with gitcommit}
%doc projects/rocthrust/README.md
%license projects/rocthrust/LICENSE
%license projects/rocthrust/NOTICES.txt
%else
%doc README.md
%license LICENSE
%license NOTICES.txt
%endif
%{pkg_prefix}/include/thrust
%{pkg_prefix}/%{pkg_libdir}/cmake/rocthrust/

%changelog
%autochangelog
