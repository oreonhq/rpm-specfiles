%global source0_hash fb931eb3434b6b75339d079a469f7a389269df155f46ee5e7cc60c2ebbae4a04
Name:           perl-Perl-Critic-PetPeeves-JTRAMMELL
Version:        0.04
Release:        1%{?dist}
Summary:        Policies to prohibit/require my pet peeves
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Perl-Critic-PetPeeves-JTRAMMELL
Source0:        https://cpan.metacpan.org/authors/id/J/JT/JTRAMMELL/Perl-Critic-PetPeeves-JTRAMMELL-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Perl::Critic)
BuildRequires:  perl(Perl::Critic::Config)
BuildRequires:  perl(Perl::Critic::Policy)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
