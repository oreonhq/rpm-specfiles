%global source0_hash 1adc0f105a32198a2a2b4da5b0e0f985f05efed99ce366190a790e165d675bf1

Name:           perl-Parse-EDID
Version:        1.0.7
Release:        23%{?dist}
Summary:        Extended display identification data (EDID) parser
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://metacpan.org/release/Parse-EDID
Source0:        https://cpan.metacpan.org/authors/id/G/GR/GROUSSE/Parse-EDID-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Kwalitee)
BuildRequires:  perl(Test::More) >= 0.93
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(warnings)

%description
This module provides some function to parse Extended Display Identification
Data binary data structures.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Parse-EDID-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -delete

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes LICENSE META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
