%global source0_hash 91994b127da735b2c97f19992e34420648c0e8c4ace8a4bcb0596e7685c48678
Name:       miniupnpd
Version:    2.3.11
Release:        1%{?dist}
Summary:        Lightweight UPnP IGD & PCP/NAT-PMP daemon
License:    LicenseRef-Callaway-BSD
URL:        https://miniupnp.tuxfamily.org/
Source0:        http://miniupnp.free.fr/files/%{name}-%{version}.tar.gz
Source1:    miniupnpd.service
Patch0:     miniupnpd-init-selinux.patch
%{?systemd_requires}
%if 0%{?with_iptables}
%else
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libmnl-devel
BuildRequires:  libnftnl-devel
BuildRequires:  libuuid-devel
BuildRequires:  make
BuildRequires:  procps-ng
BuildRequires:  systemd
# /oreon:deps
%description
The MiniUPnP daemon is an UPnP IGD & PCP/NAT-PMP daemon for gateway routers.

UPnP IGD & PCP/NAT-PMP are used to improve internet connectivity for devices behind
a NAT router. Any peer to peer network application such as games, IM, etc. can
benefit from a NAT router supporting UPnP IGD & PCP/NAT-PMP.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

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
install -Dpm 644 netfilter_nft/scripts/miniupnpd_functions.sh %{buildroot}%{_sysconfdir}/%{name}/miniupnpd_functions.sh
rm -f %{buildroot}/etc/init.d/%{name}
%oreon_autofiles main

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
