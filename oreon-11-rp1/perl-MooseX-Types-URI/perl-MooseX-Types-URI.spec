%global source0_hash 330ab1d134eef8542ae2b6852f0131eb53d7d903a02f90740cc00dc98eee08cc

Name:          perl-MooseX-Types-URI
Version:       0.10
Release:       3%{?dist}
Summary:       URI related types and coercions for Moose
# see lib/MooseX/Types/URI.pm
License:       GPL-1.0-or-later OR Artistic-1.0-Perl

URL:           https://metacpan.org/release/MooseX-Types-URI
Source:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-URI-%{version}.tar.gz
BuildArch:     noarch

# build requirements
BuildRequires: coreutils
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: sed
BuildRequires: perl(Module::Build::Tiny) >= 0.034
# runtime requirements
BuildRequires: perl(Moose) >= 0.50
BuildRequires: perl(MooseX::Types::Moose)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(URI)
BuildRequires: perl(URI::FromHash)
BuildRequires: perl(URI::QueryParam)
BuildRequires: perl(URI::WithBase)
BuildRequires: perl(URI::file)
BuildRequires: perl(namespace::autoclean)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
# test requirements
BuildRequires: perl(File::Spec)
BuildRequires: perl(Module::Metadata)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Util::TypeConstraints)
BuildRequires: perl(MooseX::Types::Path::Class)
BuildRequires: perl(MooseX::Types::Path::Class)
BuildRequires: perl(Path::Class)
BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::Needs)
BuildRequires: perl(Test::Warnings)
BuildRequires: perl(Test::Without::Module)
BuildRequires: perl(Test::use::ok)
BuildRequires: perl(namespace::clean) >= 0.08

%{?perl_default_filter}

%description
This package provides Moose types for fun (and profit) with the URI classes.

It has slightly DWIMier types than the the URI classes have due to
implementation details, so the types should be more forgiving when
ducktyping will work anyway (e.g. URI::WithBase does not inherit URI).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Types-URI-%{version}
/usr/bin/sed -i '1s,#!perl,#!/usr/bin/perl,' t/*.t

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc README Changes t/
%license LICENCE
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*.3*

%changelog
%autochangelog
