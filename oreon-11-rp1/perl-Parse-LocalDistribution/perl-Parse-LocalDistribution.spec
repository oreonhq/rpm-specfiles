%global source0_hash 664f4351e55ee9473c9b012af87d2832f652979cb89ade7954e6f38cd126a859

Name:           perl-Parse-LocalDistribution
Version:        0.20
Release:        2%{?dist}
Summary:        Parses local .pm files as PAUSE does
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Parse-LocalDistribution
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/Parse-LocalDistribution-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker::CPANfile)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Parse::CPAN::Meta)
BuildRequires:  perl(Parse::PMFile) >= 0.37
# Tests
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::UseAllModules) >= 0.10
Requires:       perl(Parse::PMFile) >= 0.37

%description
This is a sister module of Parse::PMFile. This module parses local .pm
files (and a META file if any) in a specific (current if not specified)
directory, and returns a hash reference that represents "provides"
information (with some extra meta data). This is almost the same as
Module::Metadata does (which has been in Perl core since Perl 5.13.9). The
main difference is the most of the code of this module is directly taken
from the PAUSE code as of June 2013. If you need better compatibility to
PAUSE, try this. If you need better performance, safety, or portability in
general, Module::Metadata may be a better and handier option (Parse::PMFile
(and thus Parse::LocalDistribution) actually evaluates code in the $VERSION
line (in a Safe compartment), which may be problematic in some cases).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Parse-LocalDistribution-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Parse
%{_mandir}/man3/Parse::LocalDistribution*

%changelog
%autochangelog
