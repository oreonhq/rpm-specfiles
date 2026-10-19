%global source0_hash ff8723dd0a416654420173a9bdecf075da78d4ea916267b4a0b535cd60219656
%bcond_with perl_Net_CalDAVTalk_enables_optional_test
Name:           perl-Net-CalDAVTalk
Version:        0.18
Release:        1%{?dist}
Summary:        CalDAV client with JSON data interface
License:        Artistic-2.0
URL:            https://metacpan.org/release/Net-CalDAVTalk
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRONG/Net-CalDAVTalk-%{version}.tar.gz
Patch0:         Net-CalDAVTalk-0.12-Load-Data-Dumper.patch
BuildArch:      noarch
%if %{with perl_Net_CalDAVTalk_enables_optional_test}
%endif
Requires:       perl(Data::Dumper)
Requires:       perl(Data::ICal::TimeZone) >= 1.23
Requires:       perl(DateTime::Format::ICal) >= 0.09
Requires:       perl(DateTime::Format::ISO8601) >= 0.08
Requires:       perl(Net::DAVTalk) >= 0.02
Requires:       perl(Text::LevenshteinXS) >= 0.03
Requires:       perl(Text::VCardFast) >= 0.06
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Data::ICal::TimeZone|DateTime::Format::ICal|DateTime::Format::ISO8601|Net::DAVTalk|Text::LevenshteinXS|Text::VCardFast)\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::ICal)
BuildRequires:  perl(Data::ICal::Entry::Alarm::Display)
BuildRequires:  perl(Data::ICal::Entry::Alarm::Email)
BuildRequires:  perl(Data::ICal::Entry::Event)
BuildRequires:  perl(Data::ICal::Entry::TimeZone)
BuildRequires:  perl(Data::ICal::Entry::TimeZone::Daylight)
BuildRequires:  perl(Data::ICal::Entry::TimeZone::Standard)
BuildRequires:  perl(Data::ICal::TimeZone)
BuildRequires:  perl(DateTime::Format::ICal)
BuildRequires:  perl(DateTime::Format::ISO8601)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(Net::DAVTalk)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::JSCalendar)
BuildRequires:  perl(Text::LevenshteinXS)
BuildRequires:  perl(Text::VCardFast)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::Spice)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/manifest*
rm -f %{buildroot}%{_libexecdir}/%{name}/t/pod*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" -r
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Net-CalDAVTalk-tests -f %{oreon_filedir}/perl-Net-CalDAVTalk-tests.list

%changelog

%autochangelog
