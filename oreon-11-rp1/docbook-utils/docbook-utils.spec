%global source0_hash 154b120dd897d6411a55e5a2833044807eaf31a61412df601384be6fd101ed8f
Name: docbook-utils
Version: 0.6.15
Release:        1%{?dist}
Summary:        Shell scripts for managing DocBook documents
URL: https://github.com/devexp-db/docbook-utils
License: GPL-2.0-or-later
Requires: docbook-style-dsssl >= 1.72
Requires: docbook-dtds
Requires: perl-SGMLSpm >= 1.03ii
Requires: which grep gawk
Requires: text-www-browser
Suggests: lynx
BuildArch: noarch
Source0:        https://github.com/devexp-db/docbook-utils/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1: db2html
Source2: gdp-both.dsl
Source3: docbook2man-spec.pl
Obsoletes: stylesheets < %{version}-%{release}
Provides: stylesheets = %{version}-%{release}
# oreon:deps
BuildRequires:  docbook-style-dsssl
BuildRequires:  make
BuildRequires:  openjade
BuildRequires:  perl-SGMLSpm
BuildRequires:  perl-generators
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
rm -f $RPM_BUILD_ROOT%{_bindir}/db2html
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/db2html
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/utils-%{version}/docbook-utils.dsl
install -p -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/utils-%{version}/helpers/docbook2man-spec.pl
rm -rf $RPM_BUILD_ROOT/tmp
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n docbook-utils-pdf -f %{oreon_filedir}/docbook-utils-pdf.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.15-6
- Prepare for Oreon 11 (RP1)
