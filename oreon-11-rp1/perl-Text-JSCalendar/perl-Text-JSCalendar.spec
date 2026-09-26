%global source0_hash 47b5efdd813f2ca8df2dd2f2317cdc73c8a1e31d2b361f407ecaf5010711a450

Name:           perl-Text-JSCalendar
Version:        0.06
Release:        1%{?dist}
Summary:        Convert between iCalendar and JSCalendar
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-JSCalendar
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRONG/Text-JSCalendar-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::ICal)
BuildRequires:  perl(Data::ICal::Entry::Event)
BuildRequires:  perl(Data::ICal::Entry::TimeZone)
BuildRequires:  perl(Data::ICal::Entry::TimeZone::Daylight)
BuildRequires:  perl(Data::ICal::Entry::TimeZone::Standard)
BuildRequires:  perl(Data::ICal::Entry::Alarm::Display)
BuildRequires:  perl(Data::ICal::Entry::Alarm::Email)
BuildRequires:  perl(XML::Spice)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.006
BuildRequires:  perl(Data::ICal::TimeZone) >= 1.23
BuildRequires:  perl(DateTime::Format::ICal) >= 0.09
BuildRequires:  perl(DateTime::Format::ISO8601) >= 0.08
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::LevenshteinXS) >= 0.03
BuildRequires:  perl(Text::VCardFast) >= 0.06
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
Requires:       perl(Data::ICal::TimeZone) >= 1.23
Requires:       perl(DateTime::Format::ICal) >= 0.09
Requires:       perl(DateTime::Format::ISO8601) >= 0.08
Requires:       perl(DateTime::TimeZone)
Requires:       perl(JSON)
Requires:       perl(JSON::XS)
Requires:       perl(MIME::Types)
Requires:       perl(Text::LevenshteinXS) >= 0.03
Requires:       perl(Text::VCardFast) >= 0.06

%description
Convert between iCalendar and JSCalendar using the Text::JSCalendar Perl module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n Text-JSCalendar-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Text/
%{_mandir}/man3/Text::JSCalendar*.3*

%changelog
%autochangelog
