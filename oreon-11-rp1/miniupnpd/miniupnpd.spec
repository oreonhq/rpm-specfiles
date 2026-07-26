%global source0_hash 66cb3c3d697ab2bb3a61d3c48628166d6ba328d7c2dbeb95898fdf2a3202af7b

Name:       miniupnpd
Version:    2.3.9
Release:    4%{?dist}
Summary:    Lightweight UPnP IGD & PCP/NAT-PMP daemon

# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
URL:        https://miniupnp.tuxfamily.org/
Source0:    http://miniupnp.free.fr/files/%{name}-%{version}.tar.gz
Source1:    miniupnpd.service
Patch0:     miniupnpd-init-selinux.patch

BuildRequires:  gcc
%{?systemd_requires}
BuildRequires:  systemd
%if 0%{?with_iptables}
BuildRequires:  iptables-devel
%else
Buildrequires:  libmnl-devel
Buildrequires:  libnftnl-devel
%endif
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  procps-ng

# requires ENABLE_HTTPS to be set
#BuildRequires:  openssl-devel
#BuildRequires:  zlib-devel

%description
The MiniUPnP daemon is an UPnP IGD & PCP/NAT-PMP daemon for gateway routers.

UPnP IGD & PCP/NAT-PMP are used to improve internet connectivity for devices behind
a NAT router. Any peer to peer network application such as games, IM, etc. can
benefit from a NAT router supporting UPnP IGD & PCP/NAT-PMP.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# Disable WANPPPConnection based on recommendation from Fresh Tomato and OpenWRT
# Other distros like Arch and Ubuntu do not have this change
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
./configure \
 --ipv6 \
 --igd2 \
 --disable-pppconn \
%if 0%{?with_iptables}
 --firewall=iptables
%else
 --firewall=nftables
%endif
sed -i 's/ OS_NAME.*$/ OS_NAME "Fedora"/' config.h
sed -i 's/ OS_VERSION.*$/ OS_VERSION "%{fedora}\/%%s"/' config.h
sed -i 's/ OS_URL.*$/ OS_URL "https:\/\/getfedora.org"/' config.h
sed -i 's/^CFLAGS.*$//g' Makefile
sed -i 's/^LDFLAGS.*$//g' Makefile
sed -i 's/        policy drop;/        policy accept;/' netfilter_nft/scripts/nft_init.sh
%make_build

%install
export STRIP="/bin/true"
%make_install

install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

#Install new script not caught in upstream Makefile
install -Dpm 644 netfilter_nft/scripts/miniupnpd_functions.sh %{buildroot}%{_sysconfdir}/%{name}/miniupnpd_functions.sh

#Do not ship SysVinit script
rm -f %{buildroot}/etc/init.d/%{name}

#sbin migration for F42+
%if 0%{?fedora} >= 42
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}/usr/sbin/%{name} %{buildroot}%{_bindir}/%{name}
%endif

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%doc INSTALL README
%{_sbindir}/%{name}
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/*.sh
%config(noreplace) %{_sysconfdir}/%{name}/miniupnpd.conf
%{_mandir}/man8/%{name}.8.gz
%{_unitdir}/%{name}.service

%changelog
%autochangelog
