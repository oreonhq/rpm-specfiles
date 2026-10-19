%global source0_hash 898ebfdf562cd1a3622870e17a703b38559cf2c607b2d5f79e6b3a55563af619
%undefine __cmake_in_source_build
Name: cotila
Version: 1.2.1
Release:        1%{?dist}
License: Apache-2.0
URL: https://github.com/calebzulawski/cotila
Summary:        Compile Time Linear Algebra
Source0:        https://github.com/calebzulawski/%{name}/archive/%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir cotila-%{version}
%oreon_prep
%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build
%install
%cmake_install
%oreon_autofiles cotila-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n cotila-devel -f %{oreon_filedir}/cotila-devel.list

%changelog

%autochangelog
