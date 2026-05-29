%global source0_hash 9fe6512333d14568823526a92474f8f217fb3665e916ec25b847ae104019a793

Name:           perl-Net-DAVTalk
Version:        0.24
Release:        1%{?dist}
Summary:        Client for DAV servers
License:        Artistic-2.0
URL:            https://metacpan.org/release/Net-DAVTalk
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRONG/Net-DAVTalk-0.24.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime::Format::ISO8601)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(HTTP::Tiny) >= 0.016
BuildRequires:  perl(JSON)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Tie::DataUUID) >= 1.02
BuildRequires:  perl(URI) >= 1.60
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::Fast) >= 0.11
BuildRequires:  perl(XML::Spice) >= 0.03
# Tests:
BuildRequires:  perl(Test::More)
Requires:       perl(HTTP::Tiny) >= 0.016
Requires:       perl(Tie::DataUUID) >= 1.02
Requires:       perl(URI) >= 1.60
Requires:       perl(XML::Fast) >= 0.11
Requires:       perl(XML::Spice) >= 0.03

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((HTTP::Tiny|Tie::DataUUID|URI|XML::Fast|XML::Spice)\\)$

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.24-1
- Prepare for Oreon 11 (RP1)
