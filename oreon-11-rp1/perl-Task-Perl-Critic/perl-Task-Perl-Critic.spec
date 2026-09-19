%global source0_hash 626e4d746023b1f573f05a90fdcd0a0eb8f1b292882ac6535cadbdcd281f16ce

# This file is licensed under the terms of GNU GPLv2+.

# Perform optinoal tests
%bcond_without perl_Task_Perl_Critic_enables_optional_test

Name:           perl-Task-Perl-Critic
Version:        1.008
Release:        40%{?dist}
Summary:        Install everything Perl::Critic
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Task-Perl-Critic
Source0:        https://cpan.metacpan.org/authors/id/T/TH/THALJEF/Task-Perl-Critic-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Other requires from META.yml are not needed at build and check time. There
# is no code, no provided modules. Do not BuildRequire them.
# Tests only:
BuildRequires:  perl(Test::More)
%if %{with perl_Task_Perl_Critic_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
%endif
Requires:       perl(criticism) >= 1.02
Requires:       perl(Perl::Critic) >= 1.117
Requires:       perl(Perl::Critic::Bangs) >= 1.00
Requires:       perl(Perl::Critic::Compatibility) >= 1.000
Requires:       perl(Perl::Critic::Dynamic) >= 0.05
Requires:       perl(Perl::Critic::Itch)
Requires:       perl(Perl::Critic::Lax) >= 0.007
Requires:       perl(Perl::Critic::Moose)
Requires:       perl(Perl::Critic::More) >= 1.000
Requires:       perl(Perl::Critic::Nits) >= 1.000000
Requires:       perl(Perl::Critic::PetPeeves::JTRAMMELL) >= 0.01
Requires:       perl(Perl::Critic::Pulp) >= 3
Requires:       perl(Perl::Critic::Storable)
Requires:       perl(Perl::Critic::StricterSubs) >= 0.03
# Perl::Critic::Swift: 1.000003 is decimal notion for 1.0.3 version
Requires:       perl(Perl::Critic::Swift) >= 1.0.3
Requires:       perl(Perl::Critic::Tics) >= 0.005
Requires:       perl(Test::Perl::Critic) >= 1.02
Requires:       perl(Test::Perl::Critic::Progressive) >= 0.03

%description
This module does nothing but act as a placeholder. See Task.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Task-Perl-Critic-%{version}

%build
perl Makefile.PL installdirs=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
