%global source0_hash 262864cfd198123d3e5dbe91937441b97ee9059d6d712e1a5bfbb1c54668d14d
Name:    NetworkManager
Summary:        Network connection manager and user applications
License: GPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://networkmanager.dev/
Group:   System Environment/Base
Epoch:   1
Version: 1.58.1
Release:        1%{?dist}
%global wpa_supplicant_version 1:1.1
%global ppp_version %(pkg-config --modversion pppd 2>/dev/null || sed -n 's/^#define\\s*VERSION\\s*"\\([^\\s]*\\)"$/\\1/p' %{_includedir}/pppd/patchlevel.h 2>/dev/null | grep . || echo bad)
%global glib2_version %(pkg-config --modversion glib-2.0 2>/dev/null || echo bad)
%global bcond_default_debug 0
%global bcond_default_lto %{nil}
%global bcond_default_test 0
%global obsoletes_device_plugins     1:0.9.9.95-1
%global obsoletes_ppp_plugin         1:1.5.3
%global obsoletes_initscripts_updown 1:1.36.0-0.6
%global obsoletes_ifcfg_rh           1:1.36.2
%global nmlibdir %{_prefix}/lib/%{name}
%global nmplugindir %{_libdir}/%{name}/%{version}-%{release}
%global _hardened_build 1
%global systemd_units NetworkManager.service NetworkManager-wait-online.service NetworkManager-dispatcher.service nm-priv-helper.service
%global systemd_units_cloud_setup nm-cloud-setup.service nm-cloud-setup.timer
%bcond_without dhclient
%bcond_without adsl
%bcond_without bluetooth
%bcond_without wwan
%bcond_without team
%bcond_without wifi
%bcond_without ovs
%bcond_without ppp
%bcond_without nmtui
%bcond_without nm_cloud_setup
%bcond_without regen_docs
%bcond_with    debug
%bcond_with    test
%if "%{?bcond_default_lto}" == ""
%bcond_with    lto
%else
%if %{bcond_default_lto}
%bcond_without lto
%else
%bcond_with    lto
%endif
%endif
%bcond_with    sanitizer
%bcond_with connectivity_fedora
%bcond_with connectivity_redhat
%bcond_without iwd
%bcond_with polkit_noauth_group
%global dbus_version 1.9.18
%global dbus_sys_dir %{_datadir}/dbus-1/system.d
%if %{with bluetooth} || %{with wwan}
%global with_modem_manager_1 1
%else
%global with_modem_manager_1 0
%endif
%global dns_rc_manager_default symlink
%if 0%{?fedora} >= 33 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%bcond_with default_ifcfg_rh
%else
%bcond_without default_ifcfg_rh
%endif
%bcond_without ifcfg_rh
%bcond_with split_ifcfg_rh
%bcond_with ifcfg_warning
%bcond_with ifcfg_migrate
%global ebpf_enabled "no"
%define _lto_cflags %{nil}
Source0:        https://gitlab.freedesktop.org/%{name}/%{name}/-/releases/%{version}/downloads/%{name}-%{version}.tar.xz
Source1: NetworkManager.conf
Source2: 00-server.conf
Source4: 20-connectivity-fedora.conf
Source5: 20-connectivity-redhat.conf
Source6: 22-wifi-mac-addr.conf
Source7: 70-nm-connectivity.conf
Source8: readme-ifcfg-rh.txt
Source9: readme-ifcfg-rh-migrated.txt
Requires(post): systemd
Requires(post): systemd-udev
Requires(post): /usr/sbin/update-alternatives
Requires(preun): systemd
Requires(preun): /usr/sbin/update-alternatives
Requires(postun): systemd
Requires: dbus >= %{dbus_version}
Requires: glib2 >= %{glib2_version}
Requires: %{name}-libnm%{?_isa} = %{epoch}:%{version}-%{release}
Recommends: iputils
Obsoletes: NetworkManager < %{obsoletes_device_plugins}
Obsoletes: NetworkManager < %{obsoletes_ppp_plugin}
Obsoletes: NetworkManager-wimax < 1:1.2
Obsoletes: NetworkManager < %{obsoletes_initscripts_updown}
%if %{with split_ifcfg_rh}
Obsoletes: NetworkManager < %{obsoletes_ifcfg_rh}
%endif
%if 0%{without team}
%endif
%if %{without ifcfg_rh}
%endif
Conflicts: NetworkManager-vpnc < 1:0.7.0.99-1
Conflicts: NetworkManager-openvpn < 1:0.7.0.99-1
Conflicts: NetworkManager-pptp < 1:0.7.0.99-1
Conflicts: NetworkManager-openconnect < 0:0.7.0.99-1
Conflicts: kde-plasma-networkmanagement < 1:0.9-0.49.20110527git.nm09
%if 0%{without team}
%endif
%if %{with ppp}
%endif
%if %{with regen_docs}
%endif
%if %{with bluetooth}
%endif
%if 0%{?with_modem_manager_1}
%endif
%if %{with wwan}
%endif
%if %{with nmtui}
%endif
%if %{with sanitizer}
%endif
Provides: %{name}-dispatcher%{?_isa} = %{epoch}:%{version}-%{release}
Provides: bundled(systemd) = 0
# oreon:deps
BuildRequires:  /usr/bin/dbus-launch
BuildRequires:  /usr/bin/valac
BuildRequires:  ModemManager-glib-devel
BuildRequires:  audit-libs-devel
BuildRequires:  bluez-libs-devel
BuildRequires:  dbus-devel
BuildRequires:  firewalld-filesystem
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  gnutls-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  iproute
BuildRequires:  iproute-tc
BuildRequires:  jansson-devel
BuildRequires:  libcurl-devel
BuildRequires:  libndp-devel
BuildRequires:  libnvme-devel
BuildRequires:  libpsl-devel
BuildRequires:  libselinux-devel
BuildRequires:  libtool
BuildRequires:  libudev-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  mobile-broadband-provider-info-devel
BuildRequires:  newt-devel
BuildRequires:  pkgconfig
BuildRequires:  polkit-devel
BuildRequires:  ppp-devel
BuildRequires:  python3
BuildRequires:  python3-dbus
BuildRequires:  python3-gobject-base
BuildRequires:  python3-pexpect
BuildRequires:  readline-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  teamd-devel
# /oreon:deps
%description
NetworkManager is a system service that manages network interfaces and
connections based on user or automatic configuration. It supports
Ethernet, Bridge, Bond, VLAN, Team, InfiniBand, Wi-Fi, mobile broadband
(WWAN), PPPoE and other devices, and supports a variety of different VPN
services.

