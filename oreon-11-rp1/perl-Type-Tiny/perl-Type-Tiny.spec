%global source0_hash cd583e4983039f35052d490f0c4439124ba667d4f09c4e3aec47de5200f9921a

Name:           perl-Type-Tiny
Version:        2.010001
Release:        2%{?dist}
Summary:        Tiny, yet Moo(se)-compatible type constraint
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Type-Tiny
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Type-Tiny-%{version}.tar.gz
BuildArch:      noarch

# --with reply_plugin
#	Default: --without
# Marked as unstable (cf. lib/Reply/Plugin/TypeTiny.pm)
%bcond_with reply_plugin

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  sed
BuildRequires:  %{__make}
BuildRequires:  %{__perl}

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.6.1

BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
%if "%{version}" >= "2.000001"
BuildRequires:  perl(Exporter::Tiny) >= 1.004001
%else
BuildRequires:  perl(Exporter::Tiny) >= 0.040
%endif
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.17
%if "%{version}" >= "2.000001"
BuildRequires:  perl(experimental)
%endif
BuildRequires:  perl(feature)
BuildRequires:  perl(lib)
BuildRequires:  perl(Math::BigFloat)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Tester) >= 0.109
%if "%{version}" >= "2.000001"
BuildRequires:  perl(Test::Deep)
%endif
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(Tie::Hash)
BuildRequires:  perl(Tie::Scalar)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)

# optional
BuildRequires:  perl(boolean)
# N/A in Fedora: BuildRequires:  perl(Class::InsideOut)
BuildRequires:  perl(Class::ISA)
%if "%{version}" >= "2.000001"
# N/A in Fedora: BuildRequires:  perl(Class::Plain)
%endif
BuildRequires:  perl(Data::Constraint)
BuildRequires:  perl(Devel::Hide)
BuildRequires:  perl(Devel::LexAlias) >= 0.05
BuildRequires:  perl(Devel::Refcount)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Exporter) >= 5.59
BuildRequires:  perl(Function::Parameters)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(JSON::PP) >= 2.27105
# N/A in Fedora: BuildRequires:  perl(Kavorka)
BuildRequires:  perl(match::simple)
BuildRequires:  perl(Method::Generate::Accessor)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
%if !%{defined perl_bootstrap}
# Build cycle perl-MooX-TypeTiny <-> perl-Type-Tiny
BuildRequires:  perl(MooX::TypeTiny)
%endif
# N/A in Fedora: BuildRequires:  perl(Moops)
BuildRequires:  perl(Moose) >= 2.0400
BuildRequires:  perl(Moose::Meta::TypeCoercion)
BuildRequires:  perl(Moose::Meta::TypeCoercion::Union)
BuildRequires:  perl(Moose::Meta::TypeConstraint)
BuildRequires:  perl(Moose::Meta::TypeConstraint::Class)
BuildRequires:  perl(Moose::Meta::TypeConstraint::DuckType)
BuildRequires:  perl(Moose::Meta::TypeConstraint::Enum)
BuildRequires:  perl(Moose::Meta::TypeConstraint::Union)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Getopt) >= 0.63
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Common)
# N/A in Fedora: BuildRequires:  perl(MooseX::Types::DBIx::Class)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Mouse::Meta::TypeConstraint)
BuildRequires:  perl(Mouse::Util)
BuildRequires:  perl(Mouse::Util::TypeConstraints)
BuildRequires:  perl(MouseX::Types)
BuildRequires:  perl(MouseX::Types::Common)
BuildRequires:  perl(MouseX::Types::Moose)
BuildRequires:  perl(mro)
BuildRequires:  perl(Object::Accessor)
BuildRequires:  perl(re)
BuildRequires:  perl(Ref::Util::XS) > 0.100
%{?with_reply_plugin:BuildRequires:  perl(Reply::Plugin)}
%if !%{defined perl_bootstrap}
# Build-cycle: perl-Return-Type → perl-Type-Tiny
BuildRequires:  perl(Return::Type) >= 0.004
%endif
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Role::Tiny::With)
BuildRequires:  perl(Sub::Exporter::Lexical) >= 0.092291
BuildRequires:  perl(Specio)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Sub::Quote)
# N/A in Fedora: BuildRequires:  perl(Switcheroo)
%{?with_reply_plugin:BuildRequires:  perl(Term::ANSIColor)}
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::Warnings)
%if "%{version}" < "2.000001"
BuildRequires:  perl(Type::Tie)
%endif
# N/A in Fedora: BuildRequires:  perl(Types::ReadOnly)
%if !%{defined perl_bootstrap}
# Build-cycle: perl-Type-Tiny-XS → perl-Type-Tiny
BuildRequires:  perl(Type::Tiny::XS)
# Build-cycle: perl-Types-Path-Tiny → perl-Type-Tiny
BuildRequires:  perl(Types::Path::Tiny)
# Build-cycle: perl-Validation-Class → perl-Hash-Flatten → perl-Log-Trace
# → perl-Data-Serializer → perl-Crypt-CBC → perl-Crypt-PBKDF2 → perl-Type-Tiny
BuildRequires:  perl(Validation::Class) >= 7.900017
BuildRequires:  perl(Validation::Class::Simple)
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

%check
%{__make} test

%files
%doc Changes CREDITS NEWS README
%license LICENSE COPYRIGHT
%{perl_vendorlib}/Devel
%{perl_vendorlib}/Error
%{perl_vendorlib}/Eval
%{perl_vendorlib}/Type
%{perl_vendorlib}/Types
%{!?with_reply_plugin:%exclude %{perl_vendorlib}/Reply}
%{_mandir}/man3/Error::TypeTiny*
%{_mandir}/man3/Eval::TypeTiny*
%{_mandir}/man3/Reply::Plugin*
%{_mandir}/man3/Type::*
%{_mandir}/man3/Types::*
%exclude %{perl_vendorlib}/Test
%exclude %{_mandir}/man3/Test::TypeTiny.3pm*

%files -n perl-Test-TypeTiny
%{perl_vendorlib}/Test
%{_mandir}/man3/Test::TypeTiny.3pm*

%changelog
%autochangelog
