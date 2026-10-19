%global source0_hash 3bfc70542c521d4b55a46429d808178916a579b28d048bd8c727ee76c39e2072
%global debug_package %{nil}
Name: cxxopts
Version: 3.3.1
Release:        1%{?dist}
Summary:        Lightweight C++ command line option parser
License: MIT
URL: https://github.com/jarro2783/%{name}
Source0:        https://github.com/jarro2783/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description
CXXOpts is a lightweight C++ option parser library, supporting the standard
GNU style syntax for options.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: libstdc++-devel%{?_isa}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCXXOPTS_ENABLE_INSTALL:BOOL=ON \
    -DCXXOPTS_ENABLE_WARNINGS:BOOL=OFF \
    -DCXXOPTS_BUILD_EXAMPLES:BOOL=ON \
    -DCXXOPTS_BUILD_TESTS:BOOL=ON
%cmake_build
%check

%ctest
%install
%cmake_install
%oreon_autofiles cxxopts-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n cxxopts-devel -f %{oreon_filedir}/cxxopts-devel.list

%changelog

%autochangelog
