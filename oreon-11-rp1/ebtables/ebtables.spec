# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b71f654784a726329f88b412ef7b96b4e5d786ed2bd28193ed7b4c0d677dfd2a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%undefine _ld_as_needed

Name:			ebtables
Version:		2.0.11
Release:		%{autorelease}
Summary:		Ethernet Bridge frame table administration tool
License:		GPL-2.0-or-later
URL:			http://ebtables.sourceforge.net/

Source0:		ebtables-%{version}.tar.bz2
Source1:		ebtables-legacy-save

BuildRequires: oreon-rpm-macros
BuildRequires:		autoconf
BuildRequires:		automake
BuildRequires:		libtool
BuildRequires:		clang
BuildRequires:		gcc
BuildRequires:		make

%description
Ethernet bridge tables is a firewalling tool to transparently filter network
traffic passing a bridge. The filtering possibilities are limited to link
layer filtering and some basic filtering on higher network layers.

This tool is the userspace control for the bridge and ebtables kernel
components (built by default in Oreon kernels).

The ebtables tool can be used together with the other Linux filtering tools,
like iptables. There are no known incompatibility issues.

%package legacy
Summary: Legacy user space tool to configure bridge netfilter rules in kernel
Requires(post):   /usr/sbin/update-alternatives
Requires(post):   %{_bindir}/readlink
Requires(postun): /usr/sbin/update-alternatives
Conflicts:        setup < 2.10.4-1
%if 0%{?rhel} >= 9
%else
Provides:         ebtables
%endif

%sbin_merge_compat %{_prefix}/sbin/ebtables

%description legacy
Ethernet bridge tables is a firewalling tool to transparently filter network
traffic passing a bridge. The filtering possibilities are limited to link
layer filtering and some basic filtering on higher network layers.

This tool is the userspace control for the bridge and ebtables kernel
components (built by default in Oreon kernels).

The ebtables tool can be used together with the other Linux filtering tools,
like iptables. There are no known incompatibility issues.

Note that it is considered legacy upstream since nftables provides the same
functionality in a much newer code-base. To aid in migration, there is
ebtables-nft utility, a drop-in replacement for the legacy one which uses
nftables internally. It is provided by iptables-nft package.

%prep
%oreon_sha256
%autosetup -p1 -n ebtables-%{version}
f=THANKS; iconv -f iso-8859-1 -t utf-8 $f -o $f.utf8 ; mv $f.utf8 $f

%build
./autogen.sh
%configure --disable-silent-rules LOCKFILE=/run/ebtables.lock
%make_build

%install
%make_install

install -m 755 %{SOURCE1} %{buildroot}%{_sbindir}/ebtables-legacy-save

rm %{buildroot}/%{_libdir}/libebtc.la

rm -f %{buildroot}%{_sysconfdir}/ethertypes

rm %{buildroot}/%{_sbindir}/ebtables{d,u}

%post legacy
pfx=%{_prefix}/sbin/ebtables
manpfx=%{_mandir}/man8/ebtables
for sfx in "" "-restore" "-save"; do
	if [ "$(readlink -e $pfx$sfx)" == $pfx$sfx ]; then
		rm -f $pfx$sfx
	fi
done
if [ "$(readlink -e $manpfx.8.gz)" == $manpfx.8.gz ]; then
	rm -f $manpfx.8.gz
fi
update-alternatives --remove ebtables /usr/bin/ebtables-legacy 2>/dev/null
update-alternatives --install \
	$pfx ebtables $pfx-legacy 10 \
	--slave $pfx-save ebtables-save $pfx-legacy-save \
	--slave $pfx-restore ebtables-restore $pfx-legacy-restore \
	--slave $manpfx.8.gz ebtables-man $manpfx-legacy.8.gz

%postun legacy
if [ $1 -eq 0 ]; then
	%{_sbindir}/update-alternatives --remove \
		ebtables %{_prefix}/sbin/ebtables-legacy
fi

%triggerpostun legacy -- ebtables
pfx=%{_prefix}/sbin/ebtables
manpfx=%{_mandir}/man8/ebtables
update-alternatives --install \
	$pfx ebtables $pfx-legacy 10 \
	--slave $pfx-save ebtables-save $pfx-legacy-save \
	--slave $pfx-restore ebtables-restore $pfx-legacy-restore \
	--slave $manpfx.8.gz ebtables-man $manpfx-legacy.8.gz

%files legacy
%license COPYING
%doc ChangeLog THANKS
%{_sbindir}/ebtables-legacy*
%{_mandir}/*/ebtables-legacy*
%{_libdir}/libebtc.so*
%ghost %attr(0755,root,root) %{_prefix}/sbin/ebtables
%ghost %attr(0755,root,root) %{_prefix}/sbin/ebtables-save
%ghost %attr(0755,root,root) %{_prefix}/sbin/ebtables-restore
%ghost %attr(0644,root,root) %{_mandir}/man8/ebtables.8.gz

%changelog
%autochangelog
