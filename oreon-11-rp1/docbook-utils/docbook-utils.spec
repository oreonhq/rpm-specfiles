# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 154b120dd897d6411a55e5a2833044807eaf31a61412df601384be6fd101ed8f

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: docbook-utils
Version: 0.6.15
Release: 1%{?dist}
Summary: Shell scripts for managing DocBook documents
License: GPL-2.0-or-later
URL: https://github.com/devexp-db/docbook-utils
Source0: https://github.com/devexp-db/docbook-utils/releases/download/v%{version}/docbook-utils-%{version}.tar.xz
Source1: db2html
Source2: gdp-both.dsl
Source3: docbook2man-spec.pl
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: perl-generators
BuildRequires: perl-SGMLSpm
BuildRequires: openjade
BuildRequires: docbook-style-dsssl
BuildRequires: make

Requires: docbook-style-dsssl >= 1.72
Requires: docbook-dtds
Requires: perl-SGMLSpm >= 1.03ii
Requires: which
Requires: grep
Requires: gawk

Obsoletes: stylesheets < %{version}-%{release}
Provides: stylesheets = %{version}-%{release}

%description
Scripts for converting DocBook files to other formats.

%package pdf
Summary: Convert DocBook documents to PDF
License: GPL-1.0-or-later
Requires: texlive-jadetex >= 7
Requires: texlive-passivetex
Requires: docbook-utils = %{version}
Requires: tex(dvips)
Recommends: texlive-collection-fontsrecommended
Recommends: texlive-collection-latex
Obsoletes: stylesheets-db2pdf <= %{version}-%{release}
Provides: stylesheets-db2pdf = %{version}-%{release}

%description pdf
Script for converting DocBook documents to PDF.

%prep
%oreon_sha256
%autosetup

%build
./configure --prefix=%{_prefix} --mandir=%{_mandir} --libdir=%{_libdir}
%make_build

%install
export DESTDIR=%{buildroot}
make install prefix=%{_prefix} mandir=%{_mandir} docdir=/tmp
for util in dvi html pdf ps rtf; do
  ln -s docbook2$util %{buildroot}%{_bindir}/db2$util
  ln -s jw.1.gz %{buildroot}%{_mandir}/man1/db2$util.1
done
ln -s jw.1.gz %{buildroot}%{_mandir}/man1/docbook2txt.1
rm -f %{buildroot}%{_bindir}/db2html
install -p -m 755 %{SOURCE1} %{buildroot}%{_bindir}/db2html
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/sgml/docbook/utils-%{version}/docbook-utils.dsl
install -p -m 755 %{SOURCE3} %{buildroot}%{_datadir}/sgml/docbook/utils-%{version}/helpers/docbook2man-spec.pl
rm -rf %{buildroot}/tmp

%check
test -x %{buildroot}%{_bindir}/jw
test -x %{buildroot}%{_bindir}/db2html

%files
%license COPYING
%doc README TODO
%{_bindir}/jw
%{_bindir}/docbook2html
%{_bindir}/docbook2man
%{_bindir}/docbook2rtf
%{_bindir}/docbook2tex
%{_bindir}/docbook2texi
%{_bindir}/docbook2txt
%{_bindir}/db2html
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

%files pdf
%{_bindir}/docbook2pdf
%{_bindir}/db2pdf
%{_bindir}/docbook2dvi
%{_bindir}/db2dvi
%{_bindir}/docbook2ps
%{_bindir}/db2ps
%{_mandir}/*/db2pdf.*
%{_mandir}/*/docbook2pdf.*
%{_mandir}/*/docbook2dvi.*
%{_mandir}/*/docbook2ps.*

%changelog
%autochangelog
