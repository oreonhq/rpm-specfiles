%global source1_hash c19669c65c2f1611e59219ecef948da5225946ece65e42ad4e97d8df4129c2bb
%global source0_hash 7c98de329cb5d6a99abbb03aaad2866cb041092ed9936a7246908e170005b058
Name:          perl-Net-DNS
Version:       1.57
Release:        1%{?dist}
Summary:        DNS resolver modules for Perl
License:       MIT
URL:           https://www.net-dns.org
Source0:        https://www.net-dns.org/download/Net-DNS-%{version}.tar.gz
Source1:        https://www.net-dns.org/download/Net-DNS-%{version}.tar.gz.asc
Source2:        willem.nlnetlabs.nl
BuildArch:     noarch
Suggests:      perl(Config)
Requires:      perl(Data::Dumper)
Requires:      perl(Digest::HMAC) >= 1.03
Requires:      perl(Digest::MD5) >= 2.13
Requires:      perl(Digest::SHA) >= 5.23
Requires:      perl(Encode)
Recommends:    perl(IO::Socket::IP) >= 0.38
Requires:      perl(MIME::Base64) >= 2.13
Suggests:      perl(Net::LibIDN2) >= 1
Suggests:      perl(Scalar::Util) >= 1.25
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Digest::HMAC\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Digest::MD5\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Digest::SHA\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(MIME::Base64\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CONFIG\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(OS_CONF\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\((Net::DNS::Text)\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\((Net::DNS::RR::OPT)\\)$
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(TestToolkit\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(TestToolkit\\)$
Provides:       perl(Net::DNS)
Provides:       perl(Net::DNS::Packet)
Provides:       perl(Net::DNS::Question)
Provides:       perl(Net::DNS::RR)
Provides:       perl(Net::DNS::Resolver)
Provides:       perl(Net::DNS::ZoneFile)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::HMAC)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Net::LibIDN2)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(integer)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
set -e
DIR=$(mktemp -d)
pushd "$DIR"
cp -a %{_libexecdir}/%{name}/* ./
prove -I . -I t -j "$(getconf _NPROCESSORS_ONLN)"
popd
rm -rf "$DIR"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n perl-Net-DNS-Nameserver -f %{oreon_filedir}/perl-Net-DNS-Nameserver.list
%files -n perl-Net-DNS-tests -f %{oreon_filedir}/perl-Net-DNS-tests.list

%changelog

%autochangelog
