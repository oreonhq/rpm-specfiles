%global source0_hash 1d3780aa9bea430afbe65aa8c76e718f1045ce788aadda4116f59d3b7a7ad2b4
Name:           perl-MooX-Types-MooseLike
Version:        0.29
Release:        1%{?dist}
Summary:        Some Moosish types and a type builder
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooX-Types-MooseLike
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATEU/MooX-Types-MooseLike-%{version}.tar.gz
BuildArch:      noarch
Requires:   perl(Module::Runtime) >= 0.014
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Module::Runtime\\)$
Provides:       perl(MooX::Types::MooseLike)
Provides:       perl(MooX::Types::MooseLike::Base)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
