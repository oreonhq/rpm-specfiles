%global source0_hash 7e0fb7c39f56a2dccf9d0295c82f3031ee116e807f6a12a438fa4dd41b0ec187
Name: 		perl-Algorithm-Dependency
Version: 	1.112
Release:        1%{?dist}
Summary:        Algorithmic framework for implementing dependency trees
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/Algorithm-Dependency
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Algorithm-Dependency-%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  //bin/perl
BuildRequires:  /usr/bin/make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Perl::MinimumVersion)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::ClassAPI)
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl-generators
# /oreon:deps
%description
Algorithm::Dependency is a framework for creating simple read-only
dependency hierarchies, where you have a set of items that rely on other
items in the set, and require actions on them as well.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Algorithm-Dependency-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test AUTOMATED_TESTING=1
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
