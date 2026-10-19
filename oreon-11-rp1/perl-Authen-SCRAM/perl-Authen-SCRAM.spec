%global source0_hash 45108c239a7373d00941dcf0d171acd03e7c16a63ce6f7d9568ff052b17cf5a8
Name:           perl-Authen-SCRAM
Version:        0.011
Release:        24%{?dist}
Summary:        Salted Challenge Response Authentication Mechanism (RFC 5802)
License:        Apache-2.0
URL:            https://metacpan.org/release/Authen-SCRAM
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Authen-SCRAM-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Authen::SASL::SASLprep)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(PBKDF2::Tiny)
BuildRequires:  perl(Test::FailWarnings)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
