%global base_name kdeconnect-kde

Name:    kde-connect
Version: 25.12.3
Release:	2%{?dist}
License: GPL-2.0-or-later
Summary: KDE Connect client for communication with smartphones

Url:     https://community.kde.org/KDEConnect

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{base_name}-%{version}.tar.xz

# Doesn't build on i686 as-of 25.03.80
ExcludeArch: %{ix86}

## upstream patches

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  firewalld-filesystem
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(openssl)

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6ModemManagerQt)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6People)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6ItemModels)

BuildRequires:  cmake(Qt6Bluetooth)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Core5Compat)
# wayland/clipboard deps
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  wayland-protocols-devel
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  cmake(Qca-qt6)

BuildRequires:  cmake(KF6PulseAudioQt)

BuildRequires:  libXtst-devel
BuildRequires:  pkgconfig(libfakekey)

Obsoletes: kde-connect-kde4-ioslave < %{version}-%{release}
Obsoletes: kde-connect-kde4-libs < %{version}-%{release}

# upstream name
Provides:       kdeconnect-kde = %{version}-%{release}

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kdeconnectd = %{version}-%{release}

Requires:       fuse-sshfs
Requires:       qca-qt6-ossl%{?_isa}
# /usr/bin/plasmawindowed (make optional at least until this is split out for bug #1286431)
#Recommends:     plasma-workspace
# /usr/bin/kcmshell5
Requires:       kde-cli-tools
# /usr/bin/kdeconnect-app
Requires:       kf6-kirigami2%{?_isa}
Requires:       kf6-kirigami2-addons
# kde-connect app requires the qml definition to launch
Requires:       qt6qml(org.kde.desktop)
# Required for contact synchronization with kde connect
Recommends:     kf6-kpeople

%description
KDE Connect adds communication between KDE and your smartphone.

Currently, you can pair with your Android devices over Wifi using the
KDE Connect 1.0 app from Albert Vaka which you can obtain via Google Play, F-Droid
or the project website.

%package -n kdeconnectd
Summary: KDE Connect service
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description -n kdeconnectd
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
# I think we may want to drop this, forces kdeconnectd to pull in main pkg indirectly -- rex
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package nautilus
Summary: KDEConnect extention for nautilus
Requires: kdeconnectd = %{version}-%{release}
Requires: nautilus-python
Supplements: (kdeconnectd and nautilus)
%description nautilus
%{summary}.


%prep
%autosetup -n %{base_name}-%{version} -p1


%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6

%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html

# https://bugzilla.redhat.com/show_bug.cgi?id=1296523
desktop-file-edit --remove-key=OnlyShowIn %{buildroot}%{_sysconfdir}/xdg/autostart/org.kde.kdeconnect.daemon.desktop
	
## unpackaged files
# this is a static version of the shared lib dropped in the beta
rm -fv %{buildroot}%{_kf6_libdir}/libkdeconnectinterfaces.a

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kdeconnect.metainfo.xml
for i in %{buildroot}%{_kf6_datadir}/applications/org.kde.kdeconnect*.desktop ; do
desktop-file-validate $i
done


%files -f %{name}.lang
%dir %{_kf6_datadir}/kdeconnect/
%license LICENSES/*
%{_datadir}/Thunar/
%{_datadir}/contractor/
%{_datadir}/deepin/
%{_datadir}/zsh/
%{_sysconfdir}/ufw/applications.d/kdeconnect
%{_kf6_datadir}/applications/org.kde.kdeconnect*.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/kdeconnect*
%{_kf6_datadir}/icons/hicolor/*/status/*
%{_kf6_bindir}/kdeconnect-*
%{_kf6_datadir}/kdeconnect/kdeconnect_*.qml
%{_kf6_datadir}/knotifications6/*
%{_kf6_datadir}/plasma/plasmoids/org.kde.kdeconnect/
%{_kf6_datadir}/qlogging-categories6/kdeconnect*
%{_kf6_metainfodir}/org.kde.kdeconnect.metainfo.xml
%{_kf6_plugindir}/kfileitemaction/kdeconnectfileitemaction.so
%{_kf6_plugindir}/kio/kdeconnect.so
%{_qt6_archdatadir}/qml/org/kde/kdeconnect/

%files -n kdeconnectd
%{_sysconfdir}/xdg/autostart/org.kde.kdeconnect.daemon.desktop
%{_datadir}/applications/org.kde.kdeconnect.daemon.desktop
%{_kf6_bindir}/kdeconnectd
%{_datadir}/dbus-1/services/org.kde.kdeconnect.service

%files libs
%{_kf6_libdir}/libkdeconnectcore.so.*
%{_qt6_plugindir}/kdeconnect/

%files nautilus
%{_datadir}/nautilus-python/extensions/kdeconnect-share.py*


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
