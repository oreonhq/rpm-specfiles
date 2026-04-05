%bcond kf6_pim 1

Name:    plasma-workspace
Summary: Plasma workspace, applications and applets
Version: 6.6.2
Release:	3%{?dist}

# Automatically converted from old format: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LGPL-3.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT - review is highly recommended.
License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LGPL-3.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:     https://invent.kde.org/plasma/%{name}

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{maj_ver_kf6}.%{min_ver_kf6}.%{bug_ver_kf6}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{maj_ver_kf6}.%{min_ver_kf6}.%{bug_ver_kf6}/%{name}-%{version}.tar.xz.sig

Source11:       startkderc
Source15:       fedora-lookandfeel.json
Source16:       fedoradark-lookandfeel.json
Source17:       fedoralight-lookandfeel.json

Source100:      kde
Source101:      kde-fingerprint
Source102:      kde-smartcard


## systemd user service dependencies
## (debating whether these be owned here or somewhere better...
## in the repective pkgs themselves? -- rdieter)
Source40:       ssh-agent.conf
## To be dropped when EL10 and F42 is no longer supported
## Or if spice-vd-agent >= 0.23.0 is shipped in any existing release
Source41:       spice-vdagent.conf

## upstream patches
# Fix for build failure regarding the plasma-shell wayland interface
# https://invent.kde.org/plasma/plasma-workspace/-/commit/9114115f5af2594de64477e38e8762ff8dddbbd7
Patch1:         9114115f5af2594de64477e38e8762ff8dddbbd7.patch
# Back off the logout greeter focus grab timeout to 3 seconds
# Mitigates issue where clicking logout buttons does nothing on slow systems
# https://invent.kde.org/plasma/plasma-workspace/-/merge_requests/6413
# https://bugzilla.redhat.com/show_bug.cgi?id=2442475
Patch2:         0001-Logout-greeter-back-off-initial-focus-grab-timeout-t.patch

## upstreamable Patches

## downstream Patches
# default to enable open terminal action
Patch106:       plasma-workspace-5.27.80-enable-open-terminal-action.patch
# default to enable the lock/logout actions
Patch107:       plasma-workspace-5.27.80-enable-lock-logout-action.patch

# udev
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
Requires:       unity-gtk3-module
%ifnarch s390 s390x
BuildRequires:  libraw1394-devel
%endif
BuildRequires:  libqalculate-devel
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
BuildRequires:  plasma-breeze-devel >= %{majmin_ver_kf6}

BuildRequires:  chrpath
BuildRequires:  desktop-file-utils

BuildRequires:  cmake(AppStreamQt) >= 1.0.0

# when kded_desktopnotifier.so moved here
Conflicts:      kio-extras < 5.4.0

Recommends:     plasma-welcome

Recommends:     %{name}-geolocation = %{version}-%{release}
Suggests:       imsettings-qt

Requires:       %{name}-common = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       libkworkspace6%{?_isa} = %{version}-%{release}
# for selinux settings
Requires:       (policycoreutils if selinux-policy)

Requires:       kactivitymanagerd%{?_isa}
Requires:       ksystemstats%{?_isa}
Requires:       kf6-baloo
Requires:       kf6-kded
Requires:       kf6-kdoctools
Requires:       kf6-kglobalaccel
Requires:       kf6-kquickcharts
Requires:       kf6-kirigami
Requires:       kf6-kirigami-addons
BuildRequires:  kf6-kirigami-addons
Requires:       kio-extras
BuildRequires:  kio-extras
Requires:       kio-fuse
BuildRequires:  kio-fuse

# The new volume control for PulseAudio
Recommends:       plasma-pa

# Without the platformtheme plugins we get broken fonts
Requires:       kf6-frameworkintegration

# For krunner
Recommends:       plasma-milou

# https://pagure.io/fedora-kde/SIG/issue/303
Recommends: kde-inotify-survey

# https://pagure.io/fedora-kde/SIG/issue/354
Recommends: audiocd-kio

# For a11y
Recommends: orca

# powerdevil has a versioned dep on libkworkspace6, so (may?)
# need to avoid this dep when bootstrapping
%if ! 0%{?bootstrap}
# Power management
Requires:       powerdevil
%endif

Requires:       dbus
# dbus-update-activation-environment
Requires:       dbus-tools

