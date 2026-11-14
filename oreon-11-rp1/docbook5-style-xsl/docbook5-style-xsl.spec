# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 316524ea444e53208a2fb90eeb676af755da96e1417835ba5f5eb719c81fa371

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}
%global xsldir %{_datadir}/sgml/docbook/xsl-ns-stylesheets

Name:           docbook5-style-xsl
Version:        1.79.2
Release:        1%{?dist}
Summary:        Norman Walsh's XSL stylesheets for DocBook 5
License:        DocBook-Stylesheet
URL:            https://github.com/docbook/xslt10-stylesheets
Source0:        https://github.com/docbook/xslt10-stylesheets/releases/download/release/%{version}/docbook-xsl-%{version}.tar.bz2
Source1:        catalog.xml
BuildArch:      noarch

BuildRequires:  oreon-rpm-macros
BuildRequires:  libxslt
BuildRequires:  libxml2

Requires:       libxml2
Requires:       libxslt
Provides:       docbook-xsl-ns = %{version}-%{release}

%description
These XSL stylesheets allow you to transform any DocBook 5 XML document to
other formats, such as HTML, FO, and XHTML. They also allow you to create
man pages from refentry documents.

%prep
%oreon_sha256
%autosetup -n docbook-xsl-%{version}
find . -name '*.jar' -delete
rm -rf tools docsrc tests

%build

%install
mkdir -p %{buildroot}%{xsldir}
cp -a common epub epub3 extensions eclipse fo highlighting html htmlhelp images javahelp lib manpages params profiling roundtrip slides template webhelp website xhtml xhtml-1_1 xhtml5 VERSION VERSION.xsl %{buildroot}%{xsldir}/
install -pm0644 %{SOURCE1} %{buildroot}%{xsldir}/catalog.xml
find %{buildroot}%{xsldir} -type f \( -name '*.py' -o -name '*.sh' \) -exec chmod 0644 {} +

%check
cat > refentry.xml <<'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<refentry xmlns="http://docbook.org/ns/docbook" version="5.0" xml:id="foo">
  <refmeta><refentrytitle>foo</refentrytitle><manvolnum>1</manvolnum></refmeta>
  <refnamediv><refname>foo</refname><refpurpose>does foo</refpurpose></refnamediv>
  <refsect1><title>Description</title><para>foo does foo.</para></refsect1>
</refentry>
EOF
xsltproc --nonet -o foo.1 %{buildroot}%{xsldir}/manpages/docbook.xsl refentry.xml
grep -q 'does foo' foo.1
xsltproc --nonet -o foo.html %{buildroot}%{xsldir}/xhtml/docbook.xsl refentry.xml
grep -q 'foo does foo' foo.html
rm -f foo.1
XML_CATALOG_FILES=%{buildroot}%{xsldir}/catalog.xml xsltproc http://docbook.sourceforge.net/release/xsl-ns/current/manpages/docbook.xsl refentry.xml
grep -q 'does foo' foo.1

%files
%license COPYING
%doc AUTHORS BUGS NEWS README RELEASE-NOTES.txt TODO
%{xsldir}/

%changelog
%autochangelog
