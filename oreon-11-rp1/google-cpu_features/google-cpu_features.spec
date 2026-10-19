%global source0_hash ab2463f2d38fcaff1ce806be8e4c91333449931f5e02009d543b2569a3fa471a
ExcludeArch: s390x
Name:    google-cpu_features
Version: 0.11.0
Release:        1%{?dist}
Summary:        A cross-platform C library to retrieve CPU features at runtime
License: Apache-2.0
URL:     https://github.com/google/cpu_features
Source0:        https://github.com/google/cpu_features/archive/v%{version}/cpu_features-%{version}.tar.gz
Patch0:  google-cpu_features-unbundle_gtest.patch
Patch1:  google-cpu_features-create_soname.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  make
# /oreon:deps
%description
A cross-platform C library to retrieve CPU features at runtime.

%package devel
Summary: %{name} headers and development-related files
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{name} headers and development-related files, CMake config files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir cpu_features-%{version}
%oreon_prep
%build

%cmake \
 -DCMAKE_BUILD_TYPE:STRING=Release \
 -DCPUFEATURES_VERSION_MAJOR:STRING=0 \
 -DCPUFEATURES_VERSION:STRING=0.10 \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES \
 -DBUILD_PIC:BOOL=ON -DBUILD_TESTING:BOOL=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest -- -VV
%files -f %{oreon_filedir}/main.list
%files -n google-cpu_features-devel -f %{oreon_filedir}/google-cpu_features-devel.list

%changelog

%autochangelog
