%global source0_hash 095e11cfce100b683c80fc8190459d16489f497d3b6f9a2955333256c5595dca

Name:           perl-WWW-Splunk
Version:        2.09
Release:        8%{?dist}
Summary:        Client for Splunk log search engine
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WWW-Splunk
Source0:        https://cpan.metacpan.org/authors/id/S/SK/SKIM/WWW-Splunk-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Date::Manip)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(XML::LibXML)
# Tests
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)

%description
WWW::Splunk is a client for Splunk log search engine. It consists of a utility
with command-line interface, sc, and a supporting library. It lets you query
the archived logs or conduct a real-time search.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WWW-Splunk-%{version}
# Help generators to recognize Perl scripts
for F in $(find . -type f -name *.t); do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done
# Rename sc to splunk-client
mv bin/sc bin/splunk-client

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -r -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_mandir}/man1/*
%{_bindir}/splunk-client

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
