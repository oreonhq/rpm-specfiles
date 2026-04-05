Name:    kwin-x11
Version: 6.6.2
Release:	2%{?dist}
Summary: KDE Window manager with X11 support

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:     https://userbase.kde.org/KWin

%global revision %(echo %{version} | cut -d. -f3)
%global plasma_version %(echo %{version} | cut -d. -f1-3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: https://download.kde.org/%{stable}/plasma/%{plasma_version}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable}/plasma/%{plasma_version}/%{name}-%{version}.tar.xz.sig

## upstream patches

## proposed patches

# Base
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  systemd-rpm-macros

# Qt
BuildRequires:  cmake(QAccessibilityClient6)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-static
# KWinQpaPlugin (and others?)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtsensors-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qttools-static
BuildRequires:  qt6-qtwayland-devel
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Svg)

# X11/OpenGL
BuildRequires:  pkgconfig(libxcvt)
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  libxcb-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libXcursor-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-cursor-devel
BuildRequires:  xcb-util-devel
BuildRequires:  libepoxy-devel
BuildRequires:  libcap-devel

BuildRequires:  lcms2-devel
BuildRequires:  glib2-devel
BuildRequires:  pipewire-devel

# Wayland (Why does CMakeLists.txt still require Wayland libraries here?)
BuildRequires:  wayland-devel >= 1.23.0
BuildRequires:  wayland-protocols-devel
BuildRequires:  libxkbcommon-devel >= 0.4
BuildRequires:  pkgconfig(libinput) >= 0.10
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xwayland)

# KF6
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KNightTime)

BuildRequires:  cmake(KDecoration3)
BuildRequires:  kscreenlocker-devel
BuildRequires:  plasma-breeze-devel
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  cmake(KGlobalAccelD)
BuildRequires:  libdisplay-info-devel

BuildRequires:  cmake(KWayland)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(PlasmaActivities)

# Unknowns
BuildRequires:  pkgconfig(libcanberra)

## Runtime deps
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kscreenlocker%{?_isa}
Requires:       kf6-kirigami2%{?_isa}
Requires:       kf6-kdeclarative%{?_isa}
Requires:       libplasma%{?_isa} >= %{plasma_version}
Requires:       qt6-qtmultimedia%{?_isa}
Requires:       qt6-qtdeclarative%{?_isa}

# Before kwin was split out from kde-workspace into a subpackage
Conflicts:      kde-workspace%{?_isa} < 4.11.14-2
# Split of X11 variant into subpackage
Conflicts:      kwin < 5.19.5-3

Requires:       xorg-x11-server-Xorg
# http://bugzilla.redhat.com/605675
Provides:       firstboot(windowmanager) = kwin_x11
# KWinX11Platform (and others?)

# Nothing except plasma-workspace-x11 should depend on this package. Some people
# are worried that we want to build a whole "ecosystem" around *-x11, which is
# of course not the plan. If you think you have a legitimate reason for your
# package to depend on kwin-x11, please contact the maintainer (Kevin Kofler) so
# we can find a solution together with FESCo and the KDE SIG. Note that this tag
# does NOT mean that this package is planned to be removed any time soon.
Provides:       deprecated()

%description
Alternative version of the KDE Window Manager (KWin) using the legacy X11 window
system instead of the default Wayland. This version of KWin is required by
plasma-workspace-x11, which provides the "Plasma (X11)" session type.

This version is maintained by individual Fedora packagers and NOT supported by
the Fedora KDE SIG. (See kwin-wayland for the default version, using Wayland,
maintained by the KDE SIG.)

%package        libs
Summary:        %{name} runtime libraries
# See the comment in the main package above
Provides:       deprecated()

%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6Quick)
Requires:       cmake(KF6Config)
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(KF6WindowSystem)
Requires:       pkgconfig(wayland-server)
# See the comment in the main package above
Provides:       deprecated()

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --with-html --all-name


%files -f %{name}.lang
%license LICENSES/*.txt
%{_kf6_bindir}/kwin_x11
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/applications/*.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/kconf_update/%{name}.upd
%{_kf6_datadir}/knotifications6/%{name}.notifyrc
%{_kf6_datadir}/knsrcfiles/*-x11.knsrc
%{_kf6_datadir}/krunner/dbusplugins/kwin-runner-windows-x11.desktop
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-delete-desktop-switching-shortcuts-x11
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-remove-breeze-tabbox-default-x11
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-reset-active-mouse-screen-x11
%{_kf6_libdir}/kconf_update_bin/kwin-6.1-remove-gridview-expose-shortcuts-x11
%{_kf6_libdir}/kconf_update_bin/kwin-6.5-showpaint-changes-x11
%{_kf6_libdir}/kconf_update_bin/kwin5_update_default_rules_x11
%{_kf6_qtplugindir}/%{name}/
%{_kf6_qtplugindir}/kf6/packagestructure/kwin_*_x11.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/*.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/*.so
%{_libexecdir}/kwin_killer_helper_x11
%{_libexecdir}/kwin-applywindowdecoration-x11
%{_qt6_qmldir}/org/kde/kwin_x11/
%{_userunitdir}/plasma-kwin_x11.service

%files libs
%{_kf6_datadir}/qlogging-categories6/org_kde_kwin_x11.categories
%{_kf6_libdir}/lib%{name}.so.6{,.*}
%{_kf6_libdir}/libkcmkwincommon-x11.so.6{,.*}

%files devel
%{_includedir}/%{name}/
%{_kf6_datadir}/dbus-1/interfaces/*.xml
%{_kf6_libdir}/cmake/KWinX11/
%{_kf6_libdir}/cmake/KWinX11DBusInterface/
%{_kf6_libdir}/lib%{name}.so


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
