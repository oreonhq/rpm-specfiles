%global 	framework kguiaddons

Name:		kf6-%{framework}
Version:	6.24.0
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with various classes on top of QtGui

License:	BSD-2-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only
URL:		https://invent.kde.org/frameworks/%{framework}

Source0:	https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:	https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  pkgconfig(wayland-protocols)

BuildRequires:  cmake(Qt6WaylandClient)

BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)

# required for pyside6 python bindings
BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  clang-devel
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(PySide6)

Requires:       kf6-filesystem

%description
%{summary}.

%package        -n python3-%{name}
Summary:        Qt for Python bindings for %{name}
%description    -n python3-%{name}
The package contains the pyside6 bindings library for %{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       qt6-qtbase-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        html
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    html
Developer Documentation files for %{name} in HTML format

%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build_kf6

%install
%cmake_install_kf6

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/kde-geo-uri-handler
%{_kf6_datadir}/qlogging-categories6/*categories
%{_kf6_libdir}/libKF6GuiAddons.so.*
%{_kf6_datadir}/applications/*-handler.desktop
%{_kf6_qmldir}/org/kde/guiaddons/

%files -n python3-%{name}
%{python3_sitearch}/KGuiAddons.cpython-%{python3_version_nodots}*.so

%files devel
%{_kf6_includedir}/KGuiAddons/
%{_kf6_libdir}/libKF6GuiAddons.so
%{_kf6_libdir}/cmake/KF6GuiAddons/
%{_kf6_libdir}/pkgconfig/KF6GuiAddons.pc
%{_qt6_docdir}/*/*.tags
%{_qt6_docdir}/*/*.index

%files doc
%{_qt6_docdir}/*.qch

%files html
%{_qt6_docdir}/*/*
%exclude %{_qt6_docdir}/*/*.tags
%exclude %{_qt6_docdir}/*/*.index

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)
