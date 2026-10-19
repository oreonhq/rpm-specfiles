%global source0_hash 733269474de88d199964a0ab5d82f62ddd476cd5d0ed1cd36cf63d2f4a87bc86
Name:           perl-XML-Atom-SimpleFeed
Version:        0.905
Release:        10%{?dist}
Summary:        No-fuss generation of Atom syndication feeds
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-Atom-SimpleFeed
Source0:        https://cpan.metacpan.org/authors/id/A/AR/ARISTOTLE/XML-Atom-SimpleFeed-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Date)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(URI)
BuildRequires:  perl(Web::Scraper::LibXML)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
This module provides a minimal API for generating Atom syndication feeds
quickly and easily. It supports all aspects of the Atom format, but it has
no provisions for generating feeds with extension elements.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n XML-Atom-SimpleFeed-%{version}
/usr/bin/perl -pi -e 's|#!/usr/bin/perl||' t.pl x.pl

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
