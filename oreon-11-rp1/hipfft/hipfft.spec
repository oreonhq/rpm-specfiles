%global source0_hash 94d8d901fdec2a41957f83139dea125bda4127af40d47f03b637a7920d73db50

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

%global upstreamname hipFFT
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
%global hipfft_name libhipfft0%{pkg_suffix}
%else
%global hipfft_name hipfft%{pkg_suffix}
%endif

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//' -e 's/-flto=thin//' )

%global _lto_cflags %{nil}

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
%else
%global build_test OFF
%endif

# Option to test suite for testing on real HW:
# May have to set gpu under test with
# export HIP_VISIBLE_DEVICES=<num> - 0, 1 etc.
%bcond check 1

# Compression type and level for source/binary package payloads.
#  "w7T0.xzdio" xz level 7 using %%{getncpus} threads
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio

Name:           %{hipfft_name}
%if %{with gitcommit}
Version:        git%{date0}.%{shortcommit0}
Release:        2%{?dist}
%else
Version:        %{rocm_version}
Release:        5%{?dist}
%endif
Summary:        ROCm FFT marshalling library
License:        MIT

%if %{with gitcommit}
Url:            https://github.com/ROCm/rocm-libraries
Source0:        %{url}/archive/%{commit0}/rocm-libraries-%{shortcommit0}.tar.gz
%else
Url:            https://github.com/ROCm/%{upstreamname}
Source0:        %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-rocm-%{version}.tar.gz
%endif

# https://github.com/ROCm/rocm-libraries/issues/2400
Patch1:         0001-hipfft-hipfftw-soversion.patch

# Only x86_64 works right now
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rocm-cmake%{pkg_suffix}
BuildRequires:  rocm-comgr%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  rocm-hip%{pkg_suffix}-devel
BuildRequires:  rocm-runtime%{pkg_suffix}-devel >= %{rocm_release}
BuildRequires:  rocm-rpm-macros%{pkg_suffix}
BuildRequires:  rocprim%{pkg_suffix}-static
BuildRequires:  rocfft%{pkg_suffix}-devel

%if %{with test}

BuildRequires:  boost-devel
BuildRequires:  fftw-devel
BuildRequires:  hiprand%{pkg_suffix}-devel
BuildRequires:  rocrand%{pkg_suffix}-devel

%if 0%{?suse_version}
BuildRequires:  gtest
BuildRequires:  libboost_program_options-devel
%else
BuildRequires:  gtest-devel
%endif

%endif

Provides:       hipfft%{pkg_suffix} = %{version}-%{release}

%description
hipFFT is an FFT marshalling library. Currently, hipFFT supports
the rocFFT backends

hipFFT exports an interface that does not require the client to
change, regardless of the chosen backend. It sits between the
application and the backend FFT library, marshalling inputs into
the backend and results back to the application.

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       hipfft%{pkg_suffix}-devel = %{version}-%{release}

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
cd projects/hipfft
%else
%autosetup -n %{upstreamname}-rocm-%{version} -p 1
%endif

# CMake Error at clients/tests/CMakeLists.txt:87 (find_package):
#   No "FindHIP.cmake" found in CMAKE_MODULE_PATH.
# Remove MODULE
sed -i -e 's@find_package( HIP MODULE REQUIRED )@find_package( HIP REQUIRED )@' clients/tests/CMakeLists.txt

%build
%if %{with gitcommit}
cd projects/hipfft
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
    -DBUILD_CLIENTS_TESTS=%{build_test} \
    -DBUILD_CLIENTS_TESTS_OPENMP=OFF \
    -DROCM_SYMLINK_LIBS=OFF \
    -DHIP_PLATFORM=amd

%cmake_build

%install
%if %{with gitcommit}
cd projects/hipfft
%endif
%cmake_install

rm -f %{buildroot}%{pkg_prefix}/share/doc/hipfft/LICENSE.md

%check
%if %{with test}
%if %{with check}
%if 0%{?suse_version}
export LD_LIBRARY_PATH=%{__builddir}/library:$LD_LIBRARY_PATH
%{__builddir}/clients/staging/hipfft-test
%else
export LD_LIBRARY_PATH=%{_vpath_builddir}/library:$LD_LIBRARY_PATH
%{_vpath_builddir}/clients/staging/hipfft-test
%endif
%endif
%endif

%files
%if %{with gitcommit}
%license projects/hipfft/LICENSE.md
%doc projects/hipfft/README.md
%else
%license LICENSE.md
%doc README.md
%endif

%{pkg_prefix}/%{pkg_libdir}/libhipfft.so.0{,.*}
%{pkg_prefix}/%{pkg_libdir}/libhipfftw.so.0{,.*}

%files devel
%{pkg_prefix}/include/hipfft/
%{pkg_prefix}/%{pkg_libdir}/libhipfft.so
%{pkg_prefix}/%{pkg_libdir}/libhipfftw.so
%{pkg_prefix}/%{pkg_libdir}/cmake/hipfft/

%if %{with test}
%files test
%{pkg_prefix}/bin/hipfft-test
%endif

%changelog
%autochangelog
