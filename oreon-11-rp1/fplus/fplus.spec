%global source0_hash 8864a3e9bebde6ebed71b49ac2a036cedf9ae0f02ce758bc28c21e6a2ae15803
%bcond_with test
%global debug_package %{nil}
Summary:        Functional Programming Library for C++
Name:           fplus
License:        BSL-1.0
Version:        0.2.28
Release:        1%{?dist}
URL:            https://github.com/Dobiasd/FunctionalPlus
Source0:        https://github.com/Dobiasd/FunctionalPlus/archive/v%{version}.tar.gz#/FunctionalPlus-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
FunctionalPlus is a small header-only library supporting you in
reducing code noise and in dealing with only one single level
of abstraction at a time. By increasing brevity and maintainability
of your code it can improve productivity (and fun!) in the long
run. It pursues these goals by providing pure and easy-to-use
functions that free you from implementing commonly used flows of
control over and over again.

%package devel
Summary:        Functional Programming Library for C++
Provides:       %{name}-static = %{version}-%{release}
%description devel
FunctionalPlus is a small header-only library supporting you in
reducing code noise and in dealing with only one single level
of abstraction at a time. By increasing brevity and maintainability
of your code it can improve productivity (and fun!) in the long
run. It pursues these goals by providing pure and easy-to-use
functions that free you from implementing commonly used flows of
control over and over again.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n FunctionalPlus-%{version}

# License check flags this as BSD 3-Clause
# api_search not distributed, remove to make license simpler
rm -rf api_search

%build

%cmake 
%cmake_build
%if %{with test}
%check

%ctest
%endif
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n fplus-devel -f %{oreon_filedir}/fplus-devel.list

%changelog

%autochangelog
