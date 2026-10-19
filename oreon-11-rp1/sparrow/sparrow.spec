%global source0_hash 586c34c0f46ca878a735db0d2f3e7c6ce78390a65eb42f028bfe5d34dbeeb7b6
Name:           sparrow
Version:        0.6.0
Release:        1%{?dist}
Summary:        C++20 idiomatic APIs for the Apache Arrow Columnar Format
License:        Apache-2.0
URL:            https://github.com/man-group/sparrow
%global github  https://github.com/man-group/sparrow
Source0:        %{github}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: 0001-Remove-tests-that-depend-on-nanoarrow.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doctest-devel
BuildRequires:  gcc-c++
# /oreon:deps
%description

%package devel
Summary:        %{summary}
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
%description devel

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DBUILD_TESTS=ON -DUSE_DATE_POLYFILL=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%cmake_build --target test_sparrow_lib
%cmake_build --target run_tests
%files -f %{oreon_filedir}/main.list
%files -n sparrow-devel -f %{oreon_filedir}/sparrow-devel.list

%changelog

%autochangelog
