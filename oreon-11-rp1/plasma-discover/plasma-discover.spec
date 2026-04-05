%global base_name discover
%global flatpak_version 0.8.0
# enable snap support (or not)
%global snap 1
%global snapd_glib_version 1.66
# enable fwupd support (or not)
%global fwupd 1

Name:    plasma-discover
Summary: KDE and Plasma resources management GUI
Version: 6.6.2
Release:	2%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/discover

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz.sig

## override some defaults, namely to enable offline updates
Source10: discoverrc

## upstream patches

## downstream patches
# Adjust periodic refresh from 1/24hr to 1/12hr
# This ensures that it is checked at least once during the work day.
# It is double the time that Fedora repos are set to in DNF (6h).
Patch200: discover-pk-refresh-timer.patch

## upstreamable patches

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires: appstream-qt-devel >= 1.0.0~
BuildRequires: flatpak-devel >= %{flatpak_version}
BuildRequires: libstemmer-devel
BuildRequires: libyaml-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: gettext
BuildRequires: libxml2-devel
BuildRequires: pkgconfig(libmarkdown)
BuildRequires: cmake(QCoro6)
BuildRequires: cmake(KF6ItemModels)

%if 0%{?fedora}
BuildRequires: rpm-ostree-devel
%endif

%if 0%{?fwupd}
BuildRequires: pkgconfig(fwupd)
%endif

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Purpose)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6Attica)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6IdleTime)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6UserFeedback)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6GuiAddons)

BuildRequires: pkgconfig(packagekitqt6)
BuildRequires: pkgconfig(phonon4qt6)


BuildRequires: pkgconfig(Qt6Concurrent)
BuildRequires: pkgconfig(Qt6DBus) >= 5.10.0
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6QuickWidgets)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Test)
%ifarch %{qt6_qtwebengine_arches}
BuildRequires: pkgconfig(Qt6WebView)
%endif
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Xml)

Requires: kf6-kirigami2
Requires: kf6-kitemmodels
Requires: kf6-purpose
Requires: kf6-qqc2-desktop-style

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

# Enable -packagekit and -flatpak by default
# Fedora Kinoite will explicitely exclude -packagekit and -offline-updates
Recommends: %{name}-packagekit = %{version}-%{release}
Recommends: %{name}-flatpak = %{version}-%{release}

%if 0%{?fedora} > 35
Recommends: fedora-appstream-metadata
%endif

# Enable -offline-updates by default
Recommends: %{name}-offline-updates = %{version}-%{release}

# handle upgrade path
%if ! 0%{?snap}
Obsoletes: plasma-discover-snap < %{version}-%{release}
%endif

%description
KDE and Plasma resources management GUI.

%package libs
Summary: Runtime libraries for %{name}
%description libs
%{summary}.

%package packagekit
Summary: Plasma Discover PackageKit support
Requires: %{name} = %{version}-%{release}
Requires: PackageKit
%description packagekit
%{summary}.

%package notifier
Summary: Plasma Discover Update Notifier
# -notifier replaces plasma-pk-updates for f34+
%if 0%{?fedora} > 33
Obsoletes: plasma-pk-updates < 0.5
%endif
Obsoletes: plasma-discover-updater < 5.6.95
Provides:  plasma-discover-updater = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
%description notifier
%{summary}.

%package flatpak
Summary: Plasma Discover flatpak support
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}
Requires: flatpak >= %{flatpak_version}
Requires: flatpak-libs%{?_isa} >= %{flatpak_version}
Requires: (flatpak-kcm if plasma-systemsettings)
Supplements: (%{name} and flatpak)
%description flatpak
%{summary}.

%if 0%{?snap}
%package snap
Summary: Plasma Discover snap support
BuildRequires: cmake(Snapd) >= %{snapd_glib_version}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}
Requires: snapd-qt%{?_isa} >= %{snapd_glib_version}
Requires: snapd
Supplements: (%{name} and snapd)
%description snap
%{summary}.
%endif

%package offline-updates
Summary: Plasma Discover Offline updates enablement
Requires: %{name} = %{version}-%{release}
%description offline-updates
Enable Offline Updates feature by default
in %{name}.

%if 0%{?fedora}
# Only used for Fedora Kinoite
%package rpm-ostree
Summary: Plasma Discover backend for rpm-ostree support
Requires: %{name} = %{version}-%{release}
Supplements: ((%{name} and rpm-ostree) unless dnf)
%description rpm-ostree
Plasma Discover backend for rpm-ostree support in %{name}.
%endif

