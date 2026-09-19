%global source0_hash 4f9a0656ce5c90868f551cd4deeb2d04f33899667e1fb2818b64e432fe8f629c

Summary: User space tool to set up tables of ARP rules in kernel
Name:    arptables
Version: 0.0.5
Release: 20%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later

URL:     http://ebtables.sourceforge.net/
Source0: http://ftp.netfilter.org/pub/arptables/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires: perl-generators
BuildRequires: make

%description
The arptables is a user space tool used to set up and maintain
the tables of ARP rules in the Linux kernel. These rules inspect
the ARP frames which they see. arptables is analogous to the iptables
user space tool, but is less complicated.

%package legacy
Summary: Legacy user space tool to set up tables of ARP rules in kernel
Requires(post): /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives

%sbin_merge_compat %{_prefix}/sbin/arptables

%description legacy
The arptables is a user space tool used to set up and maintain
the tables of ARP rules in the Linux kernel. These rules inspect
the ARP frames which they see. arptables is analogous to the iptables
user space tool, but is less complicated.

Note that it is considered legacy upstream since nftables provides the same
functionality in a much newer code-base. To aid in migration, there is
arptables-nft utility, a drop-in replacement for the legacy one which uses
nftables internally. It is provided by iptables-arptables package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# Makefile uses $(KERNEL_DIR) to redefine where to look for header files.
# But when it's set to standard system include directory gcc ignores it
# (see gcc(1)). It however looks that the code is not ready for using 
# system headers (instead included ones) so we don't use this option.
make all 'COPT_FLAGS=%{optflags}' 'LDFLAGS=%{build_ldflags}' %{_smp_mflags}

%install
make install DESTDIR=%{buildroot} BINDIR=%{_sbindir} MANDIR=%{_mandir}
pfx=%{buildroot}%{_sbindir}
manpfx=%{buildroot}%{_mandir}/man8
for sfx in "-restore" "-save"; do
	mv $pfx/arptables$sfx $pfx/arptables-legacy$sfx
	mv $manpfx/arptables${sfx}.8 $manpfx/arptables-legacy${sfx}.8
done

rm -rf %{buildroot}%{_initrddir}

%post legacy
pfx=%{_sbindir}/arptables
manpfx=%{_mandir}/man8/arptables
update-alternatives --install \
	$pfx arptables $pfx-legacy 10 \
	--slave $pfx-save arptables-save $pfx-legacy-save \
	--slave $pfx-restore arptables-restore $pfx-legacy-restore \
	--slave $manpfx.8.gz arptables-man $manpfx-legacy.8.gz \
	--slave $manpfx-save.8.gz arptables-save-man $manpfx-legacy-save.8.gz \
	--slave $manpfx-restore.8.gz arptables-restore-man $manpfx-legacy-restore.8.gz

%postun legacy
if [ $1 -eq 0 ]; then
	update-alternatives --remove \
		arptables %{_sbindir}/arptables-legacy
fi

%files legacy
%{!?_licensedir:%global license %%doc}
%license COPYING
%{_sbindir}/arptables-legacy*
%{_mandir}/*/arptables-legacy*
%ghost %attr(0755,root,root) %{_sbindir}/arptables{,-save,-restore}
%ghost %attr(0644,root,root) %{_mandir}/man8/arptables{,-save,-restore}.8.gz

%changelog
%autochangelog
