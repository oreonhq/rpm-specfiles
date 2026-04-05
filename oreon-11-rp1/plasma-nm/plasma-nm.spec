
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    plasma-nm
Summary: Plasma for managing network connections
Version: 6.6.2
Release:	2%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig


%ifarch %{qt6_qtwebengine_arches}
%bcond openconnect 1
%else
%bcond openconnect 0
%endif

## upstream patches


BuildRequires:  gettext

BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  qt6-qtbase-devel
BuildRequires:  cmake(QCoro6)
BuildRequires:  cmake(Qca-qt6)

BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(KF6ModemManagerQt)
BuildRequires:  cmake(KF6Svg)

# Plasma
BuildRequires:  cmake(Plasma)

# Runtime check
BuildRequires:  cmake(KF6Prison)
BuildRequires:  cmake(KF6Kirigami2)

BuildRequires:  pkgconfig(ModemManager) >= 1.0.0
BuildRequires:  pkgconfig(libnm) >= 1.0.0
BuildRequires:  pkgconfig(mobile-broadband-provider-info)

%if %{with openconnect}
BuildRequires:  pkgconfig(openconnect) >= 4.00
BuildRequires:  cmake(Qt6WebEngineWidgets)
%else
Obsoletes:      %{name}-openconnect < %{version}-%{release}
%endif

Requires:       NetworkManager >= 1.0.0
Requires:       kf6-prison
Requires:       kf6-kirigami2

Obsoletes:      kde-plasma-networkmanagement < 1:0.9.1.0
Obsoletes:      kde-plasma-networkmanagement-libs < 1:0.9.1.0
Obsoletes:      kde-plasma-nm < 5.0.0-1
Provides:       kde-plasma-nm = %{version}-%{release}

%description
Plasma applet and editor for managing your network connections in KDE 4 using
the default NetworkManager service.


%package        openvpn
Summary:        OpenVPN support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-openvpn
Obsoletes:      kde-plasma-networkmanagement-openvpn < 1:0.9.1.0
Obsoletes:      kde-plasma-nm-openvpn < 5.0.0-1
Provides:       kde-plasma-nm-openvpn = %{version}-%{release}
%description    openvpn
%{summary}.

%if %{with openconnect}
%package        openconnect
Summary:        OpenConnect support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-openconnect
Obsoletes:      kde-plasma-networkmanagement-openconnect < 1:0.9.1.0
Obsoletes:      kde-plasma-nm-openconnect < 5.0.0-1
Provides:       kde-plasma-nm-openconnect = %{version}-%{release}
Provides:       deprecated()
%description    openconnect
%{summary}.
%endif

%package        openswan
Summary:        Openswan support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-openswan
Obsoletes:      kde-plasma-nm-openswan < 5.0.0-1
Provides:       kde-plasma-nm-openswan = %{version}-%{release}
%description    openswan
%{summary}.

%package        strongswan
Summary:        Strongswan support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       strongswan
Obsoletes:      kde-plasma-nm-strongswan < 5.0.0-1
Provides:       kde-plasma-nm-strongswan = %{version}-%{release}
%description    strongswan
%{summary}.

%package        l2tp
Summary:        L2TP support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-l2tp
Obsoletes:      kde-plasma-nm-l2tp < 5.0.0-1
Provides:       kde-plasma-nm-l2tp = %{version}-%{release}
%description    l2tp
%{summary}.

%package        pptp
Summary:        PPTP support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-pptp
Obsoletes:      kde-plasma-networkmanagement-pptp < 1:0.9.1.0
Obsoletes:      kde-plasma-nm-pptp < 5.0.0-1
Provides:       kde-plasma-nm-pptp = %{version}-%{release}
%description    pptp
%{summary}.

%package        sstp
Summary:        SSTP support for %{name}
Requires:       NetworkManager-sstp
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    sstp
%{summary}.

%package        fortisslvpn
Summary:        Fortigate SSL VPN support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-fortisslvpn
%description    fortisslvpn
%{summary}.

%if 0%{?fedora}
%package        vpnc
Summary:        Vpnc support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-vpnc
Obsoletes:      kde-plasma-networkmanagement-vpnc < 1:0.9.1.0
Obsoletes:      kde-plasma-nm-vpnc < 5.0.0-1
Provides:       kde-plasma-nm-vpnc = %{version}-%{release}
%description    vpnc
%{summary}.

%package        ssh
Summary:        SSH suppor for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-ssh
%description    ssh
%{summary}.

%package        iodine
Summary:        Iodine support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       NetworkManager-iodine
%description    iodine
%{summary}.
%endif

%prep
%autosetup -p1


%build
%cmake_kf6 \
  %{!?with_openconnect:-DBUILD_OPENCONNECT=OFF} \
  %{nil}

