%global source0_hash 5c7dc4fc6a30a2c3e685ab33540df2b64d913ad1046eee7e7dc3e8ffb8ee9325
Name:           perl-Net-Stomp
Version:        0.62
Release:        1%{?dist}
Summary:        Stomp client module for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-Stomp
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAKKAR/Net-Stomp-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(IO::Socket::IP) >= 0.20
Requires:       perl(Socket)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((TestHelp)\\)
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Config)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Log::Any::Adapter)
BuildRequires:  perl(Log::Any::Adapter::TAP)
BuildRequires:  perl(Log::Any::Adapter::Test)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NiceDump)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
rm -f %{buildroot}%{_libexecdir}/%{name}/t/pod*
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Net-Stomp-tests -f %{oreon_filedir}/perl-Net-Stomp-tests.list

%changelog

%autochangelog
