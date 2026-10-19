%global source0_hash a72ff7471eb8adf8470a21aec33d70f184a20e215f167e2d4c38d56d9a377205
%global debug_package %{nil}
Name:		msgpack
Version:	9.0.0
Release:        1%{?dist}
Summary:        Binary-based efficient object serialization library
License:	BSL-1.0
URL:		http://msgpack.org
Source0:        https://github.com/msgpack/msgpack-c/archive/refs/tags/cpp-%{version}.tar.gz
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
MessagePack is a binary-based efficient object serialization
library. It enables to exchange structured objects between many
languages like JSON. But unlike JSON, it is very fast and small.

%package devel
Summary:	Libraries and header files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
Libraries and header files for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n msgpack-c-cpp-%{version}

# gtest 1.17.0 requires at least C++17
sed -i "s|-std=c++98|-std=gnu++17|g" CMakeLists.txt

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} -Dlibdir=%{_libdir} -DBUILD_SHARED_LIBS=ON
%cmake_build
%check

export GTEST_FILTER=-object_with_zone.ext_empty
%ctest
cat %_vpath_builddir/Testing/Temporary/LastTest.log
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n msgpack-devel -f %{oreon_filedir}/msgpack-devel.list

%changelog

%autochangelog