# Required for applications to show in kickoff and on task manager
Requires:       redhat-menus

# startkde (TODO: review, this is no longer a shell script)
Requires:       coreutils
Requires:       socat
Requires:       xmessage
Requires:       qt6-qttools

# kconf_update
Requires:       /usr/bin/qtpaths-qt6

Requires:       xrdb xprop

Requires:       kde-settings-plasma

# Default look-and-feel theme
Requires:       plasma-lookandfeel-fedora = %{version}-%{release}

Requires:       systemd

# Default sound theme
Requires:       ocean-sound-theme

# PolicyKit authentication agent
Requires:        polkit-kde

# onscreen keyboard
Requires:        plasma-keyboard%{?_isa}

# lockscreen look-and-feel imports qml: QtQuick.VirtualKeyboard
Requires:        qt6-qtvirtualkeyboard

Requires:        (uresourced if systemd-oomd-defaults)

# needed for task manager thumbnails under wayland and for things like
# screenshare portal
BuildRequires:  kpipewire-devel

# Require any plasmashell (plasma-desktop provides plasmashell(desktop))
%if 0%{?bootstrap}
Provides:       plasmashell = %{version}
%else
# Note: We should require >= %%{version}, but that creates a circular dependency
# at build time of plasma-desktop, because it provides the needed dependency, but
# also needs plasma-workspace to build. So for now the dependency is unversioned.
Requires:       plasmashell
%endif

# plasmashell provides dbus service org.freedesktop.Notifications
Provides: desktop-notification-daemon

# digitalclock applet
%if ! 0%{?bootstrap}
BuildRequires: pkgconfig(iso-codes)
%endif
Requires: iso-codes

# Split of Xorg session into subpackage
Obsoletes: plasma-workspace < 5.19.5-2

# khotkeys was dropped
Obsoletes: khotkeys < 6

# Require Wayland session dependencies appropriately
Requires:   kwin
Requires:   xorg-x11-server-Xwayland
Requires:   qt6-qtwayland%{?_isa}
# startplasmacompositor deps
Requires:   qt6-qttools
Requires:   xdg-desktop-portal-kde
# Enables X11 apps to screenshare a Wayland environment
Recommends: xwaylandvideobridge
# Replace the old -wayland subpackage
Obsoletes:  %{name}-wayland < 6.4.1-2
Conflicts:  %{name}-wayland < 6.4.1-2
Provides:   %{name}-wayland = %{version}-%{release}
Provides:   %{name}-wayland%{?_isa} = %{version}-%{release}

%description
Plasma 6 libraries and runtime components

%package common
Summary: Common files for %{name}
%description common
%{name}.

%package -n libkworkspace6
Summary: Runtime libkworkspace6 library
# when spilt occurred
Obsoletes: plasma-workspace < 5.4.2-2
Obsoletes: libkworkspace5 < %{version}-%{release}
Requires:  %{name}-common = %{version}-%{release}
%description -n libkworkspace6
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
# when split out
Obsoletes: plasma-workspace < 5.4.2-2
## omit dep on main pkg for now, means we can avoid pulling in a
## huge amount of deps (including kde4) into buildroot -- rex
#Requires:  %%{name}%%{?_isa} = %%{version}-%%{release}
Requires:  %{name}-common = %{version}-%{release}
# consider splitting out plasma_packagestructure content later
Provides: plasma-packagestructure = %{version}-%{release}
%description libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       libkworkspace6%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation and user manuals for %{name}
# Automatically converted from old format: GFDL - review is highly recommended.
License:        LicenseRef-Callaway-GFDL
# switch to noarch
Obsoletes:      plasma-workspace-doc < 5.3.1-2
Requires:       %{name}-common = %{version}-%{release}
BuildArch: noarch
%description    doc
Documentation and user manuals for %{name}.


%package -n sddm-wayland-plasma
Summary:        Plasma Wayland SDDM greeter configuration
Provides:       sddm-greeter-displayserver
Conflicts:      sddm-greeter-displayserver
Requires:       kwin-wayland
Requires:       layer-shell-qt
Requires:       plasma-keyboard
Supplements:    (sddm and plasma-workspace)
%if ! (0%{?fedora} && 0%{?fedora} < 38)
# Replace sddm-x11 with sddm-wayland-plasma
## N.B.: If sddm gets updated in F36/F37, this will need to be bumped
Obsoletes:      sddm-x11 < 0.19.0^git20230404.e652433-2
%endif
BuildArch:      noarch

