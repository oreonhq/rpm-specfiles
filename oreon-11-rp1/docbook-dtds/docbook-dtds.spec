%global openjadever 1.3.2
%global version_list "{3,4}.{0,1}-sgml 4.1.2-xml 4.{2,3,4,5}-{sgml,xml} 4.{2,3,4,5}-rng 4.{2,3,4,5}-xsd"
%global catalog_list "{3,4}.{0,1}-sgml 4.1.2-xml 4.{2,3,4,5}-{sgml,xml}"
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name: docbook-dtds
Version: 1.0
Release: 91%{?dist}

Summary: SGML and XML document type definitions for DocBook

License: LicenseRef-docbook-dtds
URL: http://www.oasis-open.org/docbook/

Obsoletes: docbook-dtd30-sgml < %{version}-%{release}
Obsoletes: docbook-dtd31-sgml < %{version}-%{release}
Obsoletes: docbook-dtd40-sgml < %{version}-%{release}
Obsoletes: docbook-dtd41-sgml < %{version}-%{release}
Obsoletes: docbook-dtd412-xml < %{version}-%{release}
Provides: docbook-dtd-xml = %{version}-%{release}
Provides: docbook-dtd-sgml = %{version}-%{release}
Provides: docbook-dtd30-sgml = %{version}-%{release}
Provides: docbook-dtd31-sgml = %{version}-%{release}
Provides: docbook-dtd40-sgml = %{version}-%{release}
Provides: docbook-dtd41-sgml = %{version}-%{release}
Provides: docbook-dtd412-xml = %{version}-%{release}
Provides: docbook-dtd42-sgml = %{version}-%{release}
Provides: docbook-dtd42-xml = %{version}-%{release}
Provides: docbook-dtd43-sgml = %{version}-%{release}
Provides: docbook-dtd43-xml = %{version}-%{release}
Provides: docbook-dtd44-sgml = %{version}-%{release}
Provides: docbook-dtd44-xml = %{version}-%{release}
Provides: docbook-dtd45-sgml = %{version}-%{release}
Provides: docbook-dtd45-xml = %{version}-%{release}

Requires(post): %{_bindir}/xmlcatalog
Requires(postun): %{_bindir}/xmlcatalog
Requires(post): %{_bindir}/chmod
Requires(post): sed
Requires(postun): sed
Requires: sgml-common
Requires: xml-common

BuildRequires: unzip

BuildArch: noarch
Source0: http://www.oasis-open.org/docbook/sgml/3.0/docbk30.zip
Source1: http://www.oasis-open.org/docbook/sgml/3.1/docbk31.zip
Source2: http://www.oasis-open.org/docbook/sgml/4.0/docbk40.zip
Source3: http://www.oasis-open.org/docbook/sgml/4.1/docbk41.zip
Source4: http://www.oasis-open.org/docbook/xml/4.1.2/docbkx412.zip
Source5: http://www.oasis-open.org/docbook/sgml/4.2/docbook-4.2.zip
Source6: http://www.oasis-open.org/docbook/xml/4.2/docbook-xml-4.2.zip
Source7: http://www.docbook.org/sgml/4.3/docbook-4.3.zip
Source8: http://www.docbook.org/xml/4.3/docbook-xml-4.3.zip
Source9: http://www.docbook.org/sgml/4.4/docbook-4.4.zip
Source10: http://www.docbook.org/xml/4.4/docbook-xml-4.4.zip
Source11: http://www.docbook.org/sgml/4.5/docbook-4.5.zip
Source12: http://www.docbook.org/xml/4.5/docbook-xml-4.5.zip
Source13: http://www.docbook.org/rng/4.2/docbook-rng-4.2.zip
Source14: http://www.docbook.org/rng/4.3/docbook-rng-4.3.zip
Source15: http://www.docbook.org/rng/4.4/docbook-rng-4.4.zip
# Compressed from http://www.docbook.org/rng/4.5/ upstream archive unavailable
Source16: docbook-rng-4.5.zip
Source17: http://www.docbook.org/xsd/4.2/docbook-xsd-4.2.zip
Source18: http://www.docbook.org/xsd/4.3/docbook-xsd-4.3.zip
Source19: http://www.docbook.org/xsd/4.4/docbook-xsd-4.4.zip
# Compressed from http://www.docbook.org/xsd/4.5/ upstream archive unavailable
Source20: docbook-xsd-4.5.zip

