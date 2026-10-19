%global source0_hash 3e0d811c60f8df8e486f5d49b5d485b60293b0b1aad64efd6a51b5fbb9075773
Name:           perl-MooseX-Declare
Version:        0.43
Release:        1%{?dist}
Summary:        Declarative syntax for Moose
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Declare
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Declare-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(MooseX::Declare::Context::WithOptions) = %{version}
Provides:       perl(MooseX::Declare::StackItem) = %{version}
Provides:       perl(MooseX::Declare::Syntax::MethodDeclaration::Parameterized) = %{version}
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(Devel::Declare)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Method::Signatures)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(Test::Compile)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl-generators
# /oreon:deps
%description
This module provides syntactic sugar for Moose, the postmodern object
system for Perl 5. When used, it sets up the class and role keywords.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Declare-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
