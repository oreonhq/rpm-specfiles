%global source0_hash 0b26ba2b121d8004425d4485d1d46f59001c83763aa26624dff6220d7735d7f7

Name:           perl-String-Compare-ConstantTime
Version:        0.321
Release:        25%{?dist}
Summary:        Timing side-channel protected string compare
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/String-Compare-ConstantTime
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FRACTAL/String-Compare-ConstantTime-%{version}.tar.gz
# Fix CVE-2024-13939, bug #2355705, posted upstream
# <https://github.com/hoytech/String-Compare-ConstantTime/pull/21>
Patch0:         String-Compare-ConstantTime-0.321-Prevent-from-revealing-a-length-of-the-secrect.patch
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Encode)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)

%description
This module provides one function, "equals", which works like perl's "eq", but
which does not provide a timing side-channel. Such comparison is useful when
matching against a secret string.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n String-Compare-ConstantTime-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
# COPYING is not a license text
%doc Changes COPYING README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/String*
%{_mandir}/man3/*

%changelog
%autochangelog
