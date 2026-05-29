%global source0_hash 7dc418c1d361123ffc5e45d61f1b97257940a8eb35d0bfbbc493381cc5b1f959

%global xmlxsdver 2009/01

Name: sgml-common
Version: 0.6.3
Release: 67%{?dist}

Summary: Common SGML catalog and DTD files

License: GPL-1.0-or-later

BuildArch: noarch

#Actually - there is no homepage of this project, on that URL
#page you could get complete ISO 8879 listing as was on the
#old page - only part of it is included in sgml-common package.
URL: https://www.w3.org/2003/entities/

Source0:        https://www.sourceware.org/pub/docbook-tools/new-trials/SOURCES/sgml-common-0.6.3.tgz
# Following 4 from openjade/pubtext - same maintainer as in SGML-common, so up2date:
Source1: xml.dcl
Source2: xml.soc
Source3: html.dcl
Source4: html.soc
Source5:        http://www.w3.org/2009/01/xml.xsd
Source6: http://www.w3.org/TR/xmldsig-core/xmldsig-core-schema.xsd
Source7: http://www.w3.org/2001/XMLSchema.dtd
Source8: http://www.w3.org/2001/datatypes.dtd
Source9: sgmlwhich.1
Source10: sgml.conf.5

Patch0: sgml-common-umask.patch
Patch1: sgml-common-xmldir.patch
Patch2: sgml-common-quotes.patch

BuildRequires: make
BuildRequires: libxml2
BuildRequires: automake
Requires: %{_bindir}/basename

%description
The sgml-common package contains a collection of entities and DTDs
that are useful for processing SGML, but that don't need to be
included in multiple packages.  Sgml-common also includes an
up-to-date Open Catalog file.

%package -n xml-common
Summary: Common XML catalog and DTD files
License: GPL-1.0-or-later
Requires(pre): %{_bindir}/xmlcatalog

%description -n xml-common
The xml-common is a subpackage of sgml-common which contains
a collection XML catalogs that are useful for processing XML,
but that don't need to be included in main package.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q
%patch -P0 -p1 -b .umask
%patch -P1 -p1 -b .xmldir
%patch -P2 -p1 -b .quotes

# replace bogus links with files
automakedir=`ls -1d /usr/share/automake* | head -n +1`
for file in COPYING INSTALL install-sh missing mkinstalldirs; do
   rm $file
   cp -p $automakedir/$file .
done

%build
%configure

%install
%make_install htmldir='%{_datadir}/doc'
mkdir $RPM_BUILD_ROOT%{_sysconfdir}/xml
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sgml/docbook
mkdir -p $RPM_BUILD_ROOT%{_datadir}/sgml/docbook
# Touch SGML catalog
touch $RPM_BUILD_ROOT%{_sysconfdir}/sgml/catalog
# Create an empty XML catalog.
XMLCATALOG=$RPM_BUILD_ROOT%{_sysconfdir}/xml/catalog
%{_bindir}/xmlcatalog --noout --create $XMLCATALOG
# ...and add xml.xsd in it
for type in system uri ; do
	for path in 2001 %{xmlxsdver} ; do
		%{_bindir}/xmlcatalog --noout --add $type \
			"http://www.w3.org/$path/xml.xsd" \
			"file://%{_datadir}/xml/xml.xsd" $XMLCATALOG
	done
	# Add xmldsig-core-schema.xsd to catalog
	%{_bindir}/xmlcatalog --noout --add $type \
		"http://www.w3.org/TR/xmldsig-core/xmldsig-core-schema.xsd" \
		"file://%{_datadir}/xml/xmldsig-core-schema.xsd" $XMLCATALOG
done
# Now put the common DocBook entries in it
%{_bindir}/xmlcatalog --noout --add "delegatePublic" \
	"-//OASIS//ENTITIES DocBook XML" \
	"file://%{_sysconfdir}/sgml/docbook/xmlcatalog" $XMLCATALOG
%{_bindir}/xmlcatalog --noout --add "delegatePublic" \
	"-//OASIS//DTD DocBook XML" \
	"file://%{_sysconfdir}/sgml/docbook/xmlcatalog" $XMLCATALOG
%{_bindir}/xmlcatalog --noout --add "delegatePublic" \
	"ISO 8879:1986" \
	"file://%{_sysconfdir}/sgml/docbook/xmlcatalog" $XMLCATALOG
%{_bindir}/xmlcatalog --noout --add "delegateSystem" \
	"http://www.oasis-open.org/docbook/" \
	"file://%{_sysconfdir}/sgml/docbook/xmlcatalog" $XMLCATALOG
