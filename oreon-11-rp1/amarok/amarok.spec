%global source0_hash none

# FTBFS with GCC 16 when LTO is enabled
# https://bugzilla.redhat.com/show_bug.cgi?id=2432234
%if 0%{?fedora} >= 44 || 0%{?rhel} >= 11
%define _lto_cflags %{nil}
%endif

%global __provides_exclude_from ^%{_kf6_qmldir}/org/kde/amarok/.*\.so$

Name:    amarok
Summary: Media player
Version: 3.3.2
Release: 3%{?dist}

# KDE e.V. may determine that future GPL versions are accepted
License: GPL-2.0-only OR GPL-3.0-only
Url:     https://amarok.kde.org/
%if 0%{?commitdate}
Source0: https://invent.kde.org/multimedia/amarok/-/archive/%{commit}/amarok-%{commit}.tar.bz2
%else
Source0: https://download.kde.org/%{stable_kf6}/amarok/%{version}/amarok-%{version}.tar.xz
%endif

# partially revert https://invent.kde.org/multimedia/amarok/-/commit/c095ebf8780b693605ab23efa4eae6f4dd18fc5e
# it causes amarok to crash on launch for some reason
Patch1:  revert.patch

# Version 1.2.0 is a new fork which just bumps the version for Qt6 and includes
# one patch.  Fedora's 1.1.0 is a snapshot from the old fork which includes Qt6
# and applies the same patch.
Patch2:  liblastfm-version.patch

# Needed because not every distro installs mygpo-qt6 under the same path.
# For instance, Fedora namespaces qt6
Patch10: fix-mygpo-qt6-compilation.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:   %{ix86}

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib
BuildRequires: perl-generators

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6SvgWidgets)
%ifarch %{qt6_qtwebengine_arches}
BuildRequires: cmake(Qt6WebEngineWidgets)
%endif
BuildRequires: cmake(Qt6UiTools)

BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DNSSD)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Package)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6TextEditor)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6ThreadWeaver)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6ColorScheme)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6Kirigami)
# gpodder, lastfm
BuildRequires: cmake(KF6Wallet)

BuildRequires: pkgconfig(gstreamer-audio-1.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires: pkgconfig(taglib) >= 1.12
BuildRequires: pkgconfig(libmariadb)
BuildRequires: pkgconfig(mariadb)
BuildRequires: mariadb-embedded-devel
BuildRequires: ffmpeg-free-devel
BuildRequires: fftw-devel
%if 0%{?fedora}
# dependencies not available in RHEL or EPEL
BuildRequires: liblastfm-qt6-devel >= 1.1.0
BuildRequires: cmake(Mygpo-qt6) >= 1.2.0
BuildRequires: pkgconfig(libmtp) >= 1.0.0
BuildRequires: pkgconfig(libgpod-1.0) >= 0.7.0
# only used together with libgpod
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
# MP3Tunes
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: libgcrypt-devel
BuildRequires: pkgconfig(loudmouth-1.0)
BuildRequires: pkgconfig(glib-2.0) pkgconfig(gobject-2.0)
%endif

Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
Requires:      %{name}-utils = %{version}-%{release}
Requires:      kf6-filesystem
# QML module dependencies
Requires:      kf6-kirigami%{?_isa}

Recommends:    audiocd-kio
Recommends:    kio-extras
%ifarch %{qt6_qtwebengine_arches}
# Wikipedia QML plugin
Recommends:    qt6-qtwebengine%{?_isa}
%endif
%if 0%{?fedora}
Recommends:    ifuse
Recommends:    media-player-info
%endif

%description
Amarok is a multimedia player with:
 - fresh playlist concept, very fast to use, with drag and drop
 - plays all formats supported by the various engines
 - audio effects, like reverb and compressor
 - compatible with the .m3u and .pls formats for playlists
 - nice GUI, integrates into the KDE look, but with a unique touch

%package libs
Summary: Runtime libraries for %{name}
%description libs
%{summary}.

%package utils
Summary: Amarok standalone utilities
Requires: %{name}-libs = %{version}-%{release}
%description utils
%{summary}, including amarokcollectionscanner.

%package doc
Summary: Application handbook, documentation, translations
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
%{summary}.

%prep
%autosetup %{?commitdate:-n %{name}-%{commit}} -p1

sed -i -e 's|/usr/bin/mysqld|%{_libexecdir}/mysqld|' src/importers/amarok/AmarokConfigWidget.cpp

%build
%if 0%{?flatpak}
# find /app-built libmygpo-qt headers
CXXFLAGS="$CXXFLAGS -I%{_includedir}/qt6"
%endif
# force non-use of MYSQLCONFIG, to avoid (potential bogus) stuff from: mysql_config --libmysqld-libs
%{cmake_kf6} \
%if ! 0%{?fedora}
  -DWITH_GPODDER=OFF -DWITH_IPOD=OFF -DWITH_LASTFM=OFF \
%endif
  -DMYSQLCONFIG_EXECUTABLE:BOOL=OFF -DWITH_X11=OFF
%{cmake_build}

%install
%cmake_install

%find_lang amarokcollectionscanner_qt --with-qt --without-mo --all-name
%find_lang amarok --all-name
%find_lang amarok-doc --with-html --without-mo --all-name

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}*.desktop

