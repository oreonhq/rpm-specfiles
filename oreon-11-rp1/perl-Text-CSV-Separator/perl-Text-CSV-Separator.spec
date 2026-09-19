%global source0_hash 454ac7ae1b14f3694efe824bdf948b534ef214c4a657ca2df9b61625d1c6c31d

Name:           perl-Text-CSV-Separator
Version:        0.20
Release:        38%{?dist}
Summary:        Determine the field separator of a CSV file
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-CSV-Separator
Source0:        https://cpan.metacpan.org/authors/id/E/EN/ENELL/Text-CSV-Separator-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
This module provides a fast detection of the field separator character
(also called field delimiter) of a CSV file, or more generally, of a
character separated text file (also called delimited text file), and
returns it ready to use in a CSV parser (e.g., Text::CSV_XS, Tie::CSV_File,
or Text::CSV::Simple).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-CSV-Separator-%{version}
sed -i 's/\r//' README Changes

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
