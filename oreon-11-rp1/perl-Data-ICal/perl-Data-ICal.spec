Name:           perl-Data-ICal
Version:        0.24
Release:        19%{?dist}
Summary:        Generates iCalendar (RFC 2445) calendar files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-ICal
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPS/Data-ICal-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl-generators
BuildRequires:  perl(CPAN) perl(YAML::Tiny) perl(File::Remove)

BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Class::ReturnValue)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.36
BuildRequires:  perl(MIME::QuotedPrint)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Text::vFile::asData)

# for improved tests
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::Pod) >= 1.14

BuildRequires:  perl(inc::Module::Install)

# rpm doesn't catch this
Requires:       perl(Class::Accessor)

%description
A Data::ICal object represents a VCALENDAR object as defined in the
iCalendar protocol (RFC 2445, MIME type "text/calendar"), as implemented in
many popular calendaring programs such as Apple's iCal.

%prep
%setup -q -n Data-ICal-%{version}
rm -rf inc

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps NO_PACKLIST=1 NO_PERLLOCAL=1
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.24-19
- Prepare for Oreon 11 (RP1)
