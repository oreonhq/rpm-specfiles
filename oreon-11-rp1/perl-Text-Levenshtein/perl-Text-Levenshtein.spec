%global source0_hash 6d2e92232caf7550bd6fa8034b8ebbacccd81a8dcefa7a605a8ca539a15d2f22

Name:           perl-Text-Levenshtein
Version:        0.15
Release:        12%{?dist}
Summary:        Implementation of the Levenshtein edit distance
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Levenshtein
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Text-Levenshtein-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Unicode::Collate) >= 1.04
# Tests only
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
BuildRequires:  perl(parent)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(utf8)
Requires:       perl(Unicode::Collate) >= 1.04

%description
This module implements the Levenshtein edit distance. The Levenshtein edit
distance is a measure of the degree of proximity between two strings. This
distance is the number of substitutions, deletions or insertions ("edits")
needed to transform one string into the other one (and vice versa). When
two strings have distance 0, they are the same. To learn more about the
Levenshtein metric, have a look at the Wikipedia page
<http://en.wikipedia.org/wiki/Levenshtein_distance>.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Levenshtein-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
