# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Net_CardDAVTalk_enables_optional_test
%else
%bcond_with perl_Net_CardDAVTalk_enables_optional_test
%endif

Name:           perl-Net-CardDAVTalk
Version:        0.09
Release:        24%{?dist}
Summary:        CardDAV client
License:        Artistic-2.0
URL:            https://metacpan.org/release/Net-CardDAVTalk
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRONG/Net-CardDAVTalk-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 e39ce5d284747d83505feb13c64b5aa92e477049c863880cec6540b86c8ff22d
%global source0_file Net-CardDAVTalk-0.09.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(:VERSION) >= 5.14.0
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Date::Format) >= 2.24
BuildRequires:  perl(Encode)
BuildRequires:  perl(File::MMagic) >= 1.30
BuildRequires:  perl(List::MoreUtils) >= 0.01
BuildRequires:  perl(List::Pairwise) >= 1.00
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Net::DAVTalk) >= 0.08
BuildRequires:  perl(Text::VCardFast) >= 0.07
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::Spice) >= 0.04
# Tests:
BuildRequires:  perl(Test::More)
%if %{with perl_Net_CardDAVTalk_enables_optional_test}
# Optional tests:
# Pod::Coverage 0.18 not used
# Test::CheckManifest 0.9 not used
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
%endif
Requires:       perl(Date::Format) >= 2.24
Requires:       perl(File::MMagic) >= 1.30
Requires:       perl(List::MoreUtils) >= 0.01
Requires:       perl(List::Pairwise) >= 1.00
Requires:       perl(Net::DAVTalk) >= 0.08
Requires:       perl(Text::VCardFast) >= 0.07
Requires:       perl(XML::Spice) >= 0.04

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:{%__requires_exclude}|}^perl\\((Date::Format|File::MMagic|List::MoreUtils|List::Pairwise|Net::DAVTalk|Text::VCardFast|XML::Spice)\\)$

%description
This is an CardDAV client with FastMail Perl API.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::Deep) >= 0.111

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Net-CardDAVTalk-0.09.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e39ce5d284747d83505feb13c64b5aa92e477049c863880cec6540b86c8ff22d" || { echo "oreon: Source0 SHA256 mismatch for Net-CardDAVTalk-0.09.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Net-CardDAVTalk-%{version}
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.09-24
- Prepare for Oreon 11 (RP1)
