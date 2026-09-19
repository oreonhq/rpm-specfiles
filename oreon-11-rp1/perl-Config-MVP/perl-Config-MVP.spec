%global source0_hash 018d161623ee3a67f860d9e680e22e61b79eae6018f0e7c3b525fc934f5b7d45

Name:           perl-Config-MVP
Version:        2.200013
Release:        9%{?dist}
Summary:        Multivalue-property package-oriented configuration
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Config-MVP
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Config-MVP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Class::Load) >= 0.17
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(Moose) >= 0.91
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::OneArgNew)
BuildRequires:  perl(overload)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Role::HasMessage)
BuildRequires:  perl(Role::Identifiable::HasIdent)
BuildRequires:  perl(StackTrace::Auto)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Throwable)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)
# not automatically detected
Requires:       perl(Throwable)
Requires:       perl(Role::Identifiable::HasIdent)
Requires:       perl(Role::HasMessage)
Requires:       perl(StackTrace::Auto)
Requires:       perl(MooseX::OneArgNew)

%{?perl_default_filter}

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

%check
%{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
