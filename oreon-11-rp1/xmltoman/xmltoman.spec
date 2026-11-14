# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash cdd5063ca8beb6fe51ec6ab85f70d31fc8ed034e85e32dd9b7c0b7142bb72fb6

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           xmltoman
Version:        0.6
Release:        1%{?dist}
Summary:        Scripts for converting XML to man pages in groff format
License:        GPL-2.0-or-later
URL:            https://github.com/atsb/xmltoman
Source0:        https://github.com/atsb/xmltoman/archive/%{version}/xmltoman-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  oreon-rpm-macros
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(XML::Parser)

Requires:       perl(XML::Parser)

%description
xmltoman and xmlmantohtml are two small scripts that convert a simple XML
format to man pages in groff format and to HTML, so that man pages can be
written and maintained in a single XML source.

%prep
%oreon_sha256
%autosetup

%build
%make_build prefix=%{_prefix}

%install
%make_install prefix=%{_prefix}

%check
./xmltoman xml/xmltoman.1.xml | grep -q '^\.TH'
./xmlmantohtml xml/xmltoman.1.xml | grep -q '<h2>Synopsis</h2>'

%files
%license COPYING
%doc README ChangeLog
%{_bindir}/xmltoman
%{_bindir}/xmlmantohtml
%{_datadir}/xmltoman/
%{_mandir}/man1/xmltoman.1*
%{_mandir}/man1/xmlmantohtml.1*

%changelog
%autochangelog
