%global source0_hash none

%global qt_module qtquicktimeline

#global unstable 0
%if 0%{?unstable}
%global prerelease rc
%endif

Summary: Qt6 - QuickTimeline plugin
Name:    qt6-%{qt_module}
Version: 6.11.1
Release: 1%{?dist}

License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
%else
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-rpm-macros >= %{version}
BuildRequires: qt6-qtbase-static >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel


%description
The Qt Quick Timeline plugin provides QML types to use timelines and keyframes
to animate Qt Quick user interfaces.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: qt6-qtdeclarative-devel%{?_isa}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1


%build
%cmake_qt6

%cmake_build


%install
%cmake_install

%ldconfig_scriptlets

%files
%license LICENSES/GPL*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx
%dir %{_qt6_qmldir}/QtQuick
%{_qt6_libdir}/libQt6QuickTimeline.so.6*
%{_qt6_libdir}/libQt6QuickTimelineBlendTrees.so.6*
%{_qt6_qmldir}/QtQuick/Timeline/

%files devel
%{_qt6_includedir}/QtQuickTimeline/
%{_qt6_includedir}/QtQuickTimelineBlendTrees/
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6QuickTimeline/
%dir %{_qt6_libdir}/cmake/Qt6QuickTimelinePrivate
%{_qt6_libdir}/cmake/Qt6QuickTimeline/*.cmake
%{_qt6_libdir}/cmake/Qt6QuickTimelinePrivate/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6QuickTimelineBlendTrees/
%{_qt6_libdir}/cmake/Qt6QuickTimelineBlendTrees/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6QuickTimelineBlendTreesPrivate
%{_qt6_libdir}/cmake/Qt6QuickTimelineBlendTreesPrivate/*.cmake
%{_qt6_libdir}/libQt6QuickTimeline.prl
%{_qt6_libdir}/libQt6QuickTimeline.so
%{_qt6_libdir}/libQt6QuickTimeline.prl
%{_qt6_libdir}/libQt6QuickTimeline.so
%{_qt6_libdir}/libQt6QuickTimelineBlendTrees.prl
%{_qt6_libdir}/libQt6QuickTimelineBlendTrees.so
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/pkgconfig/*.pc

%changelog
* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.3-1
- Sync module to Qt 6.10.3 (match qt6-qtbase / qt6-rpm-macros)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.2-1
- Prepare for Oreon 11 (RP1)
