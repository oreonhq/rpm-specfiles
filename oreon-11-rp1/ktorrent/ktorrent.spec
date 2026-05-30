%global source0_hash none

%global stable_kf6 stable


# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")


# 
ExcludeArch: %{ix86}

Name:    ktorrent
Version: 26.04.1
Release: 1%{?dist}
Summary: A BitTorrent program

License: GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://www.kde.org/applications/internet/ktorrent/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

## upstreamable patches

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6Test)
%ifarch %{qt6_qtwebengine_arches}
BuildRequires: cmake(Qt6WebEngineWidgets)
%endif

BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6Plotting)
BuildRequires: cmake(KF6Syndication)
BuildRequires: cmake(KF6DNSSD)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Archive)

BuildRequires: boost-devel
%global majmin %(echo %{version} | cut -d. -f1,2)
BuildRequires: cmake(KTorrent6) >= %{majmin}
BuildRequires: cmake(Phonon4Qt6)
BuildRequires: pkgconfig(libmaxminddb)
BuildRequires: pkgconfig(taglib)

## TODO: Re-enable with Plasma 6 beta or later
# %if %%{undefined flatpak}
# BuildRequires: cmake(LibKWorkspace)
# %endif

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
KTorrent is a BitTorrent program for KDE. Its main features are native KDE
integration, download of torrent files, upload speed capping, internet
searching using various search engines, UDP Trackers and UPnP support.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description libs
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{name}-%{version}%{?pre} -p1


%build
%cmake_kf6 \
  -DBUILD_WITH_GEOIP:BOOL=ON

%cmake_build


%install
%cmake_install

# ensure this exists (sometimes not, e.g. when qtwebengine support isn't available)
mkdir -p %{buildroot}%{_kf6_datadir}/ktorrent

%find_lang %{name} --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.ktorrent.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.ktorrent.desktop


%files -f %{name}.lang
%doc ChangeLog
%license LICENSES/*
%{_kf6_bindir}/ktorrent
%{_kf6_bindir}/ktmagnetdownloader
%{_kf6_bindir}/ktupnptest
%{_kf6_metainfodir}/org.kde.ktorrent.appdata.xml
%{_kf6_datadir}/applications/org.kde.ktorrent.desktop
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/ktorrent/
%{_kf6_datadir}/knotifications6/ktorrent.notifyrc
%{_kf6_datadir}/kxmlgui5/ktorrent/
%{_qt6_plugindir}/ktorrent_plugins/*.so

%files libs
%{_kf6_libdir}/libktcore.so.*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.04.1-1
- Import
