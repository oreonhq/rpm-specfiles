%global source0_hash ee8b9eca0b7a8f89075832a2da7534bce8c5478fc8fc2676f512d5d87d832102
%global source2_hash 9bc38a3015717279a3a0620efb2d4bcace430077241ae2b0da609ba67d8340bc

Name: docbook-style-xsl
Version: 1.79.2
Release: 27%{?dist}

Summary: Norman Walsh's XSL stylesheets for DocBook XML

License: LicenseRef-DMIT
URL: https://github.com/docbook/xslt10-stylesheets

Provides: docbook-xsl = %{version}
Requires: docbook-dtd-xml
# xml-common was using /usr/share/xml until 0.6.3-8.
Requires: xml-common >= 0.6.3-8
# libxml2 required because of usage of /usr/bin/xmlcatalog
Requires(post): libxml2 >= 2.4.8
Requires(postun): libxml2 >= 2.4.8
# PassiveTeX before 1.21 can't handle the newer stylesheets.
Conflicts: passivetex < 1.21
BuildRequires: make


BuildArch: noarch
Source0:        https://github.com/docbook/xslt10-stylesheets/releases/download/release%2F1.79.2/docbook-xsl-nons-1.79.2.tar.bz2
Source1: %{name}.Makefile
Source2:        https://github.com/docbook/xslt10-stylesheets/releases/download/release%2F1.79.2/docbook-xsl-doc-1.79.2.tar.bz2


#Avoid proportional-column-width for passivetex (bug #176766).
Patch1: docbook-xsl-pagesetup.patch
#Hard-code the margin-left work around to expect passivetex (bug #113456).
Patch2: docbook-xsl-marginleft.patch
#fix of #161619 - adjustColumnWidths now available
Patch3: docbook-xsl-newmethods.patch
#change a few non-constant expressions to constant - needed for passivetex(#366441)
Patch4: docbook-xsl-non-constant-expressions.patch
#added fixes for passivetex extension and list-item-body(#161371)
Patch5: docbook-xsl-list-item-body.patch
#workaround missing mandir section problem (#727251)
Patch6: docbook-xsl-mandir.patch
#Non-recursive string.subst that doesn't kill smb.conf.5 generation
Patch7: docbook-style-xsl-non-recursive-string-subst.patch
#Fix multilib problems with gtk-doc documentation
#https://github.com/docbook/xslt10-stylesheets/issues/54
Patch8: docbook-style-xsl-1.79.2-fix-gtk-doc-multilib.patch

%description
These XSL stylesheets allow you to transform any DocBook XML document to
other formats, such as HTML, FO, and XHMTL.  They are highly customizable.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; })
%setup -c -T -n docbook-xsl-%{version}
tar jxf %{SOURCE0}
mv docbook-xsl-nons-%{version}/* .
pushd ..
tar jxf %{SOURCE2}
popd
%patch -P1 -p1 -b .pagesetup
%patch -P2 -p1 -b .marginleft
%patch -P3 -p1 -b .newmethods
%patch -P4 -p1 -b .nonconstant
%patch -P5 -p1 -b .listitembody
%patch -P6 -p1 -b .mandir
%patch -P7 -p2 -b .non-recursive-subst
%patch -P8 -p1 -b .gtk-doc-multilib

cp -p %{SOURCE1} Makefile

# fix of non UTF-8 files rpmlint warnings
for fhtml in $(find ./doc -name '*.html' -type f)
do
  iconv -f ISO-8859-1 -t UTF-8 "$fhtml" -o "$fhtml".tmp
  mv -f "$fhtml".tmp "$fhtml"
  sed -i 's/charset=ISO-8859-1/charset=UTF-8/' "$fhtml"
done

for f in $(find -name "*'*")
do
  mv -v "$f" $(echo "$f" | tr -d "'")
done


%build


%install
DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT
make install BINDIR=$DESTDIR%{_bindir} DESTDIR=$DESTDIR%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}
cp -a VERSION.xsl $DESTDIR%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/VERSION.xsl
ln -s xsl-stylesheets-%{version} \
	$DESTDIR%{_datadir}/sgml/docbook/xsl-stylesheets

# Don't ship the extensions (bug #177256).
rm -rf $DESTDIR%{_datadir}/sgml/docbook/xsl-stylesheets/extensions/*


%files
%doc BUGS
%doc README
%doc TODO
%doc doc
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}
%{_datadir}/sgml/docbook/xsl-stylesheets


%post
CATALOG=%{_sysconfdir}/xml/catalog
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
 "http://cdn.docbook.org/release/xsl-nons/%{version}" \
 "file://%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "http://cdn.docbook.org/release/xsl-nons/%{version}" \
 "file://%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
 "http://cdn.docbook.org/release/xsl-nons/current/" \
 "file://%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "http://cdn.docbook.org/release/xsl-nons/current/" \
 "file://%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}" $CATALOG
#keep the old one sourceforge URIs at least temporarily
%{_bindir}/xmlcatalog --noout --add "rewriteSystem" \
 "http://docbook.sourceforge.net/release/xsl/current" \
 "file://%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}" $CATALOG
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
 "http://docbook.sourceforge.net/release/xsl/current" \
 "file://%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}" $CATALOG



%postun
# remove entries only on removal of package
if [ "$1" = 0 ]; then
  CATALOG=%{_sysconfdir}/xml/catalog
  %{_bindir}/xmlcatalog --noout --del \
   "file://%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}" $CATALOG
fi

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.79.2-27
- Prepare for Oreon 11 (RP1)
