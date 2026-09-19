%global source0_hash 04f361ee304256c41547d222b9f3b590fa22f0cdbb343f61632261a797816171

Name:           perl-CommonMark
Version:        0.310100
Release:        6%{?dist}
Summary:        Interface to the CommonMark C library
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CommonMark
Source0:        https://cpan.metacpan.org/authors/id/N/NW/NWELLNHOF/CommonMark-%{version}.tar.gz

# build requirements
BuildRequires:  cmark-devel >= 0.21.0
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(Devel::CheckLib)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime requirements
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Encode)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)

%description
This module is a wrapper around the official CommonMark C library libcmark.
It closely follows the original API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CommonMark-%{version}

%build
# -std=c17 is needed to fix build with GCC 15
# see https://github.com/Perl/perl5/issues/23192
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS -std=c17" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes
%license LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/CommonMark*
%{_mandir}/man3/*

%changelog
%autochangelog