%{_bindir}/xmlcatalog --noout --add "delegateURI" \
	"http://www.oasis-open.org/docbook/" \
	"file://%{_sysconfdir}/sgml/docbook/xmlcatalog" $XMLCATALOG
for public in "-//W3C//DTD XMLSchema 200102//EN" "-//W3C//DTD XMLSCHEMA 200102//EN" ; do
	%{_bindir}/xmlcatalog --noout --add "public" \
		"$public" \
		"file://%{_datadir}/xml/XMLSchema.dtd" $XMLCATALOG
done
%{_bindir}/xmlcatalog --noout --add "system" \
	"http://www.w3.org/2001/XMLSchema.dtd" \
	"file://%{_datadir}/xml/XMLSchema.dtd" $XMLCATALOG

# Also create the common DocBook catalog
%{_bindir}/xmlcatalog --noout --create \
	$RPM_BUILD_ROOT%{_sysconfdir}/sgml/docbook/xmlcatalog
ln -sf %{_sysconfdir}/sgml/docbook/xmlcatalog\
	$RPM_BUILD_ROOT%{_datadir}/sgml/docbook/xmlcatalog

rm -f $RPM_BUILD_ROOT%{_datadir}/sgml/xml.dcl
install -p -m0644 %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} \
	$RPM_BUILD_ROOT%{_datadir}/sgml
rm -rf $RPM_BUILD_ROOT%{_datadir}/xml/*
install -p -m0644 %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} \
	$RPM_BUILD_ROOT%{_datadir}/xml
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man5
install -p -m0644 %{SOURCE9} $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m0644 %{SOURCE10} $RPM_BUILD_ROOT%{_mandir}/man5

# remove installed doc file and prepare installation with %%doc
rm $RPM_BUILD_ROOT%{_datadir}/doc/*.html
rm -rf __dist_doc/html/
mkdir -p __dist_doc/html/
cp -p doc/HTML/*.html __dist_doc/html/


%pre -n xml-common
if [ $1 -gt 1 ] && [ -e %{_sysconfdir}/xml/catalog ]; then
	for type in system uri ; do
		for path in 2001 %{xmlxsdver} ; do
			%{_bindir}/xmlcatalog --noout --add $type \
				"http://www.w3.org/$path/xml.xsd" \
				"file://%{_datadir}/xml/xml.xsd" \
				%{_sysconfdir}/xml/catalog
		done
		%{_bindir}/xmlcatalog --noout --add $type \
			"http://www.w3.org/TR/xmldsig-core/xmldsig-core-schema.xsd" \
			"file://%{_datadir}/xml/xmldsig-core-schema.xsd" %{_sysconfdir}/xml/catalog
	done
	for public in "-//W3C//DTD XMLSchema 200102//EN" "-//W3C//DTD XMLSCHEMA 200102//EN" ; do
		%{_bindir}/xmlcatalog --noout --add "public" \
			"$public" \
			"file://%{_datadir}/xml/XMLSchema.dtd" %{_sysconfdir}/xml/catalog
	done
fi

%files
%doc __dist_doc/html/ AUTHORS NEWS ChangeLog COPYING README
%dir %{_sysconfdir}/sgml
%config(noreplace) %{_sysconfdir}/sgml/sgml.conf
%ghost %verify(not md5 size mtime) %config(noreplace,missingok) %{_sysconfdir}/sgml/catalog
%dir %{_datadir}/sgml
%dir %{_datadir}/sgml/sgml-iso-entities-8879.1986
%{_datadir}/sgml/sgml-iso-entities-8879.1986/*
%{_datadir}/sgml/xml.dcl
%{_datadir}/sgml/xml.soc
%{_datadir}/sgml/html.dcl
%{_datadir}/sgml/html.soc
%{_bindir}/sgmlwhich
%{_bindir}/install-catalog
%{_mandir}/man8/install-catalog.8*
%{_mandir}/man1/sgmlwhich.1*
%{_mandir}/man5/sgml.conf.5*

%files -n xml-common
%doc AUTHORS NEWS ChangeLog COPYING README
%dir %{_sysconfdir}/xml
%dir %{_sysconfdir}/sgml
%dir %{_sysconfdir}/sgml/docbook
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/xml/catalog
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/sgml/docbook/xmlcatalog
%dir %{_datadir}/sgml
%dir %{_datadir}/sgml/docbook
%{_datadir}/sgml/docbook/xmlcatalog
%dir %{_datadir}/xml
%{_datadir}/xml/xml.xsd
%{_datadir}/xml/xmldsig-core-schema.xsd
%{_datadir}/xml/XMLSchema.dtd
%{_datadir}/xml/datatypes.dtd

%changelog
* Sat Apr 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.3-67
- Prepare for Oreon 11 (RP1)
