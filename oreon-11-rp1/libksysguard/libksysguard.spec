%global source0_hash 6f7dbf058e453c6d2d643cf5cf25051aa0398fa3c8f3cb754bf2e46434d94cd7

%global stable_kf6 stable

Name:    libksysguard
Summary: Library for managing processes running on the system
Version:        6.7.2
Release: 1%{?dist}

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  qt6-qttools-devel
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Core5Compat)

%ifarch %{qt6_qtwebengine_arches}
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6WebChannel)
%endif

BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(libnl-3.0) pkgconfig(libnl-route-3.0)
BuildRequires:  libcap-devel
BuildRequires:  libXres-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  zlib-devel

Obsoletes:      kf5-ksysguard < 5.1.95
Provides:       kf5-ksysguard = %{version}-%{release}

Requires:       %{name}-common = %{version}-%{release}

Conflicts: ksysguard-backend < 5.21.90

%description
KSysGuard library provides API to read and manage processes
running on the system.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6Network)
Requires:       cmake(Qt6Widgets)
Requires:       cmake(KF6Config)
Requires:       cmake(KF6I18n)
Requires:       cmake(KF6IconThemes)
Obsoletes:      kf5-ksysguard-devel < 5.1.95
Provides:       kf5-ksysguard-devel = %{version}-%{release}
Conflicts:      kde-workspace-devel < 1:4.11.16-11

%package        common
Summary:        Runtime data files shared by libksysguard and ksysguard-libs
Conflicts:      libksysguard < 5.2.1-2
Conflicts:      ksysguard < 5.2
%description    common
%{summary}.

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version} -p1

%build
%cmake_kf6 -DENABLE_KAUTH_HELPER:BOOL=%{!?flatpak:ON}%{?flatpak:OFF}
%cmake_build

%install
%cmake_install
%find_lang ksysguard_qt6 --with-qt --with-kde --all-name

%files -f ksysguard_qt6.lang
%license LICENSES
%{_kf6_libdir}/libprocesscore.so.*
%{_kf6_libdir}/libKSysGuardFormatter.so*
%{_kf6_libdir}/libKSysGuardSensors.so*
%{_kf6_libdir}/libKSysGuardSensorFaces.so*
%{_kf6_datadir}/ksysguard/
%{_kf6_datadir}/qlogging-categories6/libksysguard.categories
%{_qt6_qmldir}/org/kde/ksysguard/
%{_kf6_libdir}/libKSysGuardSystemStats.so.*
%{_qt6_plugindir}/ksysguard/
%dir %{_libexecdir}/ksysguard
%caps(cap_net_raw=ep) %{_libexecdir}/ksysguard/ksgrd_network_helper
%{_kf6_datadir}/dbus-1/interfaces/org.kde.ksystemstats1.xml
%{_qt6_plugindir}/kf6/packagestructure/ksysguard_sensorface.so
%{_kf6_bindir}/ksysguard-identify

%files common
%if %{undefined flatpak}
%{_kf6_libexecdir}/kauth/ksysguardprocesslist_helper
%{_datadir}/dbus-1/system.d/org.kde.ksysguard.processlisthelper.conf
%{_datadir}/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service
%{_datadir}/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy
%endif
%{_datadir}/knsrcfiles/*

%files devel
%{_includedir}/ksysguard/
%{_kf6_libdir}/libprocesscore.so
%{_kf6_libdir}/cmake/KSysGuard/
%{_kf6_libdir}/libKSysGuardSystemStats.so

%changelog
%autochangelog
