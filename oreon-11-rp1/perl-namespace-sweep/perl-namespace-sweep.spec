%global source0_hash de99ce915ab0f93781580e3433d7dc9c2585a2789627173b280c6030ac0b1953

Name:           perl-namespace-sweep
Version:        0.006
Release:        27%{?dist}
Summary:        Sweep up imported subs in your classes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/namespace-sweep
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FRIEDO/namespace-sweep-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl-generators

BuildRequires:  perl(B::Hooks::EndOfScope) >= 0.09
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Package::Stash) >= 0.33
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Identify) >= 0.04
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Optional testsuite requirements
BuildRequires:	perl(Moo)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Mouse)

%description
Because Perl methods are just regular subroutines, it's difficult to tell
what's a method and what's just an imported function. As a result, imported
functions can be called as methods on your objects. This pragma will delete
imported functions from your class's symbol table, thereby ensuring that
your interface is as you specified it. However, code inside your module
will still be able to use the imported functions without any problems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n namespace-sweep-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}

%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
