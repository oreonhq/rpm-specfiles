%global source0_hash 9ad343cd9f86d714be9b54b9c68a443d8acc6501b6ad6b15e9ca0130b2e96f08

Name:           perl-MooseX-ConfigFromFile
Version:        0.14
Release:        34%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        An abstract Moose role for setting attributes from a configfile
URL:            https://metacpan.org/release/MooseX-ConfigFromFile
Source:         https://cpan.metacpan.org/modules/by-module/MooseX/MooseX-ConfigFromFile-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.007
BuildRequires:  perl(strict)
BuildRequires:  sed
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Types::Path::Tiny) >= 0.005
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(if)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Without::Module)
# Optional Test Requirements
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(CPAN::Meta::Prereqs) >= 2.120900
BuildRequires:  perl(MooseX::Getopt)
# Dependencies
# (none)

# Avoid doc-file dependencies from tests
%{?perl_default_filter}

Provides:       perl(MooseX::ConfigFromFile)
%description
This is an abstract role which provides an alternate constructor for
creating objects using parameters passed in from a configuration file. The
actual implementation of reading the configuration file is left to concrete
subroles.

It declares an attribute 'configfile' and a class method 'new_with_config',
and requires that concrete roles derived from it implement the class method
'get_config_from_file'.

Attributes specified directly as arguments to 'new_with_config' supersede
those in the configfile.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MooseX-ConfigFromFile-%{version}

# Fix shellbangs in tests to placate rpmlint
sed -i '1s,#!perl,#!%{__perl},' t/*.t

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
%{_mandir}/man3/MooseX::ConfigFromFile.3*

%changelog
%autochangelog
