%global source0_hash cd583e4983039f35052d490f0c4439124ba667d4f09c4e3aec47de5200f9921a
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
Name:           perl-Type-Tiny
Version:        2.010001
Release:        1%{?dist}
Summary:        Tiny, yet Moo(se)-compatible type constraint
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Type-Tiny
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Type-Tiny-%{version}.tar.gz
BuildArch:      noarch
%bcond_with reply_plugin
%if "%{version}" >= "2.000001"
%else
%endif
%if "%{version}" >= "2.000001"
%endif
%if "%{version}" >= "2.000001"
%endif
%if "%{version}" >= "2.000001"
%endif
%if !%{defined perl_bootstrap}
%endif
%{?with_reply_plugin:BuildRequires:  perl(Reply::Plugin)}
%if !%{defined perl_bootstrap}
%endif
%{?with_reply_plugin:BuildRequires:  perl(Term::ANSIColor)}
%if "%{version}" < "2.000001"
%endif
%if !%{defined perl_bootstrap}
%endif
Requires:       perl(B::Deparse)
Requires:       perl(Carp)
Requires:       perl(Data::Dumper)
Recommends:	perl(Type::Tiny::XS)
Provides:       perl(Type::Tiny)
Provides:       perl(Types::Standard)
Provides:       perl(Type::Tie)
Provides:       perl(Eval::TypeTiny)
Provides:       perl(Type::Library)
Provides:       perl(Type::Parser)
Provides:       perl(Type::Utils)
Provides:       perl(Types::TypeTiny)
Provides:       perl(Type::Tiny)
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  /usr/bin/perl
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::ISA)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Constraint)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Devel::Hide)
BuildRequires:  perl(Devel::LexAlias)
BuildRequires:  perl(Devel::Refcount)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Function::Parameters)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Method::Generate::Accessor)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::TypeTiny)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Meta::TypeCoercion)
BuildRequires:  perl(Moose::Meta::TypeCoercion::Union)
BuildRequires:  perl(Moose::Meta::TypeConstraint)
BuildRequires:  perl(Moose::Meta::TypeConstraint::Class)
BuildRequires:  perl(Moose::Meta::TypeConstraint::DuckType)
BuildRequires:  perl(Moose::Meta::TypeConstraint::Enum)
BuildRequires:  perl(Moose::Meta::TypeConstraint::Union)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Getopt)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Common)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Mouse::Meta::TypeConstraint)
BuildRequires:  perl(Mouse::Util)
BuildRequires:  perl(Mouse::Util::TypeConstraints)
BuildRequires:  perl(MouseX::Types)
BuildRequires:  perl(MouseX::Types::Common)
BuildRequires:  perl(MouseX::Types::Moose)
BuildRequires:  perl(Object::Accessor)
BuildRequires:  perl(Ref::Util::XS)
BuildRequires:  perl(Return::Type)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Role::Tiny::With)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Specio)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Sub::Exporter::Lexical)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::Scalar)
BuildRequires:  perl(Type::Tiny::XS)
BuildRequires:  perl(Types::Path::Tiny)
BuildRequires:  perl(Validation::Class)
BuildRequires:  perl(Validation::Class::Simple)
BuildRequires:  perl(boolean)
BuildRequires:  perl(constant)
BuildRequires:  perl(experimental)
BuildRequires:  perl(feature)
BuildRequires:  perl(lib)
BuildRequires:  perl(match::simple)
BuildRequires:  perl(mro)
BuildRequires:  perl(overload)
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
Type::Tiny is a tiny class for creating Moose-like type constraint objects
which are compatible with Moo, Moose and Mouse.

%package -n perl-Test-TypeTiny
Summary: Test::TypeTiny module
%description -n perl-Test-TypeTiny
Test::TypeTiny module.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Type-Tiny-%{version}
# Remove bundled modules
rm -r ./inc
sed -i -e '/^inc\//d' MANIFEST

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install} DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles perl-Test-TypeTiny usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{__make} test
%files -f %{oreon_filedir}/main.list
%files -n perl-Test-TypeTiny -f %{oreon_filedir}/perl-Test-TypeTiny.list

%changelog

%autochangelog
