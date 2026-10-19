%global source0_hash c9d5f15f0eb0722dabb6fe9f60eb9cc1701fcd06a4d9003e49cae5bbbddf87ca
Name:           perl-Test2-Tools-PerlCritic
Version:        0.08
Release:        1%{?dist}
Summary:        Testing tools to enforce Perl::Critic policies
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test2-Tools-PerlCritic
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Test2-Tools-PerlCritic-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Perl::Critic)
BuildRequires:  perl(Perl::Critic::Policy)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Test2::API)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(base)
BuildRequires:  perl(experimental)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Test for Perl::Critic violations using Test2. Although this testing tool
uses the Test2 API instead of the older Test::Builder API, the primary
motivation is to provide output in a more useful form. That is policy
violations are grouped by policy class, and the policy class name is
clearly displayed as a diagnostic. The author finds the former more useful
because he tends to address one type of violation at a time. The author
finds the latter more useful because he tends to want to lookup or adjust
the configuration of the policy as he is addressing violations.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test2-Tools-PerlCritic-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
