%global source1_hash 61573bdc27e15f20d0a7ccf29d34c0eec042550b25dce693b6d844410afedbba
%global source0_hash 1afcd33da9e8f913ace6a2126788162e207e26f5d5e29c6573c0e581ffc58b99
%global source2_key_fpr 8C5F7146A1757A65E2422A94D70D1A666ACF2B21
%global script_path %{_libexecdir}/iptables
%global legacy_actions %{_libexecdir}/initscripts/legacy-actions
%global iptc_so_ver  0
%global ipXtc_so_ver 2
Name: iptables
Summary:        Tools for managing Linux kernel packet filtering capabilities
URL: https://www.netfilter.org/projects/iptables
Version: 1.8.13
Release:        1%{?dist}
Source0:        https://www.netfilter.org/projects/iptables/files/iptables-1.8.13.tar.xz
Source1:        https://www.netfilter.org/projects/iptables/files/iptables-%{version}.tar.xz.sig
Source2:        coreteam-gpg-key-0xD70D1A666ACF2B21.txt
Source3:        iptables.init
Source4:        iptables-config
Source5:        iptables.service
Source6:        sysconfig_iptables
Source7:        sysconfig_ip6tables
Source8:        arptables-helper
Source9:        arptables.service
Source10:        ebtables.service
Source11:        ebtables-helper
Source12:        ebtables-config
License: GPL-2.0-only AND Artistic-2.0 AND ISC
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  kernel-headers
BuildRequires:  libpcap-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libnetfilter_conntrack)
BuildRequires:  pkgconfig(libnfnetlink)
BuildRequires:  pkgconfig(libnftnl)
BuildRequires:  systemd
# /oreon:deps
%description
The iptables utility controls the network packet filtering code in the
Linux kernel. If you need to set up firewalls and/or IP masquerading,
you should install this package.

%package legacy
Summary: Legacy tools for managing Linux kernel packet filtering capabilities
Requires: %{name}-legacy-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Conflicts: setup < 2.10.4-1
Conflicts: alternatives < 1.32-1
Requires(post): /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives
Provides:  %{name}-compat = %{version}-%{release}
Obsoletes: %{name}-compat < 1.8.9-7
%if "%{_sbindir}" == "%{_bindir}"
Requires: filesystem(unmerged-sbin-symlinks)
Provides: %{_prefix}/sbin/iptables
%endif
%description legacy
The iptables utility controls the network packet filtering code in the
Linux kernel. This package contains the legacy tools which are obsoleted by
nft-variants in iptables-nft package for backwards compatibility reasons.
If you need to set up firewalls and/or IP masquerading, you should not install
this package but either nftables or iptables-nft instead.

%package libs
Summary: libxtables and iptables extensions userspace support
%description libs
libxtables and associated shared object files

Libxtables provides unified access to iptables extensions in userspace. Data
and logic for those is kept in per-extension shared object files.

%package legacy-libs
Summary: iptables legacy libraries
%description legacy-libs
iptables libraries.

Please remember that libip*tc libraries do neither have a stable API nor a real
so version. For more information about this, please have a look at

  http://www.netfilter.org/documentation/FAQ/netfilter-faq-4.html#ss4.5

%package devel
Summary: Development package for iptables
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-legacy-devel%{?_isa} = %{version}-%{release}
Requires: pkgconfig
%description devel
libxtables development headers and pkgconfig files

%package legacy-devel
Summary: Development package for legacy iptables
Requires: %{name}-legacy-libs%{?_isa} = %{version}-%{release}
Requires: pkgconfig
%description legacy-devel
Legacy iptables development headers and pkgconfig files

The iptc libraries are marked as not public by upstream. The interface is not
stable and may change with every new version. It is therefore unsupported.

