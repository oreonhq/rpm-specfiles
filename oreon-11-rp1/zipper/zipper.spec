%global source0_hash 4e8110904151196987322e606d3e6d580ff1d07ccab7a1b4457563343d548e6e

Name:           zipper
Summary:        C++ wrapper around minizip compression library
Version:        1.0.3
Release:        13%{?dist}
URL:            https://github.com/sebastiandev/zipper

## Source archive from github obtained by
## git clone -b v1.0.3 --depth 1 --single-branch --progress --recursive https://github.com/sebastiandev/zipper.git
## rm -rf zipper/.git*
## tar -czvf  zipper-1.0.3.tar.gz zipper
Source0:        https://github.com/sebastiandev/zipper/archive/zipper/%{name}-%{version}.tar.gz

#Patch0:         zipper-unbundle_minizip.patch
Patch1:         zipper-gcc14.patch

# zlib and GPL+ (no version) licenses come from minizip/ source code
License:        MIT AND ZLIB AND GPL-1.0-or-later

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(zlib)
#BuildRequires:  minizip-compat-devel
Provides: bundled(minizip) = 1.1

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

%autosetup -n %{name} -p1

%build
# TODO: remove CMAKE_POLICY_VERSION_MINIMUM if the new upstream source is used
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

%check
%ctest

%files
%doc README.md VERSION.txt
%license LICENSE.md
%{_libdir}/*.so.1
%{_libdir}/*.so.1.0.2

%files devel
%{_libdir}/*.so
%{_includedir}/zipper/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/*.cmake

%files static
%{_libdir}/libZipper.a
%{_libdir}/libZipper-static.a

%changelog
%autochangelog
