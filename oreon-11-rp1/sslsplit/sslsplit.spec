%global source0_hash ba0473fd01428439e0cf22fae80fdd26d08a0bcf85e17c82177cb0810b700faf
Summary:        Transparent and scalable SSL/TLS interception
Name: sslsplit
Version: 0.5.5
Release:        1%{?dist}
License: LicenseRef-Callaway-BSD
Url: http://www.roe.ch/SSLsplit
Source0:        http://mirror.roe.ch/rel/sslsplit/sslsplit-%{version}.tar.bz2
Patch1: sslsplit-0.5.5-openssl3.patch
Requires: iptables, iproute
# oreon:deps
BuildRequires:  check-devel
BuildRequires:  gcc
BuildRequires:  libevent-devel
BuildRequires:  libnet-devel
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
%description
SSLsplit is a tool for man-in-the-middle attacks against SSL/TLS encrypted
network connections. Connections are transparently intercepted through a
network address translation engine and redirected to SSLsplit. SSLsplit
terminates SSL/TLS and initiates a new SSL/TLS connection to the original
destination address, while logging all data transmitted. SSLsplit is
intended to be useful for network forensics and penetration testing.

It uses Linux netfilter REDIRECT and TPROXY

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%autopatch -p1

%build

export CFLAGS="%{optflags}"
export DEBUG_CFLAGS="%{optflags}"
make %{?_smp_mflags}
%check

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1/
cp -a %{name} %{buildroot}%{_bindir}
cp -a %{name}.1  %{buildroot}%{_mandir}/man1/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
