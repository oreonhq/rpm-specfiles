# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 39cbd4f0efdfddc9755d88217e47f8f2d7108fa767f9d58a2ba26a16d8f7c910
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libshout
Version:        2.4.6
Release:        1%{?dist}
Summary:        Icecast source streaming library

License:        LGPL-2.0-or-later
URL:            https://www.icecast.org/
Source0:        https://downloads.us.xiph.org/releases/libshout/libshout-%{version}.tar.gz
Patch0:         libshout-2.4.3-Allow-disabling-ckport-database-installation.patch
Patch1:         libshout-2.4.3-Default-OpenSSL-cipher-list-is-PROFILE-SYSTEM.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(theora)
BuildRequires:  sed
BuildRequires: make

%description
libshout is a library for communicating with and sending data to an
icecast server.  It handles the socket connection, the timing of the
data, and prevents most bad data from getting to the icecast server.

%package        devel
Summary:        Header files for %{name} development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The libshout-devel package contains the header files needed for developing
applications that send data to an icecast server.  Install libshout-devel if
you want to develop applications using libshout.

%prep
%oreon_sha256
%setup -q
%patch -P0 -p1
%patch -P1 -p1
autoreconf -fi

%build
%configure \
  --disable-ckport \
  --enable-examples \
  --enable-pkgconfig \
  --disable-silent-rules \
  --enable-shared \
  --enable-speex \
  --disable-static \
  --enable-theora \
  --enable-thread

sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build

%install
%make_install

find $RPM_BUILD_ROOT -type f -name "*.la" -delete

rm -rf $RPM_BUILD_ROOT%{_docdir}

%files
%doc NEWS README
%license COPYING
%{_bindir}/shout
%{_libdir}/libshout.so.3
%{_libdir}/libshout.so.3.*
%{_mandir}/*/shout.*

%files devel
%doc examples/*.c doc/*.xml
%{_libdir}/libshout.so
%{_libdir}/pkgconfig/shout.pc
%{_includedir}/shout/
%{_datadir}/aclocal/shout.m4

%changelog
%autochangelog
