%global source0_hash 7740026745ae1ba4a5dd90e71a06c324f31b53dda90e066d09aff308a233fab8

Name:           foomuuri
Version:        0.32
Release:        1%{?dist}
Summary:        Multizone bidirectional nftables firewall
License:        GPL-2.0-or-later
URL:            https://github.com/FoobarOy/foomuuri
Source0:        https://github.com/FoobarOy/foomuuri/archive/v%{version}/foomuuri-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
%if (%{defined fedora} && 0%{?fedora} <= 43)
BuildRequires:  pylint
BuildRequires:  python3-dbus
BuildRequires:  python3-flake8
BuildRequires:  python3-gobject
BuildRequires:  python3-pycodestyle
BuildRequires:  python3-systemd
BuildRequires:  python3-urllib3
%endif
Requires:       nftables
Requires:       python3-dbus
Requires:       python3-gobject
Requires:       python3-systemd
Recommends:     fping
Recommends:     jq
Recommends:     python3-lxml
Recommends:     python3-urllib3
Recommends:     (foomuuri-firewalld if NetworkManager)
%{?systemd_requires}

%description
Foomuuri is a firewall generator for nftables based on the concept of zones.
It is suitable for all systems from personal machines to corporate firewalls,
and supports advanced features such as a rich rule language, IPv4/IPv6 rule
splitting, dynamic DNS lookups, a D-Bus API and FirewallD emulation for
NetworkManager's zone support.

%package firewalld
Summary:        FirewallD emulation configuration files for Foomuuri
BuildArch:      noarch
Requires:       %{name} = %{version}

%description firewalld
Foomuuri is a firewall generator for nftables based on the concept of zones.
It is suitable for all systems from personal machines to corporate firewalls,
and supports advanced features such as a rich rule language, IPv4/IPv6 rule
splitting, dynamic DNS lookups, a D-Bus API and FirewallD emulation for
NetworkManager's zone support.

This optional package provides FirewallD D-Bus emulation for Foomuuri,
allowing dynamically assign interfaces to Foomuuri zones via NetworkManager.

%package -n prometheus-foomuuri-exporter
Summary:        Prometheus exporter for Foomuuri metrics
BuildArch:      noarch
Requires:       python3-prometheus_client
Provides:       foomuuri_exporter = %{version}-%{release}
Obsoletes:      foomuuri_exporter < 0.31-4

%description -n prometheus-foomuuri-exporter
Foomuuri is a firewall generator for nftables based on the concept of zones.
It is suitable for all systems from personal machines to corporate firewalls,
and supports advanced features such as a rich rule language, IPv4/IPv6 rule
splitting, dynamic DNS lookups, a D-Bus API and FirewallD emulation for
NetworkManager's zone support.

This optional package provides Prometheus exporter for Foomuuri metrics.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build

%install
make install DESTDIR=%{buildroot} BINDIR=%{_sbindir}
make -C prometheus install DESTDIR=%{buildroot}
%if %{defined fedora} || %{defined foobar}
mkdir -p %{buildroot}%{bash_completions_dir}
cp doc/foomuuri-bash-completion %{buildroot}%{bash_completions_dir}/foomuuri
%endif

%if (%{defined fedora} && 0%{?fedora} <= 43)
%check
make test
%endif

%post
%systemd_post foomuuri.service foomuuri-boot.service foomuuri-dbus.service foomuuri-iplist.timer foomuuri-iplist.service foomuuri-monitor.service
%tmpfiles_create foomuuri.conf

%preun
%systemd_preun foomuuri.service foomuuri-boot.service foomuuri-dbus.service foomuuri-iplist.timer foomuuri-iplist.service foomuuri-monitor.service

%postun
%systemd_postun foomuuri.service foomuuri-boot.service foomuuri-iplist.service
if [ $1 -ge 1 ]; then
    systemctl try-reload-or-restart foomuuri.service > /dev/null 2>&1 || :
