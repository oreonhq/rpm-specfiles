%global source0_hash 272692bb8324bf3a3a2e63e67fc040a64e4860aeea34353c040a281d70bec9f6
Name:		libzpc
Version:	1.5.0
Release:        1%{?dist}
Summary:        Open Source library for the IBM Z Protected-key crypto feature
License:	MIT
Url:		https://github.com/opencryptoki/libzpc
Source0:        https://github.com/opencryptoki/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:	s390x
%global soversion 1
# oreon:deps
BuildRequires:  cmake
BuildRequires:  g++
BuildRequires:  gcc
BuildRequires:  json-c-devel
BuildRequires:  make
# /oreon:deps
%description
The IBM Z Protected-key Crypto library libzpc is an open-source library
targeting the 64-bit Linux on IBM Z (s390x) platform. It provides interfaces
for cryptographic primitives. The underlying implementations make use of
z/Architecture's extensive performance-boosting hardware support and its
protected-key feature which ensures that key material is never present in
main memory at any time.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n libzpc-devel -f %{oreon_filedir}/libzpc-devel.list

%changelog

%autochangelog
