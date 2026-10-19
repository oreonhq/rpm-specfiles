%global source0_hash bfa4a4e817eca722067c1ff3da12ab5ab80d6c57daa5e5e7ab9350ca2c71eb35
%global cpan_version 0.080001
Name:           perl-Math-Random-Secure
Version:        0.08.0001
Release:        1%{?dist}
Summary:        Cryptographically-secure, cross-platform replacement for rand()
License:        Artistic-2.0
URL:            https://metacpan.org/release/Math-Random-Secure
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FREW/Math-Random-Secure-%{cpan_version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Crypt::Random::Source::Factory)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Math::Random::ISAAC)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::SharedFork)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is intended to provide a cryptographically-secure replacement
for Perl's built-in rand function.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-Random-Secure-%{cpan_version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
