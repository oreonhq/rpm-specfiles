%global source0_hash ee058a63912fa1fcb9a72498f56ca421a2056dc7f9f4b67837446d6421815615

# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Class_Tiny_enables_optional_test
%else
%bcond_with perl_Class_Tiny_enables_optional_test
%endif

Name:           perl-Class-Tiny
Version:        1.008
Release:        15%{?dist}
Summary:        Minimalist class construction
License:        Apache-2.0
URL:            https://metacpan.org/release/Class-Tiny
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Class-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
# Devel::GlobalDestruction not needed on Perl >= 5.14
# mro on Perl >= 5.10
BuildRequires:  perl(mro)
# Tests
BuildRequires:  perl(base)
# CPAN::Meta 2.120900 not helpful
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(subs)
BuildRequires:  perl(Test::More) >= 0.96
%if %{with perl_Class_Tiny_enables_optional_test}
# Optional test
BuildRequires:  perl(Test::FailWarnings)
%endif
# Devel::GlobalDestruction not needed on Perl >= 5.14
# mro on Perl >= 5.10
Requires:       perl(mro)

# Filter from requires
# Devel::GlobalDestruction not needed on Perl >= 5.14
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Devel::GlobalDestruction\\)

Provides:       perl(Class::Tiny)
%description
This module offers a minimalist class construction kit in around 120 lines
of code. Here is a list of features:

* defines attributes via import arguments
* generates read-write accessors
* supports lazy attribute defaults
* supports custom accessors
* superclass provides a standard new constructor
* new takes a hash reference or list of key/value pairs
* new has heuristics to catch constructor attribute typos
* new calls BUILD for each class from parent to child
* superclass provides a DESTROY method
* DESTROY calls DEMOLISH for each class from child to parent


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Class-Tiny-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.mkdn README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.008-15
- Prepare for Oreon 11 (RP1)
