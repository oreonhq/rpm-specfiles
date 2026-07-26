%global source0_hash 14034c7ef571a93f2aca21b2280fa86b35ef5730541d3eb57557dd42d7cc506b

Name:           gnet2
Version:        2.0.8
Release:        36%{?dist}
Summary:        A simple network library built upon glib

License:        LGPL-2.0-or-later
URL:            http://www.gnetlibrary.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gnet/2.0/gnet-%{version}.tar.bz2
Patch1:         gnet2-2.0.8-build.patch

BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires: make

%description
GNet is a simple network library. It is written in C, object-oriented, and
built upon GLib. It is intended to be easy to use and port.

%package        devel
Summary:        Headers and libraries for building apps that use gnet2
Requires:       %{name} = %{version} glib2-devel

%description    devel
This package contains headers and libraries required to build applications that
use GNet 2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gnet-%{version}
%patch -P1 -p1 -b .build

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;

%ldconfig_scriptlets

%files
%doc AUTHORS BUGS COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
%doc HACKING
%{_datadir}/aclocal/*
%{_datadir}/gtk-doc/html/gnet
%{_includedir}/*
%{_libdir}/gnet-*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
%autochangelog