# Fix old catalog files
Patch0: docbook-dtd30-sgml-1.0.catalog.patch
Patch1: docbook-dtd31-sgml-1.0.catalog.patch
Patch2: docbook-dtd40-sgml-1.0.catalog.patch
Patch3: docbook-dtd41-sgml-1.0.catalog.patch
Patch4: docbook-dtd42-sgml-1.0.catalog.patch
# Fix euro sign in 4.2 dtds
Patch5: docbook-4.2-euro.patch
# Fix ISO entities in 4.3/4.4/4.5 SGML
Patch6: docbook-dtds-ents.patch
# Use system rewrite for web URL's in sgml catalogs to prevent reading from the network(#478680)
Patch7: docbook-sgml-systemrewrite.patch
# Use XML at the end of public identificators of XML 4.1.2 ISO entities
Patch8: docbook-dtd412-entities.patch
# oreon url source checksums begin
%global source0_sha256 ecf71cbe8ddbad7494ff520d5b4edf73a428c0b159178cb0cb619cba685e61c6
%global source0_file docbk30.zip
%global source1_sha256 20261d2771b9a052abfa3d8fab1aa62be05791a010281c566f9073bf0e644538
%global source1_file docbk31.zip
%global source2_sha256 dfef22f109779e4cfaafa27b6d381d975ac05eaafb5b3d4407d7043e310817bb
%global source2_file docbk40.zip
%global source3_sha256 deaafcf0a3677692e7ad4412c0e41c1db3e9da6cdcdb3dd32b2cc1f9c97d6311
%global source3_file docbk41.zip
%global source4_sha256 30f0644064e0ea71751438251940b1431f46acada814a062870f486c772e7772
%global source4_file docbkx412.zip
%global source5_sha256 67ebd2c94b342718c6865d2de60f5d4ff02d77a7e4b0d9e72a48c45f2b2635c3
%global source5_file docbook-4.2.zip
%global source6_sha256 acc4601e4f97a196076b7e64b368d9248b07c7abf26b34a02cca40eeebe60fa2
%global source6_file docbook-xml-4.2.zip
%global source7_sha256 88f52fab7bd49b2e8f40c525014129c26a5a4b8bbd1494e00387556ec76f95ee
%global source7_file docbook-4.3.zip
%global source8_sha256 23068a94ea6fd484b004c5a73ec36a66aa47ea8f0d6b62cc1695931f5c143464
%global source8_file docbook-xml-4.3.zip
%global source9_sha256 0ac7960409b032c8e517483523ecb92af4e59196a33b3e2c5617daa22b7a8a6c
%global source9_file docbook-4.4.zip
%global source10_sha256 02f159eb88c4254d95e831c51c144b1863b216d909b5ff45743a1ce6f5273090
%global source10_file docbook-xml-4.4.zip
%global source11_sha256 8043e514e80c6c19cb146b5d37937d1305bf3abf9b0097c36df7f70f611cdf43
%global source11_file docbook-4.5.zip
%global source12_sha256 4e4e037a2b83c98c6c94818390d4bdd3f6e10f6ec62dd79188594e26190dc7b4
%global source12_file docbook-xml-4.5.zip
%global source13_sha256 001d6f4945f36faf542b2d5ab421de03ed6bbda0b3adecb13ce69b22fd56b5f9
%global source13_file docbook-rng-4.2.zip
%global source14_sha256 16d3120df58237e19445bc5ca14d05597d29e0734e93eb16582ec200ec065d19
%global source14_file docbook-rng-4.3.zip
%global source15_sha256 38c0bcd5e40226b15d79b86b119341d88f5b6c6e80cd20fb262238963aec1d15
%global source15_file docbook-rng-4.4.zip
%global source17_sha256 32d105b60a1524c71acbb9e700fb210fe69faf28716b9b6703901ba43a3973e5
%global source17_file docbook-xsd-4.2.zip
%global source18_sha256 c6b988431003b857927239d11254a57158b893e4960c80ae1a5ce02e8c6af7f5
%global source18_file docbook-xsd-4.3.zip
%global source19_sha256 710db64c36ed962aa8dab97bd1b5bea1b1fb4c613e0d3b8f8adf0069f535c699
%global source19_file docbook-xsd-4.4.zip
# oreon url source checksums end

