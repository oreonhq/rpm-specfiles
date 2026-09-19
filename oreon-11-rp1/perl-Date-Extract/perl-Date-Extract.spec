%global source0_hash fa078804ade4eeec1de1472e0e0bb047ae62e4c8d4d5020701b9e50577c5b8f4

Name:           perl-Date-Extract
Version:        0.07
Release:        8%{?dist}
Summary:        Date::Extract Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Date-Extract
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Date-Extract-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(DateTime::Format::Natural) >= 0.60
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Test::MockTime::HiRes)
BuildRequires:  perl(Test::More)

%description
Search a string for something that looks like a date string, and build a
DateTime object out of it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Date-Extract-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
