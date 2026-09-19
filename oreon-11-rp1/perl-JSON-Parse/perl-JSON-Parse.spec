%global source0_hash 6273180f9392497401ddd6d820706f5aa86c1be88891dd6aab4d906b5cff66d9

Name:           perl-JSON-Parse
Version:        0.62
Release:        14%{?dist}
Summary:        Read JSON into a Perl variable
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/JSON-Parse
Source0:        https://cpan.metacpan.org/authors/id/B/BK/BKB/JSON-Parse-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
A Perl module for parsing JSON. (JSON means "JavaScript Object Notation" and it
is specified in "RFC 7159".)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n JSON-Parse-%{version}
/usr/bin/perl -pi -e 's#/home/ben/software/install/bin/perl#/usr/bin/perl#' script/* examples/*
/usr/bin/chmod -x examples/tokenize-synopsis.pl

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README examples
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/JSON*
%{_mandir}/man3/*
%{_bindir}/validjson

%changelog
%autochangelog
