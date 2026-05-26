# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 3dcd65e1f5d9c0c891b3be204fa2bb418ce485d32310e1ca052e81d36623208e
%global source1_sha256 b3f3413654003c1e773360d7fc60ebb8abd0e8c9af8e7d6c4b55f124f34d1e7f
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })} \
%{?source1_sha256:%(test -z "%{source1_sha256}" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_sha256}" || { echo "oreon: Source1 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name: docbook5-schemas
Version: 5.1
Release: 17%{?dist}

Summary: Norman Walsh's schemas (DTD, Relax NG, W3C schema) for Docbook 5.X

License: LicenseRef-OASIS-spec AND DocBook-Stylesheet AND LicenseRef-Fedora-UltraPermissive
URL: http://www.oasis-open.org/docbook/

Provides: docbook5-dtd = %{version}-%{release}
Provides: docbook5-rng = %{version}-%{release}
Provides: docbook5-sch = %{version}-%{release}
Provides: docbook5-xsd = %{version}-%{release}

Requires(post): libxml2 >= 2.4.8
Requires(postun): libxml2 >= 2.4.8
Requires: xml-common >= 0.6.3-24
BuildRequires: perl-generators
BuildRequires: unzip
BuildRequires: libxml2 >= 2.4.8

BuildArch: noarch

Source0:  https://archive.docbook.org/xml/5.0/docbook-5.0.zip
Source1:  https://archive.docbook.org/xml/5.1/docbook-v5.1-os.zip

%description
Docbook 5.X is a complete rewrite of Docbook in RELAX NG and not compatible
with previous Docbook versions. This package contains Relax NG , DTD and W3C
schema for Docbook 5.X. Syntax of those schemas is XML-compliant and is
developed by the OASIS consortium.

%prep
%oreon_verify_sources
%setup -c -T 
mkdir 5.0
mkdir 5.1

# Unzip Docbook 5.0 specification
cd 5.0
unzip %{SOURCE0}
mv docbook-5.0/* .

# Remove howto docs
rm docs/howto.html
rm docs/howto.pdf
rm docs/howto.xml
rm -rf docs/images/*

# Prepare docs to right place
mv docs/ ../
mv README ../
mv ChangeLog ../
cd ..

# Unzip Docbook 5.1 specification
cd 5.1
unzip %{SOURCE1}
mv schemas/rng .
mv schemas/sch .
mv schemas/catalog.xml .
mv schemas/docbook.nvdl .
cd ..

%build
CATALOG=docbook-5.xml
%{_bindir}/xmlcatalog --create --noout $CATALOG
for v in 5.0
do
  # DTD
  %{_bindir}/xmlcatalog --noout --add "public" \
     "-//OASIS//DTD DocBook XML ${v}//EN" \
     "file://%{_datadir}/xml/docbook5/schema/dtd/${v}/docbook.dtd" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "system" \
     "http://www.oasis-open.org/docbook/xml/${v}/dtd/docbook.dtd" \
     "file://%{_datadir}/xml/docbook5/schema/dtd/${v}/docbook.dtd" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "system" \
     "http://docbook.org/xml/${v}/dtd/docbook.dtd" \
     "file://%{_datadir}/xml/docbook5/schema/dtd/${v}/docbook.dtd" ${CATALOG}
  # XSD
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://www.oasis-open.org/docbook/xml/${v}/xsd/docbook.xsd" \
     "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/docbook.xsd" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://docbook.org/xml/${v}/xsd/docbook.xsd" \
     "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/docbook.xsd" ${CATALOG}
  # XSD + XInclude
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://www.oasis-open.org/docbook/xml/${v}/xsd/docbookxi.xsd" \
     "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/docbookxi.xsd" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://docbook.org/xml/${v}/xsd/docbookxi.xsd" \
     "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/docbookxi.xsd" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://www.oasis-open.org/docbook/xml/${v}/xsd/xi.xsd" \
     "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/xi.xsd" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://docbook.org/xml/${v}/xsd/xi.xsd" \
     "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/xi.xsd" ${CATALOG}
  # XLink + XML
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://www.oasis-open.org/docbook/xml/${v}/xsd/xlink.xsd" \
     "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/xlink.xsd" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://docbook.org/xml/${v}/xsd/xlink.xsd" \
     "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/xlink.xsd" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://www.oasis-open.org/docbook/xml/${v}/xsd/xml.xsd" \
     "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/xml.xsd" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://docbook.org/xml/${v}/xsd/xml.xsd" \
     "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/xml.xsd" ${CATALOG}
done
for v in 5.0 5.1
do
  # RNG
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://www.oasis-open.org/docbook/xml/${v}/rng/docbook.rng" \
     "file://%{_datadir}/xml/docbook5/schema/rng/${v}/docbook.rng" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://docbook.org/xml/${v}/rng/docbook.rng" \
     "file://%{_datadir}/xml/docbook5/schema/rng/${v}/docbook.rng" ${CATALOG}
  # RNG+XInclude
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://www.oasis-open.org/docbook/xml/${v}/rng/docbookxi.rng" \
     "file://%{_datadir}/xml/docbook5/schema/rng/${v}/docbookxi.rng" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://docbook.org/xml/${v}/rng/docbookxi.rng" \
     "file://%{_datadir}/xml/docbook5/schema/rng/${v}/docbookxi.rng" ${CATALOG}
  # RNC
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://www.oasis-open.org/docbook/xml/${v}/rnc/docbook.rnc" \
     "file://%{_datadir}/xml/docbook5/schema/rng/${v}/docbook.rnc" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://docbook.org/xml/${v}/rng/docbook.rnc" \
     "file://%{_datadir}/xml/docbook5/schema/rng/${v}/docbook.rnc" ${CATALOG}
  # RNC+XInclude
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://www.oasis-open.org/docbook/xml/${v}/rnc/docbookxi.rnc" \
     "file://%{_datadir}/xml/docbook5/schema/rng/${v}/docbookxi.rnc" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://docbook.org/xml/${v}/rng/docbookxi.rnc" \
     "file://%{_datadir}/xml/docbook5/schema/rng/${v}/docbookxi.rnc" ${CATALOG}
  # Schematron
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://www.oasis-open.org/docbook/xml/${v}/sch/docbook.sch" \
     "file://%{_datadir}/xml/docbook5/schema/sch/${v}/docbook.sch" ${CATALOG}
  %{_bindir}/xmlcatalog --noout --add "uri" \
     "http://docbook.org/xml/${v}/sch/docbook.sch" \
     "file://%{_datadir}/xml/docbook5/schema/sch/${v}/docbook.sch" ${CATALOG}
done
# ---------------------
# Build XML catalog files for each Schema
for v in 5.0 5.1
do
  for s in rng sch; do
   cat=${v}/${s}/catalog.xml
   %{_bindir}/xmlcatalog --noout --create ${cat}
   case $s in
    sch)
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://docbook.org/xml/${v}/${s}/docbook.${s}" \
       "docbook.${s}" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://www.oasis-open.org/docbook/xml/${v}/${s}/docbook.${s}" \
       "docbook.${s}" ${cat}
     ;;
    rng)
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://docbook.org/xml/${v}/${s}/docbook.${s}" \
       "docbook.${s}" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://www.oasis-open.org/docbook/xml/${v}/${s}/docbook.${s}" \
       "docbook.${s}" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://docbook.org/xml/${v}/${s}/docbookxi.${s}" \
       "docbookxi.${s}" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://www.oasis-open.org/docbook/xml/${v}/${s}/docbookxi.${s}" \
       "docbookxi.${s}" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://docbook.org/xml/${v}/${s}/docbook.rnc" \
       "docbook.rnc" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://www.oasis-open.org/docbook/xml/${v}/${s}/docbook.rnc" \
       "docbook.rnc" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://docbook.org/xml/${v}/${s}/docbookxi.rnc" \
       "docbookxi.rnc" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://www.oasis-open.org/docbook/xml/${v}/${s}/docbookxi.rnc" \
       "docbookxi.rnc" ${cat}
     ;;
   esac
  done
done
for v in 5.0
do
  for s in dtd xsd; do
   cat=${v}/${s}/catalog.xml
   %{_bindir}/xmlcatalog --noout --create ${cat}
   case $s in
    dtd)
     %{_bindir}/xmlcatalog --noout --add "public" \
       "-//OASIS//DTD DocBook XML ${v}//EN" \
       "docbook.dtd" ${cat}
     %{_bindir}/xmlcatalog --noout --add "system" \
       "http://www.oasis-open.org/docbook/xml/${v}/dtd/docbook.dtd" \
       "docbook.dtd" ${cat}
     ;;
    xsd)
     # http://www.oasis-open.org/docbook/xml/5.0/xsd/docbookxi.xsd
     # http://www.oasis-open.org/docbook/xml/5.0/xsd/xlink.xsd
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://docbook.org/xml/${v}/${s}/docbook.${s}" \
       "docbook.${s}" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://www.oasis-open.org/docbook/xml/${v}/${s}/docbook.${s}" \
       "docbook.${s}" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://docbook.org/xml/${v}/${s}/docbookxi.${s}" \
       "docbookxi.${s}" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://www.oasis-open.org/docbook/xml/${v}/${s}/docbookxi.${s}" \
       "docbookxi.${s}" ${cat}
     # XLink + XML:
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://docbook.org/xml/${v}/${s}/xlink.xsd" \
       "xlink.xsd" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://www.oasis-open.org/docbook/xml/${v}/${s}/xlink.xsd" \
       "xlink.xsd" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://docbook.org/xml/${v}/${s}/xml.xsd" \
       "xml.xsd" ${cat}
     %{_bindir}/xmlcatalog --noout --add "uri" \
       "http://www.oasis-open.org/docbook/xml/${v}/${s}/xml.xsd" \
       "xml.xsd" ${cat}
     ;;
   esac
  done
done

%install
DOCBOOK5DIR=$RPM_BUILD_ROOT%{_datadir}/xml/docbook5
for v in 5.0 5.1
do
mkdir -p ${DOCBOOK5DIR}/schema/rng/$v
mkdir -p ${DOCBOOK5DIR}/schema/sch/$v
install -m644 $v/rng/* ${DOCBOOK5DIR}/schema/rng/$v
install -m644 $v/sch/* ${DOCBOOK5DIR}/schema/sch/$v
done
mkdir -p ${DOCBOOK5DIR}/schema/dtd/5.0
mkdir -p ${DOCBOOK5DIR}/schema/xsd/5.0
install -m644 5.0/dtd/* ${DOCBOOK5DIR}/schema/dtd/5.0
install -m644 5.0/xsd/* ${DOCBOOK5DIR}/schema/xsd/5.0
mkdir -p $RPM_BUILD_ROOT%{_bindir}            
install -m755 %{version}/tools/db4-entities.pl $RPM_BUILD_ROOT%{_bindir}            
mkdir -p ${DOCBOOK5DIR}/stylesheet/upgrade            
install -m644 %{version}/tools/db4-upgrade.xsl ${DOCBOOK5DIR}/stylesheet/upgrade

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xml
install -m644 docbook-5.xml $RPM_BUILD_ROOT%{_sysconfdir}/xml/docbook-5.xml

%post
ROOTCATALOG=%{_sysconfdir}/xml/catalog
if [ -w $ROOTCATALOG ]
then
  for v in 5.0 5.1
  do
  %{_bindir}/xmlcatalog --noout --add "delegatePublic" \
    "-//OASIS//DTD DocBook XML ${v}//EN" \
    "file://%{_datadir}/xml/docbook5/schema/dtd/${v}/catalog.xml" \
    $ROOTCATALOG
  %{_bindir}/xmlcatalog --noout --add "delegateURI" \
    "http://docbook.org/xml/${v}/rng/"  \
    "file://%{_datadir}/xml/docbook5/schema/rng/${v}/catalog.xml" \
    $ROOTCATALOG
  %{_bindir}/xmlcatalog --noout --add "delegateURI" \
    "http://docbook.org/xml/${v}/sch/"  \
    "file://%{_datadir}/xml/docbook5/schema/sch/${v}/catalog.xml" \
    $ROOTCATALOG
   done
  %{_bindir}/xmlcatalog --noout --add "delegateURI" \
    "http://docbook.org/xml/5.0/xsd/"  \
    "file://%{_datadir}/xml/docbook5/schema/xsd/${v}/catalog.xml" \
    $ROOTCATALOG
  %{_bindir}/xmlcatalog --noout --add "delegateSystem" \
    "http://docbook.org/xml/5.0/dtd/" \
    "file://%{_datadir}/xml/docbook5/schema/dtd/${v}/catalog.xml" \
    $ROOTCATALOG
  %{_bindir}/xmlcatalog --noout --add "delegateURI" \
    "http://docbook.org/xml/5.0/dtd/" \
    "file://%{_datadir}/xml/docbook5/schema/dtd/${v}/catalog.xml" \
    $ROOTCATALOG
fi

%postun
if [ "$1" = 0 ]; then
  ROOTCATALOG=%{_sysconfdir}/xml/catalog
  if [ -w $ROOTCATALOG ]
  then
    for v in 5.0 5.1
    do
       %{_bindir}/xmlcatalog --noout --del \
       "file://%{_datadir}/xml/docbook5/schema/rng/${v}/catalog.xml" \
       $ROOTCATALOG
       %{_bindir}/xmlcatalog --noout --del \
       "file://%{_datadir}/xml/docbook5/schema/sch/${v}/catalog.xml" \
       $ROOTCATALOG
     done
      %{_bindir}/xmlcatalog --noout --del \
       "file://%{_datadir}/xml/docbook5/schema/dtd/5.0/catalog.xml" \
       $ROOTCATALOG
      %{_bindir}/xmlcatalog --noout --del \
       "file://%{_datadir}/xml/docbook5/schema/xsd/5.0/catalog.xml" \
       $ROOTCATALOG

  fi
fi

%files
%doc docs/* README ChangeLog
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/xml/docbook-5.xml
%dir %{_datadir}/xml/docbook5/
%dir %{_datadir}/xml/docbook5/schema
%dir %{_datadir}/xml/docbook5/schema/dtd
%dir %{_datadir}/xml/docbook5/schema/rng
%dir %{_datadir}/xml/docbook5/schema/sch
%dir %{_datadir}/xml/docbook5/schema/xsd
%dir %{_datadir}/xml/docbook5/stylesheet            
%dir %{_datadir}/xml/docbook5/stylesheet/upgrade
# Docbook5.0
%{_datadir}/xml/docbook5/schema/dtd/5.0
%{_datadir}/xml/docbook5/schema/rng/5.0
%{_datadir}/xml/docbook5/schema/sch/5.0
%{_datadir}/xml/docbook5/schema/xsd/5.0
# Docbook 5.1
%{_datadir}/xml/docbook5/schema/rng/%{version}
%{_datadir}/xml/docbook5/schema/sch/%{version}
%{_datadir}/xml/docbook5/stylesheet/upgrade/db4-upgrade.xsl
%{_bindir}/db4-entities.pl

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.1-17
- Prepare for Oreon 11 (RP1)
