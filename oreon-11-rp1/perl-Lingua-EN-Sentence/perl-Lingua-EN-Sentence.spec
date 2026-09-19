%global source0_hash 5aef213ae0785e7bf854cc6c12530b87cc110843edcab227149cd72fceee34b9

Name:           perl-Lingua-EN-Sentence
Version:        0.34
Release:        8%{?dist}
Summary:        Module for splitting text into sentences
# "same as perl", cf. lib/Lingua/EN/Sentence.pm
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Lingua-EN-Sentence
Source0:        https://cpan.metacpan.org/authors/id/K/KI/KIMRYAN/Lingua-EN-Sentence-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  %{__perl}

BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Carp)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(locale)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings) >= 1.0.6
BuildRequires:  perl(Test::More) >= 0.94

%description
The Lingua::EN::Sentence module contains the function get_sentences, which
splits text into its constituent sentences, based on a regular expression
and a list of abbreviations (built in and given).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lingua-EN-Sentence-%{version}
iconv -f ISO-8859-1 -t utf-8 Changes > Changes~
mv Changes~ Changes
# Eliminate of invalid use-case of PREREQ_PM in Makefile.PL causing a bogus warning
sed -i -e "/'perl' => '5.10.0'/d" Makefile.PL

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install} DESTDIR="$RPM_BUILD_ROOT"
%{_fixperms} "$RPM_BUILD_ROOT"/*

%check
%{__make} test

%files
%license LICENCE
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
