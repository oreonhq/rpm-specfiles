%global source0_hash 4077757d367a9d1b1427e8d5dfc3c49d993e90deabc6df23d05cfe9cd2fcdc45
Name:           docbook2X
Version:        0.8.8
Release:        1%{?dist}
Summary:        Convert docbook into man and Texinfo
License:        MIT
URL:            http://docbook2x.sourceforge.net/
Source0:        https://downloads.sourceforge.net/docbook2x/docbook2X-%{version}.tar.gz
Requires:       libxslt openjade texinfo %{_bindir}/sgml2xml
Requires:  perl(Exporter)
Requires:  perl(IO::File)
Requires:  perl(Text::Wrap)
Requires:  perl(vars)
Requires:  perl(XML::SAX::ParserFactory)
# oreon:deps
BuildRequires:  /usr/bin/sgml2xml
BuildRequires:  gcc
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  openjade
BuildRequires:  perl(XML::SAX::ParserFactory)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  texinfo
# /oreon:deps
%description
docbook2X converts DocBook documents into man pages and Texinfo
documents.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8.8-52
- Prepare for Oreon 11 (RP1)
