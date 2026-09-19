%global source0_hash 5b8e52cffdd84a95d368ca10b943541b996a93e0d06396f4fe19335688e4173d

Name:           perl-MooX-Locale-TextDomain-OO
Version:        0.001
Release:        25%{?dist}
Summary:        Provide API used in translator modules without translating
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooX-Locale-TextDomain-OO
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/MooX-Locale-TextDomain-OO-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Locale::TextDomain::OO)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::Locale::Passthrough)
BuildRequires:  perl(Scalar::Util)
# Tests
BuildRequires:  perl(Locale::TextDomain::OO::Lexicon::Hash)
BuildRequires:  perl(Moo) >= 1.003
BuildRequires:  perl(Test::More) >= 0.90
Requires:       perl(Moo::Role) >= 1.003
Requires:       perl(MooX::Locale::Passthrough)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moo::Role\\)\\s*$

%description
This module provides API used in translator modules without translating.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooX-Locale-TextDomain-OO-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