%description
The DocBook Document Type Definition (DTD) describes the syntax of
technical documentation texts (articles, books and manual pages).
This syntax is XML-compliant and is developed by the OASIS consortium.
This package contains SGML and XML versions of the DocBook DTD.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/docbk30.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ecf71cbe8ddbad7494ff520d5b4edf73a428c0b159178cb0cb619cba685e61c6" || { echo "oreon: Source0 SHA256 mismatch for docbk30.zip" >&2; exit 1; })
%(f=%{_sourcedir}/docbk31.zip; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "20261d2771b9a052abfa3d8fab1aa62be05791a010281c566f9073bf0e644538" || { echo "oreon: Source1 SHA256 mismatch for docbk31.zip" >&2; exit 1; })
%(f=%{_sourcedir}/docbk40.zip; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "dfef22f109779e4cfaafa27b6d381d975ac05eaafb5b3d4407d7043e310817bb" || { echo "oreon: Source2 SHA256 mismatch for docbk40.zip" >&2; exit 1; })
%(f=%{_sourcedir}/docbk41.zip; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "deaafcf0a3677692e7ad4412c0e41c1db3e9da6cdcdb3dd32b2cc1f9c97d6311" || { echo "oreon: Source3 SHA256 mismatch for docbk41.zip" >&2; exit 1; })
%(f=%{_sourcedir}/docbkx412.zip; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "30f0644064e0ea71751438251940b1431f46acada814a062870f486c772e7772" || { echo "oreon: Source4 SHA256 mismatch for docbkx412.zip" >&2; exit 1; })
%(f=%{_sourcedir}/docbook-4.2.zip; test -f "$f" || { echo "oreon: missing Source5 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "67ebd2c94b342718c6865d2de60f5d4ff02d77a7e4b0d9e72a48c45f2b2635c3" || { echo "oreon: Source5 SHA256 mismatch for docbook-4.2.zip" >&2; exit 1; })
%(f=%{_sourcedir}/docbook-xml-4.2.zip; test -f "$f" || { echo "oreon: missing Source6 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "acc4601e4f97a196076b7e64b368d9248b07c7abf26b34a02cca40eeebe60fa2" || { echo "oreon: Source6 SHA256 mismatch for docbook-xml-4.2.zip" >&2; exit 1; })
%(f=%{_sourcedir}/docbook-4.3.zip; test -f "$f" || { echo "oreon: missing Source7 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "88f52fab7bd49b2e8f40c525014129c26a5a4b8bbd1494e00387556ec76f95ee" || { echo "oreon: Source7 SHA256 mismatch for docbook-4.3.zip" >&2; exit 1; })
%(f=%{_sourcedir}/docbook-xml-4.3.zip; test -f "$f" || { echo "oreon: missing Source8 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "23068a94ea6fd484b004c5a73ec36a66aa47ea8f0d6b62cc1695931f5c143464" || { echo "oreon: Source8 SHA256 mismatch for docbook-xml-4.3.zip" >&2; exit 1; })
%(f=%{_sourcedir}/docbook-4.4.zip; test -f "$f" || { echo "oreon: missing Source9 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "0ac7960409b032c8e517483523ecb92af4e59196a33b3e2c5617daa22b7a8a6c" || { echo "oreon: Source9 SHA256 mismatch for docbook-4.4.zip" >&2; exit 1; })
%(f=%{_sourcedir}/docbook-xml-4.4.zip; test -f "$f" || { echo "oreon: missing Source10 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "02f159eb88c4254d95e831c51c144b1863b216d909b5ff45743a1ce6f5273090" || { echo "oreon: Source10 SHA256 mismatch for docbook-xml-4.4.zip" >&2; exit 1; })
%(f=%{_sourcedir}/docbook-4.5.zip; test -f "$f" || { echo "oreon: missing Source11 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8043e514e80c6c19cb146b5d37937d1305bf3abf9b0097c36df7f70f611cdf43" || { echo "oreon: Source11 SHA256 mismatch for docbook-4.5.zip" >&2; exit 1; })
%(f=%{_sourcedir}/docbook-xml-4.5.zip; test -f "$f" || { echo "oreon: missing Source12 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4e4e037a2b83c98c6c94818390d4bdd3f6e10f6ec62dd79188594e26190dc7b4" || { echo "oreon: Source12 SHA256 mismatch for docbook-xml-4.5.zip" >&2; exit 1; })
%(f=%{_sourcedir}/docbook-rng-4.2.zip; test -f "$f" || { echo "oreon: missing Source13 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "001d6f4945f36faf542b2d5ab421de03ed6bbda0b3adecb13ce69b22fd56b5f9" || { echo "oreon: Source13 SHA256 mismatch for docbook-rng-4.2.zip" >&2; exit 1; })
%(f=%{_sourcedir}/docbook-rng-4.3.zip; test -f "$f" || { echo "oreon: missing Source14 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "16d3120df58237e19445bc5ca14d05597d29e0734e93eb16582ec200ec065d19" || { echo "oreon: Source14 SHA256 mismatch for docbook-rng-4.3.zip" >&2; exit 1; })
%(f=%{_sourcedir}/docbook-rng-4.4.zip; test -f "$f" || { echo "oreon: missing Source15 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "38c0bcd5e40226b15d79b86b119341d88f5b6c6e80cd20fb262238963aec1d15" || { echo "oreon: Source15 SHA256 mismatch for docbook-rng-4.4.zip" >&2; exit 1; })
%(f=%{_sourcedir}/docbook-xsd-4.2.zip; test -f "$f" || { echo "oreon: missing Source17 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "32d105b60a1524c71acbb9e700fb210fe69faf28716b9b6703901ba43a3973e5" || { echo "oreon: Source17 SHA256 mismatch for docbook-xsd-4.2.zip" >&2; exit 1; })
%(f=%{_sourcedir}/docbook-xsd-4.3.zip; test -f "$f" || { echo "oreon: missing Source18 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c6b988431003b857927239d11254a57158b893e4960c80ae1a5ce02e8c6af7f5" || { echo "oreon: Source18 SHA256 mismatch for docbook-xsd-4.3.zip" >&2; exit 1; })
%(f=%{_sourcedir}/docbook-xsd-4.4.zip; test -f "$f" || { echo "oreon: missing Source19 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "710db64c36ed962aa8dab97bd1b5bea1b1fb4c613e0d3b8f8adf0069f535c699" || { echo "oreon: Source19 SHA256 mismatch for docbook-xsd-4.4.zip" >&2; exit 1; })
# oreon verify url source checksums end
%setup -c -T
eval mkdir %{version_list}

unzip %{SOURCE0} -d 3.0-sgml
unzip %{SOURCE1} -d 3.1-sgml
unzip %{SOURCE2} -d 4.0-sgml
unzip %{SOURCE3} -d 4.1-sgml
unzip %{SOURCE4} -d 4.1.2-xml
unzip %{SOURCE5} -d 4.2-sgml
unzip %{SOURCE6} -d 4.2-xml
unzip %{SOURCE7} -d 4.3-sgml
unzip %{SOURCE8} -d 4.3-xml
unzip %{SOURCE9} -d 4.4-sgml
unzip %{SOURCE10} -d 4.4-xml
unzip %{SOURCE11} -d 4.5-sgml
unzip %{SOURCE12} -d 4.5-xml
unzip %{SOURCE13} -d 4.2-rng
unzip %{SOURCE14} -d 4.3-rng
unzip %{SOURCE15} -d 4.4-rng
unzip %{SOURCE16} -d 4.5-rng
unzip %{SOURCE17} -d 4.2-xsd
unzip %{SOURCE18} -d 4.3-xsd
unzip %{SOURCE19} -d 4.4-xsd
unzip %{SOURCE20} -d 4.5-xsd

%patch -P 0 -p0
%patch -P 1 -p0
%patch -P 2 -p0
%patch -P 3 -p0
%patch -P 4 -p0

# Fix &euro; in SGML.
%patch -P 5 -p0

# Fix ISO entities in 4.3/4.4/4.5 SGML
%patch -P 6 -p0

# Rewrite SYSTEM to use local catalog instead web ones (#478680)
%patch -P 7 -p0

# Add XML to the end of public identificators of 4.1.2 XML entities
%patch -P 8 -p0

# Increase NAMELEN (bug #36058, bug #159382).
sed -e's,\(NAMELEN\s\+\)44\(\s\*\)\?,\1256,' -i.namelen */docbook.dcl

# Fix of \r\n issue from rpmlint
sed -i 's/\r//' */*.txt


if [ `id -u` -eq 0 ]; then
  %{_bindir}/chown -R root:root .
  %{_bindir}/chmod -R a+rX,g-w,o-w .
fi


%build


%install
# Creating a directory for SGML
eval mkdir -p %{buildroot}/etc/sgml

# Loop through sgml and xml formats
for fmt in sgml xml; do
  # Creating symbolic links for docbook catalog files
  ln -s $fmt-docbook-4.5.cat %{buildroot}/etc/sgml/$fmt-docbook.cat
done

# Loop through different versions of docbook
eval set %{version_list}
for dir in $@; do
  pushd $dir
  fmt=${dir#*-} ver=${dir%%-*} # Formatting and versioning

  # Directory paths for different formats
  case $fmt in
    sgml|xml)   DESTDIR=%{buildroot}/usr/share/sgml/docbook/$fmt-dtd-$ver ;;
    rng|xsd)    DESTDIR=%{buildroot}/usr/share/sgml/docbook/$fmt-$ver ;;
  esac

  # Installing files to the corresponding directories
  case $fmt in
    sgml)   mkdir -p $DESTDIR ; install *.dcl $DESTDIR ;;
    xml)    mkdir -p $DESTDIR/ent ; install ent/* $DESTDIR/ent ;;
    rng)    mkdir -p $DESTDIR ; install *.r* $DESTDIR ;;
    xsd)    mkdir -p $DESTDIR ; install *.xsd $DESTDIR;;
  esac
  popd
done

# Loop through different catalog versions
eval set %{catalog_list}
for dir in $@; do
  pushd $dir
  fmt=${dir#*-} ver=${dir%%-*} # Formatting and versioning
  DESTDIR=%{buildroot}/usr/share/sgml/docbook/$fmt-dtd-$ver

  # Installing dtd and mod files, along with the catalog file
  install *.dtd *.mod $DESTDIR
  install docbook.cat $DESTDIR/catalog
  popd

  # Creating ghost file for each format-version pair
  touch %{buildroot}/etc/sgml/$fmt-docbook-$ver.cat
done

# Workaround for missing support for --parents in rpm 4.11+
mkdir -p %{buildroot}%{_pkgdocdir}

# Copying text, ChangeLog, and README files to pkgdocdir with their parent directories
for i in */*.txt */ChangeLog */README; do
  cp -pr --parents $i %{buildroot}%{_pkgdocdir}
done


%files
# There is a lot of files with 0755 permissions in upstream tarballs,
# but it is not needed. 0644 is enough for every file in tarball
%doc %{_pkgdocdir}
%{_datadir}/sgml/docbook/*ml-dtd-*
%{_datadir}/sgml/docbook/rng-*
%{_datadir}/sgml/docbook/xsd-*
%config(noreplace) %{_sysconfdir}/sgml/*ml-docbook.cat
%ghost %config(noreplace) %{_sysconfdir}/sgml/*ml-docbook-*.cat

%post
catcmd='/usr/bin/xmlcatalog --noout'
xmlcatalog=%{_datadir}/sgml/docbook/xmlcatalog

# Clean up pre-docbook-dtds mess caused by broken trigger.
for v in 3.0 3.1 4.0 4.1 4.2 4.3 4.4 4.5
do
  if [ -f %{_sysconfdir}/sgml/sgml-docbook-$v.cat ]
  then
    $catcmd --sgml --del %{_sysconfdir}/sgml/sgml-docbook-$v.cat \
      %{_datadir}/sgml/openjade-%{openjadever}/catalog 2>/dev/null
  fi
done

# The STYLESHEETS/catalog command is for the case in which the style sheets
# were installed after another DTD but before this DTD
for STYLESHEETS in %{_datadir}/sgml/docbook/dsssl-stylesheets-*; do : ; done
case $STYLESHEETS in
  *-"*") STYLESHEETS= ;;
esac
eval set %{catalog_list}
for dir
do
  fmt=${dir#*-} ver=${dir%%-*}
  sgmldir=%{_datadir}/sgml/docbook/$fmt-dtd-$ver
  # SGML catalog
  # Update the centralized catalog corresponding to this version of the DTD
  for cat_dir in %{_datadir}/sgml/sgml-iso-entities-8879.1986 $sgmldir $STYLESHEETS; do
    $catcmd --sgml --add %{_sysconfdir}/sgml/$fmt-docbook-$ver.cat $cat_dir/catalog
  done
  # XML catalog
  if [ $fmt = xml -a -w $xmlcatalog ]; then
    while read f desc; do
      case $ver in 4.[45]) f=${f/-/} ;; esac
      $catcmd --add public "$desc" $sgmldir/$f $xmlcatalog
    done <<ENDENT
      ent/iso-pub.ent	ISO 8879:1986//ENTITIES Publishing//EN
      ent/iso-grk1.ent	ISO 8879:1986//ENTITIES Greek Letters//EN
      dbpoolx.mod	-//OASIS//ELEMENTS DocBook XML Information Pool V$ver//EN
      ent/iso-box.ent	ISO 8879:1986//ENTITIES Box and Line Drawing//EN
      docbookx.dtd	-//OASIS//DTD DocBook XML V$ver//EN
      ent/iso-grk3.ent	ISO 8879:1986//ENTITIES Greek Symbols//EN
      ent/iso-amsn.ent	ISO 8879:1986//ENTITIES Added Math Symbols: Negated Relations//EN
      ent/iso-num.ent	ISO 8879:1986//ENTITIES Numeric and Special Graphic//EN
      dbcentx.mod	-//OASIS//ENTITIES DocBook XML Character Entities V$ver//EN
      ent/iso-grk4.ent	ISO 8879:1986//ENTITIES Alternative Greek Symbols//EN
      dbnotnx.mod	-//OASIS//ENTITIES DocBook XML Notations V$ver//EN
      ent/iso-dia.ent	ISO 8879:1986//ENTITIES Diacritical Marks//EN
      ent/iso-grk2.ent	ISO 8879:1986//ENTITIES Monotoniko Greek//EN
      dbgenent.mod	-//OASIS//ENTITIES DocBook XML Additional General Entities V$ver//EN
      dbhierx.mod	-//OASIS//ELEMENTS DocBook XML Document Hierarchy V$ver//EN
      ent/iso-amsa.ent	ISO 8879:1986//ENTITIES Added Math Symbols: Arrow Relations//EN
      ent/iso-amso.ent	ISO 8879:1986//ENTITIES Added Math Symbols: Ordinary//EN
      ent/iso-cyr1.ent	ISO 8879:1986//ENTITIES Russian Cyrillic//EN
      ent/iso-tech.ent	ISO 8879:1986//ENTITIES General Technical//EN
      ent/iso-amsc.ent	ISO 8879:1986//ENTITIES Added Math Symbols: Delimiters//EN
      soextblx.dtd	-//OASIS//DTD XML Exchange Table Model 19990315//EN
      calstblx.dtd	-//OASIS//DTD DocBook XML CALS Table Model V$ver//EN
      ent/iso-lat1.ent	ISO 8879:1986//ENTITIES Added Latin 1//EN
      ent/iso-amsb.ent	ISO 8879:1986//ENTITIES Added Math Symbols: Binary Operators//EN
      ent/iso-lat2.ent	ISO 8879:1986//ENTITIES Added Latin 2//EN
      ent/iso-amsr.ent	ISO 8879:1986//ENTITIES Added Math Symbols: Relations//EN
      ent/iso-cyr2.ent	ISO 8879:1986//ENTITIES Non-Russian Cyrillic//EN
ENDENT
    for f in System URI; do
      $catcmd --add rewrite$f "http://www.oasis-open.org/docbook/xml/$ver" \
	$sgmldir $xmlcatalog
    done
  fi
done

# Historic versions of this scriptlet contained the following comment:
# <quote>
# Fix up SGML super catalog so that there isn't an XML DTD before an
# SGML one.  We need to do this (*sigh*) because xmlcatalog messes up
# the order of the lines, and SGML tools don't like to see XML things
# they aren't expecting.
# </quote>
# But the code that followed just found the first XML DTD and the first
# SGML DTD, swappinmg these two lines if the XML one preceded.
# But that only ensures that there is an SGML DTD before all XML ones.
# No one complained, so either this was enough, or the buggy SGML tools
# are long dead, or their users do not use bugzilla.
# Anyway, the following code, introduced in 1.0-46, does better: it ensures
# that all XML DTDs are after all SGML ones, by moving them to the end.
sed -ni '
  /xml-docbook/ H
  /xml-docbook/ !p
  $ {
          g
          s/^\n//p
  }
  ' %{_sysconfdir}/sgml/catalog

# Finally, make sure everything in /etc/sgml is readable!
%{_bindir}/chmod a+r %{_sysconfdir}/sgml/*

%postun
# Remove entries only on removal of package
if [ "$1" = 0 ]; then
  catcmd='%{_bindir}/xmlcatalog --noout'
  xmlcatalog=%{_datadir}/sgml/docbook/xmlcatalog
  entities="
ent/iso-pub.ent
ent/iso-grk1.ent
dbpoolx.mod
ent/iso-box.ent
docbookx.dtd
ent/iso-grk3.ent
ent/iso-amsn.ent
ent/iso-num.ent
dbcentx.mod
ent/iso-grk4.ent
dbnotnx.mod
ent/iso-dia.ent
ent/iso-grk2.ent
dbgenent.mod
dbhierx.mod
ent/iso-amsa.ent
ent/iso-amso.ent
ent/iso-cyr1.ent
ent/iso-tech.ent
ent/iso-amsc.ent
soextblx.dtd
calstblx.dtd
ent/iso-lat1.ent
ent/iso-amsb.ent
ent/iso-lat2.ent
ent/iso-amsr.ent
ent/iso-cyr2.ent
  "
  eval set %{catalog_list}
  for dir
  do
    fmt=${dir#*-} ver=${dir%%-*}
    sgmldir=%{_datadir}/sgml/docbook/$fmt-dtd-$ver
    ## SGML catalog
    # Update the centralized catalog corresponding to this version of the DTD
    $catcmd --sgml --del %{_sysconfdir}/sgml/catalog %{_sysconfdir}/sgml/$fmt-docbook-$ver.cat >/dev/null
    rm -f %{_sysconfdir}/sgml/$fmt-docbook-$ver.cat
    ## XML catalog
    if [ $fmt = xml -a -w $xmlcatalog ]; then
      for f in $entities; do
        case $ver in 4.[45]) f=${f/-/} ;; esac
        $catcmd --del $sgmldir/$f $xmlcatalog >/dev/null
      done
      $catcmd --del $sgmldir $xmlcatalog >/dev/null
    fi
  done

  # See the comment attached to this command in the %%post scriptlet.
  sed -ni '
  /xml-docbook/ H
  /xml-docbook/ !p
  $ {
          g
          s/^\n//p
  }
    ' %{_sysconfdir}/sgml/catalog
fi

%triggerin -- openjade >= %{openjadever}
eval set %{catalog_list}
for dir
do
  fmt=${dir#*-} ver=${dir%%-*}
  %{_bindir}/xmlcatalog --sgml --noout --add %{_sysconfdir}/sgml/$fmt-docbook-$ver.cat \
    %{_datadir}/sgml/openjade-%{openjadever}/catalog
done

%triggerun -- openjade >= %{openjadever}
[ $2 = 0 ] || exit 0
eval set %{catalog_list}
for dir
do
  fmt=${dir#*-} ver=${dir%%-*}
  %{_bindir}/xmlcatalog --sgml --noout --del %{_sysconfdir}/sgml/$fmt-docbook-$ver.cat \
    %{_datadir}/sgml/openjade-%{openjadever}/catalog
done

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0-91
- Import
