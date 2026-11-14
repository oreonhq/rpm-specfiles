# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 6000d8e8f0f9040426c4f85d7ad86789bc88d4aeaef585c4d4110adb0b214f21
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: xmlto
Version: 0.0.29
Release: 1%{?dist}
Summary: Convert XML documents to other formats
License: GPL-2.0-or-later
URL: https://pagure.io/xmlto
Source0: http://deb.debian.org/debian/pool/main/x/xmlto/xmlto_0.0.29.orig.tar.bz2

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gettext-devel
BuildRequires: flex
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: libxslt
BuildRequires: docbook-style-xsl
BuildRequires: docbook-dtds
Requires: libxslt
Requires: docbook-style-xsl
Requires: docbook-dtds

%description
xmlto runs an XSL stylesheet over an XML file. DocBook man pages use it.

%prep
%oreon_sha256
%autosetup -n xmlto-%{version}

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%check
%{buildroot}%{_bindir}/xmlto --help

%files
%license COPYING
%{_bindir}/xmlto
%{_bindir}/xmlif
%{_datadir}/xmlto/
%{_mandir}/man1/xmlto.1*
%{_mandir}/man1/xmlif.1*

%changelog
%autochangelog
