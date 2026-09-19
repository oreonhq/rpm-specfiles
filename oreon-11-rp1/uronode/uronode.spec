%global source0_hash 9548f585513f68629ef0edd894e079efe84d799349fe43f7d3b4f0c932ad855a

# hardened build if not overriden
%{!?_hardened_build:%global _hardened_build 1}

%if %{?_hardened_build}%{!?_hardened_build:0}
%global cflags_harden -fpie
%global ldflags_harden -pie -z relro -z now
%endif

Summary: Alternative packet radio system for Linux
Name: uronode
Version: 2.15
Release: 11%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://uronode.sourceforge.net
BuildRequires: make
BuildRequires: gcc
BuildRequires: zlib-devel
BuildRequires: libax25-devel
BuildRequires: systemd
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1: flexd.service
Source2: uronode@.service
Source3: uronode.socket
Source4: uronode.xinetd
Source5: uronode-README.fedora
# Sent upstream
Patch: uronode-2.7-install-fix.patch
# Sent upstream
Patch: uronode-2.7-configure-non-interactive.patch
# Sent upstream
Patch: uronode-2.15-gcc-15-fix.patch

%description
URONode is an alternative packet radio system for Linux. It supports
cross-port digipeating, automatic importing of flexnet routing,
various IP functions, and ANSI colors.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Copy Fedora readme into place
cp -p %{SOURCE5} README.fedora

# Removing bundled libax25, using system one.
rm -rf include

%build
export NON_INTERACTIVE=1
export ETC_DIR=%{_sysconfdir}/ax25
export SBIN_DIR=%{_sbindir}
export BIN_DIR=%{_bindir}
export LIB_DIR=%{_prefix}/lib
export DATA_DIR=%{_datadir}
export MAN_DIR=%{_mandir}
export VAR_DIR=%{_var}
./configure
make %{?_smp_mflags} CFLAGS="%{optflags} %{?cflags_harden}" LDFLAGS="%{?__global_ldflags} %{?ldflags_harden}"

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

# Systemd
install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/flexd.service
install -Dpm 644 %{SOURCE2} %{buildroot}%{_unitdir}/uronode@.service
install -Dpm 644 %{SOURCE3} %{buildroot}%{_unitdir}/uronode.socket

# xinetd
install -Dpm 644 %{SOURCE4} %{buildroot}%{_datadir}/%{name}/xinetd.d/uronode

# ghost files
touch %{buildroot}/%{_var}/lib/flexd/destinations
# assert for case upstream would add default content
[ -s %{buildroot}%{_var}/lib/flexd/gateways ] && exit 1
[ -s %{buildroot}%{_var}/log/uronode/lastlog ] && exit 1
[ -s %{buildroot}%{_var}/lib/uronode/loggedin ] && exit 1

%post
%systemd_post flexd.service uronode.socket

# Create empty database of current users
[ -f %{_var}/lib/uronode/loggedin ] || touch %{_var}/lib/uronode/loggedin

%preun
%systemd_preun flexd.service uronode.socket

%postun
%systemd_postun_with_restart flexd.service uronode.socket

%files
%doc README.fedora README URONode.his FAQ COLORS CHANGES.1 CHANGES.2 COPYING

%{_sbindir}/*
%{_mandir}/*/*
%config(noreplace) %{_sysconfdir}/ax25/flexd.conf
%config(noreplace) %{_sysconfdir}/ax25/uronode.announce
%config(noreplace) %{_sysconfdir}/ax25/uronode.conf
%config(noreplace) %{_sysconfdir}/ax25/uronode.info
%config(noreplace) %{_sysconfdir}/ax25/uronode.motd
%config(noreplace) %{_sysconfdir}/ax25/uronode.perms
%config(noreplace) %{_sysconfdir}/ax25/uronode.routes
%config(noreplace) %{_sysconfdir}/ax25/uronode.users
%{_datadir}/%{name}/xinetd.d/uronode
%{_unitdir}/flexd.service
%{_unitdir}/uronode@.service
%{_unitdir}/uronode.socket
%{_datadir}/%{name}
%dir %{_var}/log/uronode
%dir %{_var}/lib/flexd
%dir %{_var}/lib/uronode
%ghost %{_var}/lib/uronode/loggedin
%ghost %{_var}/lib/flexd/gateways
%ghost %{_var}/log/uronode/lastlog
%ghost %{_var}/lib/flexd/destinations

%changelog
%autochangelog
