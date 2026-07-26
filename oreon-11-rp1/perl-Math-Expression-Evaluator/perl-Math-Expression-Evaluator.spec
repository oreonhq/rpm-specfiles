%global source0_hash 21b03869abd963be14c1acd1df824a22ba3a1f8e2a3fd8bd6fe1e6997472886a

# Perform optional tests
%bcond_without perl_Math_Expression_Evaluator_enables_optional_test

Name:           perl-Math-Expression-Evaluator
Version:        0.3.2
Release:        39%{?dist}
Summary:        Parses, compiles and evaluates mathematics expressions
# lib/Math/Expression/Evaluator/Lexer.pm:   (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-Public-Domain
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/Math-Expression-Evaluator
Source0:        https://cpan.metacpan.org/authors/id/M/MO/MORITZ/Math-Expression-Evaluator-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
# for iconv tool
BuildRequires:  glibc-common
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
%if %{with perl_Math_Expression_Evaluator_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
%endif

%description
Math::Expression::Evaluator is a parser, compiler and interpreter for
mathematical expressions. It can handle normal arithmetic (including
powers wit ^ or **), built-in functions like sin() and variables.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-Expression-Evaluator-v%{version}
iconv -f iso8859-1 -t utf-8 README > README.conv && mv -f README.conv README
# Remove unused file that is packaged by a mistake (becuase of its extension)
rm benchmark.pl
perl -i -ne 'print $_ unless m{^\Qbenchmark.pl\E}' MANIFEST
%if !%{with perl_Math_Expression_Evaluator_enables_optional_test}
for F in t/01-pod.t t/02-pod-coverage.t; do
    rm "$F"
    perl -i -ne 'print $_ unless m{^\Q'"$F"'\E}' MANIFEST
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
