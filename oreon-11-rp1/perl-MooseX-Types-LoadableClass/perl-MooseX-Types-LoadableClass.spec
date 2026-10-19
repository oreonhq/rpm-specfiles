%global source0_hash f105b69bcb44cd9856edfd62753ff58c35519ffa96e17cfc9ef30bdb98994ccc
Name:           perl-MooseX-Types-LoadableClass
Version:        0.016
Release:        1%{?dist}
Summary:        ClassName type constraint with coercion to load the class
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/MooseX-Types-LoadableClass
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-LoadableClass-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
ClassName type constraint with coercion to load the class.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Types-LoadableClass-%{version}

%build

/usr/bin/perl Build.PL --installdirs=vendor
./Build
%install
./Build install '--destdir=%{buildroot}' --create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
