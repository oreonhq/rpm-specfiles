%global framework knotifications

%global stable_kf6 stable
%global majmin_ver_kf6 6.24

Name:    kf6-%{framework}
Version: 6.24.0
Release:	2%{?dist}
Summary: KDE Frameworks 6 Tier 2 solution with abstraction for system notifications

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  libcanberra-devel
BuildRequires:  cmake(KF6Config)

# required for pyside6 python bindings
BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  clang-devel
BuildRequires:  cmake(Shiboken6)
BuildRequires:  cmake(PySide6)

%description
KDE Frameworks 6 Tier 3 solution with abstraction for system
notifications.

%package        -n python3-%{name}
Summary:        Qt for Python bindings for %{name}
%description    -n python3-%{name}
The package contains the pyside6 bindings library for %{name}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6 \
    -DQDOC_BIN=/bin/true
%cmake_build_kf6

%install
%cmake_install_kf6

%find_lang_kf6 knotifications6_qt
# We own the folder
mkdir -p %{buildroot}/%{_kf6_datadir}/knotifications6

%files -f knotifications6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6Notifications.so.*
%dir %{_kf6_datadir}/knotifications6
%{_libdir}/qt6/qml/org/kde/notification/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/notification/knotificationqmlplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/notification/libknotificationqmlplugin.so
%{_libdir}/qt6/qml/org/kde/notification/qmldir

%files -n python3-%{name}
%{python3_sitearch}/KNotifications.cpython-%{python3_version_nodots}*.so

%files devel
%{_kf6_includedir}/KNotifications/
%{_kf6_libdir}/libKF6Notifications.so
%{_kf6_libdir}/cmake/KF6Notifications/

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- Pass -DQDOC_BIN=/bin/true to work around qdoc segfault until kf6-rpm-macros is deployed

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.24.0-1
- Prepare for Oreon 11 (RP1)
