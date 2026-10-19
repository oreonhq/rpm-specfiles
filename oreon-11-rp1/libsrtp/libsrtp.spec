%global source0_hash ef5569220749529d778013aae1178391d972570a2b4f7288dda22effa875b07c
Name:		libsrtp
Version:	2.8.1
Release:        1%{?dist}
Summary:        An implementation of the Secure Real-time Transport Protocol (SRTP)
License:	BSD-3-Clause
URL:		https://github.com/cisco/libsrtp
Source0:        https://github.com/cisco/libsrtp/archive/refs/tags/v%{version}.tar.gz#/libsrtp-2.6.0.tar.gz
Provides:	libsrtp-tools = %{version}-%{release}
Obsoletes:	libsrtp-tools < 2.8.0-1
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  procps-ng
# /oreon:deps
%description
This package provides an implementation of the Secure Real-time
Transport Protocol (SRTP), the Universal Security Transform (UST), and
a supporting cryptographic kernel.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{version}

%build

%meson -Dcrypto-library=openssl -Dcrypto-library-kdf=disabled
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n libsrtp-devel -f %{oreon_filedir}/libsrtp-devel.list

%changelog

%autochangelog
