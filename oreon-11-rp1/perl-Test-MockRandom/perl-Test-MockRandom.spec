%global source0_hash 2614930d84fc5deac39afbc1ee86ccd39b221507f27d4ee493ca26e5c921cce0

Name:           perl-Test-MockRandom
Version:        1.01
Release:        27%{?dist}
Summary:        Replaces random number generation with non-random number generation
License:        Apache-2.0
URL:            https://metacpan.org/release/Test-MockRandom
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-MockRandom-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
# Tests
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(lib)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(version)

Provides:       perl(Test::MockRandom)
%description
This perhaps ridiculous-seeming module was created to test routines that
manipulate random numbers by providing a known output from rand. Given a
list of seeds with srand, it will return each in turn. After seeded
random numbers are exhausted, it will always return 0. Seed numbers must
be of a form that meets the expected output from rand as called with no
arguments -- i.e. they must be between 0 (inclusive) and 1 (exclusive).
In order to facilitate generating and testing a nearly-one number, this
module exports the function oneish, which returns a number just
fractionally less than one.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-MockRandom-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CONTRIBUTING Changes examples README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
