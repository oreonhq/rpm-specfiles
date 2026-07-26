%global source0_hash 92fc3635711e48981240d5c5c4205377f89a46bbbe86eb8d79a26f2744d7450f

Name:           perl-Perl-Critic-Nits
Version:        1.0.0
Release:        42%{?dist}
Summary:        Policies of nits I like to pick
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl-Critic-Nits
Source0:        https://cpan.metacpan.org/authors/id/K/KC/KCOWGILL/Perl-Critic-Nits-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Perl::Critic::Policy) >= 1.07
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
# Tests:
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Perl::Critic::TestUtils)
BuildRequires:  perl(Test::More)
# Test::Perl::Critic not used
Requires:       perl(Perl::Critic::Policy) >= 1.07

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Perl::Critic::Policy\\)$

%description
The included policy is
Perl::Critic::Policy::ValuesAndExpressions::ProhibitAccessOfPrivateData.
It prohibits direct access to a hash-based object's hash.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl-Critic-Nits-v%{version}

%build
perl Makefile.PL INSTALLDIRS=perl
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_privlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
