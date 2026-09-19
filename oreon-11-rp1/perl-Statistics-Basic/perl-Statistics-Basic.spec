%global source0_hash 6855ce5615fd3e1af4cfc451a9bf44ff29a3140b4e7130034f1f0af2511a94fb

# Perform optional tests
%bcond_without perl_Statistics_Basic_enables_optional_test

Name:           perl-Statistics-Basic
Version:        1.6611
Release:        33%{?dist}
Summary:        A collection of very basic statistics modules
# lib/Statistics/Basic/Mean.pod:    LGPLv2+
# lib/Statistics/Basic.pod:         LGPLv2
# Automatically converted from old format: LGPLv2 and LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2 AND LicenseRef-Callaway-LGPLv2+
URL:            https://metacpan.org/release/Statistics-Basic
Source0:        https://cpan.metacpan.org/authors/id/J/JE/JETTERO/Statistics-Basic-%{version}.tar.gz
BuildArch:      noarch
%if !%{with perl_Statistics_Basic_enables_optional_test}
BuildRequires:  coreutils
%endif
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Number::Format) >= 1.42
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
# Tests
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
%if %{with perl_Statistics_Basic_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Math::BigFloat) >= 1.60
# Test::Perl::Critic not used
# Test::Pod not used
# Test::Pod::Coverage not used
%endif
Requires:       perl(Number::Format) >= 1.42

# Remove underspecified dependecies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Number::Format\\)$

%description
use Statistics::Basic qw(:all);

my $median = median( 1,2,3 );
my $mean   = mean(  [1,2,3]); # array refs are ok too

my $variance = variance( 1,2,3 );
my $stddev   = stddev(   1,2,3 );

my $correlation = correlation( [1 .. 3], [1 .. 3] );

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Statistics-Basic-%{version}
%if !%{with perl_Statistics_Basic_enables_optional_test}
rm t/60_bigfloats.t
perl -i -ne 'print $_ unless m{^t/60_bigfloats\.t\b}' MANIFEST
%endif

%build
perl Makefile.PL INSTALLDIRS=perl NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset DEBUG_STATS_B IPRES NOFILL TEST_AUTHOR TOLER
make test

%files
%doc Changes README
%{perl_privlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
