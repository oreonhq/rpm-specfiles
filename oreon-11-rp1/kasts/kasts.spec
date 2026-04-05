%global kf6_min_version 6.0.0


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           kasts
Version:        25.12.3
Release:	2%{?dist}

# Automatically converted from old format: GPLv2 and GPLv2+ and GPLv3+ and BSD and LGPLv3+ - review is highly recommended.
License:        GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-or-later AND LicenseRef-Callaway-BSD AND LGPL-3.0-or-later
Summary:        A mobile podcast application
Url:            https://apps.kde.org/%{name}
Source:         https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  taglib-devel

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Multimedia)

BuildRequires:  cmake(KF6BreezeIcons)    >= %{kf6_min_version}
BuildRequires:  cmake(KF6I18n)           >= %{kf6_min_version}
BuildRequires:  cmake(KF6CoreAddons)     >= %{kf6_min_version}
BuildRequires:  cmake(KF6Kirigami)       >= %{kf6_min_version}
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Syndication)    >= %{kf6_min_version}
BuildRequires:  cmake(KF6Config)         >= %{kf6_min_version}
BuildRequires:  cmake(KF6ThreadWeaver)   >= %{kf6_min_version}
BuildRequires:  cmake(KF6ColorScheme)    >= %{kf6_min_version}
BuildRequires:  cmake(KF6Crash)          >= %{kf6_min_version}
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  pkgconfig(libvlc)
BuildRequires:  kf6-rpm-macros           >= %{kf6_min_version}

# QML module dependencies
Requires:  kf6-kirigami%{?_isa}
Requires:  kf6-kirigami-addons%{?_isa}
Requires:  qt6-qt5compat%{?_isa}
Requires:  qt6-qtmultimedia%{?_isa}

%description
%{summary}.

%prep
%autosetup -p1

%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

%files -f %{name}.lang
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/scalable/actions/media-playback-cloud.svg
%{_kf6_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_kf6_datadir}/icons/hicolor/scalable/apps/%{name}-tray-dark.svg
%{_kf6_datadir}/icons/hicolor/scalable/apps/%{name}-tray-light.svg
%{_kf6_libdir}/libKMediaSession.so
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_qmldir}/org/kde/kmediasession/kde-qmlmodule.version
%{_kf6_qmldir}/org/kde/kmediasession/kmediasessionqmlplugin.qmltypes
%{_kf6_qmldir}/org/kde/kmediasession/libkmediasessionqmlplugin.so
%{_kf6_qmldir}/org/kde/kmediasession/qmldir
%license LICENSES/*


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
