# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2f329e120bee9ef42fbdd74ddd60e05e49786c5a7953a0ff4c680ae6bdf0e2bc
%global style_dir %{_datadir}/sgml/docbook/dsssl-stylesheets-%{version}

Name: docbook-style-dsssl
Version: 1.79
Release: 1%{?dist}
Summary: Modular DocBook DSSSL stylesheets
License: MIT
URL: https://docbook.sourceforge.net/
Source0: https://downloads.sourceforge.net/docbook/docbook-dsssl-%{version}.tar.bz2
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: perl-interpreter
Requires: perl-SGMLSpm
Requires: sgml-common

%description
Modular DSSSL stylesheets for converting DocBook SGML and XML documents to
print and HTML output.

%prep
%oreon_sha256
%autosetup -n docbook-dsssl-%{version}

%build

%install
install -d %{buildroot}%{style_dir}
cp -a bin common contrib dtds frames html images lib olink print catalog \
    %{buildroot}%{style_dir}/
chmod 0755 %{buildroot}%{style_dir}/bin/collateindex.pl
install -d %{buildroot}%{_bindir}
ln -s %{style_dir}/bin/collateindex.pl %{buildroot}%{_bindir}/collateindex.pl
ln -s dsssl-stylesheets-%{version} \
    %{buildroot}%{_datadir}/sgml/docbook/dsssl-stylesheets

%check
test -f %{buildroot}%{style_dir}/html/docbook.dsl
test -f %{buildroot}%{style_dir}/print/docbook.dsl
perl -c %{buildroot}%{style_dir}/bin/collateindex.pl

%files
%doc ChangeLog README RELEASE-NOTES.txt WhatsNew
%{_bindir}/collateindex.pl
%{_datadir}/sgml/docbook/dsssl-stylesheets
%{style_dir}

%changelog
%autochangelog
