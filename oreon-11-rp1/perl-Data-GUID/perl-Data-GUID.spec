%global source0_hash 68ea77c73fca891382f206e12449094501b6fbf2e57f54902d5064227cfd8e2e

Name:           perl-Data-GUID
Version:        0.051
Release:        9%{?dist}
Summary:        Globally unique identifiers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-GUID
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Data-GUID-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators

BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::UUID) >= 1.148
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Sub::Exporter) >= 0.90
BuildRequires:  perl(Sub::Install) >= 0.03
BuildRequires:  perl(bytes)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# tests
BuildRequires:  perl(Test::More) >= 0.96

%description
Data::GUID provides a simple interface for generating and using globally
unique identifiers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-GUID-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install} DESTDIR="$RPM_BUILD_ROOT"
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
