%global source0_hash 634d92f9bedb09e5e491e7c8ceb1c4a6607ccb8ef87f8c8b1c8a9f52e3f8c0c6

Name:           kgraphviewer
Summary:        Graphviz dot graph file viewer
Version:        25.12.3
Release:        1%{?dist}
# Bit of a mess. README states it's GPLv2+, however the source files
# indicate it's GPLv2. FDL is included in COPYING.DOC, but does not
# apply to anything.
License:        GPL-2.0-only
Url:            https://apps.kde.org/kgraphviewer/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

Requires:       graphviz
Requires:       kf6-filesystem
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  boost-devel
BuildRequires:  graphviz-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6WidgetsAddons)

%description
KGraphViewer is a Graphviz dot graph file viewer.

%package libs
Summary:        Graphviz dot graph file viewer library
Requires:       kde-filesystem

%description libs
KGraphViewer is a Graphviz dot graph file viewer for KDE.
This packages contains a library that can be shared by other tools.

%package devel
Summary:        Graphviz dot graph file viewer development files
Requires:       cmake
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
KGraphViewer is a Graphviz dot graph file viewer for KDE
This package contains files useful for software development with
th KGraphViewer library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/*.appdata.xml
%find_lang %{name} --with-html

%files -f %{name}.lang
%{_kf6_bindir}/kgraphviewer
%{_qt6_plugindir}/kf6/parts/kgraphviewerpart.so 
%{_kf6_datadir}/applications/org.kde.kgraphviewer.desktop
%{_kf6_metainfodir}/org.kde.kgraphviewer.appdata.xml
%{_kf6_datadir}/icons/hicolor
%{_kf6_datadir}/config.kcfg/kgraphviewersettings.kcfg
%{_kf6_datadir}/config.kcfg/kgraphviewer_partsettings.kcfg
%{_kf6_datadir}/qlogging-categories6/kgraphviewer.categories

%files devel
%{_includedir}/kgraphviewer
%{_kf6_libdir}/cmake/KGraphViewerPart
%{_kf6_libdir}/libkgraphviewer.so

%files libs

%{_kf6_libdir}/libkgraphviewer.so.*
%doc AUTHORS
%license COPYING

%changelog
%autochangelog
