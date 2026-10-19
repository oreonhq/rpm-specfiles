%global source0_hash be8280124707701935e6294d366e2474158b758fa4b2e3cae571d5b256d2fe34
Name:           libsocketcan
Version:        0.0.12
Release:        10%{?dist}
Summary:        Library for SocketCAN
License:        LGPL-2.1-or-later
URL:            https://public.pengutronix.de/software/libsocketcan/
Source0:        https://public.pengutronix.de/software/%{name}//%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  pkgconfig
# /oreon:deps
%description
This library allows you to control some basic functions in socketcan
from userspace.

%package devel
Summary:        Development files for the SocketCAN library
Group:          Development/Libraries/C and C++
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This library allows you to control some basic functions in socketcan
from userspace.

This package contains the libsocketcan development files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

./autogen.sh
%configure --disable-static --docdir="%_docdir/%name"
%make_build
%install
%make_install
rm -rf "%buildroot/%_libdir"/*.la "%buildroot/%_docdir/%name"
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libsocketcan-devel -f %{oreon_filedir}/libsocketcan-devel.list

%changelog

%autochangelog
