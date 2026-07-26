%global source0_hash be8280124707701935e6294d366e2474158b758fa4b2e3cae571d5b256d2fe34

Name:           libsocketcan
Version:        0.0.12
Release:        10%{?dist}
Summary:        Library for SocketCAN

License:        LGPL-2.1-or-later
URL:            https://public.pengutronix.de/software/libsocketcan/
Source0:        %{url}/%name-%version.tar.bz2

BuildRequires:  gcc
BuildRequires:  autoconf >= 2.69
BuildRequires:  automake
BuildRequires:  libtool >= 2
BuildRequires:  pkgconfig

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

%autosetup

%build
./autogen.sh
%configure --disable-static --docdir="%_docdir/%name"
%make_build

%install
%make_install
rm -rf "%buildroot/%_libdir"/*.la "%buildroot/%_docdir/%name"

%files
%doc README
%_libdir/libsocketcan.so.2*
%license LICENSE

%files devel
%_includedir/can_netlink.h
%_includedir/libsocketcan.h
%_libdir/libsocketcan.so
%_libdir/pkgconfig/libsocketcan.pc

%changelog
%autochangelog
