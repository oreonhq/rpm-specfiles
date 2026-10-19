%global source0_hash 2773f02fbf207e9745e76a037df08bf5a8cc987ed23c57040ce7f7b1561f2b7c
Name:           perl-Math-Random-ISAAC
Version:        1.004
Release:        1%{?dist}
Summary:        Perl interface to the ISAAC PRNG algorithm
License:        LicenseRef-Callaway-MIT OR GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Math-Random-ISAAC
Source0:        https://cpan.metacpan.org/authors/id/J/JA/JAWNSY/Math-Random-ISAAC-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
As with other Pseudo-Random Number Generator (PRNG) algorithms like the
Mersenne Twister (see Math::Random::MT), this algorithm is designed to take
some seed information and produce seemingly random results as output.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-Random-ISAAC-%{version}
/usr/bin/perl -pi -e 's/\r//' examples/*.pl

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
