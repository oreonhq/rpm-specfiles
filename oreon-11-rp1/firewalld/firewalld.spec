# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 99d7468c22f6cafd8c72aa53173a632f2ca29cb19aec913e8ed45b6102af322d
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary: A firewall daemon with D-Bus interface providing a dynamic firewall
Name: firewalld
Version: 2.5.2
Release: %{autorelease}
URL:     http://www.firewalld.org
License: GPL-2.0-or-later
Source0: https://github.com/firewalld/firewalld/releases/download/v%{version}/firewalld-%{version}.tar.bz2
Source1: OreonServer.xml
Source2: OreonWorkstation.xml
Source3: org.fedoraproject.FirewallD1.desktop.rules.choice
BuildArch: noarch
BuildRequires: oreon-rpm-macros
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: intltool
BuildRequires: glib2
BuildRequires: glib2-devel
BuildRequires: systemd-units
BuildRequires: docbook-style-xsl
BuildRequires: libxslt
BuildRequires: iptables
BuildRequires: ebtables
BuildRequires: ipset
BuildRequires: python3-devel
BuildRequires: make
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
%if (0%{?fedora} >= 39 || 0%{?rhel} >= 10 || 0%{?oreon})
Requires: python3-pyqt6-base
%else
Requires: python3-qt5-base
%endif
Requires: python3-gobject
Requires: libnotify
Requires: NetworkManager-libnm

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
Recommends: polkit
%endif

%description -n firewall-config
The firewall configuration application provides an configuration interface for 
firewalld.

%prep
%oreon_sha256
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
install -c -m 644 %{SOURCE1} %{buildroot}%{_prefix}/lib/firewalld/zones/OreonServer.xml
install -c -m 644 %{SOURCE2} %{buildroot}%{_prefix}/lib/firewalld/zones/OreonWorkstation.xml
install -m 644 -D %{SOURCE3} %{buildroot}%{_datadir}/polkit-1/rules.d/org.fedoraproject.FirewallD1.desktop.rules.choice

mv %{buildroot}%{_sysconfdir}/firewalld/firewalld.conf \
    %{buildroot}%{_sysconfdir}/firewalld/firewalld-standard.conf

cp -a %{buildroot}%{_sysconfdir}/firewalld/firewalld-standard.conf \
    %{buildroot}%{_sysconfdir}/firewalld/firewalld-server.conf
sed -i 's|^DefaultZone=.*|DefaultZone=OreonServer|g' \
    %{buildroot}%{_sysconfdir}/firewalld/firewalld-server.conf

cp -a %{buildroot}%{_sysconfdir}/firewalld/firewalld-standard.conf \
    %{buildroot}%{_sysconfdir}/firewalld/firewalld-workstation.conf
sed -i 's|^DefaultZone=.*|DefaultZone=OreonWorkstation|g' \
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

