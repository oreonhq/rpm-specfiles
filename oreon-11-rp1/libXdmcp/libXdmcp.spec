# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d8a5222828c3adab70adf69a5583f1d32eb5ece04304f7f8392b6a353aa2228c

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Summary: X Display Manager Control Protocol library
Name: libXdmcp
Version:        1.1.5
Release:        1%{?dist}
License: MIT-open-group
URL: http://www.x.org

Source0:        https://www.x.org/pub/individual/lib/libXdmcp-%{version}.tar.xz

BuildRequires: make
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: xorg-x11-proto-devel
BuildRequires: xmlto
BuildRequires:  oreon-rpm-macros

%description
X Display Manager Control Protocol library.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
libXdmcp development package.

%prep
%oreon_sha256

%autosetup

%build
autoreconf -v --install --force
%configure --disable-static
make V=1 %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# We intentionally don't ship *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# manual fixup later
rm -rf $RPM_BUILD_ROOT%{_docdir}

%ldconfig_post
%ldconfig_postun

%files
%doc AUTHORS COPYING ChangeLog Wraphelp.README.crypto
%{_libdir}/libXdmcp.so.6
%{_libdir}/libXdmcp.so.6.0.0

%files devel
%doc README.md
%{_includedir}/X11/Xdmcp.h
%{_libdir}/libXdmcp.so
%{_libdir}/pkgconfig/xdmcp.pc

