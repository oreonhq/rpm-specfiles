%global source0_hash d7da661711c9bc565cc4c14713e3ea5916dca245fddfa00fa0441763985b1bae

%undefine __cmake_in_source_build
%bcond_without tests
# git source
# https://invent.kde.org/network/smb4k/
# bug tracker
# https://bugs.kde.org/buglist.cgi?product=Smb4k

# add -Wl,--as-needed if not exist
%global optflags %(echo %{optflags} -Wl,--as-needed | sed "/-Wl,--as-needed/!s/$/ -Wl,--as-needed/")
%global _kf5_iconsdir %{_datadir}/icons

Name:       smb4k
Version:    4.0.0
Release:    3%{?dist}
Summary:    The SMB/CIFS Share Browser for KDE

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:    GPL-2.0-or-later
URL:        https://smb4k.sourceforge.net/
Source0:    https://downloads.sourceforge.net/smb4k/%{name}-%{version}.tar.xz

BuildRequires:  cmake3 >= 2.6.0
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KDSoap-qt6)
BuildRequires:  cmake(KDSoapWSDiscoveryClient)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DNSSD)
BuildRequires:  cmake(KF6Kirigami)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  pkgconfig(smbclient)

Requires:   kf6-kirigami
Requires:   samba-client
Requires:   cifs-utils

%{?_qt6_version:Requires: qt6-qtbase%{?_isa} >= %{_qt6_version}}

%description
Smb4K is an SMB/CIFS share browser for KDE. It uses the Samba software suite to
access the SMB/CIFS shares of the local network neighborhood. Its purpose is to
provide a program that's easy to use and has as many features as possible.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%{cmake_kf6} -Wno-dev -DSMB4K_WITH_WS_DISCOVERY=ON

%cmake_build

%install
%cmake_install

# Already have Categories=Qt;KDE;Utility;
# add-category Network, because is Network application, search and map SMB/CIFS shares of LAN.
desktop-file-install \
    --add-category Network \
    --delete-original \
    %{buildroot}%{_kf6_datadir}/applications/org.kde.smb4k.desktop

#workaround for bug https://bugzilla.redhat.com/show_bug.cgi?id=1584944
sed -i  %{buildroot}/%{_kf6_metainfodir}/*.appdata.xml -e 's/type="stock"//'

appstream-util validate-relax --nonet %{buildroot}/%{_kf6_metainfodir}/*.appdata.xml

# please look into kdenlive.spec to add --with-html on epel7
%find_lang %{name} --with-html --all-name

%check
%if %{with tests}
%ctest
%endif

%files -f %{name}.lang
%doc AUTHORS BUGS ChangeLog README.md
%license LICENSES/*
%{_kf6_bindir}/%{name}*
%{_kf6_libdir}/libsmb4kcore.so
%{_kf6_libdir}/libsmb4kdialogs.so
%{_kf6_datadir}/dbus-1/system-services/org.kde.%{name}.mounthelper.service
%{_kf6_datadir}/dbus-1/system.d/org.kde.%{name}.mounthelper.conf
%{_kf6_datadir}/polkit-1/actions/org.kde.%{name}.mounthelper.policy
%{_qt6_plugindir}/*.so
%{_kf6_libexecdir}/kauth/mounthelper
%{_kf6_datadir}/applications/org.kde.smb4k.desktop
%{_kf6_datadir}/plasma/plasmoids/org.kde.smb4kqml/
%{_kf6_datadir}/config.kcfg/%{name}.kcfg
%{_kf6_datadir}/knotifications6/%{name}.notifyrc
%{_kf6_datadir}/icons/*/*/*/*
%{_kf6_metainfodir}/*.appdata.xml
%{_kf6_qmldir}/org/kde/smb4k/

%changelog
%autochangelog
