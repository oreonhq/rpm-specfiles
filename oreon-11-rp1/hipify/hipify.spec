%global source0_hash 9fb4e739f116b5a5b8c437808c71c6c1f31dd6184c9be21d67d4b8bf1d91b4f2

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
%global upstreamname HIPIFY

%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}/
%global pkg_suffix -%{rocm_release}
%global pkg_module rocm%{pkg_suffix}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%endif

# This is a clang tool so best to build with clang
%global toolchain clang

Name:           hipify%{pkg_suffix}
Version:        %{rocm_version}
Release:        3%{?dist}
Summary:        Convert CUDA to HIP

Url:            https://github.com/ROCm
License:        MIT
Source0:        %{url}/%{upstreamname}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
Patch0:         0001-prepare-hipify-cmake-for-fedora.patch

BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  perl
# System clang may be too old, use rocm-llvm
BuildRequires:  rocm-llvm%{pkg_suffix}-static
BuildRequires:  rocm-clang%{pkg_suffix}-devel
BuildRequires:  rocm-compilersupport%{pkg_suffix}-macros
BuildRequires:  zlib-devel

Requires:       perl

# ROCm is really only on x86_64
ExclusiveArch:  x86_64

%description
HIPIFY is a set of tools to translate CUDA source code into portable
HIP C++ automatically.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstreamname}-rocm-%{version}

%build
%cmake \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/clang++ \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/clang \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/..

%cmake_build

%check
echo "void f(int *a, const cudaDeviceProp *b) { cudaChooseDevice(a,b); }" > b.cu
echo "void f(int *a, const hipDeviceProp_t *b) { hipChooseDevice(a,b); }" > e.hip
./bin/hipify-perl b.cu -o t.hip
diff e.hip t.hip

%install
%cmake_install
rm -rf %{buildroot}%{pkg_prefix}/hip
# Fix executable perm:
chmod a+x %{buildroot}%{pkg_prefix}/bin/*
# Fix script shebang (Fedora doesn't allow using "env"):
sed -i 's|\(/usr/bin/\)env perl|\1perl|' %{buildroot}%{pkg_prefix}/bin//hipify-perl

# Fix
# /usr/bin/hipify-clang: error while loading shared libraries: libclang-cpp.so.19.0git
chrpath %{buildroot}%{pkg_prefix}/bin/hipify-clang -r %rocmllvm_libdir

# No devel package
rm -rf %{buildroot}%{pkg_prefix}/include

%files
%doc README.md
%license LICENSE.txt
%{pkg_prefix}/bin/hipify-clang
%{pkg_prefix}/bin/hipify-perl
%{pkg_prefix}/libexec/hipify/

%changelog
%autochangelog
