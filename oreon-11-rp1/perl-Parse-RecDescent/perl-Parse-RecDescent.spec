%global source0_hash 1943336a4cb54f1788a733f0827c0c55db4310d5eae15e542639c9dd85656e37

Name:           perl-Parse-RecDescent
Version:        1.967015
Release:        26%{?dist}
Summary:        Generate Recursive-Descent Parsers
License:        ( GPL-1.0-or-later OR Artistic-1.0-Perl ) OR ( GPL-2.0-or-later OR Artistic-1.0-Perl )
# demo/demo_another_Cgrammar.pl:    GPLv2+ or Artistic
URL:            https://metacpan.org/release/Parse-RecDescent
Source0:        https://cpan.metacpan.org/authors/id/J/JT/JTBRAUN/Parse-RecDescent-%{version}.tar.gz
Patch0:         Parse-RecDescent-1.967002-utf8.patch
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::Balanced) >= 1.95
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Warn)
# Runtime
Requires:       perl(Data::Dumper)

Provides:       perl(Parse::RecDescent)
%description
Parse::RecDescent incrementally generates top-down recursive-descent
text parsers from simple yacc-like grammar specifications. It
provides:

 * Regular expressions or literal strings as terminals (tokens)
 * Multiple (non-contiguous) productions for any rule
 * Repeated and optional subrules within productions
 * Full access to Perl within actions specified as part of the grammar
 * Simple automated error reporting during parser generation and parsing
 * The ability to commit to, uncommit to, or reject particular
   productions during a parse
 * The ability to pass data up and down the parse tree ("down" via
   subrule argument lists, "up" via subrule return values)
 * Incremental extension of the parsing grammar (even during a parse)
 * Precompilation of parser objects
 * User-definable reduce-reduce conflict resolution via "scoring" of
   matching productions

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Parse-RecDescent-%{version}

# Recode as UTF8
%patch -P0 -p1

# Fix permissions and script interpreters
chmod -c a-x demo/* tutorial/*
perl -pi -e 's|^#!\s?/usr/local/bin/perl\b|#!/usr/bin/perl|' demo/*

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README ToDo demo/ tutorial/
%{perl_vendorlib}/Parse/
%{_mandir}/man3/Parse::RecDescent.3*

%changelog
%autochangelog
