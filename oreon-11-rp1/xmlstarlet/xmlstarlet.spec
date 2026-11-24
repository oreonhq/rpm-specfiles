# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 75ff972c326e949951f084271f73382be7ac7c7da662ba7bf9691bd2fcf35624
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name: xmlstarlet
Version: 1.7.0
Release: 1%{?dist}
Summary: Command Line XML Toolkit
License: MIT
URL: http://xmlstarlet.github.io/
Source0: https://github.com/xmlstarlet/xmlstarlet/archive/%{version}/xmlstarlet-%{version}.tar.gz

Patch1: xmlstarlet-1.7.0-fix-xxe.patch

Patch2: xmlstarlet-1.7.0-docbook-nonet.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: make
BuildRequires: xmlto
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libxslt-devel
BuildRequires: libxml2-devel >= 2.6.23
Buildrequires: docbook-style-xsl

%description
XMLStarlet is a set of command line utilities which can be used
to transform, query, validate, and edit XML documents and files
using simple set of shell commands in similar way it is done for
plain text files using UNIX grep, sed, awk, diff, patch, join, etc
commands.

%prep
%oreon_sha256
%autosetup -p1

%build
autoreconf -i
%configure --disable-static-libs --with-libxml-include-prefix=%{_includedir}/libxml2 --docdir=%{_pkgdocdir} # --libdir=%{_libdir}
%make_build DOCBOOK_DIR="%{_datadir}/sgml/docbook/xsl-stylesheets"

%install
%make_install
mv %{buildroot}%{_bindir}/xml %{buildroot}%{_bindir}/xmlstarlet

%check
make check

%files
%doc AUTHORS ChangeLog NEWS README Copyright TODO
%doc %{_pkgdocdir}/*
%{_mandir}/man1/xmlstarlet.1*
%{_bindir}/xmlstarlet

%changelog
%autochangelog
