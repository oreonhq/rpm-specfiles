%global source0_hash 21bb3a597719888edb6ceaa132418d5cf92ecb92a50cce37b94259a55e0e3796
Name:           perl-MooseX-Types-DateTime-MoreCoercions
Version:        0.15
Release:        1%{?dist}
Summary:        Extensions to MooseX::Types::DateTime
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Types-DateTime-MoreCoercions
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-DateTime-MoreCoercions-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(namespace::autoclean)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(DateTimeX::Easy)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::DateTime)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Duration::Parse)
BuildRequires:  perl(if)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(ok)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module builds on MooseX::Types::DateTime to add additional custom
types and coercions. Since it builds on an existing type, all coercions
and constraints are inherited.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Types-DateTime-MoreCoercions-%{version}

%build

export PERL_MM_FALLBACK_SILENCE_WARNING=1
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
