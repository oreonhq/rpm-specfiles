%global source0_hash c4bdcbe4daaeb50dcf40ea17dfb1483db22cb8832287abd8762a44ab98fb561f

# Tests with requirements that would need bootstrapping
%if ! (0%{?rhel})
%bcond_without perl_Moose_enables_optional_tests
%else
%bcond_with perl_Moose_enables_optional_tests
%endif

Name:           perl-Moose
Summary:        Complete modern object system for Perl 5
Version:        2.4000
Release:        5%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Moose
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Moose-%{version}.tar.gz
# configure / build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(lib)
# module runtime
BuildRequires:  perl(B)
BuildRequires:  perl(Carp) >= 1.22
BuildRequires:  perl(Class::Load) >= 0.09
BuildRequires:  perl(Class::Load::XS) >= 0.01
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::OptList) >= 0.107
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(Devel::OverloadInfo) >= 0.005
BuildRequires:  perl(Devel::PartialDump) >= 0.14
BuildRequires:  perl(Devel::StackTrace) >= 2.03
BuildRequires:  perl(Dist::CheckConflicts) >= 0.02
BuildRequires:  perl(Eval::Closure) >= 0.04
BuildRequires:  perl(Filter::Simple)
BuildRequires:  perl(if)
BuildRequires:  perl(List::Util) >= 1.56
BuildRequires:  perl(Module::Runtime) >= 0.014
BuildRequires:  perl(Module::Runtime::Conflicts) >= 0.002
BuildRequires:  perl(MRO::Compat) >= 0.05
BuildRequires:  perl(overload)
BuildRequires:  perl(Package::DeprecationManager) >= 0.11
BuildRequires:  perl(Package::Stash) >= 0.32
BuildRequires:  perl(Package::Stash::XS) >= 0.24
BuildRequires:  perl(Params::Util) >= 1.00
BuildRequires:  perl(parent) >= 0.223
BuildRequires:  perl(re)
BuildRequires:  perl(Scalar::Util) >= 1.19
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Exporter) >= 0.980
BuildRequires:  perl(Sub::Util) >= 1.40
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Try::Tiny) >= 0.17
BuildRequires:  perl(warnings)
# script runtime
BuildRequires:  perl(Getopt::Long)
# tests
BuildRequires:  perl(Algorithm::C3)
BuildRequires:  perl(CPAN::Meta::Check) >= 0.011
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::Fatal) >= 0.001
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs) >= 0.002010
BuildRequires:  perl(Tie::Scalar)
# optional tests
BuildRequires:  perl(CPAN::Meta) >= 2.120900
%if 0%{!?perl_bootstrap:1} && %{with perl_Moose_enables_optional_tests}
BuildRequires:  perl(Data::Visitor) >= 0.26
%endif
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Calendar::Mayan)
BuildRequires:  perl(DateTime::Format::MySQL)
BuildRequires:  perl(DBM::Deep) >= 1.003
BuildRequires:  perl(Declare::Constraints::Simple)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(Locale::US)
BuildRequires:  perl(Module::Refresh)
%if 0%{!?perl_bootstrap:1} && %{with perl_Moose_enables_optional_tests}
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooseX::MarkAsMethods)
BuildRequires:  perl(MooseX::NonMoose) >= 0.25
%endif
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Params::Coerce)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Specio) >= 0.10
BuildRequires:  perl(SUPER) >= 1.10
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Warnings) >= 0.016
%if 0%{!?perl_bootstrap:1} && %{with perl_Moose_enables_optional_tests}
# Break build cycle: perl-Moose → perl-Type-Tiny → perl-Moose
BuildRequires:  perl(Types::Standard)
%endif
BuildRequires:  perl(URI)
# versioned and optional dependencies
Requires:       perl(Class::Load) >= 0.09
Requires:       perl(Class::Load::XS) >= 0.01
Requires:       perl(Data::Dumper)
Requires:       perl(Data::OptList) >= 0.107
Requires:       perl(Devel::PartialDump) >= 0.14
Requires:       perl(Dist::CheckConflicts) >= 0.02
Requires:       perl(Eval::Closure) >= 0.04
Requires:       perl(Module::Runtime::Conflicts) >= 0.002
Requires:       perl(MRO::Compat) >= 0.05
Requires:       perl(Package::DeprecationManager) >= 0.11
Requires:       perl(Package::Stash) >= 0.32
Requires:       perl(Package::Stash::XS) >= 0.24
Requires:       perl(Params::Util) >= 1.00
Requires:       perl(parent) >= 0.223
Requires:       perl(Sub::Util) >= 1.40
Requires:       perl(Try::Tiny) >= 0.17

