%global source0_hash edad5faaa0bea1df124b5e8cb00bf0adbd2faeccecd3b5c146796cbcb8b5b71b
%global appname cmakerc
Name: cmrc
Version: 2.0.1
Release:        1%{?dist}
License: MIT
Summary:        Standalone CMake-Based C++ Resource Compiler
URL: https://github.com/vector-of-bool/%{name}
Source0:        https://github.com/vector-of-bool/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch
Patch100: %{name}-installation.patch
Patch101: %{name}-cmake-compatibility.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description

%package devel
Summary: Standalone CMake-Based C++ Resource Compiler
Provides: %{appname} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{appname}-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTS:BOOL=ON
%cmake_build
%check

%ctest
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
