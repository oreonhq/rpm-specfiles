%global source0_hash 7ae89620f38827dbad2313a4e5f734049958f5d6212bd62abdbcb8ae936dcbc7

# Run extra test
%if ! (0%{?rhel})
%bcond_without perl_MooseX_Getopt_enables_extra_test
%else
%bcond_with perl_MooseX_Getopt_enables_extra_test
%endif

Name:           perl-MooseX-Getopt
Summary:        Moose role for processing command line options
Version:        0.78
Release:        4%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Getopt
Source0:        https://cpan.metacpan.org/modules/by-module/MooseX/MooseX-Getopt-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  sed
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Getopt::Long) >= 2.37
BuildRequires:  perl(Getopt::Long::Descriptive) >= 0.081
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Meta::Attribute)
BuildRequires:  perl(Moose::Role) >= 0.56
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(if)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose::Meta::Class)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Path::Tiny) >= 0.009
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal) >= 0.003
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Requires) >= 0.05
BuildRequires:  perl(Test::Trap)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(version)
# Optional Test Requirements
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.120900
# MooseX::SimpleConfig → MooseX::ConfigFromFile → MooseX::Types::Path::Class → MooseX::Getopt
%if !0%{?perl_bootstrap} && %{with perl_MooseX_Getopt_enables_extra_test}
BuildRequires:  perl(MooseX::ConfigFromFile) >= 0.08
BuildRequires:  perl(MooseX::SimpleConfig) >= 0.07
BuildRequires:  perl(MooseX::StrictConstructor)
%endif
BuildRequires:  perl(Test::Warnings) >= 0.034
BuildRequires:  perl(YAML)
# Dependencies
# (none)

# Make sure we don't get doc-file dependencies from the tests
%{?perl_default_filter}

Provides:       perl(MooseX::Getopt)
%description
This is a Moose role which provides an alternate constructor for creating
objects using parameters passed in from the command line.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MooseX-Getopt-%{version}

# Silence rpmlint warnings
sed -i '1s,#!.*perl,#!%{__perl},' t/*.t
chmod -c -x t/104_override_usage.t

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0

%check
./Build test

%files
%license LICENSE
%doc Changes CONTRIBUTING README t/
%{perl_vendorlib}/MooseX/
%{_mandir}/man3/MooseX::Getopt.3*
%{_mandir}/man3/MooseX::Getopt::Basic.3*
%{_mandir}/man3/MooseX::Getopt::Dashes.3*
%{_mandir}/man3/MooseX::Getopt::GLD.3*
%{_mandir}/man3/MooseX::Getopt::Meta::Attribute.3*
%{_mandir}/man3/MooseX::Getopt::Meta::Attribute::NoGetopt.3*
%{_mandir}/man3/MooseX::Getopt::Meta::Attribute::Trait.3*
%{_mandir}/man3/MooseX::Getopt::Meta::Attribute::Trait::NoGetopt.3*
%{_mandir}/man3/MooseX::Getopt::OptionTypeMap.3*
%{_mandir}/man3/MooseX::Getopt::ProcessedArgv.3*
%{_mandir}/man3/MooseX::Getopt::Strict.3*

%changelog
%autochangelog
