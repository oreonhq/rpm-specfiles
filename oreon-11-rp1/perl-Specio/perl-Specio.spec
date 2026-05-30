%global source0_hash 0d0eecfb9e89bd0f5f710fac42e1200a882d513a862f98497eaef5927ac6c183

# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Specio_enables_optional_test
%else
%bcond_with perl_Specio_enables_optional_test
%endif

Name:		perl-Specio
Version:	0.53
Release:	2%{?dist}
Summary:	Type constraints and coercions for Perl
# lib/Specio/PartialDump.pm:	GPL-1.0-or-later OR Artistic-1.0-Perl
#				<https://github.com/houseabsolute/Specio/issues/17>
# Other files:			Artistic-2.0
License:	Artistic-2.0 AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:		https://metacpan.org/release/Specio
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Specio-%{version}.tar.gz


BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Clone)
BuildRequires:	perl(Clone::PP)
BuildRequires:	perl(Devel::StackTrace)
BuildRequires:	perl(Eval::Closure)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(IO::File)
BuildRequires:	perl(List::Util) >= 1.33
BuildRequires:	perl(Module::Implementation)
BuildRequires:	perl(Module::Runtime)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(overload)
BuildRequires:	perl(parent)
BuildRequires:	perl(re)
BuildRequires:	perl(Ref::Util) >= 0.112
BuildRequires:	perl(Role::Tiny) >= 1.003003
BuildRequires:	perl(Role::Tiny::With)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(Sub::Quote)
BuildRequires:	perl(Sub::Util) >= 1.40
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::More) >= 0.96
BuildRequires:	perl(Try::Tiny)
BuildRequires:	perl(version) >= 0.83
BuildRequires:	perl(warnings)
BuildRequires:	perl(XString)
# Test Suite
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(lib)
BuildRequires:	perl(open)
BuildRequires:	perl(Test::Needs)
BuildRequires:	perl(utf8)
%if %{with perl_Specio_enables_optional_test}
# Optional Tests (note: Moose/Mouse use DateTime and hence Specio in their test suites)
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Prereqs)
BuildRequires:	perl(Moo)
%if !%{defined perl_bootstrap}
# Break cycle: perl-Moose → perl-DateTime → perl-Specio
BuildRequires:	perl(Moose) >= 2.1207
# Break cycle: perl-Mouse → perl-Moose → perl-DateTime → perl-Specio
BuildRequires:	perl(Mouse)
%endif
BuildRequires:	perl(namespace::autoclean)
%endif
# Dependencies
Requires:	perl(Ref::Util) >= 0.112
Requires:	perl(Sub::Util) >= 1.40
Requires:	perl(XString)

# Avoid provides for private packages
%global __provides_exclude ^perl\\(_T::.*\\)

%description
The Specio distribution provides classes for representing type constraints
and coercion, along with syntax sugar for declaring them.

Note that this is not a proper type system for Perl. Nothing in this
distribution will magically make the Perl interpreter start checking a value's
type on assignment to a variable. In fact, there's no built-in way to apply a
type to a variable at all.

Instead, you can explicitly check a value against a type, and optionally coerce
values to that type.

%package -n perl-Test-Specio
Summary:	Test helpers for Specio
License:	Artistic-2.0
Requires:	%{name} = %{version}-%{release}

%description -n perl-Test-Specio
This package provides some helper functions and variables for testing Specio
types.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Specio-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md GOVERNANCE.md README.md
%doc SECURITY.md SUPPORT.md TODO.md
%{perl_vendorlib}/Specio.pm
%{perl_vendorlib}/Specio/
%{_mandir}/man3/Specio.3*
%{_mandir}/man3/Specio::Coercion.3*
%{_mandir}/man3/Specio::Constraint::AnyCan.3*
%{_mandir}/man3/Specio::Constraint::AnyDoes.3*
%{_mandir}/man3/Specio::Constraint::AnyIsa.3*
%{_mandir}/man3/Specio::Constraint::Enum.3*
%{_mandir}/man3/Specio::Constraint::Intersection.3*
%{_mandir}/man3/Specio::Constraint::ObjectCan.3*
%{_mandir}/man3/Specio::Constraint::ObjectDoes.3*
%{_mandir}/man3/Specio::Constraint::ObjectIsa.3*
%{_mandir}/man3/Specio::Constraint::Parameterizable.3*
%{_mandir}/man3/Specio::Constraint::Parameterized.3*
%{_mandir}/man3/Specio::Constraint::Role::CanType.3*
%{_mandir}/man3/Specio::Constraint::Role::DoesType.3*
%{_mandir}/man3/Specio::Constraint::Role::Interface.3*
%{_mandir}/man3/Specio::Constraint::Role::IsaType.3*
%{_mandir}/man3/Specio::Constraint::Simple.3*
%{_mandir}/man3/Specio::Constraint::Structurable.3*
%{_mandir}/man3/Specio::Constraint::Structured.3*
%{_mandir}/man3/Specio::Constraint::Union.3*
%{_mandir}/man3/Specio::Declare.3*
%{_mandir}/man3/Specio::DeclaredAt.3*
%{_mandir}/man3/Specio::Exception.3*
%{_mandir}/man3/Specio::Exporter.3*
%{_mandir}/man3/Specio::Helpers.3*
%{_mandir}/man3/Specio::Library::Builtins.3*
%{_mandir}/man3/Specio::Library::Numeric.3*
%{_mandir}/man3/Specio::Library::Perl.3*
%{_mandir}/man3/Specio::Library::String.3*
%{_mandir}/man3/Specio::Library::Structured.3*
%{_mandir}/man3/Specio::Library::Structured::Dict.3*
%{_mandir}/man3/Specio::Library::Structured::Map.3*
%{_mandir}/man3/Specio::Library::Structured::Tuple.3*
%{_mandir}/man3/Specio::OO.3*
%{_mandir}/man3/Specio::PartialDump.3*
%{_mandir}/man3/Specio::Registry.3*
%{_mandir}/man3/Specio::Role::Inlinable.3*
%{_mandir}/man3/Specio::Subs.3*
%{_mandir}/man3/Specio::TypeChecks.3*

%files -n perl-Test-Specio
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Specio.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.53-2
- Prepare for Oreon 11 (RP1)
