%global source0_hash 6349c2bdee1533463061ad8eeea8621d8f8c0d4f9d7ae1b1eecdaf03cc906487
Name:           perl-Test-WriteVariants
Version:        0.014
Release:        26%{?dist}
Summary:        Dynamic generation of tests in nested combinations of contexts
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-WriteVariants
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/Test-WriteVariants-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Data::Dumper)
Requires:       perl(Data::Tumbler) >= 0.002
Requires:       perl(File::Find::Rule) >= 0.34
Suggests:       perl(File::Slurper)
Requires:       perl(Module::Pluggable::Object) >= 4.9
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Data::Tumbler|Module::Pluggable::Object)\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Tumbler)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Slurper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Test::Directory)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
