%global source0_hash 7e5ec6891254c8f00128952ed6b9a73d827539136c3b804563521a0042abe72c
%global debug_package %{nil}
Name:           cpp-jwt
Version:        1.5.1
Release:        1%{?dist}
Summary:        JSON Web Token library for C++
License:        MIT
URL:            https://github.com/arun11299/cpp-jwt
Source0:        https://github.com/arun11299/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  json-devel
BuildRequires:  openssl-devel
# /oreon:deps
%description

%package devel
Summary:        %{summary}
Recommends:     cmake
Provides:       %{name}-static = %{version}-%{release}
%description devel
%{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake # -DCPP_JWT_BUILD_EXAMPLES=OFF
%cmake_build
%check

%ctest
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
