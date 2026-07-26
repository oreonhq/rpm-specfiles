%global source0_hash 18f277820aaab1d4c4733fec5eb9e31f05ae69ca8f0a9c09ab01515535dd6a45

Summary:	Perl extension to create simple calendars
Name:		perl-Calendar-Simple
Version:	2.1.0
Release:	5%{?dist}

License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Calendar-Simple
Source0:	https://cpan.metacpan.org/authors/id/D/DA/DAVECROSS/Calendar-Simple-v%{version}.tar.gz
BuildArch:	noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl-generators

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Required by the tests
BuildRequires:	perl(DateTime)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)

%description
Perl extension to create simple calendars.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Calendar-Simple-v%{version}
chmod -x lib/*/Simple.pm

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes.md README
%{_bindir}/pcal
%{perl_vendorlib}/Calendar
%{_mandir}/man3/*

%changelog
%autochangelog
