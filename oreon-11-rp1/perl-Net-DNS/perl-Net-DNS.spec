# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 04acb4f177d57c147dcedc4bd70e23806af3db75a532f46f95461b2bc9a94959
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:          perl-Net-DNS
Version:       1.53
Release:       2%{?dist}
Summary:       DNS resolver modules for Perl
License:       MIT
URL:           https://www.net-dns.org
Source0:       https://www.net-dns.org/download/Net-DNS-%{version}.tar.gz
Source1:       https://www.net-dns.org/download/Net-DNS-%{version}.tar.gz.asc
Source2:       http://keys.openpgp.org/pks/lookup?op=get&search=0xE5F8F8212F77A498#/willem.nlnetlabs.nl

BuildArch:     noarch

BuildRequires: gnupg2
BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: make

BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(Config)
BuildRequires: perl(constant)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(Getopt::Long)
# IO::Socket::IP or IO::Socket::INET
BuildRequires: perl(IO::Socket::IP) >= 0.38
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
# Runtime
BuildRequires: perl(base)
BuildRequires: perl(Carp)
BuildRequires: perl(Data::Dumper)
%if ! (0%{?rhel} >= 7)
# Digest::BubbleBabble is optional
BuildRequires: perl(Digest::BubbleBabble)
%endif
BuildRequires: perl(Digest::HMAC) >= 1.03
BuildRequires: perl(Digest::MD5) >= 2.37
BuildRequires: perl(Digest::SHA) >= 5.23
BuildRequires: perl(Encode)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Spec)
BuildRequires: perl(FileHandle)
BuildRequires: perl(integer)
BuildRequires: perl(IO::File)
# IO::Select is not used
BuildRequires: perl(IO::Socket) >= 1.30
# Prefer IO::Socket::IP over IO::Socket::INET for IPv6 support
BuildRequires: perl(MIME::Base64) >= 3.07
# Prefer Net::LibIDN2 over Net::LibIDN, both are optional
BuildRequires: perl(Net::LibIDN2) >= 1
BuildRequires: perl(overload)
# PerlIO is optional
# Scalar::Util is optional
BuildRequires: perl(Socket) >= 1.81
BuildRequires: perl(Time::Local)
# Win32::IPHelper is not needed
# Win32::TieRegistry is not needed
# Tests only
BuildRequires: perl(File::Find) >= 1.13
BuildRequires: perl(Test::Builder)
BuildRequires: perl(Test::More)
Suggests:      perl(Config)
Requires:      perl(Data::Dumper)
Requires:      perl(Digest::HMAC) >= 1.03
Requires:      perl(Digest::MD5) >= 2.13
Requires:      perl(Digest::SHA) >= 5.23
Requires:      perl(Encode)
# Prefer IO::Socket::IP over IO::Socket::INET for IPv6 support
Recommends:    perl(IO::Socket::IP) >= 0.38
Requires:      perl(MIME::Base64) >= 2.13
# Net::DNS::Extlang not available
# Prefer Net::LibIDN2 over Net::LibIDN, both are optional
Suggests:      perl(Net::LibIDN2) >= 1
Suggests:      perl(Scalar::Util) >= 1.25

%{?perl_default_filter}

# Do not export under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Digest::HMAC\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Digest::MD5\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Digest::SHA\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MIME::Base64\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CONFIG\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(OS_CONF\\)$
# Do not export under-specified provides
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\((Net::DNS::Text)\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\((Net::DNS::RR::OPT)\\)$
# Remove private modules
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(TestToolkit\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(TestToolkit\\)$

%description
Net::DNS is a collection of Perl modules that act as a Domain Name System
(DNS) resolver. It allows the programmer to perform DNS queries that are
beyond the capabilities of gethostbyname and gethostbyaddr.

The programmer should be somewhat familiar with the format of a DNS packet and
its various sections. See RFC 1035 or DNS and BIND (Albitz & Liu) for details.

%package Nameserver
Summary:        DNS server for Perl
License:        MIT
Recommends:     perl(IO::Socket::IP) >= 0.32

%description Nameserver
Instances of the "Net::DNS::Nameserver" class represent DNS server objects.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%oreon_verify_sources
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%setup -q -n Net-DNS-%{version} 
chmod -x demo/*
perl -MConfig -i -pe 's{^#!/usr/local/bin/perl}{$Config{startperl}}' demo/*
# Remove author tests
for F in \
    t/00-install.t \
    t/00-pod.t \
    ; do
    rm "$F"
    perl -i -ne 'print $_ unless m{\A\Q'"$F"'\E}' MANIFEST
done
# Help generators to recognize Perl scripts
for F in t/*.t; do
    chmod +x "$F"
done

%build
export PERL_MM_USE_DEFAULT=yes
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 --no-online-tests
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/bash
set -e
# Some tests write into temporary files/directories, so they will be copy
# into a writable directory and execute them from there.
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -I t -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
make test

%files
%doc README Changes demo
%{perl_vendorlib}/Net/
%exclude %{perl_vendorlib}/Net/DNS/Resolver/cygwin.pm
%exclude %{perl_vendorlib}/Net/DNS/Resolver/MSWin32.pm
%{_mandir}/man3/Net::DNS*.3*
%exclude %{_mandir}/man3/Net::DNS::Resolver::cygwin.3*
%exclude %{_mandir}/man3/Net::DNS::Resolver::MSWin32.3*
# perl-Net-DNS-Nameserver
%exclude %{perl_vendorlib}/Net/DNS/Nameserver.pm
%exclude %{_mandir}/man3/Net::DNS::Nameserver*

%files Nameserver
%{perl_vendorlib}/Net/DNS/Nameserver.pm
%{_mandir}/man3/Net::DNS::Nameserver*

%files tests
%{_libexecdir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.53-2
- Prepare for Oreon 11 (RP1)
