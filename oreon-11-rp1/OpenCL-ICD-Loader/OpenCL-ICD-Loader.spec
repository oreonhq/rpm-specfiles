%global source0_hash 2af329e7873817e8d568e9716532b8958bf722aef5ffa693718e0a6b52e94059
%global commit0 ad770a1b64c6b8d5f2ed4e153f22e4f45939f27f
%global date 20250722
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Name:           OpenCL-ICD-Loader
Version:        2026.05.29
Release:        1%{?dist}
Summary:        Khronos official OpenCL ICD Loader
License:        Apache-2.0
URL:            https://github.com/KhronosGroup/OpenCL-ICD-Loader
Source0:        https://github.com/KhronosGroup/%{name}/archive/%{commit0}/%{name}-ad770a1.tar.gz
Conflicts: ocl-icd
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  opencl-headers
# /oreon:deps
%description
%{summary}.

%package devel
Summary:        Development files for Khronos official OpenCL ICD Loader
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts: ocl-icd-devel
%description devel
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit0}

%build

%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DOPENCL_ICD_LOADER_HEADERS_DIR="/usr/include/"
%cmake_build
%install
%cmake_install
%oreon_autofiles OpenCL-ICD-Loader-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n OpenCL-ICD-Loader-devel -f %{oreon_filedir}/OpenCL-ICD-Loader-devel.list

%changelog

%autochangelog
