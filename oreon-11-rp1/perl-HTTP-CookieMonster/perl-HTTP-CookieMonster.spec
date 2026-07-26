%global source0_hash 6f592d4cdf68e2330dee93dd38207c79f3fc194513bebacb8f5fd369fd00b663

Name:           perl-HTTP-CookieMonster
Version:        0.11
Release:        18%{?dist}
Summary:        Easy access to your jar of HTTP::Cookies
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-CookieMonster
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-CookieMonster-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(Moo) >= 1.000003
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(URI::Escape)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
# Optional tests:
# CPAN::Meta not heplful
# CPAN::Meta::Prereqs not helpful
Requires:       perl(Moo) >= 1.000003

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Moo\\)$

%description
HTTP::CookieMonster gives you a simple interface for getting and setting
cookies in HTTP::Cookies objects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTTP-CookieMonster-%{version}
# Correct a shebang
perl -i -p -MConfig -e 's{\A#!/usr/bin/env perl\b}{$Config{startperl}}' \
    examples/read_cookies.pl

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING
make test

%files
%license LICENSE
%doc Changes CONTRIBUTORS examples README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
