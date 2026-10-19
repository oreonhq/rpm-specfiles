%global source0_hash 1d2f7288e158488c3e28abc0d6f3d4581f95a81202ee04e44712c32fb603d310
%define RHEL6 %([[ %{?dist}x == .el6[a-z]* ]] && echo 1 || echo 0)
%define RHEL7 %([[ %{?dist}x == .el7[a-z]* ]] && echo 1 || echo 0)
%define DBPATH %(find /usr/share/sgml/docbook/xml-dtd-4.5*/dbcentx.mod)
%define OTHER 1
%define my_vendor %(test %{OTHER} == 1 && echo "fedora" || echo "redhat")
%define TESTS 1
%define wwwdir /var/www/html/docs
Name:           publican
Version:        4.3.2
Release:        1%{?dist}
Summary:        Common files and scripts for publishing with DocBook XML
License:        (GPL-2.0-or-later OR Artistic-1.0-Perl) AND CC0-1.0
URL:            https://publican.fedorahosted.org
Source0:        https://fedorahosted.org/released/publican/Publican-v%{version}.tar.gz
Patch0:         file-spec-fix.patch
Patch1:		    xsl.patch
BuildArch:      noarch
Provides:       publican-common = %{version}
Provides:       publican-common-db5 = %{version}
Provides:       publican-API = 4.1
Obsoletes:      publican < 3
Requires:       perl(Locale::Maketext::Gettext)  >= 1.27
Requires:       rpm-build
Requires:       docbook-style-xsl >= 1.77.1
Requires:       perl(XML::LibXML)  >=  1.70
Requires:       perl(XML::LibXSLT) >=  1.70
Requires:       perl(XML::TreeBuilder) >= 5.4
Requires:       perl(HTML::WikiConverter::Markdown) >= 0.06
Requires:       perl-XML-TreeBuilder >= 5.4
Requires:       perl-Template-Toolkit
Requires:       perl(DBD::SQLite)
Requires:       perl(Text::CSV_XS)
Requires:       docbook5-schemas
Requires:       docbook5-style-xsl >= 1.78.1
Requires:       perl(Compress::Zlib) => 2.030
Requires:       rpmlint
%if %{OTHER}
Requires:       liberation-mono-fonts liberation-sans-fonts liberation-serif-fonts
Requires:       cjkuni-uming-fonts ipa-gothic-fonts ipa-pgothic-fonts
Requires:       baekmuk-ttf-batang-fonts overpass-fonts
Requires:       fop
%endif
# oreon:deps
BuildRequires:  baekmuk-ttf-batang-fonts
BuildRequires:  cjkuni-uming-fonts
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  docbook5-schemas
BuildRequires:  docbook5-style-xsl
BuildRequires:  fop
BuildRequires:  gettext
BuildRequires:  ipa-gothic-fonts
BuildRequires:  ipa-pgothic-fonts
BuildRequires:  liberation-mono-fonts
BuildRequires:  liberation-sans-fonts
BuildRequires:  liberation-serif-fonts
BuildRequires:  libicu-devel
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(Config::Simple)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::DateParse)
BuildRequires:  perl(Devel::Cover)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Inplace)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::FormatText)
BuildRequires:  perl(HTML::FormatText::WithLinks)
BuildRequires:  perl(HTML::FormatText::WithLinks::AndTables)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(HTML::WikiConverter::Markdown)
BuildRequires:  perl(I18N::LangTags::List)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Lingua::EN::Fathom)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Locale::Language)
BuildRequires:  perl(Locale::Maketext::Gettext)
BuildRequires:  perl(Locale::Maketext::Lexicon)
BuildRequires:  perl(Locale::Msgfmt)
BuildRequires:  perl(Locale::PO)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(String::Similarity)
BuildRequires:  perl(Syntax::Highlight::Engine::Kate)
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Constants)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Text::CSV_XS)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(Time::localtime)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::LibXSLT)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(XML::TreeBuilder)
BuildRequires:  perl(version)
BuildRequires:  perl-XML-TreeBuilder
BuildRequires:  perl-generators
BuildRequires:  rpm-build
# /oreon:deps
%description
Publican is a DocBook publication system, not just a DocBook processing tool.
As well as ensuring your DocBook XML is valid, publican works to ensure
your XML is up to publishable standard.

%package doc
Summary:        Documentation for the Publican package
Requires:       xdg-utils
Obsoletes:      publican-doc < 3
%description doc
Publican is a tool for publishing material authored in DocBook XML.
This guide explains how to  to create and build books and articles
using publican. It is not a DocBook XML tutorial and concentrates
solely on using the publican tools.

%package releasenotes
Summary:        Release notes for the Publican package
Requires:       xdg-utils
%description releasenotes
Release notes for Publican %{version}.

