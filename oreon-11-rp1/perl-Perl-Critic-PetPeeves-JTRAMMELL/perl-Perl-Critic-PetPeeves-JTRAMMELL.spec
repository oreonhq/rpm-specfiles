%global source0_hash fb931eb3434b6b75339d079a469f7a389269df155f46ee5e7cc60c2ebbae4a04

Name:           perl-Perl-Critic-PetPeeves-JTRAMMELL
Version:        0.04
Release:        34%{?dist}
Summary:        Policies to prohibit/require my pet peeves
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl-Critic-PetPeeves-JTRAMMELL
Source0:        https://cpan.metacpan.org/authors/id/J/JT/JTRAMMELL/Perl-Critic-PetPeeves-JTRAMMELL-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Perl::Critic::Policy)
BuildRequires:  perl(Perl::Critic::Utils)
# Tests only:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(lib)
BuildRequires:  perl(Perl::Critic)
BuildRequires:  perl(Perl::Critic::Config)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

%description
Module Perl::Critic::PetPeeves::JTRAMMELL provides policies that I want
that haven't already been implemented elsewhere.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Perl-Critic-PetPeeves-JTRAMMELL-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
