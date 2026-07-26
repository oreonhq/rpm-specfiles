%global source0_hash c92b5a7801ed1617f3bdfd0937aa7153b8c874e434b9a03a99825f73e2b910e2

%define upstream_name Test-Some
Name:       perl-%{upstream_name}
Version:    0.2.1
Release:    16%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Group:      Development/Libraries
Summary:    Run a subset of tests
Source:     https://cpan.metacpan.org/authors/id/Y/YA/YANICK/%{upstream_name}-%{version}.tar.gz
Url:        https://metacpan.org/release/%{upstream_name}
BuildArch:  noarch
Requires:   perl-interpreter
BuildRequires: coreutils
BuildRequires: make
BuildRequires: perl(:VERSION) >= 5.10.0
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Package::Stash)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(blib)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: perl-generators

%description
This module allows one to run a subset of the 'subtest' tests given in a test
file.

The module declaration takes a whitelist of the subtests we want to run.
Any subtest that doesn't match any of the whitelist items will be skipped
(or potentially bypassed).

The test files don't even need to be modified, as the module can also be
invoked from the command-line.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1
%{make_build}

%install
%{make_install}

%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
