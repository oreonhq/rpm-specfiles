%global source0_hash 9fb4e739f116b5a5b8c437808c71c6c1f31dd6184c9be21d67d4b8bf1d91b4f2
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
%global toolchain clang
Name:           hipify%{pkg_suffix}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        Convert CUDA to HIP
Url:            https://github.com/ROCm
License:        MIT
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{upstreamname}-%{version}.tar.gz
Patch0:         0001-prepare-hipify-cmake-for-fedora.patch
Requires:       perl
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  perl
BuildRequires:  rocm-clang-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-llvm-static
BuildRequires:  zlib-devel
# /oreon:deps
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
chmod a+x %{buildroot}%{pkg_prefix}/bin/*
sed -i 's|\(/usr/bin/\)env perl|\1perl|' %{buildroot}%{pkg_prefix}/bin//hipify-perl
chrpath %{buildroot}%{pkg_prefix}/bin/hipify-clang -r %rocmllvm_libdir
rm -rf %{buildroot}%{pkg_prefix}/include
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
