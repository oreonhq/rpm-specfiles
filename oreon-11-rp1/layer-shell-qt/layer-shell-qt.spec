Name:    layer-shell-qt
Version: 6.6.2
Release:	2%{?dist}
Summary: Library to easily use clients based on wlr-layer-shell

License: BSD-3-Clause AND CC0-1.0 AND LGPL-3.0-or-later AND MIT
URL:     https://invent.kde.org/plasma/%{name}

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig


BuildRequires: extra-cmake-modules

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtbase-private-devel

BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: cmake(Qt6Qml)

BuildRequires: libxkbcommon-devel
BuildRequires: plasma-wayland-protocols-devel
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel

%description
This component is meant for applications to be able to easily use clients
based on wlr-layer-shell

%package devel
Summary:  Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(Qt6Gui)
%description devel
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6

%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%files
%license LICENSES/*
%{_libdir}/libLayerShellQtInterface.so.*
%{_qt6_plugindir}/wayland-shell-integration/
%{_kf6_qmldir}/org/kde/layershell/LayerShellQtQml.qmltypes
%{_kf6_qmldir}/org/kde/layershell/kde-qmlmodule.version
%{_kf6_qmldir}/org/kde/layershell/libLayerShellQtQml.so
%{_kf6_qmldir}/org/kde/layershell/qmldir

%files devel
%{_includedir}/LayerShellQt/
%{_libdir}/libLayerShellQtInterface.so
%{_libdir}/cmake/LayerShellQt/


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
