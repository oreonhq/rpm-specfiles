%global source0_hash 0fff4ff311a7c88fdb76fceefba0e180232d56984f577db371d505e4d4c91afd
%global debug_package %{nil}
Name:           cppzmq
Version:        4.11.0
Release:        1%{?dist}
Summary:        Header-only C++ binding for libzmq
License:        MIT
URL:            https://zeromq.org
Source0:        https://github.com/zeromq/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  (cmake(Catch2) >= 2.13.9 with cmake(Catch2) < 3)
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libzmq)
# /oreon:deps
%description

%package devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}
Requires:       pkgconfig(libzmq)
%description devel

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
