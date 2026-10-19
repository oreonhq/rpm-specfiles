%global source0_hash 6f592d4cdf68e2330dee93dd38207c79f3fc194513bebacb8f5fd369fd00b663
Name:           perl-HTTP-CookieMonster
Version:        0.11
Release:        18%{?dist}
Summary:        Easy access to your jar of HTTP::Cookies
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-CookieMonster
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/HTTP-CookieMonster-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Moo) >= 1.000003
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Moo\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

unset AUTHOR_TESTING
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
