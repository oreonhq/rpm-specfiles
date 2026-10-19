%global source0_hash 6d5664b63538d4fe752defab1fe5892c01e179d6261ab25d79afbe6237118042
%define pkg docbook-slides
Summary:        DocBook Slides document type and stylesheets
Name: docbook-slides
Version: 3.4.0
Release:        1%{?dist}
License: MIT
URL: http://sourceforge.net/projects/docbook
Source0:        http://downloads.sourceforge.net/docbook/%{name}-%{version}.tar.gz
Source1: %{name}.xml
Source2: %{name}.cat
Source3: %{name}.README.redhat
Source4: %{name}-tests.tar.gz
BuildArch: noarch
Requires: docbook-dtds
Requires: docbook-xsl
Requires: docbook-simple
Requires: sgml-common
Requires(post): sed
Requires(post): libxml2 >= 2.4.8
Requires(postun): libxml2 >= 2.4.8
# oreon:deps

# /oreon:deps
%description
DocBook Slides provides customization layers of the both the
Simplified and the full DocBook XML DTD, as well as the DocBook XSL
Stylesheets. This package contains the XML document type definition
and stylesheets for processing DocBook Slides XML. The slides doctype
and stylesheets are for generating presentations, primarily in HTML.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkg}-%{version}
tar xf %{SOURCE4}

%build

%install
rm -rf $RPM_BUILD_ROOT
DESTDIR=$RPM_BUILD_ROOT%{_datadir}/xml/docbook/slides/%{version}
mkdir -p $DESTDIR
cp -a browser $DESTDIR
cp -a graphics $DESTDIR
cp -a schema $DESTDIR
cp -a xsl $DESTDIR
cp -a VERSION $DESTDIR
cp -a catalog.xml $DESTDIR
XML_CAT_DIR=$RPM_BUILD_ROOT%{_sysconfdir}/xml
mkdir -p $XML_CAT_DIR
install -p -m 644 %{SOURCE1} $XML_CAT_DIR
SGML_CAT_DIR=$RPM_BUILD_ROOT%{_sysconfdir}/sgml
mkdir -p $SGML_CAT_DIR
install -p -m 644 %{SOURCE2} $SGML_CAT_DIR
cp -p %{SOURCE3} ./README2
%oreon_autofiles main

%post

ROOT_XML_CATALOG=%{_sysconfdir}/xml/catalog
PKG_XML_CATALOG=%{_sysconfdir}/xml/docbook-slides.xml
if [ -w $ROOTCATALOG ]
then
        %{_bindir}/xmlcatalog --noout --add "delegatePublic" \
                "-//Norman Walsh//DTD Slides" \
                "file://$PKG_XML_CATALOG" $ROOT_XML_CATALOG
        %{_bindir}/xmlcatalog --noout --add "delegateSystem" \
                "http://docbook.sourceforge.net/release/slides" \
                "file://$PKG_XML_CATALOG" $ROOT_XML_CATALOG
        %{_bindir}/xmlcatalog --noout --add "delegateURI" \
                "http://docbook.sourceforge.net/release/slides" \
                "file://$PKG_XML_CATALOG" $ROOT_XML_CATALOG
fi
ROOT_SGML_CATALOG=%{_sysconfdir}/sgml/catalog
PKG_SGML_CATALOG=%{_sysconfdir}/sgml/docbook-slides.cat
if [ -w $ROOT_SGML_CATALOG ]
then
  install-catalog --add \
  $PKG_SGML_CATALOG \
  $ROOT_SGML_CATALOG 1>/dev/null
  sed -i '/^CATALOG.*log\"$/d' $PKG_SGML_CATALOG
  sed -i '/^CATALOG.*log$/d' $PKG_SGML_CATALOG
fi
/bin/chmod a+r %{_sysconfdir}/sgml/*
/bin/chmod a+r %{_sysconfdir}/xml/*
%postun

if [ "$1" = 0 ]; then
  %{_bindir}/xmlcatalog --sgml --noout --del \
    %{_sysconfdir}/sgml/catalog \
    "%{_sysconfdir}/sgml/docbook-slides.cat"
  %{_bindir}/xmlcatalog --noout --del \
    "file://%{_sysconfdir}/xml/docbook-slides.xml" \
    %{_sysconfdir}/xml/catalog
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