%package common-web
Summary:        Website style for common brand
Requires:       publican
%description common-web
Website style for common brand.

%package common-db5-web
Summary:        Website style for common brand for DocBook5 content
Requires:       publican
%description common-db5-web
Website style for common brand for DocBook5 content

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Publican-v%{version}
%autopatch -p1

%build

sed -i -e 's,PATH,%{DBPATH},g' catalog
XML_CATALOG_FILES=$dir/catalog %{__perl} Build.PL installdirs=vendor --nocolours=1
XML_CATALOG_FILES=$dir/catalog ./Build --nocolours=1
dir=`pwd`
cd Users_Guide && XML_CATALOG_FILES=$dir/catalog  %{__perl} -CDAS -I $dir/blib/lib $dir/blib/script/publican build \
    --formats=html-desktop --publish --langs=en-US \
    --common_config="$dir/blib/datadir" \
    --common_content="$dir/blib/datadir/Common_Content" --nocolours
cd $dir
cd Release_Notes && XML_CATALOG_FILES=$dir/catalog %{__perl} -CDAS -I $dir/blib/lib $dir/blib/script/publican build \
    --formats=html-desktop --publish --langs=en-US \
    --common_config="$dir/blib/datadir" \
    --common_content="$dir/blib/datadir/Common_Content" --nocolours
%install
rm -rf $RPM_BUILD_ROOT
dir=`pwd`
XML_CATALOG_FILES=$dir/catalog ./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
sed -i -e 's|@@FILE@@|%{_docdir}/%{name}-doc%{!?_docdir_fmt:-%{version}}/en-US/index.html|' %{name}.desktop
sed -i -e 's|@@ICON@@|%{_docdir}/%{name}-doc%{!?_docdir_fmt:-%{version}}/en-US/images/icon.svg|' %{name}.desktop
sed -i -e 's|@@FILE@@|%{_docdir}/%{name}-releasenotes%{!?_docdir_fmt:-%{version}}/en-US/index.html|' %{name}-releasenotes.desktop
sed -i -e 's|@@ICON@@|%{_docdir}/%{name}-releasenotes%{!?_docdir_fmt:-%{version}}/en-US/images/icon.svg|' %{name}-releasenotes.desktop
desktop-file-install --vendor="%{my_vendor}" --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{name}.desktop
desktop-file-install --vendor="%{my_vendor}" --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{name}-releasenotes.desktop
%find_lang %{name} --with-man
mkdir -p -m755 $RPM_BUILD_ROOT/%{wwwdir}/common
dir=`pwd`
cd datadir/Common_Content/common
XML_CATALOG_FILES=$dir/catalog %{__perl} -CDAS -I $dir/blib/lib $dir/blib/script/publican install_brand --web --path=$RPM_BUILD_ROOT/%{wwwdir}/common
cd -
mkdir -p -m755 $RPM_BUILD_ROOT/%{wwwdir}/common-db5
cd datadir/Common_Content/common-db5
XML_CATALOG_FILES=$dir/catalog %{__perl} -CDAS -I $dir/blib/lib $dir/blib/script/publican install_brand --web --path=$RPM_BUILD_ROOT/%{wwwdir}/common-db5
cd -
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{TESTS}
dir=`pwd`
XML_CATALOG_FILES=$dir/catalog ./Build --nocolours=1 test
%endif
%post

CATALOG=%{_sysconfdir}/xml/catalog
%{_bindir}/xmlcatalog --noout --add "rewriteURI" \
"https://fedorahosted.org/released/publican/xsl/docbook4/" \
"file://%{_datadir}/publican/xsl/"  $CATALOG
CATALOG=%{_sysconfdir}/xml/catalog
%{_bindir}/xmlcatalog --noout --add "public" \
"-//OASIS//ENTITIES DocBook Character Entities V4.5//EN" \
"file://%{DBPATH}"  $CATALOG
%postun

if [ "$1" = 0 ]; then
  CATALOG=%{_sysconfdir}/xml/catalog
  %{_bindir}/xmlcatalog --noout --del \
  "https://fedorahosted.org/released/publican/xsl/docbook4/" $CATALOG
  CATALOG=%{_sysconfdir}/xml/catalog
  %{_bindir}/xmlcatalog --noout --del \
  "-//OASIS//ENTITIES DocBook Character Entities V4.5//EN" $CATALOG
fi
%files -f %{oreon_filedir}/main.list
%files -n publican-doc -f %{oreon_filedir}/publican-doc.list
%files -n publican-releasenotes -f %{oreon_filedir}/publican-releasenotes.list
%files -n publican-common-web -f %{oreon_filedir}/publican-common-web.list
%files -n publican-common-db5-web -f %{oreon_filedir}/publican-common-db5-web.list

%changelog

%autochangelog
