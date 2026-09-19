%global source0_hash 1d2f7288e158488c3e28abc0d6f3d4581f95a81202ee04e44712c32fb603d310

# Track font name changes
%define RHEL6 %([[ %{?dist}x == .el6[a-z]* ]] && echo 1 || echo 0)
%define RHEL7 %([[ %{?dist}x == .el7[a-z]* ]] && echo 1 || echo 0)

# BUGBUG BZ #1144220 work around wrong entity string bug
%define DBPATH %(find /usr/share/sgml/docbook/xml-dtd-4.5*/dbcentx.mod)

%define OTHER 1
%if %{RHEL6}
%define OTHER 0
%endif
%if %{RHEL7}
%define OTHER 0
%endif

# required for desktop file install
%define my_vendor %(test %{OTHER} == 1 && echo "fedora" || echo "redhat")

%define TESTS 1
%define wwwdir /var/www/html/docs

Name:           publican
Version:        4.3.2
Release:        34%{?dist}
Summary:        Common files and scripts for publishing with DocBook XML
# For a breakdown of the licensing, refer to LICENSE
License:        (GPL-2.0-or-later OR Artistic-1.0-Perl) AND CC0-1.0
URL:            https://publican.fedorahosted.org
Source0:        https://fedorahosted.org/released/publican/Publican-v%{version}.tar.gz
Patch0:         file-spec-fix.patch
Patch1:		    xsl.patch

BuildArch:      noarch
Provides:       publican-common = %{version}
Provides:       publican-common-db5 = %{version}
Provides:       publican-API = 4.1

## work around arch -> noarch bug in yum
Obsoletes:      publican < 3

BuildRequires:  perl(Devel::Cover)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) => 1.14
BuildRequires:  perl(Test::Pod::Coverage) => 1.04
BuildRequires:  perl(Archive::Tar) => 1.84
BuildRequires:  perl(Archive::Zip)
# Not reall required, but sometimes koji pulls in a conflicting dep...
BuildRequires:  perl(Compress::Zlib) => 2.030
BuildRequires:  perl(Locale::Maketext::Gettext) >= 1.27
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config::Simple)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::DateParse)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy::Recursive) => 0.38
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Inplace)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::FormatText)
BuildRequires:  perl(HTML::FormatText::WithLinks)
BuildRequires:  perl(HTML::FormatText::WithLinks::AndTables) >= 0.02
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(HTML::WikiConverter::Markdown) >= 0.06
BuildRequires:  perl(I18N::LangTags::List)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Locale::Language)
BuildRequires:  perl(Locale::PO) >= 0.24
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(String::Similarity)
BuildRequires:  perl(Syntax::Highlight::Engine::Kate) >= 0.09
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Constants)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(Time::localtime)
BuildRequires:  perl(XML::LibXML) => 1.70
BuildRequires:  perl(XML::LibXSLT) => 1.70
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(XML::TreeBuilder) => 5.4
# BZ #1053609
BuildRequires:  perl-generators
BuildRequires:  perl-XML-TreeBuilder >= 5.4
BuildRequires:  docbook-style-xsl >= 1.77.1
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  perl(Text::CSV_XS)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  docbook5-schemas
BuildRequires:  docbook5-style-xsl >= 1.78.1
BuildRequires:  perl(version) >= 0.77
BuildRequires:  perl(Locale::Msgfmt)
BuildRequires:  perl(Locale::Maketext::Lexicon)
BuildRequires:  perl(Lingua::EN::Fathom)
BuildRequires:  rpm-build libicu-devel

# Most of these are handled automatically
Requires:       perl(Locale::Maketext::Gettext)  >= 1.27
Requires:       rpm-build
Requires:       docbook-style-xsl >= 1.77.1
Requires:       perl(XML::LibXML)  >=  1.70
Requires:       perl(XML::LibXSLT) >=  1.70
Requires:       perl(XML::TreeBuilder) >= 5.4
Requires:       perl(HTML::WikiConverter::Markdown) >= 0.06
# BZ #1053609
Requires:       perl-XML-TreeBuilder >= 5.4
Requires:       perl-Template-Toolkit
Requires:       perl(DBD::SQLite)
Requires:       perl(Text::CSV_XS)
Requires:       docbook5-schemas
Requires:       docbook5-style-xsl >= 1.78.1

# Not really required, but sometimes koji pulls in a conflicting dep...
Requires:       perl(Compress::Zlib) => 2.030

# Lets validate some basics
Requires:       rpmlint

