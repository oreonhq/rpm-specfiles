%global source0_hash 6d87bcdfa63b28cefcfa870803a519b6590e3ea19c300f98cecb0e190bb19305
Name: 		perl-prefork
Version: 	1.05
Release:        22%{?dist}
Summary:        Optimized module loading for forking or non-forking processes
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/prefork
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/prefork-%{version}.tar.gz
BuildArch: noarch
Provides:       perl(prefork)
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  /usr/bin/perl
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Perl::MinimumVersion)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
# /oreon:deps
%description
Optimized module loading for forking or non-forking processes

prefork.pm is intended to serve as a central and optional marshalling
point for state detection (are we running in compile-time or run-time
mode) and to act as a relatively light-weight module loader.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n prefork-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test AUTOMATED_TESTING=1
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.05-22
- Prepare for Oreon 11 (RP1)
