%global source0_hash caa5d56e05145ca093735adaaf5fe7389974c4334e44b68aec7a78c089c7443f

Name:           perl-Data-Faker
Version:        0.10
Release:        33%{?dist}
Summary:        Perl extension for generating fake data
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Faker

Source0:        https://cpan.metacpan.org/authors/id/W/WS/WSHELDAHL/Data-Faker-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(POSIX)

# Testing
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
This module creates fake (but reasonable) data that can be used
for things such as filling databases with fake information during
development of database related applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Faker-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_bindir}/datafaker
%{_mandir}/man3/*

%changelog
%autochangelog
