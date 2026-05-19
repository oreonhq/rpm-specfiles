# Don't ship Java extensions in Fedora as they are not compiled from the source
# Shipping sources instead of binary jars was requested by
# https://lists.oasis-open.org/archives/docbook-apps/201408/msg00008.html
# Sources available in the docbook stylesheets svn repository, but not packaged.
%bcond extensions 0

Name: docbook5-style-xsl
Version: 1.79.2
Release: 26%{?dist}

Summary: Norman Walsh's XSL stylesheets for DocBook 5.X

# Package is licensed as MIT/X (http://wiki.docbook.org/topic/DocBookLicense),
# some .js files under ./slides/browser/ are licensed MPLv1.1
# Automatically converted from old format: MIT and MPLv1.1 - review is highly recommended.
License: LicenseRef-Callaway-MIT AND LicenseRef-Callaway-MPLv1.1
URL: https://github.com/docbook/xslt10-stylesheets

Provides: docbook-xsl-ns = %{version}
# xml-common was using /usr/share/xml until 0.6.3-8.
Requires: xml-common >= 0.6.3-8
# libxml2 required because of usage of /usr/bin/xmlcatalog
Requires(post): libxml2 >= 2.4.8
Requires(postun): libxml2 >= 2.4.8
Conflicts: passivetex < 1.21

BuildArch: noarch
Source0: https://github.com/docbook/xslt10-stylesheets/releases/download/release%2F%{version}/docbook-xsl-%{version}.tar.bz2

%description
These XSL namespace aware stylesheets allow you to transform any
DocBook 5 document to other formats, such as HTML, manpages, FO,
XHMTL and other formats. They are highly customizable. For more
information see W3C page about XSL.

%if %{with extensions}
%package extensions
Summary: Norman Walsh's XSL stylesheets extensions for DocBook 5.X
# Package is licensed as MIT/X (http://wiki.docbook.org/topic/DocBookLicense),
# some .js files under ./slides/browser/ are licensed MPLv1.1
# Automatically converted from old format: MIT and ASL 2.0 - review is highly recommended.
License: LicenseRef-Callaway-MIT AND Apache-2.0
Requires: docbook-xsl-ns = %{version}
# Provide an alternative to removed JAR files via Fedora Packages
# lucene-core.jar (lucene-core-3.0.0.jar), lucene-analysis-common.jar (lucene-analyzers-3.0.0.jar)
Requires: lucene-core lucene-analysis-common
# ant-apache-xalan2.jar (xalan27.jar)
Requires: ant-apache-xalan2
# tagsoup.jar (tagsoup-1.2.1.jar)
Requires: tagsoup

%description extensions
This package contains Java extensions for XSL namespace aware stylesheets.
%endif

%prep
%setup -q -n docbook-xsl-%{version}

# Remove .gitignore files
rm -rf $(find -name '.gitignore' -type f)

# Remove ant buildsystem
find . -name build.xml -delete

# Remove binary JAR files
rm -f extensions/*.jar
rm -fr tools/

# Make ruby scripts executable
chmod +x epub/bin/dbtoepub

# Remove misc
rm slides/slidy/scripts/slidy.js.gz
rm roundtrip/template.dot

%build

%install
DESTDIR=$RPM_BUILD_ROOT
mkdir -p $DESTDIR%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%version
cp -a [[:lower:]]* $DESTDIR%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%version/
cp -a VERSION $DESTDIR%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%version/VERSION.xsl
ln -s VERSION.xsl \
$DESTDIR%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%version/VERSION
ln -s xsl-ns-stylesheets-%{version} \
 $DESTDIR%{_datadir}/sgml/docbook/xsl-ns-stylesheets

# Don't ship install shell script.
rm -rf $DESTDIR%{_datadir}/sgml/docbook/xsl-ns-stylesheets/install.sh

%files
%doc BUGS
%doc README COPYING
%doc TODO NEWS
%doc RELEASE-NOTES.*
%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}
%{_datadir}/sgml/docbook/xsl-ns-stylesheets
%exclude %{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}/extensions

%if %{with extensions}
%files extensions
%doc extensions/README.txt extensions/LICENSE.txt
%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}/extensions
%endif

%post
CATALOG=%{_sysconfdir}/xml/catalog
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
 "http://cdn.docbook.org/release/xsl/%{version}" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "http://cdn.docbook.org/release/xsl/%{version}" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
 "http://cdn.docbook.org/release/xsl/current/" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "http://cdn.docbook.org/release/xsl/current/" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG

%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
 "http://docbook.sourceforge.net/release/xsl-ns/current" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "http://docbook.sourceforge.net/release/xsl-ns/current" \
 "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG

%postun
# remove entries only on removal of package
if [ "$1" = 0 ]; then
  CATALOG=%{_sysconfdir}/xml/catalog
  %{_bindir}/xmlcatalog --noout --del \
   "file://%{_datadir}/sgml/docbook/xsl-ns-stylesheets-%{version}" $CATALOG
fi

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.79.2-26
- Prepare for Oreon 11 (RP1)
