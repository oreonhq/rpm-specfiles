Name:           perl-Text-LevenshteinXS
Version:        0.03
Release:        58%{?dist}
Summary:        XS implementation of the Levenshtein edit distance
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-LevenshteinXS
Source0:        https://cpan.metacpan.org/authors/id/J/JG/JGOLDBERG/Text-LevenshteinXS-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 e374ff7b237919ce5ea9245f356d1cb52cc87fd26b3a5a38b3f3e5ff82a01491
%global source0_file Text-LevenshteinXS-0.03.tar.gz
# oreon url source checksums end
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test)

%description
This module implements the Levenshtein edit distance in a XS way.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Text-LevenshteinXS-0.03.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e374ff7b237919ce5ea9245f356d1cb52cc87fd26b3a5a38b3f3e5ff82a01491" || { echo "oreon: Source0 SHA256 mismatch for Text-LevenshteinXS-0.03.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Text-LevenshteinXS-%{version}
perl -pi -e 's/\r//g' Changes README

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Text*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.03-58
- Prepare for Oreon 11 (RP1)
