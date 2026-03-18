Name:           perl-Text-vFile-asData
Version:        0.08
Release:        40%{?dist}
Summary:        Parse vFile formatted files into data structures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-vFile-asData
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Text-vFile-asData-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(Class::Accessor::Chained)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)

# for improved tests
BuildRequires:  perl(Test::Pod) >= 1.00

# rpm doesn't catch this
Requires:       perl(Class::Accessor::Chained::Fast)

%description
Text::vFile::asData reads vFile format files, such as vCard (RFC 2426) and
vCalendar (RFC 2445).

%prep
%setup -q -n Text-vFile-asData-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.08-40
- Prepare for Oreon 11 (RP1)
