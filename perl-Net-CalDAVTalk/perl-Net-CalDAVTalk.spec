# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Net_CalDAVTalk_enables_optional_test
%else
%bcond_with perl_Net_CalDAVTalk_enables_optional_test
%endif

Name:           perl-Net-CalDAVTalk
Version:        0.12
Release:        25%{?dist}
Summary:        CalDAV client with JSON data interface
License:        Artistic-2.0
URL:            https://metacpan.org/release/Net-CalDAVTalk
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRONG/Net-CalDAVTalk-%{version}.tar.gz
# Fix using Data::Dumper, CPAN RT#123646
Patch0:         Net-CalDAVTalk-0.12-Load-Data-Dumper.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
# Data::Dumper not used at tests
BuildRequires:  perl(Data::ICal)
BuildRequires:  perl(Data::ICal::Entry::Alarm::Display)
BuildRequires:  perl(Data::ICal::Entry::Alarm::Email)
BuildRequires:  perl(Data::ICal::Entry::Event)
BuildRequires:  perl(Data::ICal::Entry::TimeZone)
BuildRequires:  perl(Data::ICal::Entry::TimeZone::Daylight)
BuildRequires:  perl(Data::ICal::Entry::TimeZone::Standard)
BuildRequires:  perl(Data::ICal::TimeZone) >= 1.23
BuildRequires:  perl(DateTime::Format::ICal) >= 0.09
BuildRequires:  perl(DateTime::Format::ISO8601) >= 0.08
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(Net::DAVTalk) >= 0.02
BuildRequires:  perl(Text::LevenshteinXS) >= 0.03
BuildRequires:  perl(Text::VCardFast) >= 0.06
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::Spice)
# Tests:
BuildRequires:  perl(Test::More)
%if %{with perl_Net_CalDAVTalk_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Pod::Coverage) >= 0.18
# Test::CheckManifest 0.9 not used
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
%endif
Requires:       perl(Data::Dumper)
Requires:       perl(Data::ICal::TimeZone) >= 1.23
Requires:       perl(DateTime::Format::ICal) >= 0.09
Requires:       perl(DateTime::Format::ISO8601) >= 0.08
Requires:       perl(Net::DAVTalk) >= 0.02
Requires:       perl(Text::LevenshteinXS) >= 0.03
Requires:       perl(Text::VCardFast) >= 0.06

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Data::ICal::TimeZone|DateTime::Format::ICal|DateTime::Format::ISO8601|Net::DAVTalk|Text::LevenshteinXS|Text::VCardFast)\\)$

%description
This a Perl library for accessing CalDAV servers providing JSON interface to
the data.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::Deep) >= 0.111

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%setup -q -n Net-CalDAVTalk-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
# Remove author tests
rm -f %{buildroot}%{_libexecdir}/%{name}/t/manifest*
rm -f %{buildroot}%{_libexecdir}/%{name}/t/pod*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.12-25
- Prepare for Oreon 11 (RP1)
