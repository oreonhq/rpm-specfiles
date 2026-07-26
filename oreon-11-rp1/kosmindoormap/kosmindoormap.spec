%global source0_hash 1da64c99c29fbd3f722732a14d44ab67417e66cec8de179fa5b2ec676aa6331b

Name:    kosmindoormap
Version: 25.12.3
Release: 1%{?dist}
Summary: OSM multi-floor indoor map renderer

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND LGPL-3.0-or-later AND MIT AND ODbL-1.0
URL:     https://invent.kde.org/libraries/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)

BuildRequires:  zlib-devel
BuildRequires:  cmake(KOpeningHours)
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  osmctools
BuildRequires:  rsync
BuildRequires:  protobuf-devel
BuildRequires:  openssl-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  protobuf-lite-devel

BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KPublicTransport)
BuildRequires:  cmake(KOpeningHours)

Requires:       kf6-filesystem

%description
A library and QML component for rendering multi-level OSM indoor
maps of for example a (large) train station.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/*.txt
%doc README.md
%{_kf6_libdir}/libKOSM.so.*
%{_kf6_libdir}/libKOSMIndoorMap.so.*
%{_qt6_qmldir}/org/kde/kosmindoormap/
%{_qt6_qmldir}/org/kde/osm/editorcontroller/libkosmeditorcontrollerplugin.so
%{_qt6_qmldir}/org/kde/osm/editorcontroller/qmldir
%{_qt6_qmldir}/org/kde/osm/editorcontroller/kde-qmlmodule.version
%{_qt6_qmldir}/org/kde/osm/editorcontroller/kosmeditorcontrollerplugin.qmltypes
%{_datadir}/qlogging-categories6/org_kde_kosmindoormap.categories
%{_qt6_qmldir}/org/kde/kosmindoorrouting/
%{_kf6_libdir}/libKOSMIndoorRouting.so.*

%files devel
%{_includedir}/KOSMIndoorMap/
%{_includedir}/kosm/
%{_includedir}/kosmindoormap/
%{_includedir}/kosmindoormap_version.h
%{_includedir}/KOSM/
%{_includedir}/KOSMIndoorRouting/
%{_includedir}/kosmindoorrouting/
%{_kf6_libdir}/cmake/KOSMIndoorMap/
%{_kf6_libdir}/libKOSM.so
%{_kf6_libdir}/libKOSMIndoorMap.so
%{_kf6_libdir}/libKOSMIndoorRouting.so

%changelog
%autochangelog
