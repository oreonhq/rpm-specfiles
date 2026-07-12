%global source0_hash 1d3780aa9bea430afbe65aa8c76e718f1045ce788aadda4116f59d3b7a7ad2b4

Name:           perl-MooX-Types-MooseLike
Version:        0.29
Release:        31%{?dist}
Summary:        Some Moosish types and a type builder
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooX-Types-MooseLike
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATEU/MooX-Types-MooseLike-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Runtime) >= 0.014
# If Moose-like implementation is used, Moose::* modules required in the
# code are not real Moose packages. Those are reimplementations mimicking
# them. Depending on them would defeat the purpose of an altertnative
# Moose-like implementation that replaces Moose. Those are:
# Moose::Meta::TypeConstraint::Class
# Moose::Meta::TypeConstraint::DuckType
# Moose::Meta::TypeConstraint::Enum
# Moose::Meta::TypeConstraint::Role
# Moose::Meta::TypeConstraint::Union
# Moose::Util::TypeConstraints
BuildRequires:  perl(Scalar::Util)
# Tests:
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Moo) >= 1.004002
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(overload)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Test::Fatal) >= 0.003
BuildRequires:  perl(Test::More) >= 0.96
Requires:   perl(Module::Runtime) >= 0.014

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Module::Runtime\\)$

Provides:       perl(MooX::Types::MooseLike)
Provides:       perl(MooX::Types::MooseLike::Base)
%description
See MooX::Types::MooseLike::Base for a list of available base types. Its source
also provides an example of how to build base types, along with both
parameterizable and non-parameterizable.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MooX-Types-MooseLike-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README
%{perl_vendorlib}/MooX*
%{_mandir}/man3/MooX*

%changelog
%autochangelog
