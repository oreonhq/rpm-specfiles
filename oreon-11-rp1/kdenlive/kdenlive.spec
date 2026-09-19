%global source0_hash 12ef075c6df73637948cdce7725bb8380ccd164b158157d495e6821804ce4a7f

%global _lto_cflags %{nil}

Name:    kdenlive
Summary: Non-linear video editor
Version: 25.12.3
Release: 1%{?dist}

License: (GPL-2.0-only or GPL-3.0-only) and GPL-2.0-or-later and GPL-3.0-or-later and LGPL-3.0-only and BSD-3-Clause and CC0-1.0
URL:     http://www.kdenlive.org

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: gettext

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Bookmarks)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6Plotting)
BuildRequires: cmake(KF6Purpose)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6FileMetaData)

BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6OpenGL)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6UiPlugin)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt6NetworkAuth)

BuildRequires: pkgconfig(libv4l2)
BuildRequires: pkgconfig(mlt++-7) >= 7.12.0
BuildRequires: cmake(OpenTimelineIO)
BuildRequires: ffmpeg-free-devel
BuildRequires: cmake(KDDockWidgets-qt6)

Requires: dvdauthor
Requires: /usr/bin/ffmpeg
# Require version of mlt with qt6 support
Requires: mlt%{?_isa} >= 7.22.0-2
Suggests: dvgrab
#qt5-qtquickcontrols is still required rfbz #5701 and #5702
Requires: frei0r-plugins
Requires: kf6-qqc2-desktop-style
Requires: kf6-kirigami2

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval            
ExcludeArch: %{ix86}

%description
Kdenlive is an intuitive and powerful multi-track video editor, including most
recent video technologies.

%package        doc
Summary:        Developer Documentation files for %{name}
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# disabling QCH as some files don't seem to end up installed in the right place
%{cmake_kf6} \
  -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON -Wno-dev \
  -DQT_MAJOR_VERSION=6 \
  -DBUILD_QCH:BOOL=OFF \
  -DFETCH_OTIO=OFF

%cmake_build

%install
%cmake_install

## unpackaged files
rm -rfv  %{buildroot}%{_datadir}/doc/Kdenlive/

%find_lang %{name} --with-html --all-name

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%doc AUTHORS README.md
%license COPYING LICENSES/*
%{_kf6_bindir}/kdenlive_render
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/kdenlive/
%{_kf6_datadir}/mime/packages/org.kde.kdenlive.xml
%{_kf6_datadir}/mime/packages/westley.xml
%{_kf6_datadir}/icons/*/*/*/*
%{_kf6_datadir}/config.kcfg/kdenlivesettings.kcfg
%{_kf6_datadir}/knotifications6/kdenlive.notifyrc
%{_datadir}/knsrcfiles/*.knsrc
%{_kf6_datadir}/qlogging-categories6/kdenlive.categories
%{_kf6_mandir}/man1/kdenlive.1*
%{_kf6_mandir}/man1/kdenlive_render.1*
%{_kf6_qmldir}/org/kde/kdenlive/
%{_kf6_libdir}/libkdenliveLibplugin.a
%{_kf6_datadir}/qlogging-categories6/kdenlive.renamecategories
# consider subpkg for multilib
%{_kf6_plugindir}/thumbcreator/mltpreview.so

%changelog
%autochangelog
