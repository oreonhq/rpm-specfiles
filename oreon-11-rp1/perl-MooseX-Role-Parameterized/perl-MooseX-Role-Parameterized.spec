%global source0_hash 1cfe766c5d7f0ecab57f733dcca430a2a2acd6b995757141b940ade3692bec9e
Name:           perl-MooseX-Role-Parameterized
Summary:        Make your roles flexible through parameterization
Version:        1.11
Release:        19%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Role-Parameterized
Source0:        https://cpan.metacpan.org/modules/by-module/MooseX/MooseX-Role-Parameterized-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Moose) >= 2.0300
Provides:       perl(MooseX::Role::Parameterized)
Provides:       perl(MooseX::Role::Parameterized)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Check)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Meta::Role)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Role::WithOverloading)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
Roles are composable units of behavior. They are useful for factoring out
functionality common to many classes from any part of your class hierarchy.
(See Moose::Cookbook::Roles::Recipe1 for an introduction to Moose::Role.)

While combining roles affords you a great deal of flexibility, individual
roles have very little in the way of configurability. Core Moose provides
alias for renaming methods to avoid conflicts, and excludes for ignoring
methods you don't want or need (see Moose::Cookbook::Roles::Recipe2 for more
about alias and excludes).

Because roles serve many different masters, they usually provide only the
least common denominator of functionality. To empower roles further, more
configurability than alias and excludes is required. Perhaps your role needs
to know which method to call when it is done. Or what default value to use for
its url attribute.

Parameterized roles offer exactly this solution.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MooseX-Role-Parameterized-%{version}
sed -i -e '1s,#!.*perl,,' t/*.t

%build

PERL_MM_FALLBACK_SILENCE_WARNING=1 perl Makefile.PL \
  INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
