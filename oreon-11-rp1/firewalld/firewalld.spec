%global source0_hash 99d7468c22f6cafd8c72aa53173a632f2ca29cb19aec913e8ed45b6102af322d
Summary:        A firewall daemon with D-Bus interface providing a dynamic firewall
Name: firewalld
Version: 2.5.2
Release:        1%{?dist}
URL:     http://www.firewalld.org
License: GPL-2.0-or-later
Source0:        https://github.com/firewalld/firewalld/releases/download/v%{version}/firewalld-%{version}.tar.bz2
Source1: FedoraServer.xml
Source2: FedoraWorkstation.xml
Source3: org.fedoraproject.FirewallD1.desktop.rules.choice
Patch0: fedora-only-MDNS-default.patch
BuildArch: noarch
Recommends: iptables, ebtables, ipset
Suggests: iptables-nft
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: firewalld-filesystem = %{version}-%{release}
Requires: python3-firewall  = %{version}-%{release}
Obsoletes: firewalld-selinux < 0.4.4.2-2
Conflicts: selinux-policy < 3.14.1-28
Conflicts: cockpit-ws < 173-2
Recommends: libcap-ng-python3
Provides: variant_config(Server)
Provides: variant_config(Workstation)
Provides: variant_config(KDE Plasma)
Obsoletes: firewalld-config-standard <= 0.3.15
Obsoletes: firewalld-config-cloud <= 0.3.15
Obsoletes: firewalld-config-server <= 0.3.15
Obsoletes: firewalld-config-workstation <= 0.3.15
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  ebtables
BuildRequires:  gettext
BuildRequires:  glib2
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  ipset
BuildRequires:  iptables
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  systemd-units
# /oreon:deps
%description
firewalld is a firewall service daemon that provides a dynamic customizable 
firewall with a D-Bus interface.

%package -n python3-firewall
Summary: Python3 bindings for firewalld
%{?python_provide:%python_provide python3-firewall}
Obsoletes: python-firewall < 0.5.2-2
Obsoletes: python2-firewall < 0.5.2-2
Requires: python3-dbus
Requires: python3-gobject-base
Requires: python3-nftables
%description -n python3-firewall
Python3 bindings for firewalld.

%package -n firewalld-filesystem
Summary: Firewalld directory layout and rpm macros
%description -n firewalld-filesystem
This package provides directories and rpm macros which
are required by other packages that add firewalld configuration files.

%package -n firewalld-test
Summary: Firewalld testsuite
Requires: firewalld-filesystem = %{version}-%{release}
%description -n firewalld-test
This package provides the firewalld testsuite.

%package -n firewall-applet
Summary: Firewall panel applet
%if !0%{?flatpak}
Requires: %{name} = %{version}-%{release}
%endif
Requires: firewalld-filesystem = %{version}-%{release}
Requires: firewall-config = %{version}-%{release}
Requires: python3-firewall = %{version}-%{release}
Requires: hicolor-icon-theme
Requires: python3-qt5-base
Requires: python3-gobject
Requires: libnotify
Requires: NetworkManager-libnm
%if !0%{?flatpak}
Requires: dbus-x11
%endif
%description -n firewall-applet
The firewall panel applet provides a status information of firewalld and also 
the firewall settings.

%package -n firewall-config
Summary: Firewall configuration application
%if !0%{?flatpak}
Requires: %{name} = %{version}-%{release}
%endif
Requires: python3-firewall = %{version}-%{release}
Requires: firewalld-filesystem = %{version}-%{release}
Requires: hicolor-icon-theme
Requires: gtk3
Requires: python3-gobject
Requires: NetworkManager-libnm
%if !0%{?flatpak}
Requires: dbus-x11
Recommends: polkit
%endif
%description -n firewall-config
The firewall configuration application provides an configuration interface for 
firewalld.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
%if 0%{?flatpak}
sed -i -e 's|/usr|%{_prefix}|' src/firewall-applet.in src/firewall/config/__init__.py.in
%endif

%build

OPTS=(
  --enable-sysconfig
  --enable-rpmmacros
  --with-systemd-unitdir=%{_unitdir}
  --with-iptables=/usr/sbin/iptables
  --with-iptables-restore=/usr/sbin/iptables-restore
  --with-ip6tables=/usr/sbin/ip6tables
  --with-ip6tables-restore=/usr/sbin/ip6tables-restore
  --with-ebtables=/usr/sbin/ebtables
  --with-ebtables-restore=/usr/sbin/ebtables-restore
  --with-ipset=/usr/sbin/ipset
  PYTHON="%{__python3} %{py3_shbang_opts}"
)
%configure "${OPTS[@]}"
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
desktop-file-install --delete-original \
  --dir %{buildroot}%{_sysconfdir}/xdg/autostart \
  %{buildroot}%{_sysconfdir}/xdg/autostart/firewall-applet.desktop
desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/firewall-config.desktop
install -d -m 755 %{buildroot}%{_prefix}/lib/firewalld/zones/
install -c -m 644 %{SOURCE1} %{buildroot}%{_prefix}/lib/firewalld/zones/FedoraServer.xml
install -c -m 644 %{SOURCE2} %{buildroot}%{_prefix}/lib/firewalld/zones/FedoraWorkstation.xml
install -m 644 -D %{SOURCE3} %{buildroot}%{_datadir}/polkit-1/rules.d/org.fedoraproject.FirewallD1.desktop.rules.choice
mv %{buildroot}%{_sysconfdir}/firewalld/firewalld.conf \
    %{buildroot}%{_sysconfdir}/firewalld/firewalld-standard.conf
cp -a %{buildroot}%{_sysconfdir}/firewalld/firewalld-standard.conf \
    %{buildroot}%{_sysconfdir}/firewalld/firewalld-server.conf
sed -i 's|^DefaultZone=.*|DefaultZone=FedoraServer|g' \
    %{buildroot}%{_sysconfdir}/firewalld/firewalld-server.conf
cp -a %{buildroot}%{_sysconfdir}/firewalld/firewalld-standard.conf \
    %{buildroot}%{_sysconfdir}/firewalld/firewalld-workstation.conf
sed -i 's|^DefaultZone=.*|DefaultZone=FedoraWorkstation|g' \
    %{buildroot}%{_sysconfdir}/firewalld/firewalld-workstation.conf
sed -i 's|^IPv6_rpfilter=.*|IPv6_rpfilter=loose|g' \
    %{buildroot}%{_sysconfdir}/firewalld/firewalld-workstation.conf
rm -f %{buildroot}%{_datadir}/polkit-1/actions/org.fedoraproject.FirewallD1.policy
rm -f %{buildroot}%{_datadir}/man/man1/firewallctl.1
rm -f %{buildroot}%{_prefix}/lib/firewalld/services/kodi-*.xml
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/firewalld/gtk3_*
%if 0%{?flatpak}
mkdir -p %{buildroot}%{_rpmmacrodir}
mv %{buildroot}%{_prefix}/lib/rpm/macros.d/* %{buildroot}%{_rpmmacrodir}
%endif
%find_lang %{name} --all-name
%oreon_autofiles python3-firewall usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles firewalld-filesystem usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles firewalld-test usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles firewall-applet usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles firewall-config usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post firewalld.service
%preun

%systemd_preun firewalld.service
%postun

%systemd_postun_with_restart firewalld.service
%posttrans

. /etc/os-release || :
if [ ! -e %{_sysconfdir}/firewalld/firewalld.conf ]; then
    case "$VARIANT_ID" in
        server)
            ln -sf firewalld-server.conf %{_sysconfdir}/firewalld/firewalld.conf || :
            ;;
        workstation | silverblue | kde | kinoite)
            ln -sf firewalld-workstation.conf %{_sysconfdir}/firewalld/firewalld.conf || :
            ;;
        *)
            ln -sf firewalld-standard.conf %{_sysconfdir}/firewalld/firewalld.conf
            ;;
    esac
fi
if [ ! -e %{_datadir}/polkit-1/actions/org.fedoraproject.FirewallD1.policy ]; then
    case "$VARIANT_ID" in
        workstation | silverblue | kde | kinoite)
            ln -sf org.fedoraproject.FirewallD1.desktop.policy.choice %{_datadir}/polkit-1/actions/org.fedoraproject.FirewallD1.policy || :
            ln -sf org.fedoraproject.FirewallD1.desktop.rules.choice  %{_datadir}/polkit-1/rules.d/org.fedoraproject.FirewallD1.rules ||:
            ;;
        *)
            ln -sf org.fedoraproject.FirewallD1.server.policy.choice %{_datadir}/polkit-1/actions/org.fedoraproject.FirewallD1.policy || :
            rm -f %{_datadir}/polkit-1/rules.d/org.fedoraproject.FirewallD1.rules || :
    esac
fi
%files -f %{oreon_filedir}/main.list
%files -n python3-firewall -f %{oreon_filedir}/python3-firewall.list
%files -n firewalld-filesystem -f %{oreon_filedir}/firewalld-filesystem.list
%files -n firewalld-test -f %{oreon_filedir}/firewalld-test.list
%files -n firewall-applet -f %{oreon_filedir}/firewall-applet.list
%files -n firewall-config -f %{oreon_filedir}/firewall-config.list

%changelog

%autochangelog
