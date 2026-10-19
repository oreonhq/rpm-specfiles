%global source0_hash e30c2aea5b66f53821d1eb971f81b9be1350e4b04a4577c8283803a1c8c5210b
Name: libphonenumber
Version: 9.0.39
Release:        1%{?dist}
Summary:        Library to handle international phone numbers
License: Apache-2.0 AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT
URL: https://github.com/google/libphonenumber/
Source0:        https://github.com/google/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:  libphonenumber-8.13.27-new-protobuf-cmake-logic.patch
%ifarch %{java_arches}
%endif
# oreon:deps
BuildRequires:  abseil-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  libicu-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  re2-devel
# /oreon:deps
%description
Google's common C++ library for parsing, formatting, storing and validating
international phone numbers.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: abseil-cpp-devel
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Gtest 1.13.0 requires at least C++14; C++17 matches how abseil-cpp is built;
# simply setting -DCMAKE_CXX_STANDARD=17 does not override this in practice.
sed -r -i 's/\b(CMAKE_CXX_STANDARD[[:blank:]]+)11\b/\117/' \
    cpp/CMakeLists.txt tools/cpp/CMakeLists.txt

sed -i 's/ -Werror//g'  cpp/CMakeLists.txt tools/cpp/CMakeLists.txt

%build

pushd cpp
%ifarch %{java_arches}
%cmake \
%else
touch src/phonenumbers/test_metadata.h
%cmake -DREGENERATE_METADATA=OFF \
%endif
    -DCMAKE_POSITION_INDEPENDENT_CODE=ON
%cmake_build
popd
%install
pushd cpp
%cmake_install
find %{buildroot} -name '*.a' -delete
find %{buildroot} -name '*.la' -delete
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libphonenumber-devel -f %{oreon_filedir}/libphonenumber-devel.list

%changelog

%autochangelog

%{_libdir}/libgeocoding.so
%{_libdir}/libphonenumber.so
