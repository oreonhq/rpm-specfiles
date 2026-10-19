%global stable_kf6 stable
%global source0_hash 68e9e83d7d8c0cbdd470958e768815f573d61f3ce32be7bc1b87fb56d622436e
%if 0%{?fedora} >= 44 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
%define _lto_cflags %{nil}
%endif
%global __provides_exclude_from ^%{_kf6_qmldir}/org/kde/amarok/.*\.so$
Name:    amarok
Summary:        Media player
Version: 3.3.3
Release:        1%{?dist}
License: GPL-2.0-only OR GPL-3.0-only
Url:     https://amarok.kde.org/
%if 0%{?commitdate}
Source0:        https://download.kde.org/%{stable_kf6}/%{name}/%{version}/%{name}-%{version}.tar.xz
%else
Source0:        https://download.kde.org/%{stable_kf6}/%{name}/%{version}/%{name}-%{version}.tar.xz
%endif
Patch1:  revert.patch
Patch2:  liblastfm-version.patch
Patch10: fix-mygpo-qt6-compilation.patch
ExcludeArch:   %{ix86}
%ifarch %{qt6_qtwebengine_arches}
%endif
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
Requires:      %{name}-utils = %{version}-%{release}
Requires:      kf6-filesystem
Requires:      kf6-kirigami%{?_isa}
Recommends:    audiocd-kio
Recommends:    kio-extras
%ifarch %{qt6_qtwebengine_arches}
Recommends:    qt6-qtwebengine%{?_isa}
%endif
# oreon:deps
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DNSSD)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6ThreadWeaver)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Mygpo-qt6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  ffmpeg-free-devel
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libgcrypt-devel
BuildRequires:  liblastfm-qt6-devel
BuildRequires:  mariadb-embedded-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgpod-1.0)
BuildRequires:  pkgconfig(libmariadb)
BuildRequires:  pkgconfig(libmtp)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(loudmouth-1.0)
BuildRequires:  pkgconfig(mariadb)
BuildRequires:  pkgconfig(taglib)
# /oreon:deps
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
CXXFLAGS="$CXXFLAGS -I%{_includedir}/qt6"
%endif
%{cmake_kf6} \
  -DMYSQLCONFIG_EXECUTABLE:BOOL=OFF -DWITH_X11=OFF
%{cmake_build}
%install
%cmake_install
%find_lang amarokcollectionscanner_qt --with-qt --without-mo --all-name
%find_lang amarok --all-name
%find_lang amarok-doc --with-html --without-mo --all-name
%oreon_autofiles amarok-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles amarok-utils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles amarok-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}*.desktop
%files -f %{oreon_filedir}/main.list
%files -n amarok-libs -f %{oreon_filedir}/amarok-libs.list
%files -n amarok-utils -f %{oreon_filedir}/amarok-utils.list
%files -n amarok-doc -f %{oreon_filedir}/amarok-doc.list

%changelog

%autochangelog
