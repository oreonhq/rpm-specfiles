%global source0_hash 50558ad423e6ba0e805313a4a07a4eba437053bd4e74d67252fb447589b3bde9
%global debug_package %{nil}
Name:           libheinz
Version:        4.1.0
Release:        1%{?dist}
Summary:        C++ base library of Heinz Maier-Leibnitz Zentrum
License:        0BSD
URL:            https://jugit.fz-juelich.de/mlz/libheinz
Source0:        https://jugit.fz-juelich.de/mlz/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
It is a header-only C++ base library of Heinz Maier-Leibnitz Zentrum, which
provides several generic utilities for use in several products of the Scientific
Computing Group.

Contents:
- [Complex.h](inc/heinz/Complex.h). Defines `complex_t`, and a few elementary
functions.
- [Vectors3D.h](inc/heinz/Vectors3D.h). Templated 3D vectors, and abbreviations
`I3`, `R3`, `C3`.
- [Rotations3D.h](inc/heinz/Rotations3D.h). SO3 rotations, internally
parameterized by quaternions.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-v%{version}

sed -i 's|lib/cmake|%{_libdir}/cmake|g' CMakeLists.txt

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n libheinz-devel -f %{oreon_filedir}/libheinz-devel.list

%changelog

%autochangelog
