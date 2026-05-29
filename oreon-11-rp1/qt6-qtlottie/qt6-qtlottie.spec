%global source0_hash none

%global qt_module qtlottie

#global unstable 0
%if 0%{?unstable}
%global prerelease rc
%endif

%global examples 1

Summary: Qt6 - Lottie Animation
Name:    qt6-%{qt_module}
Version: 6.10.3
Release: 1%{?dist}

License: GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
%else
Source0:        https://download.qt.io/archive/qt/%{qt_version}/submodules/qtlottie-everywhere-src-%{qt_version}.tar.xz
%endif

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel >= %{version}
BuildRequires: qt6-qtsvg-devel >= %{version}
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: openssl-devel

%description
Qt Lottie Animation provides a QML API for rendering graphics and animations
that are exported in JSON format by the Bodymovin plugin for Adobe After
Effects.

%package devel
Summary: Development files for %{name}
Requires: qt6-qtbase-devel%{?_isa}
%description devel
%{summary}.

%if 0%{?examples}
%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1


%build
%cmake_qt6

%cmake_build

%install
%cmake_install


%files
%license LICENSES/GPL*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx
%{_qt6_libdir}/libQt6Lottie.so.6*
%{_qt6_libdir}/libQt6LottieVectorImageGenerator.so.6*
%{_qt6_libdir}/libQt6LottieVectorImageHelpers.so.6*
%{_qt6_plugindir}/vectorimageformats/libqlottievectorimage.so
%{_qt6_qmldir}/Qt/labs/lottieqt/

%files devel
%{_qt6_bindir}/lottietoqml
%{_qt6_libdir}/libQt6Lottie.so
%{_qt6_libdir}/libQt6LottieVectorImageGenerator.so
%{_qt6_libdir}/libQt6LottieVectorImageHelpers.so
%{_qt6_libdir}/libQt6Lottie.prl
%{_qt6_libdir}/libQt6LottieVectorImageGenerator.prl
%{_qt6_libdir}/libQt6LottieVectorImageHelpers.prl
%{_qt6_headerdir}/QtLottie
%{_qt6_headerdir}/QtLottieVectorImageGenerator
%{_qt6_headerdir}/QtLottieVectorImageHelpers
%dir %{_qt6_libdir}/cmake/Qt6Lottie
%dir %{_qt6_libdir}/cmake/Qt6LottiePrivate
%dir %{_qt6_libdir}/cmake/Qt6LottieTools
%dir %{_qt6_libdir}/cmake/Qt6LottieVectorImageGeneratorPrivate
%dir %{_qt6_libdir}/cmake/Qt6LottieVectorImageHelpers
%dir %{_qt6_libdir}/cmake/Qt6LottieVectorImageHelpersPrivate
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtLottieTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Lottie/*.cmake
%{_qt6_libdir}/cmake/Qt6LottiePrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6LottieTools/*.cmake
%{_qt6_libdir}/cmake/Qt6LottieVectorImageGeneratorPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6LottieVectorImageHelpers/*.cmake
%{_qt6_libdir}/cmake/Qt6LottieVectorImageHelpersPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/*
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/pkgconfig/*.pc

%if 0%{?examples}
%files examples
%{_qt6_examplesdir}/
%endif

%changelog
* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.3-1
- Sync module to Qt 6.10.3 (match qt6-qtbase / qt6-rpm-macros)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.2-1
- Prepare for Oreon 11 (RP1)
