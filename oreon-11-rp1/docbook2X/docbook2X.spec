Name:           docbook2X
Version:        0.8.8
Release:        52%{?dist}
Summary:        Convert docbook into man and Texinfo

License:        MIT
URL:            http://docbook2x.sourceforge.net/
Source0:        http://downloads.sourceforge.net/docbook2x/docbook2X-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 4077757d367a9d1b1427e8d5dfc3c49d993e90deabc6df23d05cfe9cd2fcdc45
%global source0_file docbook2X-0.8.8.tar.gz
# oreon url source checksums end


BuildRequires:  gcc
BuildRequires:  perl-interpreter perl-generators libxslt openjade texinfo %{_bindir}/sgml2xml
# required by the perl -c calls during build
BuildRequires:  perl(XML::SAX::ParserFactory)
BuildRequires: make
# rpmlint isn't happy with libxslt, but we need xsltproc
Requires:       libxslt openjade texinfo %{_bindir}/sgml2xml
# Required by bin/* scripts, who does know why rpmbuild does not generate
# dependencies automatically:
Requires:  perl(Exporter)
Requires:  perl(IO::File)
Requires:  perl(Text::Wrap)
Requires:  perl(vars)
Requires:  perl(XML::SAX::ParserFactory)

%description
docbook2X converts DocBook documents into man pages and Texinfo
documents.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/docbook2X-0.8.8.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4077757d367a9d1b1427e8d5dfc3c49d993e90deabc6df23d05cfe9cd2fcdc45" || { echo "oreon: Source0 SHA256 mismatch for docbook2X-0.8.8.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build
# to avoid clashing with docbook2* from docbook-utils
%configure --program-transform-name='s/docbook2/db2x_docbook2/'
make %{?_smp_mflags}
rm -rf __dist_html
mkdir -p __dist_html/html
cp -p doc/*.html __dist_html/html


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -c -p'
rm -rf $RPM_BUILD_ROOT/%{_datadir}/doc/
rm -f $RPM_BUILD_ROOT%{_infodir}/dir


%files
%doc COPYING README THANKS AUTHORS __dist_html/html/
%{_bindir}/db2x_manxml
%{_bindir}/db2x_texixml
%{_bindir}/db2x_xsltproc
%{_bindir}/db2x_docbook2man
%{_bindir}/db2x_docbook2texi
%{_bindir}/sgml2xml-isoent
%{_bindir}/utf8trans
%dir %{_datadir}/docbook2X
%{_datadir}/docbook2X/VERSION
%dir %{_datadir}/docbook2X/charmaps
%dir %{_datadir}/docbook2X/dtd
%dir %{_datadir}/docbook2X/xslt
%{_datadir}/docbook2X/charmaps/*
%{_datadir}/docbook2X/dtd/*
%{_datadir}/docbook2X/xslt/*
%{_mandir}/man1/*.1*
%{_infodir}/docbook2*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8.8-52
- Prepare for Oreon 11 (RP1)