%if %{with adsl}
%endif
%package adsl
Summary: ADSL device plugin for NetworkManager
Group: System Environment/Base
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes: NetworkManager < %{obsoletes_device_plugins}
%description adsl
This package contains NetworkManager support for ADSL devices.

%if %{with bluetooth}
%endif
%package bluetooth
Summary: Bluetooth device plugin for NetworkManager
Group: System Environment/Base
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: NetworkManager-wwan = %{epoch}:%{version}-%{release}
Requires: bluez >= 4.101-5
Obsoletes: NetworkManager < %{obsoletes_device_plugins}
%description bluetooth
This package contains NetworkManager support for Bluetooth devices.

%if %{with team}
%endif
%package team
Summary: Team device plugin for NetworkManager
Group: System Environment/Base
BuildRequires: teamd-devel
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes: NetworkManager < %{obsoletes_device_plugins}
Obsoletes: NetworkManager < 1:1.0.0
%description team
This package contains NetworkManager support for team devices.

%if %{with wifi}
%endif
%package wifi
Summary: Wifi plugin for NetworkManager
Group: System Environment/Base
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%if 0%{?fedora} >= 29 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
Requires: wireless-regdb
%else
Requires: crda
%endif
%if %{with iwd}
Requires: (wpa_supplicant >= %{wpa_supplicant_version} or iwd)
Suggests: wpa_supplicant
%else
Requires: wpa_supplicant >= %{wpa_supplicant_version}
%endif
Obsoletes: NetworkManager < %{obsoletes_device_plugins}
%description wifi
This package contains NetworkManager support for Wifi and OLPC devices.

%if %{with wwan}
%endif
%package wwan
Summary: Mobile broadband device plugin for NetworkManager
Group: System Environment/Base
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: ModemManager
Obsoletes: NetworkManager < %{obsoletes_device_plugins}
%description wwan
This package contains NetworkManager support for mobile broadband (WWAN)
devices.

