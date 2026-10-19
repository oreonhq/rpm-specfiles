%global source0_hash 027840fa3c4e11abfe4fd0fffe9909c5c4ed1428d4b9397fb6d2f5ea69325918
Name:		netsniff-ng
Version:	0.6.9
Release:        1%{?dist}
Summary:        Packet sniffing beast
License:	GPL-2.0-only
URL:		http://netsniff-ng.org/
Source0:        http://www.netsniff-ng.org/pub/netsniff-ng/netsniff-ng-%{version}.tar.xz
Patch:		netsniff-ng-0.6.9-gcc-15-fix.patch
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libcli-devel
BuildRequires:  libnet-devel
BuildRequires:  libnetfilter_conntrack-devel
BuildRequires:  libnl3-devel
BuildRequires:  libpcap-devel
BuildRequires:  libsodium-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl-podlators
BuildRequires:  userspace-rcu-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
netsniff-ng is a high performance Linux network sniffer for packet inspection.
It can be used for protocol analysis, reverse engineering or network
debugging. The gain of performance is reached by 'zero-copy' mechanisms, so
that the kernel does not need to copy packets from kernelspace to userspace.

netsniff-ng toolkit currently consists of the following utilities:

* netsniff-ng: the zero-copy sniffer, pcap capturer and replayer itself.
* trafgen: a high performance zero-copy network packet generator.
* ifpps: a top-like kernel networking and system statistics tool.
* curvetun: a lightweight curve25519-based multiuser IP tunnel.
* ashunt: an autonomous system trace route and ISP testing utility.
* flowtop: a top-like netfilter connection tracking tool.
* bpfc: a tiny Berkeley Packet Filter compiler supporting Linux extensions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export NACL_INC_DIR=$(pkg-config --variable=includedir libsodium )/sodium
export NACL_LIB=sodium
./configure --prefix='%{_prefix}' --sysconfdir='%{_sysconfdir}'
make %{?_smp_mflags} ETCDIR=%{_sysconfdir} Q= STRIP=: \
  CFLAGS="%{optflags} -fPIC -fcommon" LDFLAGS="%{?__global_ldflags}"
%install
make install PREFIX=%{_prefix} ETCDIR=%{_sysconfdir} SBINDIR=%{_sbindir} DESTDIR="%{buildroot}"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
