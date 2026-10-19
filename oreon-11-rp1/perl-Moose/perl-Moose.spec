%global source0_hash c4bdcbe4daaeb50dcf40ea17dfb1483db22cb8832287abd8762a44ab98fb561f
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond_with perl_Moose_enables_optional_tests
Name:           perl-Moose
Summary:        Complete modern object system for Perl 5
Version:        2.4000
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Moose
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Moose-%{version}.tar.gz
%if 0%{!?perl_bootstrap:1} && %{with perl_Moose_enables_optional_tests}
%endif
%if 0%{!?perl_bootstrap:1} && %{with perl_Moose_enables_optional_tests}
%endif
%if 0%{!?perl_bootstrap:1} && %{with perl_Moose_enables_optional_tests}
%endif
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
Provides:       perl(Moose::Conflicts) = 0
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
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Algorithm::C3)
BuildRequires:  perl(B)
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Check)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Class::Load::XS)
BuildRequires:  perl(Config)
BuildRequires:  perl(DBM::Deep)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::OptList)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Calendar::Mayan)
BuildRequires:  perl(DateTime::Format::MySQL)
BuildRequires:  perl(Declare::Constraints::Simple)
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(Devel::OverloadInfo)
BuildRequires:  perl(Devel::PartialDump)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Dist::CheckConflicts)
BuildRequires:  perl(Eval::Closure)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Filter::Simple)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Locale::US)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Refresh)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Module::Runtime::Conflicts)
BuildRequires:  perl(Package::DeprecationManager)
BuildRequires:  perl(Package::Stash)
BuildRequires:  perl(Package::Stash::XS)
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Params::Coerce)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(SUPER)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Specio)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Tie::Scalar)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(re)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles perl-Test-Moose usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Test-Moose -f %{oreon_filedir}/perl-Test-Moose.list

%changelog

%autochangelog