%if %{with ovs}
%endif
%package ovs
Summary: Open vSwitch device plugin for NetworkManager
Group: System Environment/Base
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description ovs
This package contains NetworkManager support for Open vSwitch bridges.

%if %{with ppp}
%endif
%package ppp
Summary: PPP plugin for NetworkManager
Group: System Environment/Base
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires: ppp = %{ppp_version}
Requires: NetworkManager = %{epoch}:%{version}-%{release}
Obsoletes: NetworkManager < %{obsoletes_ppp_plugin}
%description ppp
This package contains NetworkManager support for PPP.

%package libnm
Summary: Libraries for adding NetworkManager support to applications.
Group: Development/Libraries
Conflicts: NetworkManager-glib < 1:1.31.0
License: LGPL-2.1-or-later
%description libnm
This package contains the libraries that make it easier to use some
NetworkManager functionality from applications.

%package libnm-devel
Summary: Header files for adding NetworkManager support to applications.
Group: Development/Libraries
Requires: %{name}-libnm%{?_isa} = %{epoch}:%{version}-%{release}
Requires: glib2-devel
Requires: pkgconfig
License: LGPL-2.1-or-later
%description libnm-devel
This package contains the header and pkg-config files for development
applications using NetworkManager functionality from applications.

%if %{with connectivity_redhat}
%endif
%package config-connectivity-redhat
Summary: NetworkManager config file for connectivity checking via Red Hat servers
Group: System Environment/Base
BuildArch: noarch
Provides: NetworkManager-config-connectivity = %{epoch}:%{version}-%{release}
%description config-connectivity-redhat
This adds a NetworkManager configuration file to enable connectivity checking
via Red Hat infrastructure.

%package config-server
Summary: NetworkManager config file for "server-like" defaults
Group: System Environment/Base
BuildArch: noarch
%description config-server
This adds a NetworkManager configuration file to make it behave more
like the old "network" service. In particular, it stops NetworkManager
from automatically running DHCP on unconfigured ethernet devices, and
allows connections with static IP addresses to be brought up even on
ethernet devices with no carrier.

This package is intended to be installed by default for server
deployments.

%if %{with ifcfg_rh}
%endif
%package dispatcher-routing-rules
Summary: NetworkManager dispatcher file for advanced routing rules
Group: System Environment/Base
%if %{with split_ifcfg_rh}
Requires: %{name}-initscripts-ifcfg-rh
%endif
Requires: ipcalc
BuildArch: noarch
Provides: %{name}-config-routing-rules = %{epoch}:%{version}-%{release}
Obsoletes: %{name}-config-routing-rules < 1:1.31.0
%description dispatcher-routing-rules
This adds a NetworkManager dispatcher file to support networking
configurations using "/etc/sysconfig/network-scripts/rule-NAME" files
(eg, to do policy-based routing).

%if %{with nmtui}
%endif
%package tui
Summary: NetworkManager curses-based UI
Group: System Environment/Base
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: %{name}-libnm%{?_isa} = %{epoch}:%{version}-%{release}
%description tui
This adds a curses-based "TUI" (Text User Interface) to
NetworkManager, to allow performing some of the operations supported
by nm-connection-editor and nm-applet in a non-graphical environment.

%if %{with split_ifcfg_rh}
%endif
%package initscripts-ifcfg-rh
Summary: NetworkManager plugin for reading and writing connections in ifcfg-rh format
Group: System Environment/Base
Requires: %{name} = %{epoch}:%{version}-%{release}
Obsoletes: NetworkManager < %{obsoletes_ifcfg_rh}
%description initscripts-ifcfg-rh
Installs a plugin for reading and writing connection profiles using
the Red Hat ifcfg format in /etc/sysconfig/network-scripts/.

%if %{with nm_cloud_setup}
%endif
%package cloud-setup
Summary: Automatically configure NetworkManager in cloud
Group: System Environment/Base
Requires: %{name} = %{epoch}:%{version}-%{release}
Requires: %{name}-libnm%{?_isa} = %{epoch}:%{version}-%{release}
%description cloud-setup
Installs a nm-cloud-setup tool that can automatically configure
NetworkManager in cloud environment. Only certain cloud providers
like Aliyun, Azure, EC2, GCP are supported.