# Pull in the fonts for all languages, else you can't build translated PDF in brew/koji
%if %{RHEL6}
Requires:       liberation-mono-fonts liberation-sans-fonts liberation-serif-fonts
Requires:       cjkuni-uming-fonts ipa-gothic-fonts ipa-pgothic-fonts
Requires:       lklug-fonts baekmuk-ttf-batang-fonts
Requires:       lohit-assamese-fonts lohit-bengali-fonts lohit-devanagari-fonts
Requires:       lohit-gujarati-fonts lohit-hindi-fonts lohit-kannada-fonts
Requires:       lohit-kashmiri-fonts lohit-konkani-fonts lohit-maithili-fonts
Requires:       lohit-malayalam-fonts lohit-marathi-fonts lohit-nepali-fonts
Requires:       lohit-oriya-fonts lohit-punjabi-fonts lohit-sindhi-fonts
Requires:       lohit-tamil-fonts lohit-telugu-fonts dejavu-lgc-sans-mono-fonts
Requires:       dejavu-fonts-common dejavu-serif-fonts dejavu-sans-fonts
Requires:       dejavu-sans-mono-fonts overpass-fonts
Requires:       wqy-zenhei-fonts
Requires:       wkhtmltopdf >= 0.12.1.devlopment
BuildRequires:  wkhtmltopdf >= 0.12.1.development
BuildRequires:  liberation-mono-fonts liberation-sans-fonts liberation-serif-fonts
BuildRequires:  cjkuni-uming-fonts ipa-gothic-fonts ipa-pgothic-fonts
BuildRequires:  lklug-fonts baekmuk-ttf-batang-fonts
BuildRequires:  dejavu-fonts-common dejavu-serif-fonts dejavu-sans-fonts
BuildRequires:  dejavu-sans-mono-fonts overpass-fonts dejavu-lgc-sans-mono-fonts
%endif
%if %{RHEL7}
Requires:       liberation-mono-fonts liberation-sans-fonts liberation-serif-fonts
Requires:       cjkuni-uming-fonts ipa-gothic-fonts ipa-pgothic-fonts
Requires:       lklug-fonts baekmuk-ttf-batang-fonts overpass-fonts
Requires:       wkhtmltopdf >= 0.12.1.devlopment
BuildRequires:  wkhtmltopdf >= 0.12.1.development
BuildRequires:  liberation-mono-fonts liberation-sans-fonts liberation-serif-fonts
BuildRequires:  cjkuni-uming-fonts ipa-gothic-fonts ipa-pgothic-fonts
BuildRequires:  lklug-fonts baekmuk-ttf-batang-fonts
%endif
%if %{OTHER}
Requires:       liberation-mono-fonts liberation-sans-fonts liberation-serif-fonts
Requires:       cjkuni-uming-fonts ipa-gothic-fonts ipa-pgothic-fonts
Requires:       baekmuk-ttf-batang-fonts overpass-fonts
Requires:       fop
BuildRequires:  fop
BuildRequires:  liberation-mono-fonts liberation-sans-fonts liberation-serif-fonts
BuildRequires:  cjkuni-uming-fonts ipa-gothic-fonts ipa-pgothic-fonts
BuildRequires:  baekmuk-ttf-batang-fonts
%endif

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

# Package web common files
mkdir -p -m755 $RPM_BUILD_ROOT/%{wwwdir}/common
dir=`pwd`
cd datadir/Common_Content/common
XML_CATALOG_FILES=$dir/catalog %{__perl} -CDAS -I $dir/blib/lib $dir/blib/script/publican install_brand --web --path=$RPM_BUILD_ROOT/%{wwwdir}/common
cd -
mkdir -p -m755 $RPM_BUILD_ROOT/%{wwwdir}/common-db5
cd datadir/Common_Content/common-db5
XML_CATALOG_FILES=$dir/catalog %{__perl} -CDAS -I $dir/blib/lib $dir/blib/script/publican install_brand --web --path=$RPM_BUILD_ROOT/%{wwwdir}/common-db5
cd -

%check
%if %{TESTS}
dir=`pwd`
XML_CATALOG_FILES=$dir/catalog ./Build --nocolours=1 test
%endif

%post
# hack to allow branch directory BZ #800252
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

%files -f %{name}.lang
%doc Changes README COPYING Artistic pod1/publican
%{perl_vendorlib}/Publican.pm
%{perl_vendorlib}/Publican
%{_mandir}/man3/Publican*
%{_mandir}/man1/*
%{_bindir}/publican
%{_bindir}/db5-valid
%{_bindir}/db4-2-db5
%{_datadir}/publican
%config(noreplace) %{_datadir}/publican/default.db
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/publican-website.cfg
%config(noreplace) %{_sysconfdir}/bash_completion.d/_publican

%files doc
%doc Users_Guide/publish/desktop/*
%{_datadir}/applications/%{my_vendor}-%{name}.desktop
%doc fdl.txt

%files releasenotes
%doc Release_Notes/publish/desktop/*
%{_datadir}/applications/%{my_vendor}-%{name}-releasenotes.desktop
%doc fdl.txt

%files common-web
%{wwwdir}/common

%files common-db5-web
%{wwwdir}/common-db5

%changelog
%autochangelog