%description -n sddm-wayland-plasma
This package contains configuration and dependencies for SDDM
to use KWin for the Wayland compositor for the greeter.

%package -n plasma-lookandfeel-fedora
Summary:  Fedora look-and-feel for Plasma
Requires: %{name} = %{version}-%{release}
# lockscreen look-and-feel imports qml: QtQuick.VirtualKeyboard
Requires: qt6-qtvirtualkeyboard
# when switched to noarch
Obsoletes: plasma-lookandfeel-fedora < 5.8.0-5
# https://bugzilla.redhat.com/show_bug.cgi?id=1356890
Obsoletes: f22-kde-theme < 22.4
Obsoletes: f23-kde-theme < 23.1
Obsoletes: f24-kde-theme < 24.6
Obsoletes: f24-kde-theme-core < 5.10.5-2
BuildArch: noarch
%description -n plasma-lookandfeel-fedora
%{summary}.


%prep
%autosetup -p1

# Populate initial lookandfeel package
cp -a lookandfeel/org.kde.breeze lookandfeel/org.fedoraproject.fedora
cp -a lookandfeel/org.kde.breeze lookandfeel/org.fedoraproject.fedoradark
cp -a lookandfeel/org.kde.breeze lookandfeel/org.fedoraproject.fedoralight
# Overwrite settings to configure twilight mode
cp -a lookandfeel/org.kde.breezetwilight/* lookandfeel/org.fedoraproject.fedora
# Overwrite settings to configure dark mode
cp -a lookandfeel/org.kde.breezedark/* lookandfeel/org.fedoraproject.fedoradark
# Write the correct lookandfeel package names
install -m 0644 %{SOURCE15} lookandfeel/org.fedoraproject.fedora/metadata.json
install -m 0644 %{SOURCE16} lookandfeel/org.fedoraproject.fedoradark/metadata.json
install -m 0644 %{SOURCE17} lookandfeel/org.fedoraproject.fedoralight/metadata.json
cat >> lookandfeel/CMakeLists.txt <<EOL
plasma_install_package(org.fedoraproject.fedora org.fedoraproject.fedora.desktop look-and-feel lookandfeel)
plasma_install_package(org.fedoraproject.fedoradark org.fedoraproject.fedoradark.desktop look-and-feel lookandfeel)
plasma_install_package(org.fedoraproject.fedoralight org.fedoraproject.fedoralight.desktop look-and-feel lookandfeel)
EOL


%build
%cmake_kf6 \
  -DINSTALL_SDDM_WAYLAND_SESSION:BOOL=ON \
  -DWITH_X11_SESSION:BOOL=OFF \
  -DGLIBC_LOCALE_GEN:BOOL=OFF \
  -DGLIBC_LOCALE_PREGENERATED:BOOL=ON
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
#chrpath --delete %{buildroot}%{_kf6_qtplugindir}/phonon_platform/kde.so

# General startplasma symlink
ln -sr %{buildroot}%{_kf6_bindir}/startplasma-wayland %{buildroot}%{_kf6_bindir}/startplasma

# Drop (Wayland) qualifier from plasma.desktop
sed -E 's| \(.*\)||g' -i %{buildroot}%{_datadir}/wayland-sessions/plasma.desktop

# move sddm configuration snippet to the right place
mkdir -p %{buildroot}%{_prefix}/lib/sddm
mv %{buildroot}%{_sysconfdir}/sddm.conf.d %{buildroot}%{_prefix}/lib/sddm

## customize plasma-lookandfeel-fedora defaults
# from [Wallpaper] Image=Next to Image=Fedora
sed -i -e 's|^Image=.*$|Image=Fedora|g' \
  %{buildroot}%{_kf6_datadir}/plasma/look-and-feel/org.fedoraproject.fedora*.desktop/contents/defaults

# PAM
# https://invent.kde.org/plasma/kscreenlocker/-/merge_requests/163#less-simple-method-for-redhat-and-redhat-adjacent-fedora-opensuse-etc-systems
install -m644 -p -D %{SOURCE100} %{buildroot}%{_sysconfdir}/pam.d/kde
install -m644 -p -D %{SOURCE101} %{buildroot}%{_sysconfdir}/pam.d/kde-fingerprint
install -m644 -p -D %{SOURCE102} %{buildroot}%{_sysconfdir}/pam.d/kde-smartcard

# Make kdestart use systemd
install -m644 -p -D %{SOURCE11} %{buildroot}%{_sysconfdir}/xdg/startkderc

# systemd user service deps
mkdir -p %{buildroot}%{_userunitdir}/plasma-core.target.d/
mkdir -p %{buildroot}%{_userunitdir}/plasma-workspace@.target.d/

install -m644 -p -D %{SOURCE40} %{buildroot}%{_userunitdir}/plasma-core.target.d/ssh-agent.conf
%if ! (0%{?rhel} >= 11 || 0%{?fedora} >= 43)
install -m644 -p -D %{SOURCE41} %{buildroot}%{_userunitdir}/plasma-core.target.d/spice-vdagent.conf
%endif

%find_lang all --with-html --all-name

grep "%{_kf6_docdir}" all.lang > %{name}-doc.lang
grep libkworkspace.mo all.lang > libkworkspace6.lang
# any translations not used elsewhere, include in main pkg
cat *.lang | sort | uniq -u > %{name}.lang


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.{plasmashell,kcolorschemeeditor,kfontview,plasmawindowed,klipper,plasma-interactiveconsole,baloorunner,secretprompter}.desktop

%post
if [ -s /usr/sbin/setsebool ] ; then
  setsebool -P selinuxuser_execmod 1 ||:
fi

%files common
%license LICENSES

%files -f %{name}.lang
%{_libexecdir}/ksecretprompter
%{_kf6_datadir}/applications/org.kde.baloorunner.desktop
%{_kf6_datadir}/applications/org.kde.secretprompter.desktop
%{_kf6_datadir}/xdg-desktop-portal/kde-portals.conf
%{_sysconfdir}/xdg/menus/plasma-applications.menu
%{_kf6_bindir}/gmenudbusmenuproxy
%{_kf6_bindir}/kcminit
%{_kf6_bindir}/kcminit_startup
%{_kf6_bindir}/krunner
%{_kf6_bindir}/ksmserver
%{_kf6_bindir}/ksplashqml
%{_kf6_bindir}/plasmashell
%{_kf6_bindir}/plasmawindowed
%{_kf6_bindir}/plasma_session
%{_kf6_bindir}/plasma-apply-*
%{_kf6_bindir}/plasma-interactiveconsole
%{_kf6_bindir}/plasma-shutdown
%{_kf6_bindir}/plasma_waitforname
%{_kf6_bindir}/xembedsniproxy
%{_kf6_bindir}/kcolorschemeeditor
%{_kf6_bindir}/kde-systemd-start-condition
%{_kf6_bindir}/kfontinst
%{_kf6_bindir}/kfontview
%{_kf6_bindir}/lookandfeeltool
%{_kf6_qmldir}/org/kde/*
%{_libexecdir}/baloorunner
%{_libexecdir}/ksmserver-logout-greeter
%{_libexecdir}/kf6/kauth/fontinst*
%{_libexecdir}/kfontprint
%{_libexecdir}/plasma-changeicons
%{_libexecdir}/plasma-dbus-run-session-if-needed
%{_libexecdir}/plasma-fallback-session-*
%{_kf6_datadir}/plasma/avatars/
%{_kf6_datadir}/plasma/plasmoids/
%{_kf6_datadir}/plasma/wallpapers/
%dir %{_kf6_datadir}/plasma/look-and-feel/
%{_kf6_datadir}/plasma/look-and-feel/org.kde.breeze.desktop/
%{_kf6_datadir}/plasma/look-and-feel/org.kde.breezedark.desktop/
%{_kf6_datadir}/plasma/look-and-feel/org.kde.breezetwilight.desktop/
%{_kf6_datadir}/solid/
%{_kf6_datadir}/kstyle/
%{_sysconfdir}/xdg/startkderc
%{_sysconfdir}/xdg/autostart/*.desktop
%{_datadir}/zsh/site-functions/_krunner
%{_datadir}/zsh/site-functions/_plasmashell
%{_datadir}/icons/hicolor/*/*/*font*.png
%{_datadir}/icons/hicolor/scalable/apps/preferences-desktop-font-installer.svgz
%{_datadir}/desktop-directories/*.directory
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/system-services/org.kde.fontinst.service
%{_datadir}/dbus-1/system.d/org.kde.fontinst.conf
%{_datadir}/knsrcfiles/*.knsrc
%{_datadir}/kfontinst/icons/hicolor/*/actions/*font*.png
%{_datadir}/konqsidebartng/virtual_folders/services/fonts.desktop
%{_datadir}/krunner/dbusplugins/plasma-runner-baloosearch.desktop
%{_datadir}/kxmlgui5/kfontviewpart/kfontviewpart.rc
%{_datadir}/kxmlgui5/kfontview/kfontviewui.rc
%{_kf6_datadir}/knotifications6/*.notifyrc
%{_kf6_datadir}/config.kcfg/*
%{_kf6_datadir}/kio_desktop/
%{_kf6_datadir}/applications/kcm_*
%{_kf6_datadir}/applications/org.kde.plasmashell.desktop
%{_kf6_datadir}/applications/org.kde.kcolorschemeeditor.desktop
%{_kf6_datadir}/applications/org.kde.kfontview.desktop
%{_kf6_datadir}/applications/org.kde.kfontinst.desktop
%{_kf6_datadir}/applications/org.kde.plasmawindowed.desktop
%{_kf6_datadir}/applications/org.kde.plasma-fallback-session-save.desktop
%{_kf6_datadir}/applications/org.kde.klipper.desktop
%{_kf6_datadir}/kio/servicemenus/installfont.desktop
%{_kf6_datadir}/qlogging-categories6/*.categories
%{_sysconfdir}/xdg/plasmanotifyrc
%{_kf6_datadir}/polkit-1/actions/org.kde.fontinst.policy
%{_userunitdir}/*.service
%{_userunitdir}/plasma-core.target
%dir %{_userunitdir}/plasma-core.target.d/
%{_userunitdir}/plasma-core.target.d/ssh-agent.conf
%if ! (0%{?rhel} >= 11 || 0%{?fedora} >= 43)
%{_userunitdir}/plasma-core.target.d/spice-vdagent.conf
%endif
%{_userunitdir}/plasma-workspace.target
%{_userunitdir}/plasma-workspace-wayland.target
%{_userunitdir}/plasma-workspace-x11.target
%dir %{_userunitdir}/plasma-workspace@.target.d/
%{_libdir}/kconf_update_bin/plasma6.3-update-clipboard-database-2-to-3
%{_datadir}/kconf_update/plasma6.3-update-clipboard-database-2-to-3.upd
%{_libdir}/kconf_update_bin/plasmashell-6.5-remove-stop-activity-shortcut
%{_datadir}/kconf_update/plasmashell-6.5-remove-stop-activity-shortcut.upd
%{_kf6_datadir}/timezonefiles/timezones.json
%{_kf6_datadir}/applications/org.kde.plasma-interactiveconsole.desktop
# PAM
%config(noreplace) %{_sysconfdir}/pam.d/kde
%config(noreplace) %{_sysconfdir}/pam.d/kde-fingerprint
%config(noreplace) %{_sysconfdir}/pam.d/kde-smartcard
# Plasma Wayland
%{_kf6_bindir}/startplasma
%{_kf6_bindir}/startplasma-wayland
%{_datadir}/wayland-sessions/plasma.desktop

%files doc -f %{name}-doc.lang

%files -n libkworkspace6 -f libkworkspace6.lang
%{_libdir}/libkworkspace6.so.*

%files libs
%{_libdir}/libbatterycontrol.so.*
%{_libdir}/libtaskmanager.so.*
%{_libdir}/libklipper.so.*
%{_libdir}/libkrdb.so
%{_libdir}/libnotificationmanager.*
%{_libdir}/libkfontinst*
%{_libdir}/libkmpris.so.*
# multilib'able plugins
%{_kf6_qtplugindir}/plasma/applets/
%if %{with kf6_pim}
%{_kf6_qtplugindir}/plasmacalendarplugins/
%endif
%{_kf6_plugindir}/kio/*.so
%{_kf6_plugindir}/kded/*.so
%{_libdir}/libklookandfeel.so.6
%{_libdir}/libklookandfeel.so.%{version}
%{_kf6_plugindir}/krunner/*
%{_qt6_plugindir}/plasma/kcms/systemsettings/kcm_*.so
%{_kf6_qtplugindir}/kf6/parts/kfontviewpart.so
%{_kf6_qtplugindir}/kf6/thumbcreator/fontthumbnail.so
%{_kf6_qtplugindir}/kf6/kfileitemaction/wallpaperfileitemaction.so
%{_kf6_qtplugindir}/kf6/packagestructure/plasma_layouttemplate.so
%{_kf6_qtplugindir}/kf6/packagestructure/plasma_lookandfeel.so
%{_kf6_qtplugindir}/kf6/packagestructure/wallpaper_images.so
%{_kf6_qtplugindir}/plasma/containmentactions/org.kde.applauncher.so
%{_kf6_qtplugindir}/plasma/containmentactions/org.kde.contextmenu.so
%{_kf6_qtplugindir}/plasma/containmentactions/org.kde.paste.so
%{_kf6_qtplugindir}/plasma/containmentactions/org.kde.switchdesktop.so
%{_kf6_qtplugindir}/plasma/containmentactions/switchwindow.so
%{_kf6_qtplugindir}/plasma/containmentactions/switchactivity.so
%{_kf6_qtplugindir}/plasma/kcminit/kcm_fonts_init.so
%{_kf6_qtplugindir}/plasma/kcminit/kcm_style_init.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/kcm_fontinst.so
%{_libexecdir}/plasma-sourceenv.sh
%{_kf6_datadir}/kconf_update/plasma6.0-remove-dpi-settings.upd
%{_kf6_datadir}/kconf_update/plasmashell-6.0-keep-default-floating-setting-for-plasma-5-panels.upd
%{_kf6_datadir}/kconf_update/plasma6.0-remove-old-shortcuts.upd
%{_kf6_datadir}/kconf_update/migrate-calendar-to-plugin-id.upd
%{_kf6_datadir}/kconf_update/migrate-calendar-to-plugin-id.py
%{_kf6_datadir}/kconf_update/plasmashell-6.0-keep-custom-position-of-panels.upd
%{_kf6_datadir}/kconf_update/plasma6.4-migrate-fullscreen-notifications-to-dnd.upd
%{_libdir}/kconf_update_bin/plasma6.0-remove-old-shortcuts
%{_libdir}/kconf_update_bin/plasmashell-6.0-keep-default-floating-setting-for-plasma-5-panels
%{_libdir}/kconf_update_bin/plasma6.0-remove-dpi-settings
%{_libdir}/kconf_update_bin/plasmashell-6.0-keep-custom-position-of-panels
%{_libdir}/kconf_update_bin/plasma6.4-migrate-fullscreen-notifications-to-dnd
%{_kf6_datadir}/kglobalaccel/org.kde.krunner.desktop

%files devel
%{_libdir}/libbatterycontrol.so
%{_libdir}/libklipper.so
%{_libdir}/libtaskmanager.so
%{_libdir}/libkworkspace6.so
%{_includedir}/kworkspace6/
%{_includedir}/taskmanager/
%{_includedir}/notificationmanager/
%{_libdir}/cmake/KRunnerAppDBusInterface/
%{_libdir}/cmake/KSMServerDBusInterface/
%{_libdir}/cmake/LibKLookAndFeel/
%{_libdir}/cmake/LibKWorkspace/
%{_libdir}/cmake/LibTaskManager/
%{_libdir}/cmake/LibNotificationManager/
%{_datadir}/dbus-1/interfaces/*.xml
%{_includedir}/krdb/krdb.h
%{_includedir}/krdb/krdb_export.h
%{_includedir}/klookandfeel/
%{_libdir}/cmake/Krdb/*.cmake
%{_libdir}/libklookandfeel.so

%files -n sddm-wayland-plasma
%{_prefix}/lib/sddm/sddm.conf.d/plasma-wayland.conf

%files -n plasma-lookandfeel-fedora
%{_kf6_datadir}/plasma/look-and-feel/org.fedoraproject.fedora*.desktop/


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-2
- Prepare for Oreon 11 (RP1)
