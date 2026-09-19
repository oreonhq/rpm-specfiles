%global source0_hash 8f383beada857b522a59b9259ae1f1f83554c5d25d3c39a39fb6f172ec0f889d

## experimental ninja support
#global ninja 1
## FIXME: many tests require GLX, which doesn't appear to work as-is under koji
#global tests 1

Name:    konqueror
Version: 25.12.3
Release: 1%{?dist}
Summary: KDE File Manager and Browser

# Automatically converted from old format: GPLv2+ and LGPLv2+ and GFDL - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-GFDL
URL:     https://apps.kde.org/konqueror/
Source:  https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

## upstream patches

## upstreamable patches

## Fedora specific patches

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules >= 5.101
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: qt6-qtbase-private-devel

BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(PlasmaActivities)
# libkonq
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(KF6Bookmarks)
BuildRequires: pkgconfig(zlib)
# webenginepart
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6Notifications)
# plugins
BuildRequires: cmake(Qt6TextToSpeech)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Su)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6XmlGui)
# sidebar
BuildRequires: cmake(KF6JobWidgets)

%if 0%{?ninja}
BuildRequires:  ninja-build
%else
BuildRequires:  make
%endif

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif

Requires:      kwebenginepart%{?_isa} = %{version}-%{release}
Requires:      %{name}-libs%{?_isa} = %{version}-%{release} 
Requires:      hicolor-icon-theme
Requires:      keditbookmarks

%description
Konqueror allows you to manage your files and browse the web in a
unified interface.

%package devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
%description   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package libs
Summary:       Runtime libraries for %{name}
Requires:      %{name} = %{version}-%{release}
%description libs
%{summary}.

%package -n kwebenginepart
Summary:  A KPart based on QtWebEngine
%description -n kwebenginepart
KWebEnginePart is a web browser component for KDE (KPart)
based on (Qt)WebEngine. You can use it for example for
browsing the web in Konqueror.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6 \
  -DQT_MAJOR_VERSION=6 \
  -Wno-dev \
  %{?ninja:-G Ninja} \
  %{?tests:-DBUILD_TESTING:BOOL=ON}

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.konqueror.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/kfmclient.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/kfmclient_html.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/kfmclient_war.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/konqbrowser.desktop
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
## cant use %%ninja_test here for some reason, doesn't inherit env vars from xvfb or dbus -- rex
xvfb-run -a \
%if 0%{?ninja}
ninja test -v -C %{_target_platform} ||:
%else
make test -C %{_target_platform} ARGS="--output-on-failure --timeout 300" ||:
%endif
%endif

%files -f %{name}.lang
%license LICENSES/*
%doc AUTHORS ChangeLog
%{_kf6_datadir}/qlogging-categories6/*
%{_kf6_bindir}/fsview
%{_kf6_bindir}/kcreatewebarchive
%{_kf6_bindir}/kfmclient
%{_kf6_bindir}/konqueror
%{_kf6_datadir}/akregator/pics/feed.png
%{_kf6_metainfodir}/org.kde.konqueror.appdata.xml
%{_kf6_datadir}/applications/*.desktop
%{_kf6_datadir}/config.kcfg/*.kcfg
%{_kf6_datadir}/dbus-1/interfaces/*.xml
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/kcmcss/
%{_kf6_datadir}/kcontrol/
%{_kf6_datadir}/kf6/kbookmark/
%{_kf6_datadir}/kio_bookmarks/
%{_kf6_datadir}/konqueror/
%{_kf6_sysconfdir}/xdg/autostart/konqy_preload.desktop
%{_kf6_sysconfdir}/xdg/translaterc
%{_kf6_sysconfdir}/xdg/konqs*
%{_kf6_sysconfdir}/xdg/konqautofiltersrc
%{_kf6_sysconfdir}/xdg/useragenttemplatesrc
%{_kf6_datadir}/konqsidebartng/

%files libs
%{_kf6_libdir}/libKF6Konq.so.{7,*.*}
%{_kf6_libdir}/libKF6KonqSettings.so.{7,*.*}
%{_kf6_libdir}/libKF6KonqSettings.so.{5,*.*}
%{_kf6_libdir}/libkonqsidebarplugin.so.{6,*.*}
%{_kf6_libdir}/libkonquerorprivate.so.{5,*.*}
%{_kf6_qtplugindir}/*.so
%{_kf6_qtplugindir}/konqueror_kcms/
%{_kf6_qtplugindir}/dolphinpart/kpartplugins/dirfilterplugin.so
%{_kf6_qtplugindir}/dolphinpart/kpartplugins/kimgallery.so
%{_kf6_qtplugindir}/dolphinpart/kpartplugins/konq_shellcmdplugin.so
%{_kf6_qtplugindir}/konqueror/kpartplugins/
%{_kf6_qtplugindir}/konqueror/sidebar/
%{_kf6_qtplugindir}/webenginepart/kpartplugins/*
%{_kf6_plugindir}/kfileitemaction/akregatorplugin.so
%{_kf6_plugindir}/kio/bookmarks.so
%dir %{_kf6_plugindir}/parts/
%{_kf6_plugindir}/parts/fsviewpart.so
%{_kf6_plugindir}/parts/konq_sidebar.so
%{_kf6_plugindir}/thumbcreator/webarchivethumbnail.so

%files devel
#{_includedir}/konqsidebarplugin.h
%{_kf6_includedir}/konq*.h
%{_kf6_includedir}/libkonq_export.h
%{_kf6_libdir}/cmake/KF6Konq/
%{_kf6_libdir}/libKF6Konq.so
%{_kf6_libdir}/libkonqsidebarplugin.so
%{_kf6_includedir}/libkonqsettings_export.h
%{_kf6_includedir}/selectorinterface.h
%{_kf6_libdir}/libKF6KonqSettings.so

%files -n kwebenginepart
%{_kf6_datadir}/webenginepart/
%{_kf6_datadir}/kconf_update/webengine*
%{_kf6_libdir}/libkwebenginepart.so
%{_kf6_plugindir}/parts/webenginepart.so

%changelog
%autochangelog
