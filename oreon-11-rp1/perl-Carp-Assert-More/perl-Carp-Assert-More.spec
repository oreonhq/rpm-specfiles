%global source0_hash cdf7d445a2caeb55ff0a3f92f3b0f6d589a0bab935bb6028792e7e1261b48b14

Name:           perl-Carp-Assert-More
Version:        2.9.0
Release:        3%{?dist}
Summary:        Convenience wrappers around Carp::Assert
License:        Artistic-2.0
URL:            https://metacpan.org/release/Carp-Assert-More
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/Carp-Assert-More-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
# BuildRequires:  perl(Carp::Assert)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(constant)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.18
# Optional tests
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
Requires:       perl(Carp)

%description
Carp::Assert::More is a set of wrappers around the Carp::Assert
functions to make the habit of writing assertions even easier.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Carp-Assert-More-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README.md
%{perl_vendorlib}/Carp/
%{_mandir}/man3/Carp*.3pm*

%changelog
%autochangelog
