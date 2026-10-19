%global source0_hash 3e7d14fa97f31f4862eaf24fa5fa24892aaeb7b363e15222dcdcc82a7caf5e50
Name:           perl-Text-Levenshtein-Damerau
Version:        0.41
Release:        1%{?dist}
Summary:        Damerau Levenshtein edit distance
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Levenshtein-Damerau
Source0:        https://cpan.metacpan.org/authors/id/U/UG/UGEXE/Text-Levenshtein-Damerau-%{version}.tar.gz
BuildArch:      noarch
Recommends:     perl(Text::Levenshtein::Damerau::XS)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Returns the true Damerau Levenshtein edit distance of strings with adjacent
transpositions. Useful for fuzzy matching, DNA variation metrics, and fraud
detection.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Levenshtein-Damerau-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
