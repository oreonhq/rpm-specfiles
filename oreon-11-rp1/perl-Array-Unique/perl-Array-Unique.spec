%global source0_hash 653ce782b482800ece0bb0558e98f7a8f1986f41631261b9bb1598ab7accddf7

Name:           perl-Array-Unique
Version:        0.09
Release:        9%{?dist}
Summary:        Tie-able array that allows only unique values
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Array-Unique

Source0:        https://cpan.metacpan.org/authors/id/S/SZ/SZABGAB/Array-Unique-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)

# Testing
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Array)
BuildRequires:  perl(warnings)

%description
This package lets you create an array which will allow only one
occurrence of any value. In other words, no matter how many times
you put in 42 it will keep only the first occurrence and the rest
will be dropped. You use the module via tie and once you tied your
array to this module it will behave correctly.

Uniqueness is checked with the 'eq' operator so among other things
it is case sensitive. As a side effect the module does not allow
undef as a value in the array.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Array-Unique-%{version}

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
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
