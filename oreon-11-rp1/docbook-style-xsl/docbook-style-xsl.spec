# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ee8b9eca0b7a8f89075832a2da7534bce8c5478fc8fc2676f512d5d87d832102
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: docbook-style-xsl
Version: 1.79.2
Release: 1%{?dist}
Summary: DocBook XSL stylesheets
License: DocBook
URL: https://github.com/docbook/xslt10-stylesheets
Source0: https://github.com/docbook/xslt10-stylesheets/releases/download/release/%{version}/docbook-xsl-nons-%{version}.tar.bz2
BuildArch: noarch

BuildRequires: oreon-rpm-macros
Requires: docbook-dtds
Provides: docbook-xsl = %{version}-%{release}

%description
XSL stylesheets that turn DocBook XML into man pages and HTML.

%prep
%oreon_sha256
%autosetup -n docbook-xsl-nons-%{version}

%build

%install
mkdir -p %{buildroot}%{_datadir}/sgml/docbook/xsl-stylesheets
cp -a * %{buildroot}%{_datadir}/sgml/docbook/xsl-stylesheets/
mkdir -p %{buildroot}/etc/xml
cat > %{buildroot}/etc/xml/catalog <<'EOF'
<?xml version="1.0"?>
<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">
  <rewriteURI uriStartString="http://docbook.sourceforge.net/release/xsl/current" rewritePrefix="file:///usr/share/sgml/docbook/xsl-stylesheets"/>
  <rewriteSystem systemIdStartString="http://docbook.sourceforge.net/release/xsl/current" rewritePrefix="file:///usr/share/sgml/docbook/xsl-stylesheets"/>
  <rewriteURI uriStartString="http://docbook.sourceforge.net/release/xsl/1.79.2" rewritePrefix="file:///usr/share/sgml/docbook/xsl-stylesheets"/>
  <rewriteSystem systemIdStartString="http://docbook.sourceforge.net/release/xsl/1.79.2" rewritePrefix="file:///usr/share/sgml/docbook/xsl-stylesheets"/>
  <nextCatalog catalog="file:///usr/share/sgml/docbook/xsl-stylesheets/catalog.xml"/>
  <nextCatalog catalog="file:///usr/share/xml/docbook/xml-dtd-4.4/catalog.xml"/>
  <nextCatalog catalog="file:///usr/share/xml/docbook/xml-dtd-4.5/catalog.xml"/>
</catalog>
EOF

%files
/etc/xml/catalog
%{_datadir}/sgml/docbook/xsl-stylesheets/
