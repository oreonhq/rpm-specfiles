Name:    kscreenlocker
Version: 6.6.2
Release: 1%{?dist}
Summary: Library and components for secure lock screen architecture

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

# help upgrades, split from plasma-workspace since 5.5
Conflicts: plasma-workspace < 5.5

## upstream patches

BuildRequires: cmake(LayerShellQt)

BuildRequires:  perl-generators
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  cmake(Qt6Quick)

BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Screen)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6KirigamiPlatform)

BuildRequires:  libX11-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(xi)

# Plasma
BuildRequires:  cmake(PlasmaQuick)

BuildRequires:  libXcursor-devel
BuildRequires:  pam-devel

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name} --with-qt --all-name


%files -f %{name}.lang
%license COPYING
%{_kf6_libdir}/libKScreenLocker.so.*
%{_kf6_datadir}/knotifications6/*.notifyrc
%{_libexecdir}/kscreenlocker_greet
%dir %{_kf6_datadir}/ksmserver/
%{_kf6_datadir}/ksmserver/screenlocker/
%{_kf6_datadir}/applications/kcm_screenlocker.desktop
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_screenlocker.so
%{_kf6_datadir}/qlogging-categories6/kscreenlocker.categories

%files devel
%{_kf6_libdir}/libKScreenLocker.so
%{_kf6_libdir}/cmake/ScreenSaverDBusInterface/
%{_kf6_libdir}/cmake/KScreenLocker/
%{_includedir}/KScreenLocker/
%{_datadir}/dbus-1/interfaces/*.xml


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