%package services
Summary: iptables and ip6tables services for iptables
Requires: %{name} = %{version}-%{release}
Requires: %{name}-utils = %{version}-%{release}
%{?systemd_ordering}
Obsoletes: %{name} < 1.4.16.1
Obsoletes: %{name}-ipv6 < 1.4.11.1
Conflicts: %{name}-nft < 1.8.11-5
Obsoletes: arptables-services < 0.0.5-16
Provides: arptables-services = %{version}-%{release}
Obsoletes: ebtables-services < 2.0.11-20
Provides: ebtables-services = 1:%{version}-%{release}
BuildArch: noarch
%description services
iptables services for IPv4 and IPv6

This package provides the services iptables and ip6tables that have been split
out of the base package since they are not active by default anymore.

%package utils
Summary: iptables and ip6tables misc utilities
Requires: %{name} = %{version}-%{release}
%description utils
Utils for iptables

This package provides nfnl_osf with the pf.os database and nfbpf_compile,
a bytecode generator for use with xt_bpf. Also included is iptables-apply,
a safer way to update iptables remotely.

%package nft
Summary: nftables compatibility for iptables, arptables and ebtables
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires(post): /usr/sbin/update-alternatives
Requires(post): /usr/bin/readlink
Requires(postun): /usr/sbin/update-alternatives
Obsoletes: iptables-compat < 1.6.2-4
Provides: arptables-helper
Provides: iptables
Provides: arptables
Provides: ebtables
Conflicts: arptables-legacy < 0.0.5-16
%if "%{_sbindir}" == "%{_bindir}"
Requires: filesystem(unmerged-sbin-symlinks)
Provides: %{_prefix}/sbin/iptables
%endif
%description nft
nftables compatibility for iptables, arptables and ebtables.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n iptables-1.8.13

%build

./autogen.sh
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing " \
%configure --enable-devel --enable-bpf-compiler --with-kernel=/usr --with-kbuild=/usr --with-ksource=/usr
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
rm -f include/linux/types.h
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
install -d -m 755 %{buildroot}%{script_path}
install -c -m 755 %{SOURCE3} %{buildroot}%{script_path}/iptables.init
sed -e 's;iptables;ip6tables;g' -e 's;IPTABLES;IP6TABLES;g' < %{SOURCE3} > ip6tables.init
install -c -m 755 ip6tables.init %{buildroot}%{script_path}/ip6tables.init
install -p -m 755 %{SOURCE8} %{SOURCE11} %{buildroot}%{_libexecdir}/
install -d -m 755 %{buildroot}%{_sysconfdir}/sysconfig
install -c -m 600 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/iptables-config
sed -e 's;iptables;ip6tables;g' -e 's;IPTABLES;IP6TABLES;g' < %{SOURCE4} > ip6tables-config
install -c -m 600 ip6tables-config %{buildroot}%{_sysconfdir}/sysconfig/ip6tables-config
install -c -m 600 %{SOURCE6} %{buildroot}%{_sysconfdir}/sysconfig/iptables
install -c -m 600 %{SOURCE7} %{buildroot}%{_sysconfdir}/sysconfig/ip6tables
echo '# Configure prior to use' > %{buildroot}%{_sysconfdir}/sysconfig/arptables
install -c -m 600 %{SOURCE12} %{buildroot}%{_sysconfdir}/sysconfig/
touch %{buildroot}%{_sysconfdir}/sysconfig/ebtables
install -d -m 755 %{buildroot}/%{_unitdir}
install -c -m 644 %{SOURCE5} %{SOURCE9} %{SOURCE10} %{buildroot}/%{_unitdir}
sed -e 's;iptables;ip6tables;g' -e 's;IPv4;IPv6;g' -e 's;/usr/libexec/ip6tables;/usr/libexec/iptables;g' < %{SOURCE5} > ip6tables.service
install -c -m 644 ip6tables.service %{buildroot}/%{_unitdir}
install -d %{buildroot}/%{legacy_actions}/iptables
install -d %{buildroot}/%{legacy_actions}/ip6tables
cat << EOF > %{buildroot}/%{legacy_actions}/iptables/save
exec %{script_path}/iptables.init save
EOF
chmod 755 %{buildroot}/%{legacy_actions}/iptables/save
sed -e 's;iptables.init;ip6tables.init;g' -e 's;IPTABLES;IP6TABLES;g' < %{buildroot}/%{legacy_actions}/iptables/save > ip6tabes.save-legacy
install -c -m 755 ip6tabes.save-legacy %{buildroot}/%{legacy_actions}/ip6tables/save
cat << EOF > %{buildroot}/%{legacy_actions}/iptables/panic
exec %{script_path}/iptables.init panic
EOF
chmod 755 %{buildroot}/%{legacy_actions}/iptables/panic
sed -e 's;iptables.init;ip6tables.init;g' -e 's;IPTABLES;IP6TABLES;g' < %{buildroot}/%{legacy_actions}/iptables/panic > ip6tabes.panic-legacy
install -c -m 755 ip6tabes.panic-legacy %{buildroot}/%{legacy_actions}/ip6tables/panic
rm -f %{buildroot}%{_sysconfdir}/ethertypes
touch %{buildroot}%{_mandir}/man8/arptables.8
touch %{buildroot}%{_mandir}/man8/arptables-save.8
touch %{buildroot}%{_mandir}/man8/arptables-restore.8
touch %{buildroot}%{_mandir}/man8/ebtables.8
rm %{buildroot}%{_sbindir}/{ip,ip6,arp,eb}tables{,-save,-restore}
touch %{buildroot}%{_sbindir}/{ip,ip6,arp,eb}tables{,-save,-restore}
ln -sf --relative %{buildroot}%{_sbindir}/xtables-legacy-multi %{buildroot}%{_bindir}/iptables-xml
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post legacy

