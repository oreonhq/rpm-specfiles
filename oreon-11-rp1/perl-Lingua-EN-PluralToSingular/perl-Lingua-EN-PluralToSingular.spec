%global source0_hash f8a8b7de28c25c96190d7f48c90b5ad9b9bf517f3835c77641f0e8fa546c0d1d

Name:           perl-Lingua-EN-PluralToSingular
Version:        0.21
Release:        25%{?dist}
Summary:        Change an English plural to a singular
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Lingua-EN-PluralToSingular
Source0:        https://cpan.metacpan.org/authors/id/B/BK/BKB/Lingua-EN-PluralToSingular-%{version}.tar.gz

BuildArch:      noarch
# build deps
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl
# runtime deps
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test deps
BuildRequires:  perl(Test::More)

%description
This converts words denoting a plural in the English language into words
denoting a singular noun.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lingua-EN-PluralToSingular-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
# upstream package has no LICENSE file.
# https://github.com/benkasminbullock/Lingua-EN-PluralToSingular/issues/19
%doc Changes README
%{perl_vendorlib}/Lingua*
%{_bindir}/singular
%{_mandir}/man1/singular*
%{_mandir}/man3/Lingua*

%changelog
%autochangelog
