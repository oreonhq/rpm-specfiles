%global source0_hash 30e9dbfc5e0cc2ee14eae8f3465a908a710daecbd0a3ebdb2888fc4504fa18aa
Name: 		perl-Test-ClassAPI
Version: 	1.07
Release:        1%{?dist}
Summary:        Provides basic first-pass API testing for large class trees
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/Test-ClassAPI
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-ClassAPI-%{version}.tar.gz
BuildArch: 	noarch
%if !%{defined perl_bootstrap}
%endif
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  /usr/bin/perl
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
# /oreon:deps
%description
Provides basic first-pass API testing for large class trees.

For many APIs with large numbers of classes, it can be very useful to be 
able to do a quick once-over to make sure that classes, methods, and 
inheritance is correct, before doing more comprehensive testing.
This module aims to provide such a capability.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-ClassAPI-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%if !%{defined perl_bootstrap}
%{__make} test AUTOMATED_TESTING=1
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