%files -f amarok.lang
%doc AUTHORS ChangeLog README
%license COPYING
%{_qt6_settingsdir}/amarok_homerc
%{_kf6_bindir}/amarok
%{_kf6_bindir}/amarok_afttagger
%{_kf6_datadir}/amarok/
%{_kf6_datadir}/applications/org.kde.amarok.desktop
%{_kf6_datadir}/applications/org.kde.amarok_containers.desktop
%{_kf6_datadir}/config.kcfg/amarokconfig.kcfg
%{_kf6_datadir}/dbus-1/interfaces/*.xml
%{_kf6_datadir}/dbus-1/services/org.kde.amarok.service
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/kio/servicemenus/amarok_append.desktop
%{_kf6_datadir}/knotifications6/amarok.notifyrc
%{_kf6_datadir}/kpackage/amarok
%{_kf6_datadir}/solid/actions/amarok-play-audiocd.desktop
%{_kf6_metainfodir}/org.kde.amarok.*.xml
%{_kf6_qmldir}/org/kde/amarok
%{_kf6_qtplugindir}/amarok_collection-audiocdcollection.so
%{_kf6_qtplugindir}/amarok_collection-daapcollection.so
%if 0%{?fedora}
%{_kf6_qtplugindir}/amarok_collection-ipodcollection.so
%{_kf6_qtplugindir}/amarok_collection-mtpcollection.so
%endif
%{_kf6_qtplugindir}/amarok_collection-mysqlcollection.so
%{_kf6_qtplugindir}/amarok_collection-playdarcollection.so
%{_kf6_qtplugindir}/amarok_collection-umscollection.so
%{_kf6_qtplugindir}/amarok_importer-amarok.so
%{_kf6_qtplugindir}/amarok_importer-banshee.so
%{_kf6_qtplugindir}/amarok_importer-clementine.so
%{_kf6_qtplugindir}/amarok_importer-fastforward.so
%{_kf6_qtplugindir}/amarok_importer-itunes.so
%{_kf6_qtplugindir}/amarok_importer-rhythmbox.so
%{_kf6_qtplugindir}/amarok_service_*.so
%{_kf6_qtplugindir}/amarok_storage-mysqlestorage.so
%{_kf6_qtplugindir}/amarok_storage-mysqlserverstorage.so
%{_kf6_qtplugindir}/kcm_amarok_service*.so

%files libs
%{_kf6_libdir}/libamarokcore.so.1*
%{_kf6_libdir}/libamaroklib.so.1*
%{_kf6_libdir}/libamarokshared.so.1*
%{_kf6_libdir}/libamarok-sqlcollection.so.1*
%{_kf6_libdir}/libamarok-transcoding.so.1*
%{_kf6_libdir}/libampache_account_login.so
%{_kf6_libdir}/libamarok-sqlcollection.so
%{_kf6_libdir}/libamarok-transcoding.so
%{_kf6_libdir}/libamarokcore.so
%{_kf6_libdir}/libamaroklib.so
%{_kf6_libdir}/libamarokpud.so
%{_kf6_libdir}/libamarokshared.so
%if 0%{?fedora}
%{_kf6_libdir}/libamarok_service_lastfm_config.so
%{_kf6_libdir}/libgpodder_service_config.so
%endif

%files utils -f amarokcollectionscanner_qt.lang
%{_kf6_bindir}/amarokcollectionscanner

%files doc -f amarok-doc.lang

%changelog
%autochangelog
