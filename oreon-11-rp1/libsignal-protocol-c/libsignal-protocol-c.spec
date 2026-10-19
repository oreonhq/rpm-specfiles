%global source0_hash c22e7690546e24d46210ca92dd808f17c3102e1344cd2f9a370136a96d22319d
Name:       libsignal-protocol-c
Version:    2.3.3
Release:        1%{?dist}
License:    GPL-3.0-only
Summary:        Signal Protocol C library
URL:        https://github.com/signalapp/libsignal-protocol-c
Source0:        https://github.com/signalapp/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:     0001-CVE-2022-48468-unsigned-integer-overflow.patch
Provides: bundled(protobuf-c) = 1.1.1
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
# /oreon:deps
%description
This is a ratcheting forward secrecy protocol that works in synchronous
and asynchronous messaging environments.

%package devel
Summary:    Development files for libsignal-protocol-c
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for libsignal-protocol-c.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake -DCMAKE_BUILD_TYPE=Debug .
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

ctest -V %{?_smp_mflags}
%files -f %{oreon_filedir}/main.list
%files -n libsignal-protocol-c-devel -f %{oreon_filedir}/libsignal-protocol-c-devel.list

%changelog

%autochangelog
