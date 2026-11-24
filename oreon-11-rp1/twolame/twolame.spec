# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash cc35424f6019a88c6f52570b63e1baf50f62963a3eac52a03a800bb070d7c87d
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:       twolame
Version:    0.4.0
Release:    1%{?dist}
Summary:    Optimized MPEG Audio Layer 2 encoding library based on tooLAME
License:    LGPL-2.1-or-later
URL:        http://www.twolame.org/

Source0:        http://downloads.sourceforge.net/twolame/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  pkgconfig(sndfile) >= 1.0.0

Requires:   %{name}-libs%{?_isa} = %{version}-%{release}

%description
TwoLAME is an optimized MPEG Audio Layer 2 (MP2) encoder. It should be able to
be used as a drop-in replacement for LAME (a MPEG Layer 3 encoder). The frontend
takes very similar command line options to LAME, and the backend library has a
very similar API to LAME.

This package contains the command line frontend.

%package libs
Summary:    TwoLAME is an optimized MPEG Audio Layer 2 encoding library based on tooLAME
%description libs
TwoLAME is an optimized MPEG Audio Layer 2 (MP2) encoder. It should be able to
be used as a drop-in replacement for LAME (a MPEG Layer 3 encoder). The frontend
takes very similar command line options to LAME, and the backend library has a
very similar API to LAME.

This package contains the shared library.

%package devel
Summary:    Development tools for TwoLAME applications
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and documentation needed to develop
applications with TwoLAME.

%prep
%oreon_sha256
%autosetup

%build
autoreconf -vif
%configure \
    --disable-static \
    --enable-sndfile
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/*.la

rm -rf %{buildroot}%{_docdir}

%if 0%{?rhel} == 7
%ldconfig_scriptlets libs
%endif

%files
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files libs
%license COPYING
%{_libdir}/lib%{name}.so.*

%files devel
%doc doc/api.txt doc/html doc/psycho.txt doc/vbr.txt
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h

%changelog
%autochangelog
