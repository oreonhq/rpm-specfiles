%global source1_hash 6dcda75745574faaa0a5457707e653e536995aa229bd8630f4dc557ad87f85fe
%global source0_hash 6469ff89e26d44565292c968df595b3a68f353707255ba48725c1bae2a67f3be
%global stable_kf6 stable
ExcludeArch: %{ix86}
Name:    plasma-nm
Summary:        Plasma for managing network connections
Version:        6.7.5
Release:        1%{?dist}
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig
%ifarch %{qt6_qtwebengine_arches}
%bcond openconnect 1
%else
%bcond openconnect 0
%endif
%if %{with openconnect}
%else
Obsoletes:      %{name}-openconnect < %{version}-%{release}
%endif
Requires:       NetworkManager >= 1.0.0
Requires:       kf6-prison
Requires:       kf6-kirigami2
Requires:       qt6qml(org.kde.kirigamiaddons.formcard)
Requires:       kf6-kquickcharts
Obsoletes:      kde-plasma-networkmanagement < 1:0.9.1.0
Obsoletes:      kde-plasma-networkmanagement-libs < 1:0.9.1.0
Obsoletes:      kde-plasma-nm < 5.0.0-1
Provides:       kde-plasma-nm = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6ModemManagerQt)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Prison)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(QCoro6)
BuildRequires:  cmake(Qca-qt6)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-kirigami-addons
BuildRequires:  kf6-rpm-macros
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(ModemManager)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(mobile-broadband-provider-info)
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
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

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 \
  %{!?with_openconnect:-DBUILD_OPENCONNECT=OFF} \
  %{nil}
%cmake_build
%install
%cmake_install
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n plasma-nm-openvpn -f %{oreon_filedir}/plasma-nm-openvpn.list
%files -n plasma-nm-openswan -f %{oreon_filedir}/plasma-nm-openswan.list
%files -n plasma-nm-strongswan -f %{oreon_filedir}/plasma-nm-strongswan.list
%files -n plasma-nm-l2tp -f %{oreon_filedir}/plasma-nm-l2tp.list
%files -n plasma-nm-pptp -f %{oreon_filedir}/plasma-nm-pptp.list
%files -n plasma-nm-sstp -f %{oreon_filedir}/plasma-nm-sstp.list
%files -n plasma-nm-fortisslvpn -f %{oreon_filedir}/plasma-nm-fortisslvpn.list

%changelog

%autochangelog