fi
%systemd_postun_with_restart foomuuri-dbus.service foomuuri-monitor.service foomuuri-iplist.timer

%triggerun -- foomuuri < 0.27-3
systemctl stop foomuuri-resolve.timer foomuuri-resolve.service > /dev/null 2>&1 || :

%pretrans -n prometheus-foomuuri-exporter
if [ $1 -eq 1 ]; then
    if systemctl --quiet is-enabled foomuuri_exporter.service 2>/dev/null; then
        touch %{_sharedstatedir}/rpm-state/prometheus-foomuuri-exporter.enabled
    fi
    if systemctl --quiet is-active foomuuri_exporter.service 2>/dev/null; then
        touch %{_sharedstatedir}/rpm-state/prometheus-foomuuri-exporter.active
    fi
    if [ -f %{_sysconfdir}/default/foomuuri_exporter ]; then
        cp -p %{_sysconfdir}/default/foomuuri_exporter %{_sysconfdir}/default/prometheus-foomuuri-exporter
    fi
fi

%post -n prometheus-foomuuri-exporter
%systemd_post prometheus-foomuuri-exporter.service

%preun -n prometheus-foomuuri-exporter
%systemd_preun prometheus-foomuuri-exporter.service

%postun -n prometheus-foomuuri-exporter
%systemd_postun_with_restart prometheus-foomuuri-exporter.service

%posttrans -n prometheus-foomuuri-exporter
if [ $1 -eq 1 ]; then
    if [ -f %{_sharedstatedir}/rpm-state/prometheus-foomuuri-exporter.enabled ]; then
        rm -f %{_sharedstatedir}/rpm-state/prometheus-foomuuri-exporter.enabled
        systemctl enable prometheus-foomuuri-exporter.service >/dev/null 2>&1
    fi
    if [ -f %{_sharedstatedir}/rpm-state/prometheus-foomuuri-exporter.active ]; then
        rm -f %{_sharedstatedir}/rpm-state/prometheus-foomuuri-exporter.active
        systemctl start prometheus-foomuuri-exporter.service >/dev/null 2>&1
    fi
fi

%files
%license COPYING
%doc README.md CHANGELOG.md
%doc %{_mandir}/man8/foomuuri.8*
%attr(0750, root, adm) %dir %{_sysconfdir}/foomuuri
%{_sbindir}/foomuuri
%{_sysctldir}/50-foomuuri.conf
%dir %{_datadir}/foomuuri
%{_datadir}/foomuuri/default.services.conf
%{_datadir}/foomuuri/block.fw
%{_datadir}/foomuuri/static.nft
%{_unitdir}/foomuuri.service
%{_unitdir}/foomuuri-boot.service
%{_unitdir}/foomuuri-dbus.service
%{_unitdir}/foomuuri-iplist.service
%{_unitdir}/foomuuri-iplist.timer
%{_unitdir}/foomuuri-monitor.service
%{_tmpfilesdir}/foomuuri.conf
%ghost %dir %{_rundir}/foomuuri
%attr(0700, root, root) %dir %{_sharedstatedir}/foomuuri
%{_datadir}/dbus-1/system.d/fi.foobar.Foomuuri1.conf
%{_datadir}/polkit-1/actions/fi.foobar.Foomuuri1.policy
%if %{defined fedora} || %{defined foobar}
%{bash_completions_dir}/foomuuri
%endif

%files firewalld
%{_datadir}/dbus-1/system.d/fi.foobar.Foomuuri-FirewallD.conf
%{_datadir}/foomuuri/dbus-firewalld.conf

%files -n prometheus-foomuuri-exporter
%{_bindir}/prometheus-foomuuri-exporter
%config(noreplace) %{_sysconfdir}/default/prometheus-foomuuri-exporter
%{_unitdir}/prometheus-foomuuri-exporter.service

%changelog
%autochangelog
