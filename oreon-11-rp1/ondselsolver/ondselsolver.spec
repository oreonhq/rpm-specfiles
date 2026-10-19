%global source0_hash 890fb6ddeb1b42face95854689ff7b96c926c368b7d616d9e31e4b35f79ddde8
%global  commit       09d6175a2ba69e7016fcecc4f384946a2f84f92d
%global  shortcommit  09d6175
%global  commitdate   21012025
Name:           ondselsolver
Version:        1.0.1^%{commitdate}git%{shortcommit}
Release:        1%{?dist}
Summary:        Assembly Constraints and Multibody Dynamics code
License:        LGPL-2.1-only
URL:            https://github.com/FreeCAD/OndselSolver
VCS:            git:%{URL}.git
Source0:        https://github.com/FreeCAD/OndselSolver/archive/%{shortcommit}/OndselSolver-%{commit}.tar.gz
Patch:          packaged-gtest.patch
Patch:          https://github.com/gentoo/gentoo/blob/1896fac74ffa1cdb67fd9c9d3d85a618096c5d40/sci-libs/ondselsolver/files/ondselsolver-1.0.1-properly-demangle-typenames.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
# /oreon:deps
%description
Assembly Constraints and Multibody Dynamics code.

%package devel
Summary:  Development libraries and header files for libOndselSolver
Requires:  ondselsolver%{?isa} = %{version}-%{release}
%description devel
Development libraries and header files for libOndselSolver.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n OndselSolver-%{commit}

%build

%cmake -DONDSELSOLVER_BUILD_TESTS=ON \
       -DONDSELSOLVER_BUILD_EXE=ON \
       -DONDSELSOLVER_BUILD_SHARED=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

skip="${skip-}${skip+}OndselSolver.Gears|"
skip="${skip-}${skip+}OndselSolver.anglejoint|"
skip="${skip-}${skip+}OndselSolver.fourbot"
%ctest -E "${skip-}"
%files -f %{oreon_filedir}/main.list
%files -n ondselsolver-devel -f %{oreon_filedir}/ondselsolver-devel.list

%changelog

%autochangelog