%files -f %{name}.lang
%doc COPYING README.md
%{_sbindir}/firewalld
%{_bindir}/firewall-cmd
%{_bindir}/firewall-offline-cmd
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/firewall-cmd
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_firewalld
%{_datadir}/polkit-1/rules.d/org.fedoraproject.FirewallD1.desktop.rules.choice
%ghost %config(missingok,noreplace) %{_datadir}/polkit-1/rules.d/org.fedoraproject.FirewallD1.rules
%{_prefix}/lib/firewalld/icmptypes/*.xml
%{_prefix}/lib/firewalld/ipsets/README.md
%{_prefix}/lib/firewalld/policies/*.xml
%{_prefix}/lib/firewalld/services/*.xml
%{_prefix}/lib/firewalld/zones/*.xml
%{_prefix}/lib/firewalld/helpers/*.xml
%{_prefix}/lib/firewalld/xmlschema/check.sh
%{_prefix}/lib/firewalld/xmlschema/*.xsd
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld
%ghost %config(noreplace) %{_sysconfdir}/firewalld/firewalld.conf
%config(noreplace) %{_sysconfdir}/firewalld/firewalld-standard.conf
%config(noreplace) %{_sysconfdir}/firewalld/firewalld-server.conf
%config(noreplace) %{_sysconfdir}/firewalld/firewalld-workstation.conf
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld/helpers
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld/icmptypes
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld/ipsets
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld/policies
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld/services
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld/zones
%defattr(0644,root,root)
%config(noreplace) %{_sysconfdir}/sysconfig/firewalld
%{_unitdir}/firewalld.service
%config(noreplace) %{_datadir}/dbus-1/system.d/FirewallD.conf
%{_datadir}/polkit-1/actions/org.fedoraproject.FirewallD1.desktop.policy.choice
%{_datadir}/polkit-1/actions/org.fedoraproject.FirewallD1.server.policy.choice
%ghost %{_datadir}/polkit-1/actions/org.fedoraproject.FirewallD1.policy
%{_mandir}/man1/firewall*cmd*.1*
%{_mandir}/man1/firewalld*.1*
%{_mandir}/man5/firewall*.5*
%{_sysconfdir}/modprobe.d/firewalld-sysctls.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/firewalld

%files -n python3-firewall
%attr(0755,root,root) %dir %{python3_sitelib}/firewall
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/__pycache__
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/config
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/config/__pycache__
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/core
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/core/__pycache__
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/core/io
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/core/io/__pycache__
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/server
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/server/__pycache__
%{python3_sitelib}/firewall/__pycache__/*.py*
%{python3_sitelib}/firewall/*.py*
%{python3_sitelib}/firewall/config/*.py*
%{python3_sitelib}/firewall/config/__pycache__/*.py*
%{python3_sitelib}/firewall/core/*.py*
%{python3_sitelib}/firewall/core/__pycache__/*.py*
%{python3_sitelib}/firewall/core/io/*.py*
%{python3_sitelib}/firewall/core/io/__pycache__/*.py*
%{python3_sitelib}/firewall/server/*.py*
%{python3_sitelib}/firewall/server/__pycache__/*.py*

%files -n firewalld-filesystem
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/helpers
%dir %{_prefix}/lib/firewalld/icmptypes
%dir %{_prefix}/lib/firewalld/ipsets
%dir %{_prefix}/lib/firewalld/policies
%dir %{_prefix}/lib/firewalld/services
%dir %{_prefix}/lib/firewalld/zones
%dir %{_prefix}/lib/firewalld/xmlschema
%dir %{_datadir}/firewalld
%{_rpmmacrodir}/macros.firewalld

%files -n firewalld-test
%dir %{_datadir}/firewalld/testsuite
%{_datadir}/firewalld/testsuite/README.md
%{_datadir}/firewalld/testsuite/testsuite
%dir %{_datadir}/firewalld/testsuite/integration
%{_datadir}/firewalld/testsuite/integration/testsuite
%dir %{_datadir}/firewalld/testsuite/python
%{_datadir}/firewalld/testsuite/python/firewalld_config.py
%{_datadir}/firewalld/testsuite/python/firewalld_direct.py
%{_datadir}/firewalld/testsuite/python/firewalld_rich.py
%{_datadir}/firewalld/testsuite/python/firewalld_misc.py

%files -n firewall-applet
%{_bindir}/firewall-applet
%defattr(0644,root,root)
%config(noreplace) %{_sysconfdir}/xdg/autostart/firewall-applet.desktop
%dir %{_sysconfdir}/firewall
%config(noreplace) %{_sysconfdir}/firewall/applet.conf
%{_datadir}/icons/hicolor/*/apps/firewall-applet*.*
%{_mandir}/man1/firewall-applet*.1*

%files -n firewall-config
%{_bindir}/firewall-config
%defattr(0644,root,root)
%{_datadir}/firewalld/firewall-config.glade
%attr(0755,root,root) %dir %{_datadir}/firewalld/__pycache__
%pycached %{_datadir}/firewalld/gtk3_chooserbutton.py
%pycached %{_datadir}/firewalld/gtk3_niceexpander.py
%{_datadir}/applications/firewall-config.desktop
%{_datadir}/metainfo/org.firewalld.firewall-config.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/firewall-config*.*
%{_datadir}/glib-2.0/schemas/org.fedoraproject.FirewallConfig.gschema.xml
%{_mandir}/man1/firewall-config*.1*

%changelog
%autochangelog
