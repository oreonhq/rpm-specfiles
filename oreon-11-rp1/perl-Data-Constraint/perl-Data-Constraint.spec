%global source0_hash 6b8ec3d57acb36dfff55da62268814325be49cb7e0a255ba198e42f28305fc72

Name:           perl-Data-Constraint
Version:        1.205
Release:        4%{?dist}
Summary:        Prototypical value checking
License:        Artistic-2.0

URL:            https://metacpan.org/dist/Data-Constraint
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRIANDFOY/Data-Constraint-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  %{__make}
BuildRequires:  %{__perl}

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.8

BuildRequires:  perl(Class::Prototyped)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)


Provides:       perl(Data::Constraint)
%description
A constraint is some sort of condition on a datum. This module checks one
condition against one value at a time, and I call the thing that checks
that condition the "constraint". A constraint returns true or false, and
that's it. It should have no side effects, it should not change program
flow, and it should mind its own business. Let the thing that calls the
constraint figure out what to do with it. I want something that says "yes"
or "no" (and I discuss why this needs a fancy module later).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Data-Constraint-%{version}

# bogus permissions in source tarball
chmod -x lib/Data/Constraint.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
