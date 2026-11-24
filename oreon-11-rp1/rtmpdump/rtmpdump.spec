# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 31b6a7ff7ce2dd5e79e6df84e33cbd27399781e21dc8154fd6b0ae82861679cd
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global commit 138fdb258d9fc26f1843fd1b891180416c9dc575
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20251114

Name:           rtmpdump
Version:        2.6
Release:        1%{?dist}
Summary:        Toolkit for RTMP streams

SourceLicense:  GPL-2.0-or-later AND LGPL-2.0-or-later
License:        GPL-2.0-or-later
URL:            https://rtmpdump.mplayerhq.hu/
Source0:        rtmpdump-%{version}.tar.gz
Patch0:         rtmpdump-nettle4.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  gnutls-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  make
BuildRequires:  nettle-devel
BuildRequires:  zlib-devel

Requires: librtmp%{?_isa} = %{version}-%{release}

%description
rtmpdump is a toolkit for RTMP streams. All forms of RTMP are supported,
including rtmp://, rtmpt://, rtmpe://, rtmpte://, and rtmps://.

%package -n librtmp
Summary:        Support library for RTMP streams
License:        LGPL-2.0-or-later

%description -n librtmp
librtmp is a support library for RTMP streams. All forms of RTMP are supported,
including rtmp://, rtmpt://, rtmpe://, rtmpte://, and rtmps://.

%package -n librtmp-devel
Summary:        Files for librtmp development
License:        LGPL-2.0-or-later
Requires:       librtmp%{?_isa} = %{version}-%{release}

%description -n librtmp-devel
librtmp is a support library for RTMP streams. The librtmp-devel package
contains include files needed to develop applications using librtmp.

%prep
%oreon_sha256
%autosetup -p1

%build
%make_build SYS=posix CRYPTO=GNUTLS SHARED=yes XCFLAGS="%{build_cflags}" XLDFLAGS="%{build_ldflags}"

%install
%make_install CRYPTO=GNUTLS SHARED=yes prefix=%{_prefix} mandir=%{_mandir} libdir=%{_libdir} sbindir=%{_sbindir} install
rm -v %{buildroot}%{_libdir}/librtmp.a

%files
%doc README
%license COPYING
%{_bindir}/rtmpdump
%{_sbindir}/rtmpsrv
%{_sbindir}/rtmpgw
%{_sbindir}/rtmpsuck
%{_mandir}/man1/rtmpdump.1*
%{_mandir}/man8/rtmpgw.8*

%files -n librtmp
%doc ChangeLog
%license librtmp/COPYING
%{_libdir}/librtmp.so.1

%files -n librtmp-devel
%{_includedir}/librtmp/
%{_libdir}/librtmp.so
%{_libdir}/pkgconfig/librtmp.pc
%{_mandir}/man3/librtmp.3*

%changelog
%autochangelog
