%global source0_hash 6dde6419963965757167ed7c25ef437193f0992ddfd9172dfec39f31901837d3
Name: docbook-simple
Version: 1.1
Release:        1%{?dist}
Summary:        Simplified DocBook is a small subset of the DocBook XML DTD
License: DocBook-DTD
URL: http://www.oasis-open.org/docbook/xml/simple/
Source0:        http://www.docbook.org/xml/simple/1.1/%{name}-%{version}.zip
Source1: %{name}.README.redhat
Source2: %{name}.xml
Source3: %{name}.cat
BuildArch: noarch
Requires: sgml-common
Requires(post): sed
Requires(post): libxml2 >= 2.4.8
Requires(postun): libxml2 >= 2.4.8
Requires: docbook-dtds
# oreon:deps
BuildRequires:  unzip
# /oreon:deps
%description
Simplified DocBook is an attempt to provide a proper subset of DocBook
that is simultaneously smaller and still useful. Documents written in
the subset must be 100% legal DocBook documents. This is a subset for
single documents (articles, white papers, etc.), so there's no need
for books or sets, just 'articles'. Simplified DocBook documents are 
viewable in online browsers if styled with CSS. (it's XML not SGML).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# splatter the files into a version-numbered directory
%setup -q -c -n %{version}

# see http://rpm-devel.colug.net/max-rpm/s1-rpm-inside-macros.html
# setup -c creates the dir then changes to it to expand SOURCE0

%build

%install
rm -rf $RPM_BUILD_ROOT
DESTDIR=$RPM_BUILD_ROOT%{_datadir}/xml/docbook/simple
mkdir -p $DESTDIR
cp -a ../%{version} $DESTDIR
XML_CAT_DIR=$RPM_BUILD_ROOT%{_sysconfdir}/xml
mkdir -p $XML_CAT_DIR
install -p -m 644 %{SOURCE2} $XML_CAT_DIR
SGML_CAT_DIR=$RPM_BUILD_ROOT%{_sysconfdir}/sgml
mkdir -p $SGML_CAT_DIR
install -p -m 644 %{SOURCE3} $SGML_CAT_DIR
cp -p %{SOURCE1} ./README
%clean
rm -rf $RPM_BUILD_ROOT
rm -rf ../%{version}
%oreon_autofiles main

%post

ROOT_XML_CATALOG=%{_sysconfdir}/xml/catalog
PKG_XML_CATALOG=%{_sysconfdir}/xml/docbook-simple.xml
if [ -w $ROOT_XML_CATALOG ]
then
        %{_bindir}/xmlcatalog --noout --add "delegatePublic" \
                "-//OASIS//DTD Simplified" \
                "file://$PKG_XML_CATALOG" $ROOT_XML_CATALOG
        %{_bindir}/xmlcatalog --noout --add "delegateURI" \
                "http://www.oasis-open.org/docbook/xml/simple/1.1/" \
                "file://$PKG_XML_CATALOG" $ROOT_XML_CATALOG
        %{_bindir}/xmlcatalog --noout --add "delegateSystem" \
                "http://www.oasis-open.org/docbook/xml/simple/1.1/" \
                "file://$PKG_XML_CATALOG" $ROOT_XML_CATALOG
fi
ROOT_SGML_CATALOG=%{_sysconfdir}/sgml/catalog
PKG_SGML_CATALOG=%{_sysconfdir}/sgml/docbook-simple.cat
if [ -w $ROOT_SGML_CATALOG ]
then
  install-catalog --add \
  "$PKG_SGML_CATALOG" \
  "$ROOT_SGML_CATALOG" 1>/dev/null
  sed -i '/^CATALOG.*log\"$/d' $PKG_SGML_CATALOG
  sed -i '/^CATALOG.*log$/d' $PKG_SGML_CATALOG   
fi
/bin/chmod a+r  %{_sysconfdir}/sgml/*
/bin/chmod a+r  %{_sysconfdir}/xml/*
%postun

if [ "$1" = 0 ]; then
  %{_bindir}/xmlcatalog --sgml --noout --del \
     %{_sysconfdir}/sgml/catalog \
     %{_sysconfdir}/sgml/docbook-simple.cat
  %{_bindir}/xmlcatalog --noout --del \
    "file://%{_sysconfdir}/xml/docbook-simple.xml" \
     %{_sysconfdir}/xml/catalog 
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
