%global source0_hash f4061299a69dc9e3cf83c0e54c174708d8dc748ae208d30a04b274c552586dbf

%global stable_kf6 stable


Name:           libksysguard
Version:        6.6.3
Release:        5%{?dist}
Summary:        KDE system monitoring libraries and plugin runtime for Plasma
License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://invent.kde.org/plasma/libksysguard
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kf6-kquickcharts-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  libdrm-devel
BuildRequires:  libnl3-devel
BuildRequires:  libpcap-devel
BuildRequires:  libplasma-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  ninja-build
BuildRequires:  gettext-devel
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Designer)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6Sensors)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)

Requires:       kf6-filesystem
Requires:       kf6-kquickcharts%{?_isa}
Requires:       libksysguard-system-stats%{?_isa} = %{version}-%{release}
Requires:       libksysguard-processcore%{?_isa} = %{version}-%{release}
Requires:       libksysguard-formatter%{?_isa} = %{version}-%{release}
Requires:       libksysguard-sensor-faces%{?_isa} = %{version}-%{release}
Requires:       libksysguard-sensors%{?_isa} = %{version}-%{release}

%description
Libraries, QML components, and helpers used by Plasma system monitor and
ksystemstats.


%package -n libksysguard-system-stats
Summary:        KSysGuard system stats shared library

%description -n libksysguard-system-stats
%{summary}.

%package -n libksysguard-processcore
Summary:        KSysGuard process core shared library

%description -n libksysguard-processcore
%{summary}.

%package -n libksysguard-formatter
Summary:        KSysGuard formatter shared library

%description -n libksysguard-formatter
%{summary}.

%package -n libksysguard-sensor-faces
Summary:        KSysGuard sensor faces shared library

%description -n libksysguard-sensor-faces
%{summary}.

%package -n libksysguard-sensors
Summary:        KSysGuard sensors shared library

%description -n libksysguard-sensors
%{summary}.

%package        devel
Summary:        Development files for libksysguard
Requires:       libksysguard%{?_isa} = %{version}-%{release}
Requires:       libksysguard-system-stats%{?_isa} = %{version}-%{release}
Requires:       libksysguard-processcore%{?_isa} = %{version}-%{release}
Requires:       libksysguard-formatter%{?_isa} = %{version}-%{release}
Requires:       libksysguard-sensor-faces%{?_isa} = %{version}-%{release}
Requires:       libksysguard-sensors%{?_isa} = %{version}-%{release}

%description    devel
Headers and CMake files for libksysguard.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n libksysguard-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-qt --all-name


%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/libksysguard.categories
%{_datadir}/dbus-1/interfaces/org.kde.ksystemstats1.xml
%{_libexecdir}/kf6/kauth/ksysguardprocesslist_helper
%dir %{_libexecdir}/ksysguard
%{_libexecdir}/ksysguard/ksgrd_network_helper
%{_kf6_datadir}/dbus-1/system.d/org.kde.ksysguard.processlisthelper.conf
%{_kf6_datadir}/dbus-1/system-services/org.kde.ksysguard.processlisthelper.service
%{_kf6_qmldir}/org/kde/ksysguard
%{_kf6_qtplugindir}/kf6/packagestructure/ksysguard_sensorface.so
%{_kf6_datadir}/knsrcfiles/systemmonitor-faces.knsrc
%{_kf6_datadir}/knsrcfiles/systemmonitor-presets.knsrc
%{_kf6_datadir}/ksysguard/sensorfaces
%{_datadir}/polkit-1/actions/org.kde.ksysguard.processlisthelper.policy
%dir %{_kf6_qtplugindir}/ksysguard
%dir %{_kf6_qtplugindir}/ksysguard/process
%{_kf6_qtplugindir}/ksysguard/process/ksysguard_plugin_network.so
%{_kf6_qtplugindir}/ksysguard/process/ksysguard_plugin_gpu.so

%files -n libksysguard-system-stats
%{_libdir}/libKSysGuardSystemStats.so.2*
%{_libdir}/libKSysGuardSystemStats.so.6*

%files -n libksysguard-processcore
%{_libdir}/libprocesscore.so.10*
%{_libdir}/libprocesscore.so.6*

%files -n libksysguard-formatter
%{_libdir}/libKSysGuardFormatter.so.2*
%{_libdir}/libKSysGuardFormatter.so.6*

%files -n libksysguard-sensor-faces
%{_libdir}/libKSysGuardSensorFaces.so.2*
%{_libdir}/libKSysGuardSensorFaces.so.6*

%files -n libksysguard-sensors
%{_libdir}/libKSysGuardSensors.so.2*
%{_libdir}/libKSysGuardSensors.so.6*

%files devel
# 6.6.x installs formatter/sensors/etc. under include/ksysguard/ (not top-level KSysGuard*)
%{_includedir}/ksysguard
%{_libdir}/libKSysGuardSystemStats.so
%{_libdir}/libprocesscore.so
%{_libdir}/libKSysGuardFormatter.so
%{_libdir}/libKSysGuardSensorFaces.so
%{_libdir}/libKSysGuardSensors.so
%{_libdir}/cmake/KSysGuard


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-2
- Add libksysguard stack for Plasma system monitor
