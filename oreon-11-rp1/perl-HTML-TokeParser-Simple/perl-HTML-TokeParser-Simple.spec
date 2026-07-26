%global source0_hash ed11135c6839e6e0eaf96952e6ac353a2f22ebb40a721659671e5d2dcc0e4a9d

Name:           perl-HTML-TokeParser-Simple
Version:        3.16
Release:        37%{?dist}
Summary:        Easy to use HTML::TokeParser interface
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/HTML-TokeParser-Simple
Source0:        https://cpan.metacpan.org/authors/id/O/OV/OVID/HTML-TokeParser-Simple-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser) >= 3.25
BuildRequires:  perl(HTML::TokeParser) >= 2.24
# Tests:
BuildRequires:  perl(Sub::Override)
BuildRequires:  perl(Test::More)
Requires:       perl(HTML::Parser) >= 3.25
Requires:       perl(HTML::TokeParser) >= 2.24

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(HTML::TokeParser\\)$

%description
HTML::TokeParser is an excellent module that's often used for parsing HTML.
However, the tokens returned are not exactly intuitive to parse.  To simplify
this, HTML::TokeParser::Simple allows the user ask more intuitive (read: more
self-documenting) questions about the tokens returned.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-TokeParser-Simple-%{version}

%build
/usr/bin/perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/HTML*
%{_mandir}/man3/HTML*

%changelog
%autochangelog
