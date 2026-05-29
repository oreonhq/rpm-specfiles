%global source0_hash none

%global qt_module qtwebview

#global unstable 0
%if 0%{?unstable}
%global prerelease rc
%endif

%global examples 1

Summary: Qt6 - WebView component
Name:    qt6-%{qt_module}
Version: 6.10.3
Release: 1%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
%else
Source0:        https://download.qt.io/official_releases/qt/%{qt_version}/submodules/qtwebview-everywhere-src-%{qt_version}.tar.xz
%endif

%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel >= %{version}
BuildRequires: qt6-qtwebengine-devel
BuildRequires: pkgconfig(xkbcommon) >= 0.4.1
# WebEngine backend plugin needs full qt6-qtwebengine stack at runtime
Requires:      qt6-qtwebengine%{?_isa} >= %{majmin}

%description
Qt WebView provides a way to display web content in a QML application
without necessarily including a full web browser stack by using native
APIs where it makes sense.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: qt6-qtdeclarative-devel%{?_isa}
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
%cmake_qt6 \
  -DQT_BUILD_EXAMPLES:BOOL=%{?examples:ON}%{!?examples:OFF} \
  -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF}

%cmake_build


%install
%cmake_install


%files
%license LICENSES/GPL* LICENSES/LGPL*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx
%{_qt6_libdir}/libQt6WebView.so.6{,.*}
%{_qt6_libdir}/libQt6WebViewQuick.so.6{,.*}
%{_qt6_qmldir}/QtWebView/
%dir %{_qt6_plugindir}/webview/
%{_qt6_plugindir}/webview/libqtwebview_webengine.so

%files devel
%dir %{_qt6_headerdir}/QtWebView
%{_qt6_headerdir}/QtWebView/*
%dir %{_qt6_headerdir}/QtWebViewQuick
%{_qt6_headerdir}/QtWebViewQuick/*
%dir %{_qt6_libdir}/cmake/Qt6WebView
%dir %{_qt6_libdir}/cmake/Qt6WebViewPrivate
%dir %{_qt6_libdir}/cmake/Qt6WebViewQuick
%dir %{_qt6_libdir}/cmake/Qt6WebViewQuickPrivate
%{_qt6_libdir}/cmake/Qt6/FindWebView2.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtWebViewTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/cmake/Qt6WebView/*.cmake
%{_qt6_libdir}/cmake/Qt6WebViewPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6WebViewQuick/*.cmake
%{_qt6_libdir}/cmake/Qt6WebViewQuickPrivate/*.cmake
%{_qt6_libdir}/libQt6WebView.so
%{_qt6_libdir}/libQt6WebView.prl
%{_qt6_libdir}/libQt6WebViewQuick.so
%{_qt6_libdir}/libQt6WebViewQuick.prl
%{_qt6_libdir}/pkgconfig/Qt6WebView.pc
%{_qt6_libdir}/pkgconfig/Qt6WebViewQuick.pc
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/metatypes/*.json
%{_qt6_libdir}/qt6/modules/*.json

%if 0%{?examples}
%files examples
%{_qt6_examplesdir}/
%endif


%changelog
* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.3-1
- Sync module to Qt 6.10.3 (match qt6-qtbase / qt6-rpm-macros)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.2-1
- Prepare for Oreon 11 (RP1)
