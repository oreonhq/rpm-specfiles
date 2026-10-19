%global source0_hash 174ebc4e769928959614789c5b4e9c3d0a0f81a62bb608756b127bfebfb21331
%global debug_package %{nil}
Name: doctest
Version: 2.5.3
Release:        1%{?dist}
Summary:        Feature-rich header-only C++ testing framework
License: MIT AND CC-BY-4.0 AND BSL-1.0 AND BSD-3-Clause
URL: https://github.com/doctest/%{name}
Source0:        https://github.com/%{name}/%{name}/archive/refs/tags/v%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git
# /oreon:deps
%description
A fast (both in compile times and runtime) C++ testing framework, with the
ability to write tests directly along production source (or in their own
source, if you prefer).

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: libstdc++-devel%{?_isa}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DDOCTEST_WITH_TESTS:BOOL=ON \
  %{nil}
%cmake_build
%check

%ctest
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n doctest-devel -f %{oreon_filedir}/doctest-devel.list

%changelog

%autochangelog
