
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    gwenview
Summary: An image viewer
Epoch:   1
Version: 25.12.3
Release: 1%{?dist}

# app + lib: GPL-2.0-or-later
# lib/jlibjpeg: IJG
# lib/zoomcombobox: LGPL-2.1-or-later
# lib/cms/iccjpeg.c: MIT
# lib/flowlayout.cpp: GPL-2.0-only OR GPL-3.0-only (see https://gitlab.com/fedora/legal/fedora-license-data/-/issues/718 )
# doc: GFDL-1.2-only (but is not packaged)
License: GPL-2.0-or-later AND IJG AND LGPL-2.1-or-later AND MIT AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://www.kde.org/applications/graphics/gwenview/

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

## upstreamable patches

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Baloo)
BuildRequires: cmake(PlasmaActivities)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6Purpose)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KDcrawQt6)
BuildRequires: cmake(kColorPicker-Qt6)
BuildRequires: cmake(kImageAnnotator-Qt6)
BuildRequires: libappstream-glib
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(exiv2)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(cfitsio)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: cmake(phonon4qt6)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6OpenGL)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: cmake(Qt6WaylandScannerTools)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: qt6-qtbase-private-devel
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)

Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

# support for more formats, e.g. jp2, tiff, webp
Recommends: qt6-qtimageformats%{?_isa}
# eps, etc...
Recommends: kf6-kimageformats%{?_isa}

# when split occurred
Conflicts: kdegraphics < 7:4.6.95-10

# translations moved here
Conflicts: kde-l10n < 17.03

%description
%{summary}.

%package  libs
Summary:  Runtime files for %{name}
# lib/cms/iccjpeg.c: MIT
# lib/jlibjpeg: IJG
# lib/zoomcombobox: LGPL-2.1-or-later
# lib/cms/iccjpeg.c: MIT
# lib/flowlayout.cpp: GPL-2.0-only OR GPL-3.0-only (see https://gitlab.com/fedora/legal/fedora-license-data/-/issues/718 )
License:  IJG AND MIT AND LGPL-2.1-or-later AND (GPL-2.0-only OR GPL-3.0-only)
Requires: %{name} = %{epoch}:%{version}-%{release}
%description libs
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.gwenview.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.gwenview.desktop


%files -f %{name}.lang
%license COPYING
%{_kf6_bindir}/gwenview
%{_kf6_bindir}/gwenview_importer
%{_kf6_datadir}/applications/org.kde.gwenview.desktop
%{_kf6_datadir}/applications/org.kde.gwenview_importer.desktop
%{_kf6_datadir}/gwenview/
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/qlogging-categories6/gwenview.categories
%{_kf6_datadir}/solid/actions/gwenview_importer*.desktop
%{_kf6_metainfodir}/org.kde.gwenview.appdata.xml


%files libs
%{_kf6_libdir}/libgwenviewlib.so.*
%{_kf6_plugindir}/parts/gvpart.so
%{_kf6_plugindir}/kfileitemaction/slideshowfileitemaction.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
