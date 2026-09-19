%global source0_hash bef22243d64bb6b3eddec3db1334d9b3deebc0ea065e71e058aefad1350eb587

%global stable_kf6 stable


%global kde_name org.kde.plasma.dialer

Name:           plasma-dialer
Epoch:          1
Version:        24.08.0
Release: 1%{?dist}
License:        BSD and CC0 and GPLv2 and GPLv2+ and GPLv3 and GPLv3+ and LGPLv2+ and LGPLv2.1 and LGPLv2.1+ and LGPLv3 and LGPLv3
Summary:        Convergent Plasma Mobile dialer application
Url:            https://invent.kde.org/plasma-mobile/plasma-dialer
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz

## patches

ExclusiveArch:  %{java_arches}

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  libappstream-glib

BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6People)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6ModemManagerQt)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Crash)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(libphonenumber)
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  wayland-devel
BuildRequires:  callaudiod-devel
BuildRequires:  pkgconfig(protobuf)

BuildRequires:  wayland-devel



%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{epoch}:%{version}-%{release}

Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       libphonenumber-devel
Requires:       protobuf-devel
Provides:       %{name}-static = %{epoch}:%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_datadir}/metainfo/%{kde_name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/%{kde_name}.desktop

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/plasma-dialer-fakeserver
%{_kf6_bindir}/plasma-dialer
%{_kf6_metainfodir}/%{kde_name}.appdata.xml
%{_kf6_datadir}/applications/%{kde_name}.desktop
%{_kf6_sysconfdir}/xdg/autostart/org.kde.modem.daemon.desktop
%{_kf6_sysconfdir}/xdg/autostart/org.kde.telephony.daemon.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/dialer.svg
%{_kf6_datadir}/knotifications6/plasma-dialer.notifyrc
%{_kf6_datadir}/dbus-1/interfaces/org.kde.telephony.*
%{_kf6_datadir}/dbus-1/services/org.kde.telephony.service
%{_kf6_datadir}/dbus-1/services/org.kde.modemdaemon.service
%{_kf6_qmldir}/org/kde/telephony
%{_libexecdir}/kde-telephony-daemon
%{_libexecdir}/modem-daemon

%files devel
%{_includedir}/KF6/kTelephonyMetaTypes
%{_kf6_libdir}/libktelephonymetatypes.a

%changelog
%autochangelog
