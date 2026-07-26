%global source0_hash a7cac5bccee9f2e2d8ad0f605400163712cd0ac64df2fb834f760fb49f2f6fd0

Name:          perl-URI-FromHash 
Version:       0.05
Release:       30%{?dist}
Summary:       Build a URI from a set of named parameters 
# see lib/URI/FromHash.pm
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:       GPL-1.0-or-later OR Artistic-1.0-Perl

Url:           https://metacpan.org/release/URI-FromHash
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/URI-FromHash-%{version}.tar.gz 

BuildArch:     noarch
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Test::Fatal)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI) >= 1.22

%{?perl_default_filter}

%description
This module provides a simple one-subroutine "named parameters" style
interface for creating URIs. Underneath the hood it uses 'URI.pm', though
because of the simplified interface it may not support all possible options
for all types of URIs.

It was created for the common case where you simply want to have a simple
interface for creating syntactically correct URIs from known components
(like a path and query string). Doing this using the native 'URI.pm'
interface is rather tedious, requiring a number of method calls, which is
particularly ugly when done inside a templating system such as Mason or
TT2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n URI-FromHash-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/URI*
%{_mandir}/man3/URI*.3*

%changelog
%autochangelog
