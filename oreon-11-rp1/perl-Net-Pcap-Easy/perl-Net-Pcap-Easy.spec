%global source0_hash ec285b712533eea3393965183cc70ed2172d57095bbe2aa1791e5188cf54e5c2

Name:           perl-Net-Pcap-Easy
Version:        1.4210
Release:        33%{?dist}
Summary:        Convenience functions to make Net::Pcap easier to use
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://metacpan.org/release/Net-Pcap-Easy
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-Pcap-Easy-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(Net::Netmask)
BuildRequires:  perl(NetPacket::ARP)
BuildRequires:  perl(NetPacket::Ethernet)
BuildRequires:  perl(NetPacket::ICMP)
BuildRequires:  perl(NetPacket::IGMP)
BuildRequires:  perl(NetPacket::IP)
BuildRequires:  perl(NetPacket::TCP)
BuildRequires:  perl(NetPacket::UDP)
BuildRequires:  perl(Net::Pcap)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)

%description
This module is little more than a collection of macros and convenience
functions. Net::Pcap does all the real work (of lifting libpcap into
perl anyway).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-Pcap-Easy-%{version}

%build
TEST_DEVICE=skip %{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README examples contrib
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
