%global source0_hash 6349c2bdee1533463061ad8eeea8621d8f8c0d4f9d7ae1b1eecdaf03cc906487

Name:           perl-Test-WriteVariants
Version:        0.014
Release:        26%{?dist}
Summary:        Dynamic generation of tests in nested combinations of contexts
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-WriteVariants
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/Test-WriteVariants-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Tumbler) >= 0.002
BuildRequires:  perl(File::Basename)
# File::Find::Rule bahaves as a hard dependency, CPAN RT#122100
BuildRequires:  perl(File::Find::Rule) >= 0.34
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Pluggable::Object) >= 4.9
BuildRequires:  perl(Module::Runtime)
# Optional run-time:
BuildRequires:  perl(File::Slurper)
# Tests:
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::Directory) >= 0.041
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Most)
# Optional tests:
BuildRequires:  perl(Module::Pluggable) >= 4.9
Requires:       perl(Data::Dumper)
Requires:       perl(Data::Tumbler) >= 0.002
# File::Find::Rule bahaves as a hard dependency, CPAN RT#122100
Requires:       perl(File::Find::Rule) >= 0.34
Suggests:       perl(File::Slurper)
Requires:       perl(Module::Pluggable::Object) >= 4.9

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Data::Tumbler|Module::Pluggable::Object)\\)$

%description
This is a library for generating Perl tests for every possible combination of
contexts. The output is another set of Perl test files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-WriteVariants-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license ARTISTIC-1.0 GPL-1 GPL-2.0 LICENSE
# TODO is empty
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
