%global source0_hash 6afb541f6df6b535ccf7642d361ae18d7a95a3f93ace1bc5373f64c2410ca5af

Name:           perl-Email-Address
Version:        1.913
Release:        9%{?dist}
Summary:        RFC 2822 Address Parsing and Creation (DEPRECATED)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Email-Address
Source0:        https://cpan.metacpan.org/modules/by-module/Email/Email-Address-%{version}.tar.gz



BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.12
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
# Module
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::MIME::Header)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Time::HiRes)
# Dependencies

%description
This class implements a regex-based RFC 2822 parser that locates email
addresses in strings and returns a list of Email::Address objects found.
Alternatively you may construct objects manually. The goal of this software
is to be correct, and very very fast.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Email-Address-%{version}
perl -pi -e 's|^#!/usr/local/bin/perl\b|#!%{__perl}|' bench/ea-vs-ma.pl


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}


%install
%{make_install}
%{_fixperms} -c %{buildroot}


%check
make test


%files
%license LICENSE
%doc Changes README bench/
%{perl_vendorlib}/Email/
%{_mandir}/man3/Email::Address.3*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.913-9
- Import
