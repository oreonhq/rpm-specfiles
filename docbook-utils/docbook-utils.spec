Name: docbook-utils
Version: 0.6.15
Release: 6%{?dist}

Summary: Shell scripts for managing DocBook documents
URL: https://github.com/devexp-db/docbook-utils

License: GPL-2.0-or-later

Requires: docbook-style-dsssl >= 1.72
Requires: docbook-dtds
Requires: perl-SGMLSpm >= 1.03ii
Requires: which grep gawk
Requires: text-www-browser

# In the absence of an already-installed text-www-browser, prefer lynx
Suggests: lynx

BuildRequires: perl-generators
BuildRequires: perl-SGMLSpm, openjade, docbook-style-dsssl
BuildRequires: make

BuildArch: noarch
Source0: https://github.com/devexp-db/docbook-utils/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1: db2html
Source2: gdp-both.dsl
#We will ship newer version of docbook2man-spec.pl for better handling of docbook2man conversion
#You could check it at http://sourceforge.net/projects/docbook2x/
Source3: docbook2man-spec.pl

Obsoletes: stylesheets < %{version}-%{release}
Provides: stylesheets = %{version}-%{release}

%description
This package contains scripts are for easy conversion from DocBook
files to other formats (for example, HTML, RTF, and PostScript), and
for comparing SGML files.

%package pdf
Requires: texlive-jadetex >= 7
Requires: docbook-utils = %{version}
Requires: tex(dvips)
Requires: texlive-collection-fontsrecommended
Requires: texlive-collection-formatsextra
License: GPL-1.0-or-later
Obsoletes: stylesheets-db2pdf <= %{version}-%{release}
Provides: stylesheets-db2pdf = %{version}-%{release}
Summary: A script for converting DocBook documents to PDF format
URL: http://sources.redhat.com/docbook-tools/

%description pdf
This package contains a script for converting DocBook documents to
PDF format.

%prep
%setup -q

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir} --libdir=%{_libdir}
make %{?_smp_mflags}

%install
export DESTDIR=$RPM_BUILD_ROOT
make install prefix=%{_prefix} mandir=%{_mandir} docdir=/tmp
for util in dvi html pdf ps rtf
do
	ln -s docbook2$util $RPM_BUILD_ROOT%{_bindir}/db2$util
	ln -s jw.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1/db2$util.1
done
ln -s jw.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1/docbook2txt.1
# db2html is not just a symlink, as it has to create the output directory
rm -f $RPM_BUILD_ROOT%{_bindir}/db2html
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/db2html
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/utils-%{version}/docbook-utils.dsl
install -p -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/utils-%{version}/helpers/docbook2man-spec.pl

rm -rf $RPM_BUILD_ROOT/tmp

%files
%doc README COPYING TODO
%{_bindir}/jw
%{_bindir}/docbook2html
%{_bindir}/docbook2man
%{_bindir}/docbook2rtf
%{_bindir}/docbook2tex
%{_bindir}/docbook2texi
%{_bindir}/docbook2txt
%attr(0755,root,root) %{_bindir}/db2html
%{_bindir}/db2rtf
%{_bindir}/sgmldiff
%{_datadir}/sgml/docbook/utils-%{version}
%{_mandir}/*/db2dvi.*
%{_mandir}/*/db2html.*
%{_mandir}/*/db2ps.*
%{_mandir}/*/db2rtf.*
%{_mandir}/*/docbook2html.*
%{_mandir}/*/docbook2rtf.*
%{_mandir}/*/docbook2man.*
%{_mandir}/*/docbook2tex.*
%{_mandir}/*/docbook2texi.*
%{_mandir}/*/docbook2txt.*
%{_mandir}/*/jw.*
%{_mandir}/*/sgmldiff.*
%{_mandir}/*/*-spec.*

%files pdf
%{_bindir}/docbook2pdf
%{_bindir}/docbook2dvi
%{_bindir}/docbook2ps
%{_bindir}/db2dvi
%{_bindir}/db2pdf
%{_bindir}/db2ps
%{_mandir}/*/db2pdf.*
%{_mandir}/*/docbook2pdf.*
%{_mandir}/*/docbook2dvi.*
%{_mandir}/*/docbook2ps.*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.15-6
- Prepare for Oreon 11 (RP1)
