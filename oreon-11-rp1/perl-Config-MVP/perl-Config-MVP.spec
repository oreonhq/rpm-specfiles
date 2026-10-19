%global source0_hash 018d161623ee3a67f860d9e680e22e61b79eae6018f0e7c3b525fc934f5b7d45
Name:           perl-Config-MVP
Version:        2.200013
Release:        1%{?dist}
Summary:        Multivalue-property package-oriented configuration
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Config-MVP
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Config-MVP-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Throwable)
Requires:       perl(Role::Identifiable::HasIdent)
Requires:       perl(Role::HasMessage)
Requires:       perl(StackTrace::Auto)
Requires:       perl(MooseX::OneArgNew)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::OneArgNew)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Role::HasMessage)
BuildRequires:  perl(Role::Identifiable::HasIdent)
BuildRequires:  perl(StackTrace::Auto)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Throwable)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
MVP is a mechanism for loading configuration (or other information) for
libraries. It doesn't read a file or a database. It's a helper for
things that do.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Config-MVP-%{version}

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
