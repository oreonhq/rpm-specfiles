%global source0_hash bfa4a4e817eca722067c1ff3da12ab5ab80d6c57daa5e5e7ab9350ca2c71eb35

%global cpan_version 0.080001
Name:           perl-Math-Random-Secure
Version:        0.08.0001
Release:        27%{?dist}
Summary:        Cryptographically-secure, cross-platform replacement for rand()
License:        Artistic-2.0

URL:            https://metacpan.org/release/Math-Random-Secure
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FREW/Math-Random-Secure-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Crypt::Random::Source::Factory)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(if)
BuildRequires:  perl(Math::Random::ISAAC)
BuildRequires:  perl(Moo)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::SharedFork)
BuildRequires:  perl(Test::Warn)
# Optional tests
BuildRequires:  perl(Test::LeakTrace)

%{?perl_default_filter}

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

%check
%{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Math*
%{_mandir}/man3/Math*

%changelog
%autochangelog
