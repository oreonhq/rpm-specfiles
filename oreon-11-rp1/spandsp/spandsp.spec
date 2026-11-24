# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 3729c3c37cbaf4e619d4d2be8ed0074b3ef89d45949a2efcff85657f21250a20
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           spandsp
Summary:        A DSP library for telephony
Version:        0.0.6
Release:        23%{?pre:.pre%{pre}}%{?dist}
License:        LGPL-2.1-only AND GPL-2.0-only
URL:            https://www.soft-switch.org
Source0:	spandsp-%{version}%{?pre:pre%{pre}}-clean.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: make
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool

BuildRequires:  libxml2-devel
BuildRequires:  libtiff-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  doxygen
BuildRequires:  libxslt
BuildRequires:  docbook-style-xsl

%description
SpanDSP is a library of DSP functions for telephony, in the 8000
sample per second world of E1s, T1s, and higher order PCM channels. It
contains low level functions, such as basic filters. It also contains
higher level functions, such as cadenced supervisory tone detection,
and a complete software FAX machine. The software has been designed to
avoid intellectual property issues, using mature techniques where all
relevant patents have expired. See the file DueDiligence for important
information about these intellectual property issues.

%package devel
Summary:        SpanDSP development files
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       libtiff-devel%{?_isa}

%description devel
%{summary}.

%package apidoc
Summary:        SpanDSP API documentation

%description apidoc
%{summary}.

%prep
%oreon_sha256
%autosetup

%build
autoreconf -f -v -i
%configure --enable-doc --disable-static --disable-rpath
%make_build
find doc/api -type f | xargs touch -r configure

%install
%make_install
rm -vf %{buildroot}%{_libdir}/*.la
mkdir -p %{buildroot}%{_datadir}/%{name}

%ldconfig_scriptlets

%files
%license COPYING
%doc DueDiligence ChangeLog AUTHORS NEWS README
%{_libdir}/lib%{name}.so.*
%{_datadir}/%{name}/

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files apidoc
%doc doc/api/html/*

%changelog
%autochangelog