%if %{with ifcfg_rh}
%endif
%package initscripts-updown
Summary: Legacy ifup/ifdown scripts for NetworkManager that replace initscripts (network-scripts)
Group: System Environment/Base
BuildArch: noarch
Requires: NetworkManager
Requires: /usr/bin/nmcli
Obsoletes: NetworkManager < %{obsoletes_initscripts_updown}
%description initscripts-updown
Installs alternative ifup/ifdown scripts that talk to NetworkManager.
This is only for backward compatibility with initscripts (network-scripts).
Preferably use nmcli instead.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n NetworkManager-%{version_no_tilde}

%build

%meson \
	-Db_ndebug=false \
	--warnlevel 2 \
%if %{with test}
	--werror \
%endif
	-Dnft=%{_sbindir}/nft \
	-Diptables=%{_sbindir}/iptables \
	-Dip6tables=%{_sbindir}/ip6tables \
%if %{with dhclient}
	-Ddhclient=%{_sbindir}/dhclient \
%else
	-Ddhclient=no \
%endif
	-Ddhcpcd=no \
	-Dcrypto=gnutls \
%if %{with debug}
	-Dmore_logging=true \
	-Dmore_asserts=10000 \
%else
	-Dmore_logging=false \
	-Dmore_asserts=0 \
%endif
	-Dld_gc=true \
%if %{with lto}
	-D b_lto=true \
%else
	-D b_lto=false \
%endif
	-Dlibaudit=yes-disabled-by-default \
%if 0%{?with_modem_manager_1}
	-Dmodem_manager=true \
%else
	-Dmodem_manager=false \
%endif
%if %{with wifi}
	-Dwifi=true \
	-Dwext=false \
%else
	-Dwifi=false \
%endif
%if %{with iwd}
	-Diwd=true \
%else
	-Diwd=false \
%endif
%if %{with bluetooth}
	-Dbluez5_dun=true \
%else
	-Dbluez5_dun=false \
%endif
%if %{with nmtui}
	-Dnmtui=true \
%else
	-Dnmtui=false \
%endif
%if %{with nm_cloud_setup}
	-Dnm_cloud_setup=true \
%else
	-Dnm_cloud_setup=false \
%endif
	-Dvapi=true \
	-Dintrospection=true \
%if %{with regen_docs}
	-Ddocs=true \
%else
	-Ddocs=false \
%endif
	-Dqt=false \
%if %{with team}
	-Dteamdctl=true \
%else
	-Dteamdctl=false \
%endif
%if %{with ovs}
	-Dovs=true \
%else
	-Dovs=false \
%endif
	-Dselinux=true \
	-Dpolkit=true  \
	-Dconfig_auth_polkit_default=true \
%if %{with polkit_noauth_group}
	-Dpolkit_noauth_group=wheel \
%endif
	-Dconcheck=true \
	-Dlibpsl=false \
%if %{ebpf_enabled} != "yes"
	-Debpf=false \
%else
	-Debpf=true \
%endif
	-Dsession_tracking=systemd \
	-Dsuspend_resume=systemd \
	-Dsystemdsystemunitdir=%{_unitdir} \
	-Dsystem_ca_path=/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem \
	-Ddbus_conf_dir=%{dbus_sys_dir} \
	-Dtests=yes \
	-Dvalgrind=no \
%if %{with ifcfg_rh}
	-Difcfg_rh=true \
%else
	-Difcfg_rh=false \
%endif
	-Difupdown=false \
%if %{with ppp}
	-Dppp=true \
	-Dpppd="%{_sbindir}/pppd" \
	-Dpppd_plugin_dir="%{_libdir}/pppd/%{ppp_version}" \
%else
	-Dppp=false \
%endif
	-Ddist_version=%{version}-%{release} \
%if %{with default_ifcfg_rh}
	-Dconfig_plugins_default=ifcfg-rh \
%endif
%if %{with ifcfg_migrate}
	-Dconfig_migrate_ifcfg_rh_default=true \
%endif
	-Dresolvconf=no \
	-Dnetconfig=no \
	-Dconfig_dns_rc_manager_default=%{dns_rc_manager_default} \
	-Dconfig_logging_backend_default=journal
