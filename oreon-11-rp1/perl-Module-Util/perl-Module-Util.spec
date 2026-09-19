%global source0_hash 6cfbcb6a45064446ec8aa0ee1a7dddc420b54469303344187aef84d2c7f3e2c6

Name:       perl-Module-Util
Version:    1.09
Release:    38%{?dist}
# see lib/Module/Util.pm
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Module name tools and transformations
Source:     https://cpan.metacpan.org/authors/id/M/MA/MATTLAW/Module-Util-%{version}.tar.gz
Url:        https://metacpan.org/release/Module-Util
BuildArch:  noarch
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(Module::Build)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
# Run-time
BuildRequires: perl(Exporter)
# ExtUtils::MakeMaker not used at tests
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Spec::Functions)
# Getopt::Long not used at tests
# List::Util not used at tests
# Pod::Usage not used at tests
# Tests
BuildRequires: perl(Test::More)

%{?perl_default_filter}

%description
This module provides a few useful functions for manipulating module names.
Its main aim is to centralize some of the functions commonly used by
modules that manipulate other modules in some way, like converting module
names to relative paths.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Util-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README t/
%dir %{perl_vendorlib}/Module
%{perl_vendorlib}/Module/Util.pm
%{_bindir}/pm_which
%{_mandir}/man1/pm_which.1*
%{_mandir}/man3/Module::Util.3*

%changelog
%autochangelog