pfx=%{_sbindir}/iptables
pfx6=%{_sbindir}/ip6tables
update-alternatives --install \
	$pfx iptables $pfx-legacy 10 \
	--follower $pfx6 ip6tables $pfx6-legacy \
	--follower $pfx-restore iptables-restore $pfx-legacy-restore \
	--follower $pfx-save iptables-save $pfx-legacy-save \
	--follower $pfx6-restore ip6tables-restore $pfx6-legacy-restore \
	--follower $pfx6-save ip6tables-save $pfx6-legacy-save
%if "%{_sbindir}" == "%{_bindir}"
for name in ip{,6}tables{,-save,-restore}; do
    test -h /usr/sbin || ln -s ../bin/$name /usr/sbin/$name 2>/dev/null || :
done
%endif
%postun legacy

if [ $1 -eq 0 ]; then
	update-alternatives --remove \
		iptables %{_sbindir}/iptables-legacy
fi
%triggerun legacy -- iptables > 1.8.0

alternatives --list | awk '/^iptables/{print $3; exit}' \
		>/var/tmp/alternatives.iptables.current
cp /var/lib/alternatives/iptables /var/tmp/alternatives.iptables.setup
%triggerpostun legacy -- iptables > 1.8.0

pfx=%{_sbindir}/iptables
pfx6=%{_sbindir}/ip6tables
update-alternatives --install \
	$pfx iptables $pfx-legacy 10 \
	--follower $pfx6 ip6tables $pfx6-legacy \
	--follower $pfx-restore iptables-restore $pfx-legacy-restore \
	--follower $pfx-save iptables-save $pfx-legacy-save \
	--follower $pfx6-restore ip6tables-restore $pfx6-legacy-restore \
	--follower $pfx6-save ip6tables-save $pfx6-legacy-save
alternatives --set iptables $(</var/tmp/alternatives.iptables.current)
rm /var/tmp/alternatives.iptables.current
mv /var/tmp/alternatives.iptables.setup /var/lib/alternatives/iptables
%if "%{_sbindir}" == "%{_bindir}"
for name in ip{,6}tables{,-save,-restore}; do
    test -h /usr/sbin || ln -s ../bin/$name /usr/sbin/$name 2>/dev/null || :
