%global source0_hash 45108c239a7373d00941dcf0d171acd03e7c16a63ce6f7d9568ff052b17cf5a8

Name:           perl-Authen-SCRAM
Version:        0.011
Release:        24%{?dist}
Summary:        Salted Challenge Response Authentication Mechanism (RFC 5802)
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://metacpan.org/release/Authen-SCRAM
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Authen-SCRAM-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Authen::SASL::SASLprep) >= 1.100
BuildRequires:  perl(Carp)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Encode)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Moo) >= 1.001000
BuildRequires:  perl(Moo::Role) >= 1.001000
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(PBKDF2::Tiny) >= 0.003
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Types::Standard)
# Optional run-time:
# String::Compare::ConstantTime 0.310 do not build-require to exercise
# a fall-back code.
# Tests:
BuildRequires:  perl(base)
# CPAN::Meta not useful
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
# Authen-SCRAM-0.010 disabled String::Compare::ConstantTime temporarily.
#Recommends:   perl(String::Compare::ConstantTime) >= 0.310

%description
These Perl modules implement the Salted Challenge Response Authentication
Mechanism (SCRAM) from RFC 5802.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Authen-SCRAM-%{version}
# Fix shell bangs
perl -MConfig -i -p -e 's{\A#!/usr/bin/env perl\b}{$Config{startperl}}' \
    devel/scram-examples.pl

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc devel/scram-examples.pl Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
