Name:    kwin
Version: 6.6.2
Release:	3%{?dist}
Summary: KDE Window manager

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:     https://userbase.kde.org/KWin

%global plasma_version %(echo %{version} | cut -d. -f1-3)

Source0: http://download.kde.org/%{stable_kf6}/plasma/%{maj_ver_kf6}.%{min_ver_kf6}.%{bug_ver_kf6}/%{name}-%{version}.tar.xz
Source1: http://download.kde.org/%{stable_kf6}/plasma/%{maj_ver_kf6}.%{min_ver_kf6}.%{bug_ver_kf6}/%{name}-%{version}.tar.xz.sig

## upstream patches

## proposed patches


# Base
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  systemd-rpm-macros

# Qt
BuildRequires:  cmake(QAccessibilityClient6)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-static
# KWinQpaPlugin (and others?)
BuildRequires:  qt6-qtbase-private-devel
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

# Wayland
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
BuildRequires:  libeis-devel
BuildRequires:  pkgconfig(libcanberra)

## Runtime deps
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-common%{?_isa} = %{version}-%{release}
Requires:       kscreenlocker%{?_isa}
Requires:       kf6-kirigami2%{?_isa}
Requires:       kf6-kdeclarative%{?_isa}
Requires:       libplasma%{?_isa} >= %{plasma_version}
Requires:       qt6-qtmultimedia%{?_isa}
Requires:       qt6-qtdeclarative%{?_isa}
Requires:       aurorae%{?_isa}
Requires:       iio-sensor-proxy%{?_isa}

# Before kwin was split out from kde-workspace into a subpackage
Conflicts:      kde-workspace%{?_isa} < 4.11.14-2

Obsoletes:      kwin-gles < 5
Obsoletes:      kwin-gles-libs < 5

# Split of X11 variant into subpackage
Obsoletes: kwin < 5.19.5-3

Requires:   %{name}-wayland = %{version}-%{release}

# Merge -wayland subpackage
Conflicts: %{name}-wayland < 6.3.90
Obsoletes: %{name}-wayland < 6.3.90
Provides:  %{name}-wayland = %{version}-%{release}
Provides:  %{name}-wayland%{?_isa} = %{version}-%{release}

# Obsolete kwin-wayland-nvidia package as this is now done automatically
# by kwin-wayland
Obsoletes:      %{name}-wayland-nvidia < 5.20.2-2
Provides:       %{name}-wayland-nvidia = %{version}-%{release}
# Obsolete -x11 for Plasma 6
%if 0%{?fedora}
Obsoletes:      %{name}-x11 < 5.92.0
%else
Obsoletes:      %{name}-x11 < %{version}-%{release}
Conflicts:      %{name}-x11 < %{version}-%{release}
%endif
%if ! 0%{?rhel} >= 10
Requires:       (kwayland-integration%{?_isa} if kf5-kwindowsystem%{?_isa})
%endif
%if ! 0%{?bootstrap}
BuildRequires:  xorg-x11-server-Xwayland
%endif
Requires:       xorg-x11-server-Xwayland
# KWinQpaPlugin (and others?)

%description
%{summary}.


%package        common
Summary:        Common files for KWin X11 and KWin Wayland
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       kwayland%{?_isa}
# Split of X11 variant into subpackage
Obsoletes:      %{name}-common < 5.19.5-3
%description    common
%{summary}.

%package        libs
Summary:        KWin runtime libraries
# Before kwin-libs was split out from kde-workspace into a subpackage
Conflicts:      kde-workspace-libs%{?_isa} < 4.11.14-2
# kwin uses wl_display_set_default_max_buffer_size from wayland 1.23.0
# https://bugzilla.redhat.com/show_bug.cgi?id=2312499
Requires:       libwayland-server%{?_isa} >= 1.23.0
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-common%{?_isa} = %{version}-%{release}
Requires:       kf6-kconfig-devel
Requires:       kf6-kservice-devel
Requires:       kf6-kwindowsystem-devel
Conflicts:      kde-workspace-devel < 5.0.0-1
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        User manual for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    doc
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --with-html --all-name
grep "%{_kf6_docdir}" %{name}.lang > %{name}-doc.lang
cat %{name}.lang %{name}-doc.lang | sort | uniq -u > kwin6.lang

# co-own Xwayland-session.d folder
mkdir -p %{buildroot}%{_sysconfdir}/xdg/Xwayland-session.d

# temporary(?) hack to allow initial-setup to use /usr/bin/kwin too
ln -sr %{buildroot}%{_kf6_bindir}/kwin_wayland %{buildroot}%{_bindir}/kwin


%files
%{_bindir}/kwin
%{_bindir}/kwin_wayland_wrapper
%{_datadir}/kwin-wayland/
%caps(cap_sys_nice=ep) %{_kf6_bindir}/kwin_wayland
%{_userunitdir}/plasma-kwin_wayland.service
%dir %{_sysconfdir}/xdg/Xwayland-session.d

%files common -f kwin6.lang
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/*.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/*.so
%{_kf6_qtplugindir}/kwin/
%{_kf6_qtplugindir}/kf6/packagestructure/kwin_*.so
%{_qt6_qmldir}/org/kde/kwin/
%{_kf6_libdir}/kconf_update_bin/kwin5_update_default_rules
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-delete-desktop-switching-shortcuts
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-remove-breeze-tabbox-default
%{_kf6_libdir}/kconf_update_bin/kwin-6.0-reset-active-mouse-screen
%{_kf6_libdir}/kconf_update_bin/kwin-6.1-remove-gridview-expose-shortcuts
%{_kf6_libdir}/kconf_update_bin/kwin-6.5-showpaint-changes
%{_libexecdir}/kwin_killer_helper
%{_libexecdir}/kwin-applywindowdecoration
%{_libexecdir}/kwin-tabbox-preview
%{_datadir}/kconf_update/kwin.upd
%{_kf6_datadir}/knotifications6/kwin.notifyrc
%{_kf6_datadir}/config.kcfg/kwin.kcfg
%{_kf6_datadir}/config.kcfg/kwindecorationsettings.kcfg
%{_kf6_datadir}/config.kcfg/virtualdesktopssettings.kcfg
%{_kf6_datadir}/config.kcfg/nightlightsettings.kcfg
%{_datadir}/icons/hicolor/*/apps/kwin.*
%{_datadir}/knsrcfiles/*.knsrc
%{_datadir}/krunner/dbusplugins/kwin-runner-windows.desktop
%{_datadir}/applications/*.desktop
%{_bindir}/kwindowprop

%files libs
%{_kf6_datadir}/qlogging-categories6/org_kde_kwin.categories
%{_libdir}/libkwin.so.*
%{_libdir}/libkcmkwincommon.so.*

%files devel
%{_datadir}/dbus-1/interfaces/*.xml
%{_libdir}/cmake/KWinDBusInterface
%{_includedir}/kwin
%{_libdir}/cmake/KWin
%{_libdir}/libkwin.so

%files doc -f %{name}-doc.lang
%license LICENSES/*.txt


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-2
- Prepare for Oreon 11 (RP1)
