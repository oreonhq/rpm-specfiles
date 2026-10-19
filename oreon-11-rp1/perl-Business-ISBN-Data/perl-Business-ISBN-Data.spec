%global source0_hash 2838c159ffae256381c5f04bc8f0b9baff1483e85ddeff791268fcfefed0e8a0
Name:           perl-Business-ISBN-Data
Version:        20260704.001
Release:        1%{?dist}
Summary:        The data pack for Business::ISBN
License:        Artistic-2.0
URL:            https://metacpan.org/release/Business-ISBN-Data
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRIANDFOY/Business-ISBN-Data-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Business::ISBN::Data)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MM_Any)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::Manifest)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
