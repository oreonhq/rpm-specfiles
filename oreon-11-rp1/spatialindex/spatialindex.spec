%global source0_hash c59932395e98896038d59199f2e2453595df6d730ffbe09d69df2a661bcb619b
Name:      spatialindex
Version:   2.1.0
Release:        4%{?dist}
%global so_version 8
Summary:        Spatial index library
License:   MIT
URL:       https://libspatialindex.org
Source0:        https://github.com/libspatialindex/libspatialindex/releases/download/%{version}/%{name}-src-%{version}.tar.bz2
Patch:          https://github.com/libspatialindex/libspatialindex/pull/270.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(GTest)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
Spatialindex provides a general framework for developing spatial indices.
Currently it defines generic interfaces, provides simple main memory and
disk based storage managers and a robust implementation of an R*-tree,
an MVR-tree and a TPR-tree.

%package devel
Summary: Development files for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-src-%{version} -p1
# Remove bundled gtest:
rm -rv test/gtest/gtest-*

%conf
# Since https://src.fedoraproject.org/rpms/cmake/pull-request/45 in Fedora 43,
# the expansion of %%cmake no longer overrides INCLUDE_INSTALL_DIR and
# LIB_INSTALL_DIR, which don’t mean exactly the same thing here as they do in
# whatever historical convention %%cmake was trying to support. See discussion
# in https://github.com/libspatialindex/libspatialindex/issues/271. However, we
# retain the workaround of undefining them in case this version of the spec
# file is branched to EPEL10.
#
# GTest >=1.17 requires C++17 (-DCMAKE_CXX_STANDARD=17).
%cmake \
    -DBUILD_TESTING:BOOL=ON \
    -DSYSTEM_GTEST:BOOL=ON \
    -UINCLUDE_INSTALL_DIR -ULIB_INSTALL_DIR \
    -DCMAKE_CXX_STANDARD=17

%build

%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n spatialindex-devel -f %{oreon_filedir}/spatialindex-devel.list

%changelog

%autochangelog