%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%if ! 0%{?fedora}
rm -f %{buildroot}%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_vpncui.so
rm -f %{buildroot}%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_sshui.so
rm -f %{buildroot}%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_iodineui.so
rm -f %{buildroot}/usr/share/locale/*/LC_MESSAGES/plasmanetworkmanagement_iodineui.mo
rm -f %{buildroot}/usr/share/locale/*/LC_MESSAGES/plasmanetworkmanagement_sshui.mo
rm -f %{buildroot}/usr/share/locale/*/LC_MESSAGES/plasmanetworkmanagement_vpncui.mo 
%endif
%if %{without openconnect}
rm -f %{buildroot}/usr/share/locale/*/LC_MESSAGES/plasmanetworkmanagement_openconnectui.mo
%endif

%find_lang plasma_applet_org.kde.plasma.networkmanagement
%find_lang plasmanetworkmanagement-kded
%find_lang plasmanetworkmanagement-kcm
%find_lang plasmanetworkmanagement-libs
%find_lang plasmanetworkmanagement_openvpnui
%find_lang kcm_cellular_network
%find_lang kcm_mobile_hotspot
%find_lang kcm_mobile_wifi
%find_lang kcm_mobile_wired
%if %{with openconnect}
%find_lang plasmanetworkmanagement_openconnectui
%endif
%find_lang plasmanetworkmanagement_libreswanui
%find_lang plasmanetworkmanagement_strongswanui
%find_lang plasmanetworkmanagement_l2tpui
%find_lang plasmanetworkmanagement_pptpui
%find_lang plasmanetworkmanagement_sstpui
%find_lang plasmanetworkmanagement_fortisslvpnui
%if 0%{?fedora}
%find_lang plasmanetworkmanagement_vpncui
%find_lang plasmanetworkmanagement_sshui
%find_lang plasmanetworkmanagement_iodineui
%endif


%files -f plasma_applet_org.kde.plasma.networkmanagement.lang -f plasmanetworkmanagement-kded.lang -f plasmanetworkmanagement-libs.lang -f plasmanetworkmanagement-kcm.lang -f kcm_cellular_network.lang -f kcm_mobile_wifi.lang -f kcm_mobile_hotspot.lang -f kcm_mobile_wired.lang
%{_libdir}/libplasmanm_internal.so
%{_libdir}/libplasmanm_editor.so
# plasma-nm applet
%{_qt6_qmldir}/org/kde/plasma/networkmanagement/
%{_kf6_qtplugindir}/plasma/applets/org.kde.plasma.networkmanagement.so
%{_datadir}/qlogging-categories6/plasma-nm.categories
# plasma-nm notifications
%{_kf6_datadir}/knotifications6/networkmanagement.notifyrc
# plasma-nm kded
%{_kf6_plugindir}/kded/networkmanagement.so

# kcm
%{_qt6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_networkmanagement.so
%{_qt6_plugindir}/plasma/kcms/systemsettings/kcm_cellular_network.so
%{_qt6_plugindir}/plasma/kcms/systemsettings/kcm_mobile_hotspot.so
%{_qt6_plugindir}/plasma/kcms/systemsettings/kcm_mobile_wifi.so
%{_qt6_plugindir}/plasma/kcms/systemsettings/kcm_mobile_wired.so
%{_datadir}/kcm_networkmanagement/qml/
%{_kf6_datadir}/applications/kcm_networkmanagement.desktop
%{_kf6_datadir}/applications/org.kde.vpnimport.desktop
%{_kf6_datadir}/applications/kcm_cellular_network.desktop
%{_kf6_datadir}/applications/kcm_mobile_hotspot.desktop
%{_kf6_datadir}/applications/kcm_mobile_wifi.desktop
%{_kf6_datadir}/applications/kcm_mobile_wired.desktop


%files openvpn -f plasmanetworkmanagement_openvpnui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_openvpnui.so

%if %{with openconnect}
%files openconnect -f plasmanetworkmanagement_openconnectui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_anyconnect.so
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_globalprotectui.so
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_juniperui.so
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_pulseui.so
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_arrayui.so
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_f5ui.so
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_openconnect_fortinetui.so
%endif

%files openswan -f plasmanetworkmanagement_libreswanui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_libreswanui.so

%files strongswan -f plasmanetworkmanagement_strongswanui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_strongswanui.so

%files l2tp -f plasmanetworkmanagement_l2tpui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_l2tpui.so

%files pptp -f plasmanetworkmanagement_pptpui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_pptpui.so

%files sstp -f plasmanetworkmanagement_sstpui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_sstpui.so

%files fortisslvpn -f plasmanetworkmanagement_fortisslvpnui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_fortisslvpnui.so

%if 0%{?fedora}
%files vpnc -f plasmanetworkmanagement_vpncui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_vpncui.so

%files ssh -f plasmanetworkmanagement_sshui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_sshui.so

%files iodine -f plasmanetworkmanagement_iodineui.lang
%{_kf6_qtplugindir}/plasma/network/vpn/plasmanetworkmanagement_iodineui.so
%endif

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
