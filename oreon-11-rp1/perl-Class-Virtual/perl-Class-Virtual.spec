%global source0_hash c6499b42d3b4e5c6488a5e82fbc28698e6c9860165072dddfa6749355a9cfbb2

Name:           perl-Class-Virtual
Version:        0.08
Release:        28%{?dist}
Summary:        Base class for virtual base classes in Perl
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Virtual

Source0:        https://cpan.metacpan.org/authors/id/M/MS/MSCHWERN/Class-Virtual-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

# Run-time:
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

# Testing
BuildRequires:  perl(base)
BuildRequires:  perl(Carp::Assert)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(Class::ISA)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

Requires:       perl(Carp)

%description
This is a base class for implementing virtual base classes (what some
people call an abstract class). It allows the programmer to explicitly
declare what methods are virtual and that must be implemented by subclasses.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-Virtual-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
