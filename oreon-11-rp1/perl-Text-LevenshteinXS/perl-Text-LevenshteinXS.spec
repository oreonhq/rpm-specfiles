%global source0_hash e374ff7b237919ce5ea9245f356d1cb52cc87fd26b3a5a38b3f3e5ff82a01491
Name:           perl-Text-LevenshteinXS
Version:        0.03
Release:        1%{?dist}
Summary:        XS implementation of the Levenshtein edit distance
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-LevenshteinXS
Source0:        https://cpan.metacpan.org/authors/id/J/JG/JGOLDBERG/Text-LevenshteinXS-%{version}.tar.gz
Provides:       perl(Text::LevenshteinXS)
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module implements the Levenshtein edit distance in a XS way.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Text-LevenshteinXS-%{version}
perl -pi -e 's/\r//g' Changes README

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.03-58
- Prepare for Oreon 11 (RP1)
