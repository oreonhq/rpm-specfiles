%global source0_hash 75afd9c1627846ed350253b0885a71207a0c2d52f350ded86daa5d18712bad93
%global debug_package %{nil}
%global forgeurl https://github.com/contour-terminal/boxed-cpp
Version:        1.4.3
%forgemeta
Name:           boxed-cpp
Release:        1%{?dist}
Summary:        Boxing primitive types in C++
License:        Apache-2.0
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  catch-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
%description    devel
The %{name}-devel package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%cmake -DBOXED_CPP_TESTS=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n boxed-cpp-devel -f %{oreon_filedir}/boxed-cpp-devel.list

%changelog

%autochangelog