%package kns
Summary: Plasma Discover KNewStuff support
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}
Supplements: (%{name} and plasma-workspace%{?_isa})
%description kns
%{summary}.


%prep
%autosetup -n %{base_name}-%{version} -p1


%build
%cmake_kf6 \
  -DPACKAGEKIT_AUTOREMOVE:BOOL=ON \
%if 0%{?fedora}
  -DBUILD_RpmOstreeBackend:BOOL=ON
%endif

%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
install -m644 -p -D %{SOURCE10} %{buildroot}%{_kf6_sysconfdir}/xdg/discoverrc

## unpackaged files
%if !0%{?snap}
rm -fv %{buildroot}%{_datadir}/applications/org.kde.discover.snap.desktop
%endif

%find_lang libdiscover
%find_lang kcm_updates
%find_lang plasma-discover --with-html
%find_lang plasma-discover-notifier

cat kcm_updates.lang plasma-discover.lang | sort | uniq -u > discover.lang


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.discover.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.discover.flatpak.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.discover.packagekit.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.discover.desktop


%files -f discover.lang
%{_bindir}/plasma-discover
%{_kf6_metainfodir}/org.kde.discover.appdata.xml
%{_datadir}/applications/org.kde.discover.desktop
%{_datadir}/applications/org.kde.discover.urlhandler.desktop
%{_datadir}/icons/hicolor/*/apps/plasmadiscover.*
%{_datadir}/icons/hicolor/*/apps/flatpak-discover.*
%{_datadir}/icons/hicolor/*/apps/snapdiscover.svg
%{_datadir}/kxmlgui5/plasmadiscover/
%if 0%{?snap}
%{_libexecdir}/discover/
%endif
%{_kf6_datadir}/applications/kcm_updates.desktop

%files notifier -f plasma-discover-notifier.lang
%{_datadir}/knotifications6/discoverabstractnotifier.notifyrc
%{_sysconfdir}/xdg/autostart/org.kde.discover.notifier.desktop
%{_datadir}/applications/org.kde.discover.notifier.desktop
%{_libexecdir}/DiscoverNotifier

%files libs -f libdiscover.lang
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/discover.categories
%dir %{_libdir}/plasma-discover/
%{_libdir}/plasma-discover/libDiscoverNotifiers.so
%{_libdir}/plasma-discover/libDiscoverCommon.so
%dir %{_kf6_qtplugindir}/discover
%dir %{_kf6_qtplugindir}/discover-notifier/
%if 0%{?fwupd}
%{_kf6_qtplugindir}/discover/fwupd-backend.so
%endif
%dir %{_datadir}/libdiscover
%dir %{_datadir}/libdiscover/categories
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_updates.so

%files packagekit
%{_kf6_metainfodir}/org.kde.discover.packagekit.appdata.xml
%{_kf6_qtplugindir}/discover-notifier/DiscoverPackageKitNotifier.so
%{_kf6_qtplugindir}/discover/packagekit-backend.so
%{_datadir}/libdiscover/categories/packagekit-backend-categories.xml

%files flatpak
%{_kf6_metainfodir}/org.kde.discover.flatpak.appdata.xml
%{_kf6_qtplugindir}/discover-notifier/FlatpakNotifier.so
%{_kf6_qtplugindir}/discover/flatpak-backend.so
%{_datadir}/libdiscover/categories/flatpak-backend-categories.xml
%{_datadir}/applications/org.kde.discover.flatpak.desktop

%if 0%{?snap}
%files snap
%dir %{_libexecdir}/discover/
%{_libexecdir}/discover/SnapMacaroonDialog
%{_kf6_libexecdir}/kauth/libsnap_helper
%{_kf6_metainfodir}/org.kde.discover.snap.appdata.xml
%{_kf6_qtplugindir}/discover/snap-backend.so
%{_datadir}/dbus-1/system.d/org.kde.discover.libsnapclient.conf
%{_datadir}/dbus-1/system-services/org.kde.discover.libsnapclient.service
%{_datadir}/polkit-1/actions/org.kde.discover.libsnapclient.policy
%{_kf6_datadir}/applications/org.kde.discover.snap.desktop
%endif

%files offline-updates
%{_kf6_sysconfdir}/xdg/discoverrc

%if 0%{?fedora}
%files rpm-ostree
%{_datadir}/libdiscover/categories/rpm-ostree-backend-categories.xml
%{_kf6_qtplugindir}/discover/rpm-ostree-backend.so
%{_kf6_qtplugindir}/discover-notifier/rpm-ostree-notifier.so
%endif

%files kns
%{_kf6_qtplugindir}/discover/kns-backend.so

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
