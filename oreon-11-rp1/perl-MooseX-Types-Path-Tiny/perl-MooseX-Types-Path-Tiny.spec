%global source0_hash 19eede02dd654e70f73e34cd7af0063765173bcaefeeff1bdbe21318ecfd9158
Name:		perl-MooseX-Types-Path-Tiny
Summary:        Path::Tiny types and coercions for Moose
Version:	0.012
Release:        27%{?dist}
License:	Apache-2.0
URL:		https://metacpan.org/release/MooseX-Types-Path-Tiny
Source0:        https://cpan.metacpan.org/modules/by-module/MooseX/MooseX-Types-Path-Tiny-%{version}.tar.gz
BuildArch:	noarch
Requires:	perl(MooseX::Getopt)
Requires:	perl(namespace::autoclean)
Provides:       perl(MooseX::Types::Path::Tiny)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Conflicts)
BuildRequires:  perl(MooseX::Getopt)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Types::Stringlike)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(if)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides Path::Tiny types for Moose. It handles two important
types of coercion:

 * Coercing objects with overloaded stringification

 * Coercing to absolute paths

It also can check to ensure that files or directories exist.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MooseX-Types-Path-Tiny-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
