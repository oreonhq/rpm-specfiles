%global source0_hash 4fedaf72028511d80eb6afba523993e9aaa245d7af558345d5d4ed46e2e82ce1

Name:           perl-String-TtyLength
Version:        0.03
Release:        15%{?dist}
Summary:        Length or width of string excluding ANSI tty codes
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/pod/String::TtyLength
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/String-TtyLength-%{version}.tar.gz
BuildArch:      noarch
# build requirements
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime requirements
BuildRequires:  perl(Exporter)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(Unicode::EastAsianWidth) >= 12.0
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(utf8)

%{?perl_default_filter}

%description
This module provides two functions which tell you the length and width
of a string as it will appear on a terminal (tty), excluding any ANSI
escape codes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n String-TtyLength-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/String*
%{_mandir}/man3/String*

%changelog
%autochangelog
