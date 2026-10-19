%global source0_hash 55058911a99f1755de3eb449a99ffbeb92d88c01ff5dc60511a24679050ddea8
Name:           perl-Lingua-EN-Inflect-Phrase
Version:        0.20
Release:        24%{?dist}
Summary:        Inflect short English Phrases
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Lingua-EN-Inflect-Phrase
Source0:        https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/Lingua-EN-Inflect-Phrase-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Lingua::EN::FindNumber)
BuildRequires:  perl(Lingua::EN::Inflect)
BuildRequires:  perl(Lingua::EN::Inflect::Number)
BuildRequires:  perl(Lingua::EN::Number::IsOrdinal)
BuildRequires:  perl(Lingua::EN::Tagger)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(blib)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Attempts to pluralize or singularize short English phrases.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lingua-EN-Inflect-Phrase-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
