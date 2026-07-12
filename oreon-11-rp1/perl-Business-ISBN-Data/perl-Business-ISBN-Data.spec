%global source0_hash 2838c159ffae256381c5f04bc8f0b9baff1483e85ddeff791268fcfefed0e8a0

Name:           perl-Business-ISBN-Data
Version:        20260704.001
Release:        1%{?dist}
Summary:        The data pack for Business::ISBN
License:        Artistic-2.0
URL:            https://metacpan.org/release/Business-ISBN-Data
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRIANDFOY/Business-ISBN-Data-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MM_Any)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Manifest) >= 1.21
# Module Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More) >= 0.95
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
# Dependencies
# (none)

Provides:       perl(Business::ISBN::Data)
%description
This is a data pack for Business::ISBN.  You can update
the ISBN data without changing the version of Business::ISBN.
Most of the interesting stuff is in Business::ISBN.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Business-ISBN-Data-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes examples/ README.pod SECURITY.md t/
%{perl_vendorlib}/Business/
%{_mandir}/man3/Business::ISBN::Data.3*

%changelog
%autochangelog
