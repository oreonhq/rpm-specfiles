%global source0_hash ea20d806ad652282d0353498e2860df8125c80b6491630c25d263bd880c618d7

Name:       perl-Template-Plugin-JavaScript
Version:    0.02
Release:    40%{?dist}
# see lib/Template/Plugin/JavaScript.pm
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Encodes text to be safe in JavaScript
Source:     https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Template-Plugin-JavaScript-%{version}.tar.gz
Url:        https://metacpan.org/release/Template-Plugin-JavaScript
BuildArch:  noarch
# Build
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires: perl(base)
BuildRequires: perl(strict)
BuildRequires: perl(Template::Plugin)
BuildRequires: perl(vars)
# Tests
BuildRequires: perl(lib)
BuildRequires: perl(Template::Test)
BuildRequires: perl(Test::More) >= 0.32

%?perl_default_filter

%description
Template::Plugin::JavaScript is a TT filter that filters text so it can
be safely used in JavaScript quotes. e.g:

  [% USE JavaScript %]
  document.write("[% FILTER js %] Here's some text going on. [% END %]");

will become:

  document.write("\nHere\'s some text going on.\n");

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Template-Plugin-JavaScript-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
