%global source0_hash 97e3819bdcffc3e4047b6ac57ca14e04af85380bd93afe314bee9dd5c7f46a0a
Name: curlpp
Version: 0.8.1
Release:        1%{?dist}
Summary:        A C++ wrapper for libcURL
License: MIT
URL: http://curlpp.org/
Source0:        https://github.com/jpbarrette/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: curlpp-0.8.1-fix-curloption.patch
Patch1: curlpp-0.8.1-fix-pkgconfig.patch
Patch2: curlpp-0.8.1-cmake_minimum.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  gcc-c++
# /oreon:deps
%description
cURLpp is a C++ wrapper for libcURL.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: boost-devel
Requires: curl-devel
Requires: pkgconfig
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

# Convert CRLF line endings to LF in the examples
for file in examples/*.cpp
do
	sed 's/\r//' $file > $file.new && \
	touch -r $file $file.new && \
	mv $file.new $file
done

# remove deps on global.h which in turn pulls in config.h
sed -i '28 d' include/curlpp/Types.hpp

# unexport private build flags
sed -i 's/ @LDFLAGS@//; s/ @CURLPP_CXXFLAGS@//;' \
  extras/curlpp.pc.in \
  extras/curlpp-config.in

%build

%cmake CMAKE_C_FLAGS="%{optflags}" -Wno-dev .
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/*.a
%ldconfig_scriptlets
%oreon_autofiles curlpp-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

ctest -V %{?_smp_mflags}
%files -f %{oreon_filedir}/main.list
%files -n curlpp-devel -f %{oreon_filedir}/curlpp-devel.list

%changelog

%autochangelog
