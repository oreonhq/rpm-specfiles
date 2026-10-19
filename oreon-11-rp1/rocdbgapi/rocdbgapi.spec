%global source0_hash 334a5bc39f5d1b3e7fe415206f499985156a0f76556b2f91789f528ccbc3e9a2
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
%global upstreamname ROCdbgapi
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
%global toolchain clang
Name:       rocdbgapi%{pkg_suffix}
Version:    %{rocm_version}
Release:        1%{?dist}
Summary:        AMD Debugger API
License:    MIT
URL:        https://github.com/ROCm/%{upstreamname}
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{upstreamname}-%{version}.tar.gz
ExclusiveArch: x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hipcc-7.1
BuildRequires:  rocm-comgr-7.1-devel
BuildRequires:  rocm-compilersupport-7.1-macros
BuildRequires:  rocm-runtime-7.1-devel
# /oreon:deps
%description
The AMD Debugger API is a library that provides all the support necessary
for a debugger and other tools to perform low level control of the
execution and inspection of execution state of AMD's commercially
available GPU architectures.

%package devel
Summary: Libraries and headers for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstreamname}-rocm-%{version}

%build

%cmake \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix}
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocm-dbgapi/LICENSE.txt
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocm-dbgapi-asan/LICENSE.txt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n rocdbgapi-7.1-devel -f %{oreon_filedir}/rocdbgapi-7.1-devel.list

%changelog

%autochangelog
