%global source0_hash e5d3b284ccc907f190d3ab10995a0ae7fa0f505088acc69edc7adfcc6a8140d6

%global framework knotifications

%global stable_kf6 stable
%global majmin_ver_kf6 6.28


Name:    kf6-%{framework}
Version: 6.28.0
Release:        2%{?dist}
Summary: KDE Frameworks 6 Tier 2 solution with abstraction for system notifications

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  libcanberra-devel
BuildRequires:  cmake(KF6Config) >= %{version}

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

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6 -DBUILD_PYTHON_BINDINGS=OFF
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
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

%files devel
%{_kf6_includedir}/KNotifications/
%{_kf6_libdir}/libKF6Notifications.so
%{_kf6_libdir}/cmake/KF6Notifications/


%autochangelog

