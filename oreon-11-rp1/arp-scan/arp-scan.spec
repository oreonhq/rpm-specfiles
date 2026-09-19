%global source0_hash 204b13487158b8e46bf6dd207757a52621148fdd1d2467ebd104de17493bab25

%global gittag  1.10.0

Name:           arp-scan
Version:        %{gittag}
Release:        10%{?dist}
Summary:        Scanning and fingerprinting tool

# Includes getopt, which is LGPLv2+, but the whole is GPLv2+.
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/royhills/arp-scan
Source0:        https://github.com/royhills/arp-scan/archive/%{gittag}/%{name}-%{version}.tar.gz

BuildRequires:  libpcap-devel
BuildRequires:  gcc
BuildRequires:  perl-generators
BuildRequires:  automake autoconf
BuildRequires: make
Requires:       perl(LWP::Simple)

%description
arp-scan is a command-line tool that uses the ARP protocol to discover and
fingerprint IP hosts on the local network.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
autoreconf --install
#install to sbindir
%configure --bindir=%{_sbindir}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

#fix permissions for -debuginfo package
chmod 0644 $RPM_BUILD_DIR/%{name}-%{version}/mt19937ar.c

#fix permissions for files in sbindir
chmod 0755 $RPM_BUILD_ROOT%{_sbindir}/*

%files
%doc AUTHORS ChangeLog COPYING README TODO 
%{_sbindir}/*
%{_datadir}/arp-scan
%{_mandir}/man?/*
%{_sysconfdir}/arp-scan/mac-vendor.txt

%changelog
%autochangelog
