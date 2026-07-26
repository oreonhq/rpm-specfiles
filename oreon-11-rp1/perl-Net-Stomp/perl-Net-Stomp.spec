%global source0_hash 5c7dc4fc6a30a2c3e685ab33540df2b64d913ad1046eee7e7dc3e8ffb8ee9325

Name:           perl-Net-Stomp
Version:        0.62
Release:        5%{?dist}
Summary:        Stomp client module for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Stomp
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAKKAR/Net-Stomp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Config)
BuildRequires:  perl(Module::Build) >= 0.42
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(IO::Select)
# Prefer IO::Socket::IP over IO::Socket::INET
# IO::Socket::IP 0.20 not used at tests
BuildRequires:  perl(Log::Any)
# Socket not used at tests
# Optional run-time:
# IO::Socket::SSL 1.75 not used at tests
# Tests:
BuildRequires:  perl(lib)
BuildRequires:  perl(Log::Any::Adapter)
BuildRequires:  perl(Log::Any::Adapter::TAP)
BuildRequires:  perl(Log::Any::Adapter::Test)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NiceDump)
# Optional tests:
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::Pod) >= 1.14
# Prefer IO::Socket::IP over IO::Socket::INET
Requires:       perl(IO::Socket::IP) >= 0.20
Requires:       perl(Socket)
# Keep IO::Socket::SSL optional

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((TestHelp)\\)

%description
This module allows you to write a Stomp client. Stomp, the Streaming Text
Orientated Messaging Protocol, is a simple and easy to implement protocol
for working with Message Orientated Middleware.

Net::Stomp can be used to communicate with Apache ActiveMQ, an
enterprise-level Java Message Service 1.1 (JMS) message broker.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Log::Any::Adapter::TAP)

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Stomp-%{version}
# Help generators to recognize a Perl code
for F in t/*.t; do
    perl -i -MConfig -pe 'print qq{$Config{startperl}\n} if $. == 1 && !s{\A#!.*\bperl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done
# Perl interpreter path
sed -i -e 's~^#!perl~%(perl -MConfig -e 'print $Config{startperl}')~' examples/*.pl

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/pod*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
set -e
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc CHANGES examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%files tests
%{_libexecdir}/%{name}

%changelog
%autochangelog
