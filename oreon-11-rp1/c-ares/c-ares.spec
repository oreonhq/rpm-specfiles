%global source0_hash c222b6d681096f9444d2c4863d2c1174019e27cacca0a4a5c114d36dd7d7bf78
%global use_cmake 1
Summary:        A library that performs asynchronous DNS operations
Name: c-ares
Version: 1.34.8
Release:        1%{?dist}
License: MIT
URL: http://c-ares.org/
Source0:        https://github.com/c-ares/c-ares/releases/download/v%{version}/c-ares-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

%package devel
Summary: Development files for c-ares
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the header files and libraries needed to
compile applications or shared objects that use c-ares.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%{cmake} -DCARES_BUILD_TOOLS:BOOL=OFF
%cmake_build
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles c-ares-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n c-ares-devel -f %{oreon_filedir}/c-ares-devel.list

%changelog

%autochangelog
