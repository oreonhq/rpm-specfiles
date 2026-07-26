%global source0_hash 122877276af68032eb6d7f899ff4ec91c9e21380198fba73839b2e04ecd4ba63

Name:           perl-Test-NiceDump
Version:        1.0.1
Release:        18%{?dist}
Summary:        Get a nice and human readable dump of objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-NiceDump/
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAKKAR/Test-NiceDump-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-tiem
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Data::Dump::Filtered)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(overload)
BuildRequires:  perl(Safe::Isa) >= 1.000010
BuildRequires:  perl(Test::Builder)
# Tests
BuildRequires:  perl(Test::More)

%description
This module uses Data::Dump::Filtered and a set of sensible filters to dump
test data in a more readable way.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-NiceDump-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING
make test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
