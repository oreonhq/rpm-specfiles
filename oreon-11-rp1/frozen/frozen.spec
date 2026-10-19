%global source0_hash ed8339c017d7c5fe019ac2c642477f435278f0dc643c1d69d3f3b1e95915e823
%global debug_package %{nil}
Name:           frozen
Version:        1.2.0
Release:        1%{?dist}
Summary:        A header-only, constexpr alternative to gperf for C++14 users
License:        Apache-2.0
URL:            https://github.com/serge-sans-paille/frozen
Source0:        https://github.com/serge-sans-paille/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
Header-only library that provides 0 cost initialization
for immutable containers, fixed-size containers, and
various algorithms.

%package devel
Summary:        Development files for %{name}
BuildArch:      noarch
Requires:       pkgconfig
Provides:       %{name}-static = %{version}-%{release}
%description devel
Development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build
%check

%ctest
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n frozen-devel -f %{oreon_filedir}/frozen-devel.list

%changelog

%autochangelog