done
%endif
%post services

%systemd_post arptables.service ebtables.service
%systemd_post iptables.service ip6tables.service
%preun services

%systemd_preun arptables.service ebtables.service
%systemd_preun iptables.service ip6tables.service
%postun services

%?ldconfig
%systemd_postun arptables.service ebtables.service
%systemd_postun iptables.service ip6tables.service
%post -e nft

[[ %%{_excludedocs} == 1 ]] || do_man=true
for pfx in %{_prefix}/sbin/{eb,arp}tables; do
	for sfx in "" "-restore" "-save"; do
		if [ "$(readlink -e $pfx$sfx)" == $pfx$sfx ]; then
			rm -f $pfx$sfx
		fi
	done
done
for manpfx in %{_mandir}/man8/{eb,arp}tables; do
	for sfx in {,-restore,-save}.8.gz; do
		if [ "$(readlink -e $manpfx$sfx)" == $manpfx$sfx ]; then
			rm -f $manpfx$sfx
		fi
	done
done
pfx=%{_sbindir}/iptables
pfx6=%{_sbindir}/ip6tables
update-alternatives --install \
	$pfx iptables $pfx-nft 10 \
	--follower $pfx6 ip6tables $pfx6-nft \
	--follower $pfx-restore iptables-restore $pfx-nft-restore \
	--follower $pfx-save iptables-save $pfx-nft-save \
	--follower $pfx6-restore ip6tables-restore $pfx6-nft-restore \
	--follower $pfx6-save ip6tables-save $pfx6-nft-save
pfx=%{_sbindir}/ebtables
manpfx=%{_mandir}/man8/ebtables
update-alternatives --install \
	$pfx ebtables $pfx-nft 10 \
	--follower $pfx-save ebtables-save $pfx-nft-save \
	--follower $pfx-restore ebtables-restore $pfx-nft-restore \
	${do_man:+--follower $manpfx.8.gz ebtables-man $manpfx-nft.8.gz}
pfx=%{_sbindir}/arptables
manpfx=%{_mandir}/man8/arptables
update-alternatives --install \
	$pfx arptables $pfx-nft 10 \
	--follower $pfx-save arptables-save $pfx-nft-save \
	--follower $pfx-restore arptables-restore $pfx-nft-restore \
	${do_man:+--follower $manpfx.8.gz arptables-man $manpfx-nft.8.gz} \
	${do_man:+--follower $manpfx-save.8.gz arptables-save-man $manpfx-nft-save.8.gz} \
	${do_man:+--follower $manpfx-restore.8.gz arptables-restore-man $manpfx-nft-restore.8.gz}
%if "%{_sbindir}" == "%{_bindir}"
for name in ip{,6}tables{,-save,-restore} ebtables{,-save,-restore} arptables{,-save,-restore}; do
    test -h /usr/sbin || ln -s ../bin/$name /usr/sbin/$name 2>/dev/null || :
done
%endif
%postun nft

if [ $1 -eq 0 ]; then
	for cmd in iptables ebtables arptables; do
		update-alternatives --remove $cmd %{_sbindir}/$cmd-nft
	done
fi
%files -f %{oreon_filedir}/main.list
%files -n iptables-legacy -f %{oreon_filedir}/iptables-legacy.list
%files -n iptables-libs -f %{oreon_filedir}/iptables-libs.list
%files -n iptables-legacy-libs -f %{oreon_filedir}/iptables-legacy-libs.list
%files -n iptables-devel -f %{oreon_filedir}/iptables-devel.list
%files -n iptables-legacy-devel -f %{oreon_filedir}/iptables-legacy-devel.list
%files -n iptables-services -f %{oreon_filedir}/iptables-services.list
%files -n iptables-utils -f %{oreon_filedir}/iptables-utils.list
%files -n iptables-nft -f %{oreon_filedir}/iptables-nft.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.8.13-1
- Prepare for Oreon 11 (RP1)
