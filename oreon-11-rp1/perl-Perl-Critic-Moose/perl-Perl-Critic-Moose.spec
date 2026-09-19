%global source0_hash 52eb8e22c42643f17fe297a21714017efdb9e2986c24e3337e030f3650f92201

Name:           perl-Perl-Critic-Moose
Version:        1.05
Release:        28%{?dist}
Summary:        Policies for Perl::Critic concerned with using Moose
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl-Critic-Moose
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Perl-Critic-Moose-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Perl::Critic::Policy)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Perl::Critic::Utils::PPI)
BuildRequires:  perl(Readonly)
# Tests only
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Perl::Critic::Policy)

%description
Some Perl::Critic policies that will help you keep your code in good shape
with regards to Moose.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl-Critic-Moose-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING.md README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
