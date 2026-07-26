%global source0_hash 21bb3a597719888edb6ceaa132418d5cf92ecb92a50cce37b94259a55e0e3796

Name:           perl-MooseX-Types-DateTime-MoreCoercions
Version:        0.15
Release:        31%{?dist}
Summary:        Extensions to MooseX::Types::DateTime
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Types-DateTime-MoreCoercions
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-DateTime-MoreCoercions-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(DateTime) >= 0.4302
BuildRequires:  perl(DateTime::Duration) >= 0.4302
BuildRequires:  perl(DateTimeX::Easy) >= 0.085
BuildRequires:  perl(if)
BuildRequires:  perl(Moose) >= 0.41
BuildRequires:  perl(MooseX::Types) >= 0.04
BuildRequires:  perl(MooseX::Types::DateTime) >= 0.07
BuildRequires:  perl(MooseX::Types::Moose) >= 0.04
# MooseX::Types >= 0.42 needs namespace::autoclean
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean) >= 0.19
BuildRequires:  perl(Time::Duration::Parse) >= 0.06
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(ok)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
# Optional tests:
# CPAN::Meta 2.120900 is not needed but its absence causes an unitialized
# variable warning, CPAN RT#97618. We can live with the warning.
# MooseX::Types >= 0.42 needs namespace::autoclean
Requires:       perl(namespace::autoclean)

%description
This module builds on MooseX::Types::DateTime to add additional custom
types and coercions. Since it builds on an existing type, all coercions
and constraints are inherited.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Types-DateTime-MoreCoercions-%{version}

%build
# We prefer ExtUtils::MakeMaker over Module::Build::Tiny
export PERL_MM_FALLBACK_SILENCE_WARNING=1
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
