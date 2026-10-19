%global source0_hash f6c4dab91ae9a03b3019e7cab0572743afd0e1b6e75b97fcca50259c737c924e
%global commit0 072586a71b55b7f8c584153d223e95687148a900
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20200517
%global debug_package %{nil}
Summary:        P(ortable) SIMD
Name:           psimd
License:        MIT
Version:        %{date0}.%{shortcommit0}
Release:        1%{?dist}
URL:            https://github.com/Maratyszcza
Source0:        https://github.com/Maratyszcza/%{name}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
# /oreon:deps
%description
Portable 128-bit SIMD intrinsics

%package devel
Summary: P(ortable) SIMD
BuildArch:      noarch
Provides:       %{name}-static = %{version}-%{release}
%description devel
Portable 128-bit SIMD intrinsics

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit0}

# For CMake 4
sed -i -e 's@CMAKE_MINIMUM_REQUIRED(VERSION 2.8.12 FATAL_ERROR@CMAKE_MINIMUM_REQUIRED(VERSION 3.5@' CMakeLists.txt

%build

%cmake 
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n psimd-devel -f %{oreon_filedir}/psimd-devel.list

%changelog

%autochangelog
