
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    plasma-workspace-x11
Summary: Xorg support for Plasma
Version: 6.6.2
Release: 2%{?dist}

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LGPL-3.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:     https://invent.kde.org/plasma/plasma-workspace

%global revision %(echo %{version} | cut -d. -f3)
%global plasma_version %(echo %{version} | cut -d. -f1-3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: https://download.kde.org/%{stable}/plasma/%{plasma_version}/plasma-workspace-%{version}.tar.xz
Source1: https://download.kde.org/%{stable}/plasma/%{plasma_version}/plasma-workspace-%{version}.tar.xz.sig

## upstreamable Patches

## downstream Patches

## upstream Patches

BuildRequires:  cmake
BuildRequires:  gcc-c++

BuildRequires:  zlib-devel
BuildRequires:  libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXau-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXft-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-cursor-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-renderutil-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-devel
BuildRequires:  glib2-devel
BuildRequires:  fontconfig-devel
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(libusb)
BuildRequires:  libbsd-devel
BuildRequires:  pam-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  pciutils-devel
BuildRequires:  pipewire-devel
BuildRequires:  unity-gtk3-module
%ifnarch s390 s390x
BuildRequires:  libraw1394-devel
%endif
BuildRequires:  libqalculate-devel
%global kf6_pim 1
BuildRequires:  libicu-devel

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtwayland-devel
BuildRequires:  cmake(Qt6Location)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  polkit-qt6-1-devel
BuildRequires:  libcanberra-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libudev)
BuildRequires:  systemd

BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF6Baloo)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6Su)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6People)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6UnitConversion)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6ThreadWeaver)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6QuickCharts)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6KDED)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(KF6Screen)
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KF6Prison)
BuildRequires:  cmake(KF6UserFeedback)
BuildRequires:  cmake(KNightTime)
BuildRequires:  cmake(Plasma5Support)

BuildRequires:  wayland-devel >= 1.3.0
BuildRequires:  libksysguard-devel
BuildRequires:  kscreenlocker-devel
BuildRequires:  kwin-devel
BuildRequires:  layer-shell-qt-devel
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  PackageKit-Qt6-devel
BuildRequires:  cmake(KExiv2Qt6)

BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(KWayland)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(PlasmaActivitiesStats)

# workaround for
#   The imported target "Qt6::XkbCommonSupport" references the file
#     "/usr/lib64/libQt6XkbCommonSupport.a"
#  but this file does not exist.
BuildRequires:  qt6-qtbase-static
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(QCoro6)
BuildRequires:  pkgconfig(libxcrypt)

BuildRequires:  wayland-protocols-devel
BuildRequires:  plasma-wayland-protocols-devel
BuildRequires:  plasma-breeze-devel >= %{plasma_version}

BuildRequires:  chrpath
BuildRequires:  desktop-file-utils

BuildRequires:  cmake(AppStreamQt) >= 1.0.0

BuildRequires:  kf6-kirigami-addons
BuildRequires:  kio-extras
BuildRequires:  kio-fuse

# Rename this package to match upstream
Obsoletes:      plasma-workspace-xorg < 5.20.90-2
Provides:       plasma-workspace-xorg = %{version}-%{release}
Provides:       plasma-workspace-xorg%{?_isa} = %{version}-%{release}
# Split of Xorg session into subpackage
Obsoletes:      plasma-workspace < 5.19.5-2
Requires:       plasma-workspace >= %{plasma_version}
Requires:       kwin-x11
Requires:       kf6-kidletime-x11
Requires:       xorg-x11-server-Xorg
Requires:       xsetroot

# Nothing should depend on this package. Some people are worried that we want to
# build a whole "ecosystem" around *-x11, which is of course not the plan. If
# you think you have a legitimate reason for your package to depend on
# plasma-workspace-x11, please contact the maintainer (Kevin Kofler) so we can
# find a solution together with FESCo and the KDE SIG. Note that this tag does
# NOT mean that this package is planned to be removed any time soon.
Provides:       deprecated()

%description
Support for the legacy X11 window system in KDE Plasma, as opposed to the
default Wayland. This package provides the legacy "Plasma (X11)" session type
and the startplasma-x11 executable required by that session type. (Other
requirements such as kwin-x11 are found in the package dependencies.) The
session type can be switched between "Plasma (X11)" and the default "Plasma
(Wayland)" in the display manager (e.g., SDDM).

This version is maintained by individual Fedora packagers and NOT supported by
the Fedora KDE SIG. (See plasma-workspace-wayland for the default version, using
Wayland, maintained by the KDE SIG.)


%prep
%setup -q -n plasma-workspace-%{version}

# set component for the install step
sed -i \
 -e 's/install(TARGETS startplasma-x11 /install(TARGETS startplasma-x11 COMPONENT X11 /g' \
 startkde/CMakeLists.txt
sed -i \
 -e 's# DESTINATION \${KDE_INSTALL_DATADIR}/xsessions$# DESTINATION ${KDE_INSTALL_DATADIR}/xsessions COMPONENT X11#g' \
 login-sessions/CMakeLists.txt


%build
%cmake_kf6 \
  -DINSTALL_SDDM_WAYLAND_SESSION:BOOL=OFF \
  -DPLASMA_X11_DEFAULT_SESSION:BOOL=OFF \
  -DGLIBC_LOCALE_GEN:BOOL=OFF \
  -DGLIBC_LOCALE_PREGENERATED:BOOL=ON
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose --target startplasma-x11

%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose --component X11


%files
%{_kf6_bindir}/startplasma-x11
%{_datadir}/xsessions/plasmax11.desktop


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: inline cmake build/install with --component (no qt6 install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
