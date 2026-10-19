%global source0_hash 204b13487158b8e46bf6dd207757a52621148fdd1d2467ebd104de17493bab25
%global gittag  1.10.0
Name:           arp-scan
Version:        %{gittag}
Release:        1%{?dist}
Summary:        Scanning and fingerprinting tool
License:        GPL-2.0-or-later
URL:            https://github.com/royhills/arp-scan
Source0:        https://github.com/royhills/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       perl(LWP::Simple)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  perl-generators
# /oreon:deps
%description
arp-scan is a command-line tool that uses the ARP protocol to discover and
fingerprint IP hosts on the local network.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

autoreconf --install
%configure --bindir=%{_sbindir}
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
chmod 0644 $RPM_BUILD_DIR/%{name}-%{version}/mt19937ar.c
chmod 0755 $RPM_BUILD_ROOT%{_sbindir}/*
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
