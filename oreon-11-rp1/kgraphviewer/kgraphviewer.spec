%global stable_kf6 stable
%global source0_hash 634d92f9bedb09e5e491e7c8ceb1c4a6607ccb8ef87f8c8b1c8a9f52e3f8c0c6
Name:           kgraphviewer
Summary:        Graphviz dot graph file viewer
Version:        25.12.3
Release:        1%{?dist}
License:        GPL-2.0-only
Url:            https://apps.kde.org/kgraphviewer/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Requires:       graphviz
Requires:       kf6-filesystem
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  graphviz-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kgraphviewer-libs -f %{oreon_filedir}/kgraphviewer-libs.list
%files -n kgraphviewer-devel -f %{oreon_filedir}/kgraphviewer-devel.list

%changelog

%autochangelog
