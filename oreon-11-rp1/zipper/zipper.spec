%global source0_hash 4e8110904151196987322e606d3e6d580ff1d07ccab7a1b4457563343d548e6e
Name:           zipper
Summary:        C++ wrapper around minizip compression library
Version:        1.0.3
Release:        1%{?dist}
URL:            https://github.com/sebastiandev/zipper
Source0:        https://github.com/sebastiandev/zipper/archive/zipper/%{name}-%{version}.tar.gz
Patch1:         zipper-gcc14.patch
License:        MIT AND ZLIB AND GPL-1.0-or-later
Provides: bundled(minizip) = 1.1
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
Zipper brings the power and simplicity of minizip to a more
object oriented/c++ user friendly library.
It was born out of the necessity of a compression library that would be
reliable, simple and flexible. 
By flexibility I mean supporting all kinds of inputs and outputs,
but specifically been able to compress into memory instead of been
restricted to file compression only, and using data from memory instead
of just files as well.

Features:
- Create zip in memory
- Allow files, vector and generic streams as input to zip
- File mappings for replacing strategies
  (overwrite if exists or use alternative name from mapping)
- Password protected zip
- Multi platform

%package devel
Summary: Development files of %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides header files, shared and static library files of %{name}.

%package static
Summary: Static library of %{name}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description static
This package provides static library file of %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -Wno-cpp -Wno-dev \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DBUILD_SHARED_VERSION:BOOL=ON -DBUILD_STATIC_VERSION:BOOL=ON \
 -DCMAKE_VERBOSE_MAKEFILE:BOOL=TRUE -DCMAKE_COLOR_MAKEFILE:BOOL=ON \
 -DCMAKE_SKIP_INSTALL_RPATH:BOOL=YES -DCMAKE_SKIP_RPATH:BOOL=YES \
 -DINSTALL_PKGCONFIG_DIR:PATH=%{_libdir}/pkgconfig \
 -DZLIB_INCLUDE_DIR:PATH=%{_includedir} -DZLIB_LIBRARY_RELEASE:FILEPATH=%{_libdir}/libz.so \
%if "%{?_lib}" == "lib64"
  %{?_cmake_lib_suffix64}
%endif
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{_bindir}/Zipper-test
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n zipper-devel -f %{oreon_filedir}/zipper-devel.list
%files -n zipper-static -f %{oreon_filedir}/zipper-static.list

%changelog

%autochangelog