%meson_build
%install
%meson_install
cp %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}/
cp %{SOURCE2} %{buildroot}%{nmlibdir}/conf.d/
%if %{with connectivity_redhat}
cp %{SOURCE5} %{buildroot}%{nmlibdir}/conf.d/
mkdir -p %{buildroot}%{_sysctldir}
cp %{SOURCE7} %{buildroot}%{_sysctldir}
%endif
%if %{with ifcfg_warning}
cp %{SOURCE8} %{buildroot}%{_sysconfdir}/sysconfig/network-scripts
%endif
%if %{with ifcfg_migrate}
cp %{SOURCE9} %{buildroot}%{_sysconfdir}/sysconfig/network-scripts/readme-ifcfg-rh.txt
%endif
%if %{with ifcfg_rh}
cp examples/dispatcher/10-ifcfg-rh-routes.sh %{buildroot}%{nmlibdir}/dispatcher.d/
ln -s ../no-wait.d/10-ifcfg-rh-routes.sh %{buildroot}%{nmlibdir}/dispatcher.d/pre-up.d/
ln -s ../10-ifcfg-rh-routes.sh %{buildroot}%{nmlibdir}/dispatcher.d/no-wait.d/
%endif
%find_lang %{name}
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/pppd/%{ppp_version}/*.la
rm -f %{buildroot}%{nmplugindir}/*.la
rm -f %{buildroot}%{_unitdir}/NetworkManager-config-initrd.service
rm -f %{buildroot}%{_unitdir}/NetworkManager-initrd.service
rm -f %{buildroot}%{_unitdir}/NetworkManager-wait-online-initrd.service
find %{buildroot}%{_datadir}/gtk-doc -exec touch --reference meson.build '{}' \+
%if 0%{?__debug_package} && ! 0%{?flatpak}
mkdir -p %{buildroot}%{_prefix}/src/debug/NetworkManager-%{version_no_tilde}
cp valgrind.suppressions %{buildroot}%{_prefix}/src/debug/NetworkManager-%{version_no_tilde}
%endif
%if %{with ifcfg_rh}
touch %{buildroot}%{_sbindir}/ifup
touch %{buildroot}%{_sbindir}/ifdown
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

%if %{with test}
%meson_test
%else
%ninja_test -C %{_vpath_builddir} || :
%endif
%pre

if [ -f "%{_unitdir}/network-online.target.wants/NetworkManager-wait-online.service" ] ; then
    systemctl enable NetworkManager-wait-online.service || :
fi
%post

if [ -S /run/udev/control ]; then
    /usr/bin/udevadm control --reload-rules || :
    /usr/bin/udevadm trigger --subsystem-match=net || :
fi
%firewalld_reload
%systemd_post %{systemd_units}
%if %{with ifcfg_rh}
%post initscripts-updown

if [ -f %{_sbindir}/ifup -a ! -L %{_sbindir}/ifup ]; then
    /usr/sbin/update-alternatives --remove ifup %{_libexecdir}/nm-ifup >/dev/null 2>&1 || :
else
    /usr/sbin/update-alternatives --install %{_sbindir}/ifup ifup %{_libexecdir}/nm-ifup 50 \
        --slave %{_sbindir}/ifdown ifdown %{_libexecdir}/nm-ifdown
fi
%endif
%if %{with nm_cloud_setup}
%post cloud-setup

%systemd_post %{systemd_units_cloud_setup}
%endif
%preun

if [ $1 -eq 0 ]; then
    /bin/systemctl --no-reload disable NetworkManager.service >/dev/null 2>&1 || :
fi
%systemd_preun NetworkManager-wait-online.service NetworkManager-dispatcher.service nm-priv-helper.service
%if %{with ifcfg_rh}
%preun initscripts-updown

if [ $1 -eq 0 ]; then
    /usr/sbin/update-alternatives --remove ifup %{_libexecdir}/nm-ifup >/dev/null 2>&1 || :
fi
%endif
%if %{with nm_cloud_setup}
%preun cloud-setup

%systemd_preun %{systemd_units_cloud_setup}
%endif
%postun

/usr/bin/udevadm control --reload-rules || :
/usr/bin/udevadm trigger --subsystem-match=net || :
%firewalld_reload
%systemd_postun %{systemd_units}
%if %{with nm_cloud_setup}
%postun cloud-setup

%systemd_postun %{systemd_units_cloud_setup}
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
