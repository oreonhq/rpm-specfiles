%global source0_hash ba0473fd01428439e0cf22fae80fdd26d08a0bcf85e17c82177cb0810b700faf

Summary: Transparent and scalable SSL/TLS interception
Name: sslsplit
Version: 0.5.5
Release: 18%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
Url: http://www.roe.ch/SSLsplit
Source: http://mirror.roe.ch/rel/sslsplit/sslsplit-%{version}.tar.bz2

# https://github.com/droe/sslsplit/commit/e17de8454a65d2b9ba432856971405dfcf1e7522
Patch1: sslsplit-0.5.5-openssl3.patch

BuildRequires: make
Buildrequires: libevent-devel, openssl-devel, check-devel gcc
%if 0%{?fedora} >= 41
BuildRequires:  openssl-devel-engine
%endif
Buildrequires: libpcap-devel libnet-devel
Requires: iptables, iproute

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
# work around some odd build system option passing
export CFLAGS="%{optflags}"
export DEBUG_CFLAGS="%{optflags}"
make %{?_smp_mflags}

%check
# Requires a network connection
# make test

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1/
cp -a %{name} %{buildroot}%{_bindir}
cp -a %{name}.1  %{buildroot}%{_mandir}/man1/

%files
%attr(0755,root,root) %{_bindir}/%{name}
%doc *.md
%{_mandir}/*/*

%changelog
%autochangelog
