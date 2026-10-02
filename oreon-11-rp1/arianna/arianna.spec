%global source0_hash affa1f27d97608bad8ab0871ca06906d47127c0731bd4759f975e7e59cd1ff00

%global stable_kf6 stable


Name:          arianna
Version:       26.08.1
Release:       1%{?dist}
Summary:       EPub Reader for mobile devices
# Complete license breakdown can be found in the "LICENSE-BREAKDOWN" file.
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:       GPL-3.0-only
URL:           https://invent.kde.org/graphics/%{name}

Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6WebSockets)
BuildRequires: cmake(Qt6WebChannel)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6HttpServer)
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6FileMetaData)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6QuickCharts)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6QQC2DesktopStyle)
BuildRequires: cmake(Qt6WebEngineQuick)
BuildRequires: qt6-qtwebengine-devel >= 6.11.1-5
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Baloo)
BuildRequires: cmake(KF6ColorScheme)
BuildRequires: fdupes
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

# QML module dependencies
Requires: kf6-kirigami%{?_isa}
Requires: kf6-kirigami-addons%{?_isa}
Requires: kf6-kitemmodels%{?_isa}
Requires: kf6-kquickcharts%{?_isa}
Requires: kf6-qqc2-desktop-style%{?_isa}
Requires: qt6-qt5compat%{?_isa}
Requires: qt6-qtwebchannel%{?_isa}
Requires: qt6-qtwebengine%{?_isa}

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
# Package doesn't build on arches that qtwebengine is not built on.
ExclusiveArch: %{qt6_qtwebengine_arches}

%description
An ebook reader and library management app


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%cmake_kf6 %{?flatpak:-DQT_BUILD_CMAKE_PREFIX_PATH=%{_libdir}/cmake}
%cmake_build
%fdupes

%install
%cmake_install
%find_lang %{name} --with-kde --with-man --all-name

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.arianna.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.arianna.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/arianna
%{_kf6_datadir}/applications/org.kde.arianna.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.arianna.svg
%{_kf6_datadir}/qlogging-categories6/arianna.categories
%{_kf6_metainfodir}/org.kde.arianna.appdata.xml

%changelog
%autochangelog
