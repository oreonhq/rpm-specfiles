%global source0_hash 7a7c4e91995867e85bb0ee4f68992d6f09a6fb5db33adbf4374e39ed35d1727d

%global framework kactivities

Name:    kf5-%{framework}
Summary: A KDE Frameworks 5 Tier 3 to organize user work into separate activities
Version: 5.116.0
Release: 5%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0:        http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

BuildRequires:  boost-devel
BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kcmutils-devel >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kdbusaddons-devel >= %{majmin}
BuildRequires:  kf5-kdeclarative-devel >= %{majmin}
BuildRequires:  kf5-kglobalaccel-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kio-devel >= %{majmin}
BuildRequires:  kf5-kservice-devel >= %{majmin}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{majmin}
BuildRequires:  kf5-kwindowsystem-devel >= %{majmin}
BuildRequires:  kf5-kxmlgui-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel

Obsoletes:      kf5-kactivities-libs < 5.47.0-2
Provides:       kf5-kactivities-libs = %{version}-%{release}
Provides:       kf5-kactivities-libs%{?_isa} = %{version}-%{release}

%description
A KDE Frameworks 5 Tier 3 API for using and interacting with Activities as a
consumer, application adding information to them or as an activity manager.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build
%cmake_kf5

%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_bindir}/kactivities-cli
#files libs
%{_kf5_libdir}/libKF5Activities.so.*
%{_kf5_qmldir}/org/kde/activities/

%files devel
%{_kf5_libdir}/libKF5Activities.so
%{_kf5_libdir}/cmake/KF5Activities/
%{_kf5_includedir}/KActivities/

%{_kf5_libdir}/pkgconfig/libKActivities.pc
%{_kf5_archdatadir}/mkspecs/modules/qt_KActivities.pri

%changelog
%autochangelog
