%global source0_hash 25b7b49d484bec74fa6c40ae33c7740a23c125e0aa909b5834335697c934f1cd

# The man pages documenting ifcfg format don't necessarily
# describe valid configs for RH/Fedora systems...
%bcond_with ifcfg_manpages

%global wicked_piddir   %{_rundir}/%{name}
%global wicked_statedir %{_rundir}/%{name}
%global wicked_storedir %{_sharedstatedir}/%{name}

%if 0%{?rhel} && 0%{?rhel} < 9
%global dbus_service dbus-daemon.service
%else
%global dbus_service dbus-broker.service
%endif

Name:           wicked
Version:        0.6.77
Release:        3%{?dist}
Summary:        Network configuration infrastructure
License:        GPL-2.0-or-later
URL:            https://en.opensuse.org/Portal:Wicked
Source0:        https://github.com/openSUSE/%{name}/archive/version-%{version}/%{name}-version-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-route-3.0)
BuildRequires:  libgcrypt-devel

Requires:       dbus-common
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
%{?systemd_requires}

%description
Wicked is a network configuration infrastructure incorporating a number
of existing frameworks into a unified architecture, providing a DBUS
interface to network configuration.

%package devel
Summary:        Network configuration infrastructure - Development files
Requires:       lib%{name}%{?_isa} = %{version}-%{release}

%description devel
Wicked is a network configuration infrastructure incorporating a number
of existing frameworks into a unified architecture, providing a DBUS
interface to network configuration.

This package provides the wicked development files.

%package -n     lib%{name}
Summary:        Network configuration infrastructure - Shared library

%description -n lib%{name}
Wicked is a network configuration infrastructure incorporating a number
of existing frameworks into a unified architecture, providing a DBUS
interface to network configuration.

This package provides the wicked shared library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-version-%{version} -p1

%build
test -x ./configure || autoreconf --force --install --verbose
# Wicked does not build on GCC5+ without gnu89 mode... :(
export CFLAGS="-std=gnu89 %{__global_cflags}"
%configure \
	--with-piddir=%{wicked_piddir}	\
	--with-statedir=%{wicked_statedir} \
	--with-storedir=%{wicked_storedir} \
	--with-compat=redhat \
	--enable-systemd		\
	--with-systemd-unitdir=%{_unitdir} \
	--without-dbus-servicedir	\
	--disable-static

%make_build

%install
%make_install

# remove libwicked.a and la
rm -f %{buildroot}%{_libdir}/libwicked*.*a
# create reboot-persistent (leases) store directory
mkdir -p -m 0750 %{buildroot}%{wicked_storedir}

# move dbus policy configs to /usr/share
mv %{buildroot}%{_sysconfdir}/dbus-1 %{buildroot}%{_datadir}

# remove suse if{up,down,status} manpages, as they don't apply for us
rm -f %{buildroot}%{_mandir}/man8/if{up,down,status}.*

%if ! %{with ifcfg_manpages}
# remove ifcfg manpages as they don't necessarily document valid setups for RH/Fedora
rm -f %{buildroot}%{_mandir}/man5/if{cfg,route,rule,sysctl}*
rm -f %{buildroot}%{_mandir}/man5/routes*
%endif

%preun
# stop the daemons on removal
# - stopping wickedd should be sufficient ... other just to be sure.
# - stopping of the wicked.service does not stop network, but removes
#   the wicked.service --> network.service link and resets its status.
%systemd_preun wickedd.service wickedd-auto4.service wickedd-dhcp4.service wickedd-dhcp6.service wickedd-nanny.service wicked.service

%post
# reload dbus after install or upgrade to apply new policies
systemctl reload %{dbus_service} 2>/dev/null || :
# Run preset configuration for wicked service
%systemd_post wicked.service

%postun
# restart wickedd after upgrade
%systemd_postun_with_restart wickedd.service
# reload dbus after uninstall, our policies are gone again
if [ $1 -eq 0 ]; then
	/usr/bin/systemctl reload %{dbus_service} 2>/dev/null || :
fi

%ldconfig_scriptlets -n lib%{name}

%files
%doc ChangeLog ANNOUNCE README TODO samples
%license COPYING
%{_sbindir}/wicked*
%{_libexecdir}/%{name}/
%dir %{_sysconfdir}/wicked
%config(noreplace) %{_sysconfdir}/wicked/common.xml
%config(noreplace) %{_sysconfdir}/wicked/client.xml
%config(noreplace) %{_sysconfdir}/wicked/client-nbft.xml
%config(noreplace) %{_sysconfdir}/wicked/server.xml
%config(noreplace) %{_sysconfdir}/wicked/nanny.xml
%dir %{_sysconfdir}/wicked/scripts
%config(noreplace) %{_sysconfdir}/wicked/scripts/*
%dir %{_sysconfdir}/wicked/extensions
%config(noreplace) %{_sysconfdir}/wicked/extensions/*
%dir %{_sysconfdir}/wicked/ifconfig
%{_datadir}/dbus-1/system.d/org.opensuse.Network.conf
%{_datadir}/dbus-1/system.d/org.opensuse.Network.AUTO4.conf
%{_datadir}/dbus-1/system.d/org.opensuse.Network.DHCP4.conf
%{_datadir}/dbus-1/system.d/org.opensuse.Network.DHCP6.conf
%{_datadir}/dbus-1/system.d/org.opensuse.Network.Nanny.conf
%{_unitdir}/*.service
%dir %{_datadir}/wicked/
%dir %{_datadir}/wicked/schema
%{_datadir}/wicked/schema/*.xml
%{_mandir}/man5/wicked-config.5*
%if %{with ifcfg_manpages}
%{_mandir}/man5/ifcfg.5*
%{_mandir}/man5/ifcfg-bonding.5*
%{_mandir}/man5/ifcfg-bridge.5*
%{_mandir}/man5/ifcfg-dhcp.5*
%{_mandir}/man5/ifcfg-dummy.5*
%{_mandir}/man5/ifcfg-lo.5*
%{_mandir}/man5/ifcfg-macvlan.5*
%{_mandir}/man5/ifcfg-macvtap.5*
%{_mandir}/man5/ifcfg-ppp.5*
%{_mandir}/man5/ifcfg-ovs-bridge.5*
%{_mandir}/man5/ifcfg-team.5*
%{_mandir}/man5/ifcfg-tunnel.5*
%{_mandir}/man5/ifcfg-vlan.5*
%{_mandir}/man5/ifcfg-vxlan.5*
%{_mandir}/man5/ifcfg-wireless.5*
%{_mandir}/man5/ifroute.5*
%{_mandir}/man5/ifrule.5*
%{_mandir}/man5/ifsysctl.5*
%{_mandir}/man5/routes.5*
%endif
%{_mandir}/man8/wicked.8*
%{_mandir}/man8/wicked-redfish.8*
%{_mandir}/man8/wickedd.8*
%{_mandir}/man8/wicked-ethtool.8*
%{_mandir}/man8/wicked-firmware.8*
%attr(0750,root,root) %dir %{wicked_storedir}

%files devel
%{_includedir}/wicked/
%{_libdir}/libwicked.so
%{_datadir}/pkgconfig/wicked.pc
%{_mandir}/man7/wicked.7*

%files -n lib%{name}
%license COPYING
%{_libdir}/libwicked-%{version}.so

%changelog
%autochangelog
