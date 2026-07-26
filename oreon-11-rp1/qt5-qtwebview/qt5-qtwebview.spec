%global source0_hash 0cc3ead5422619c557977135062cc74db3bda056b54d3eabd260e7baa730cf29

%global qt_module qtwebview

Summary: Qt5 - WebView component
Name:    qt5-%{qt_module}
Version: 5.15.18
Release: 2%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

BuildRequires: make
BuildRequires: qt5-qtbase-devel >= %{version}
BuildRequires: qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires: qt5-qtdeclarative-devel >= %{version}
# for 5.11, watch progress on
# https://bugreports.qt.io/browse/QTBUG-63137
BuildRequires: qt5-qtwebengine-devel

%description
Qt WebView provides a way to display web content in a QML application without necessarily
including a full web browser stack by using native APIs where it makes sense.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
Requires: qt5-qtdeclarative-devel%{?_isa}
%description devel
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{qt_module}-everywhere-src-%{version} -p1

%build
%{qmake_qt5} \
  %{?_qt5_examplesdir:CONFIG+=qt_example_installs}

%make_build

%install
make install INSTALL_ROOT=%{buildroot}

%ldconfig_scriptlets

%files
%license LICENSE.*
%{_qt5_libdir}/libQt5WebView.so.5*
%{_qt5_qmldir}/QtWebView/
%dir %{_qt5_plugindir}/webview/
# consider subpkg with rich/soft dependency -- rex
%{_qt5_plugindir}/webview/libqtwebview_webengine.so

%files devel
%{_qt5_headerdir}/QtWebView/
%{_qt5_libdir}/libQt5WebView.so
%{_qt5_libdir}/libQt5WebView.prl
%{_qt5_libdir}/pkgconfig/Qt5WebView.pc
%{_qt5_libdir}/cmake/Qt5WebView
%{_qt5_archdatadir}/mkspecs/modules/*
%exclude %{_qt5_libdir}/libQt5WebView.la

%if 0%{?_qt5_examplesdir:1}
%files examples
%{_qt5_examplesdir}/
%endif

%changelog
%autochangelog