# hidden from PAUSE
Provides:       perl(Moose::Conflicts) = 0

# virtual provides for perl-Any-Moose
Provides:       perl(Any-Moose) = %{version}

%{?perl_default_filter}

Provides:       perl(Moose)
Provides:       perl(Moose::Role)
Provides:       perl(Moose::Util::TypeConstraints)
Provides:       perl(Class::MOP)
Provides:       perl(Class::MOP::Class)
Provides:       perl(Moose::Exporter)
Provides:       perl(Moose::Util::MetaRole)
Provides:       perl(metaclass)
Provides:       perl(Moose::Meta::Role)
Provides:       perl(Moose::Meta::TypeCoercion)
Provides:       perl(Moose::Meta::TypeCoercion::Union)
Provides:       perl(Moose::Meta::TypeConstraint)
Provides:       perl(Moose::Meta::TypeConstraint::Class)
Provides:       perl(Moose::Meta::TypeConstraint::DuckType)
Provides:       perl(Moose::Meta::TypeConstraint::Enum)
Provides:       perl(Moose::Meta::TypeConstraint::Union)
Provides:       perl(Moose::Util)
Provides:       perl(Test::Moose)
Provides:       perl(Moose::Exception)
Provides:       perl(Moose::Meta::Attribute)
Provides:       perl(Moose::Meta::Class)
Provides:       perl(Moose::Meta::Method)
Provides:       perl(Moose::Object)
Provides:       perl(Moose::Exporter)
Provides:       perl(Moose::Util::MetaRole)
%description
Moose is an extension of the Perl 5 object system.

The main goal of Moose is to make Perl 5 Object Oriented programming easier,
more consistent and less tedious. With Moose you can to think more about what
you want to do and less about the mechanics of OOP.

Additionally, Moose is built on top of Class::MOP, which is a metaclass system
for Perl 5. This means that Moose not only makes building normal Perl 5
objects better, but it provides the power of metaclass programming as well.
Moose is different from other Perl 5 object systems because it is not a new
system, but instead an extension of the existing one.

%package -n perl-Test-Moose
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Test functions for Moose specific features
Requires:   %{name} = %{version}-%{release}

%description -n perl-Test-Moose
This module provides some useful test functions for Moose based classes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Moose-%{version}

# silence rpmlint warnings
find benchmarks/ -type f -name '*.pl' -print0 \
  | xargs -0 sed -i '1s,#!.*perl,#!%{__perl},'
find t/ -type f -name '*.t' -print0 \
  | xargs -0 sed -i '1s,#!.*perl,#!%{__perl},'

%build
perl Makefile.PL \
  INSTALLDIRS=vendor \
  OPTIMIZE="%{optflags}" \
  NO_PERLLOCAL=1 \
  NO_PACKLIST=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes Changes.Class-MOP README.md TODO
%doc t/ benchmarks/ doc/
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/
%{_mandir}/man3/*
%{_bindir}/moose-outdated
%exclude %{perl_vendorarch}/Test
%exclude %{_mandir}/man3/Test::Moose*

%files -n perl-Test-Moose
%{perl_vendorarch}/Test
%{_mandir}/man3/Test::Moose*

%changelog
%autochangelog
