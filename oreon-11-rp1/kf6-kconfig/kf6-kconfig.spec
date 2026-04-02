%global		framework kconfig

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:		kf6-%{framework}
Version:	6.24.0
Release:	1%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with advanced configuration system
License:	BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND MIT
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:	https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:	https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	extra-cmake-modules >= %{version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	pkgconfig(xkbcommon)

Requires:	kf6-filesystem

%description
KDE Frameworks 6 Tier 1 addon with advanced configuration system made of two
parts: KConfigCore and KConfigGui.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig(Qt6Xml)
Requires: cmake(Qt6Qml)
%description	devel
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

%find_lang_kf6 kconfig6_qt

%files -f kconfig6_qt.lang
%doc DESIGN README.md TODO
%license LICENSES/*.txt
%{_kf6_bindir}/kreadconfig6
%{_kf6_bindir}/kwriteconfig6
%{_kf6_datadir}/qlogging-categories6/%{framework}*
%{_kf6_libdir}/libKF6ConfigCore.so.6*
%{_kf6_libdir}/libKF6ConfigQml.so.6*
%{_kf6_libdir}/libKF6ConfigGui.so.6*
%{_kf6_libexecdir}/kconf_update
%{_kf6_libexecdir}/kconfig_compiler_kf6
%{_qt6_qmldir}/org/kde/config/qmldir
%{_qt6_qmldir}/org/kde/config/kde-qmlmodule.version
%{_qt6_qmldir}/org/kde/config/KF6ConfigQml.qmltypes
%{_qt6_qmldir}/org/kde/config/libKF6ConfigQmlplugin.so

%files devel
%{_kf6_includedir}/KConfig/
%{_kf6_includedir}/KConfigCore/
%{_kf6_includedir}/KConfigGui/
%{_kf6_includedir}/KConfigQml/
%{_kf6_libdir}/cmake/KF6Config/
%{_kf6_libdir}/libKF6ConfigCore.so
%{_kf6_libdir}/libKF6ConfigGui.so
%{_kf6_libdir}/libKF6ConfigQml.so
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
