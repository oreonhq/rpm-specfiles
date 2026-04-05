
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kscreen
Epoch:   1
Version: 6.6.2
Release:	2%{?dist}
Summary: KDE Display Management software

License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  systemd-rpm-macros

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtsensors-devel

BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Screen)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  wayland-devel

BuildRequires:  cmake(Plasma)

BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xi)

%description
KCM and KDED modules for managing displays in KDE.


%prep
%autosetup -p1


%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --with-kde --all-name


%files -f %{name}.lang
%license LICENSES
%{_bindir}/kscreen-console
%{_bindir}/hdrcalibrator
%{_kf6_datadir}/applications/kcm_kscreen.desktop
%{_kf6_datadir}/kglobalaccel/org.kde.kscreen.desktop
%{_kf6_datadir}/dbus-1/services/org.kde.kscreen.osdService.service
%{_kf6_datadir}/qlogging-categories6/kscreen.categories
%{_kf6_plugindir}/kded/kscreen.so
%{_kf6_qtplugindir}/plasma/applets/org.kde.kscreen.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_kscreen.so
%{_libexecdir}/kscreen_osd_service
%{_userunitdir}/plasma-kscreen-osd.service

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
