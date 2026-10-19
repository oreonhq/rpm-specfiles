%global source0_hash 7560d3a9321bd8fc5077d1bc8a24d71d2bc33d2350fa18f0a66f1177a068bf95
Name:           perl-Net-DAVTalk
Version:        0.25
Release:        1%{?dist}
Summary:        Client for DAV servers
License:        Artistic-2.0
URL:            https://metacpan.org/release/Net-DAVTalk
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRONG/Net-DAVTalk-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(HTTP::Tiny) >= 0.016
Requires:       perl(Tie::DataUUID) >= 1.02
Requires:       perl(URI) >= 1.60
Requires:       perl(XML::Fast) >= 0.11
Requires:       perl(XML::Spice) >= 0.03
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((HTTP::Tiny|Tie::DataUUID|URI|XML::Fast|XML::Spice)\\)$
Provides:       perl(Net::DAVTalk)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DateTime::Format::ISO8601)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(JSON)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::DataUUID)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::Fast)
BuildRequires:  perl(XML::Spice)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a Perl library for accessing DAV servers.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Net-DAVTalk-%{version}
# Remove author tests
for F in \
    t/boilerplate.t \
    t/manifest.t \
    t/pod.t \
    t/pod-coverage.t \
    ; do
    rm "$F"
    perl -i -ne 'print $_ unless m{\A\Q'"$F"'\E}' MANIFEST
done
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
%{_fixperms} %{buildroot}/*
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Net-DAVTalk-tests -f %{oreon_filedir}/perl-Net-DAVTalk-tests.list

%changelog

%autochangelog
