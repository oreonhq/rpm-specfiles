%global source0_hash 485930001af56d647825cb5b99a7693b70a3270b1b270b32224a5f81dc69b44b

%global framework knotifications

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 2 solution with abstraction for system notifications

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

## upstream patches

BuildRequires:  dbusmenu-qt5-devel
BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kcodecs-devel >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kwindowsystem-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros

BuildRequires:  phonon-qt5-devel
BuildRequires:  pkgconfig(libcanberra)

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  cmake(Qt5Quick)

%if !0%{?bootstrap}
%if 0%{?fedora}
BuildRequires:  pkgconfig(Qt5TextToSpeech)
%endif
%endif

%if 0%{?tests}
BuildRequires: dbus-x11
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif

%description
KDE Frameworks 5 Tier 3 solution with abstraction for system
notifications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf5 \
  %{?tests:-DBUILD_TESTING:BOOL=ON}

%cmake_build

%install
%cmake_install

%find_lang_kf5 knotifications5_qt

# We own the folder
mkdir -p %{buildroot}/%{_kf5_datadir}/knotifications5

%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a dbus-launch --exit-with-session \
time make test -C %{_target_platform} ARGS="--output-on-failure --timeout 300" ||:
%endif

%ldconfig_scriptlets

%files -f knotifications5_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf5_datadir}/qlogging-categories5/%{framework}.*
%{_kf5_libdir}/libKF5Notifications.so.*
%{_kf5_datadir}/knotifications5/
%{_kf5_qmldir}/org/kde/notification/

%files devel

%{_kf5_includedir}/KNotifications/
%{_kf5_libdir}/libKF5Notifications.so
%{_kf5_libdir}/cmake/KF5Notifications/
%{_kf5_datadir}/dbus-1/interfaces/*.xml
%{_kf5_archdatadir}/mkspecs/modules/qt_KNotifications.pri

%changelog
%autochangelog
