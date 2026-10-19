%global source0_hash d2ad4e64753a7c9843b766b8de8081d9c1d7acfaeb53c12b3aed7fdb9235766c
Name:           sofia-sip
Version:        1.13.18
Release:        1%{?dist}
Summary:        Sofia SIP User-Agent library
License:        LGPL-2.1-or-later
URL:            http://sofia-sip.sourceforge.net/
Source0:        https://github.com/freeswitch/%{name}/archive/refs/tags/v%{version}.tar.gz
Patch0:         0001-Fix-incompatible-pointer-type-in-sip_basic.c.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  libtool
BuildRequires:  lksctp-tools-devel
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
%description
Sofia SIP is a RFC-3261-compliant library for SIP user agents and
other network elements.  The Session Initiation Protocol (SIP) is an
application-layer control (signaling) protocol for creating,
modifying, and terminating sessions with one or more
participants. These sessions include Internet telephone calls,
multimedia distribution, and multimedia conferences.

%package devel
Summary:        Sofia-SIP Development Package
Requires:       sofia-sip = %{version}-%{release}
Requires:       pkgconfig
%description devel
Development package for Sofia SIP UA library.

%package glib
Summary:        Glib bindings for Sofia-SIP
Requires:       sofia-sip = %{version}-%{release}
%description glib
GLib interface to Sofia SIP User Agent library.

%package glib-devel
Summary:        Glib bindings for Sofia SIP development files
Requires:       sofia-sip-glib = %{version}-%{release}
Requires:       sofia-sip-devel = %{version}-%{release}
Requires:       pkgconfig
%description  glib-devel
Development package for Sofia SIP UA Glib library. This package
includes libraries and include files for developing glib programs
using Sofia SIP.

%package utils
Summary:        Sofia-SIP Command Line Utilities
Requires:       sofia-sip = %{version}-%{release}
%description utils
Command line utilities for the Sofia SIP UA library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

sh autogen.sh
%configure --disable-rpath --disable-static --without-doxygen --disable-stun
make %{?_smp_mflags}
%install
%make_install
find %{buildroot} -name \*.la -delete
find %{buildroot} -name \*.h.in -delete
find . -name installdox -delete
%ldconfig_scriptlets
%ldconfig_scriptlets glib
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n sofia-sip-devel -f %{oreon_filedir}/sofia-sip-devel.list
%files -n sofia-sip-glib -f %{oreon_filedir}/sofia-sip-glib.list
%files -n sofia-sip-glib-devel -f %{oreon_filedir}/sofia-sip-glib-devel.list
%files -n sofia-sip-utils -f %{oreon_filedir}/sofia-sip-utils.list

%changelog

%autochangelog
