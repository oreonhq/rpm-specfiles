%global source0_hash a8792dd8c1aac97001032337b36a356be96e2d74c4f039ef9a363b641db4ae61

Name:           perl-Text-Reform
Version:        1.20
Release:        43%{?dist}
Summary:        Manual text wrapping and reformatting
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Reform
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHORNY/Text-Reform-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
# XXX: BuildRequires:  perl(TeX::Hyphen)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::More)
# Optional tests only
BuildRequires:  perl(Test::Pod) >= 1.14 
Requires:       perl(TeX::Hyphen)

%description
The module supplies a re-entrant, highly configurable replacement for the
built-in Perl format() mechanism.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-Reform-%{version}
chmod 644 -c Changes README lib/Text/*.pm

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# the testsuite fails for locales with decimal point != ".", i.e. it
# fails for almost all European languages except en
LC_NUMERIC=C ./Build test

%files
%doc Changes README demo/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
