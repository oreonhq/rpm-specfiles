%global source0_hash 7e0fb7c39f56a2dccf9d0295c82f3031ee116e807f6a12a438fa4dd41b0ec187

Name: 		perl-Algorithm-Dependency
Version: 	1.112
Release: 	13%{?dist}
Summary: 	Algorithmic framework for implementing dependency trees
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/Algorithm-Dependency
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/Algorithm-Dependency-%{version}.tar.gz

BuildArch: noarch

BuildRequires: %{__perl}
BuildRequires: %{__make}

BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)		>= 0.80
BuildRequires: perl(Test::ClassAPI)	>= 0.6
BuildRequires: perl(Test::More)		>= 0.47
BuildRequires: perl(Params::Util)	>= 0.31
BuildRequires: perl(List::Util)		>= 1.11

BuildRequires: perl(Test::Pod)		>= 1.00
BuildRequires: perl(Test::CPAN::Meta)	>= 0.12
BuildRequires: perl(Perl::MinimumVersion) >= 1.20
BuildRequires: perl(Test::MinimumVersion) >= 0.008

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

%check
%{__make} test AUTOMATED_TESTING=1

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/Algorithm
%{_mandir}/man3/*

%changelog
%autochangelog
