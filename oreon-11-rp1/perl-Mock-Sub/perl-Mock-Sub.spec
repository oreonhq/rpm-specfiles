%global source0_hash 86ac0ff242e712df040c559aa0dcb871914d92f4b86977cf1402b6f8131a9c10

Name:           perl-Mock-Sub
Version:        1.09
Release:        26%{?dist}
Summary:        Mock package, object and standard subroutines, with unit testing in mind
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mock-Sub

Source0:        https://cpan.metacpan.org/authors/id/S/ST/STEVEB/Mock-Sub-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Scalar::Util)

# Testing
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::CheckManifest) >= 0.9
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(lib)

%description
Easy to use and very lightweight module for mocking out sub calls. Very
useful for testing areas of your own modules where getting coverage may
be difficult due to nothing to test against, and/or to reduce test run
time by eliminating the need to call subs that you really don't want or
need to test.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mock-Sub-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -delete

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
