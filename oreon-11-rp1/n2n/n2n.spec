%global source0_hash 311f89d147558ae4dfb0d8f8698f5429c05a3e19a9d25cb8c85bd73d02aff834

Name:           n2n
Version:        3.1.1
Release:        1%{?dist}
Summary:        A layer-two peer-to-peer virtual private network

# Most of the code is GPLv3 or later.
# BSD-1-Clause: include/uthash.h
# BSD-3-Clause-Tso: src/n2n_port_mapping.c
# MIT: include/tf.h, src/tf.c
License:        GPL-3.0-or-later AND BSD-1-Clause AND BSD-3-Clause-Tso AND MIT

URL:            http://www.ntop.org/n2n
Source0:        https://github.com/ntop/n2n/archive/%{version}/%{name}-%{version}.tar.gz

# Upstream n2n builds against a rather old version of miniupnpc.
# Newer versions made some breaking changes to the public API.
Patch0:         0000-upnp-api-change.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libcap-devel
BuildRequires:  libnatpmp-devel
BuildRequires:  libpcap-devel
BuildRequires:  libzstd-devel
BuildRequires:  miniupnpc-devel
BuildRequires:  openssl-devel

%description
n2n is a layer-two peer-to-peer virtual private network (VPN) which
allows users to exploit features typical of P2P applications at
network instead of application level. This means that users can gain
native IP visibility (e.g. two PCs belonging to the same n2n network
can ping each other) and be reachable with the same network IP address
regardless of the network where they currently belong.  In a nutshell,
as OpenVPN moved SSL from application (e.g. used to implement the
HTTPS protocol) to network protocol, n2n moves P2P from application to
network level.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf -vif

%build
%configure \
	--enable-cap --enable-pcap \
	--enable-miniupnp --enable-natpmp \
	--enable-pthread \
	--with-openssl \
	--with-zstd
%make_build SBINDIR="%{_bindir}"

%install
%make_install SBINDIR="%{buildroot}%{_bindir}"

%files
%doc README.md
%license COPYING
%{_bindir}/edge
%{_bindir}/n2n-benchmark
%{_bindir}/n2n-decode
%{_bindir}/n2n-keygen
%{_bindir}/supernode
%{_mandir}/man1/supernode.1*
%{_mandir}/man7/n2n.7*
%{_mandir}/man8/edge.8*

%changelog
%autochangelog
