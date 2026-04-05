%global scim 1
%if 0%{?rhel} && 0%{?rhel} > 7
%undefine scim
%endif

Name:    plasma-desktop
Summary: Plasma Desktop shell
Version: 6.6.2
Release:	2%{?dist}

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{maj_ver_kf6}.%{min_ver_kf6}.%{bug_ver_kf6}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{maj_ver_kf6}.%{min_ver_kf6}.%{bug_ver_kf6}/%{name}-%{version}.tar.xz.sig

# breeze fedora sddm theme components
# includes f40-based preview (better than breeze or nothing at least)
Source20:       breeze-fedora-0.3.tar.gz

## upstream patches

## downstream patches
# default kickoff/kicker favorites: +kwrite +konsole
# Patch100: plasma-desktop-5.90.0-default_favorites.patch

# Hide virtual keyboard indicator on sddm.
# Do not remove this as it breaks Fedora's QA policy
Patch101:       hide-virtual-keyboard-indicator-on-sddm.patch

## upstreamable patches

BuildRequires:  pkgconfig(libusb)
BuildRequires:  fontconfig-devel
BuildRequires:  libX11-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-renderutil-devel
BuildRequires:  xcb-util-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  pkgconfig(xkeyboard-config)

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtwayland-devel
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  wayland-protocols-devel

BuildRequires:  ibus-devel
%if 0%{?scim}
BuildRequires:  scim-devel
%endif

BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6Su)
BuildRequires:  cmake(KF6Attica)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6Baloo)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6People)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6KDED)
BuildRequires:  cmake(KF6KIO)

BuildRequires:  cmake(KSysGuard)
BuildRequires:  cmake(Plasma5Support)
BuildRequires:  kscreenlocker-devel
BuildRequires:  kwin-devel
BuildRequires:  plasma-breeze-qt6
BuildRequires:  plasma-workspace-devel

BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(PlasmaActivitiesStats)
BuildRequires:  cmake(Plasma)

# For theming info
# /usr/share/backgrounds/default.{jxl,png}
BuildRequires:  desktop-backgrounds-compat


# Optional
%if 0%{?fedora}
BuildRequires:  cmake(AppStreamQt)
%endif
BuildRequires:  intltool
BuildRequires:  cmake(KAccounts6)
BuildRequires:  PackageKit-Qt6-devel
BuildRequires:  libcanberra-devel
BuildRequires:  boost-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  SDL2-devel
BuildRequires:  chrpath
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(libwacom)

BuildRequires:  xdg-user-dirs

# xorg-x11 doesn't have hw_server and disable for s390/s390x
%ifnarch s390 s390x
# KCM touchpad has been merged to plasma-desktop in 5.3
Provides:       kcm_touchpad = %{version}-%{release}
Obsoletes:      kcm_touchpad < 5.3.0
# for xserver-properties
BuildRequires:  xorg-x11-server-devel
Requires:       kf6-kded

# for kcm_keyboard
BuildRequires:  pkgconfig(libudev)
Requires:       iso-codes

# for kcm_input, kcm_touchpad
BuildRequires:  pkgconfig(xorg-evdev)
BuildRequires:  pkgconfig(xorg-libinput)

%endif

# kcm_users
Requires:       accountsservice
# kcm_clock
Requires:       qt6-qtlocation%{?_isa}

# Desktop
Requires:       plasma-workspace

# xdg-utils integration
Requires:       xdg-utils >= 1.2.0~
Requires:       kde-cli-tools

# Qt Integration (brings in Breeze)
Requires:       plasma-integration

# Install systemsettings, full set of KIO slaves and write() notifications
Requires:       plasma-systemsettings
Requires:       kio-extras
Requires:       kwrited

# Install KWin
Requires:       kwin

# kickoff -> edit applications (#1229393)
Requires:       kmenuedit

BuildRequires:  cmake(KF6Kirigami)
Requires:       kf6-kirigami%{?_isa}
BuildRequires:  cmake(KF6KirigamiAddons)
Requires:       kf6-kirigami-addons%{?_isa}
BuildRequires:  kf6-qqc2-desktop-style
Requires:       kf6-qqc2-desktop-style%{?_isa}
BuildRequires:  kpipewire
Requires:       kpipewire%{?_isa}
BuildRequires:  signon-plugin-oauth2-devel
Requires:       signon-plugin-oauth2%{?_isa}

# applets/kickoff/KickoffSingleton.qml unconditionally imports org.kde.plasma.plasma5support
Requires:       qt6qml(org.kde.plasma.plasma5support)

# for kimpanel-ibus-panel and kimpanel-ibus-panel-launcher
Recommends: ibus

# for drawing tablet support
Recommends: udev-hid-bpf-stable

# Virtual provides for plasma-workspace
Provides:       plasmashell(desktop) = %{version}-%{release}
Provides:       plasmashell = %{version}-%{release}

Obsoletes:      kde-workspace < 5.0.0-1

Obsoletes:      kactivities-workspace < 5.6.0
Provides:       kactivities-workspace = %{version}-%{release}

Obsoletes:      plasma-user-manager < 5.19.50
Provides:       plasma-user-manager = %{version}-%{release}

# kimpanel moved here from kdeplasma-addons-5.5.x
Conflicts:      kdeplasma-addons < 5.6.0

# kcm_activities.mo moved here (#1325724)
Conflicts:      kde-l10n < 15.12.3-4

# See https://pagure.io/fedora-kde/SIG/issue/455 for more information
Conflicts:      kde-settings < 39.1-7

%description
%{summary}.

%package        kimpanel-scim
Summary:        SCIM backend for kimpanel
Requires:       %{name} = %{version}-%{release}
%description    kimpanel-scim
A backend for the kimpanel panel icon for input methods using the SCIM input
method framework.

%package        doc
Summary:        Documentation and user manuals for %{name}
# when conflicting HTML docs were removed
Conflicts:      kcm_colors < 1:4.11.16-10
# when conflicting HTML docs were removed
Conflicts:      kde-runtime-docs < 17.08.3-6
# when made noarch
Obsoletes: plasma-desktop-doc < 5.3.1-2
BuildArch: noarch
%description    doc
%{summary}.


%package -n sddm-breeze
Summary:        SDDM breeze theme
Requires:       kde-settings-sddm
# upgrade path, when sddm-breeze was split out
Obsoletes: plasma-workspace < 5.3.2-8
# theme files from breeze plasma
Requires:       libplasma
# QML imports:
# QtQuick.VirtualKeyboard
Requires:       qt6-qtvirtualkeyboard
# QML imports:
# org.kde.plasma.breeze.components
# org.kde.plasma.*
# The dependency is with 3 version numbers due to upstream occasional respins containing an etra number (i.e: 6.0.5.1)
Requires:       plasma-workspace >= %{maj_ver_kf6}.%{min_ver_kf6}
# /usr/share/backgrounds/default.{jxl,png}
Requires:       desktop-backgrounds-compat
# for jxl support
Requires:       kf6-kimageformats
BuildArch: noarch

%description -n sddm-breeze
%{summary}.


%prep
%autosetup -a 20 -p1


%build
%cmake_kf6 \
%ifarch s390 s390x
    -DBUILD_KCM_MOUSE_X11=OFF \
    -DBUILD_KCM_TOUCHPAD_X11=OFF
%endif

%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --with-html --all-name

grep "%{_kf6_docdir}" %{name}.lang > %{name}-doc.lang
cat  %{name}.lang %{name}-doc.lang | sort | uniq -u > plasmadesktop6.lang

# make fedora-breeze sddm theme variant.
cp -alf %{buildroot}%{_datadir}/sddm/themes/breeze/ \
        %{buildroot}%{_datadir}/sddm/themes/01-breeze-fedora
# replace items
install -m644 -p breeze-fedora/* \
        %{buildroot}%{_datadir}/sddm/themes/01-breeze-fedora/
# Set Fedora background
bg_file_ext="jxl"
if [ -f "/usr/share/backgrounds/default.png" ]; then
bg_file_ext="png"
fi
sed -i -e "s|^background=.*$|background=/usr/share/backgrounds/default.${bg_file_ext}|g" %{buildroot}%{_datadir}/sddm/themes/01-breeze-fedora/theme.conf
# Set Fedora distro vendor logo
sed -i -e 's|^showlogo=.*$|showlogo=shown|g' %{buildroot}%{_datadir}/sddm/themes/01-breeze-fedora/theme.conf
sed -i -e 's|^logo=.*$|logo=%{_datadir}/pixmaps/fedora_whitelogo.svg|g' %{buildroot}%{_datadir}/sddm/themes/01-breeze-fedora/theme.conf


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/kcm_{keyboard,access,clock,splashscreen,landingpage,keys,smserver,desktoppaths,gamecontroller,activities,recentFiles,kded,krunnersettings,plasmasearch,qtquicksettings,tablet,touchscreen,workspace,baloofile,solid_actions,mouse,touchpad}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/kcmspellchecking.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.knetattach.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.kde.plasma.emojier.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/kaccess.desktop

%files -f plasmadesktop6.lang
%license LICENSES
%{_bindir}/kaccess
%{_bindir}/knetattach
%{_bindir}/solid-action-desktop-gen
%{_bindir}/plasma-emojier
%{_bindir}/tastenbrett
%{_bindir}/krunner-plugininstaller
%{_kf6_libexecdir}/kauth/kcmdatetimehelper
%{_libexecdir}/kimpanel-ibus-panel
%{_libexecdir}/kimpanel-ibus-panel-launcher
%{_kf6_qmldir}/org/kde/plasma/private
%{_kf6_qtplugindir}/attica_kde.so
%{_kf6_qtplugindir}/plasma/kcms/desktop/kcm_krunnersettings.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/*.so
%{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/*.so
%{_kf6_qtplugindir}/plasma/kcminit/kcm_touchpad_init.so
%{_kf6_plugindir}/kded/*.so
%{_kf6_plugindir}/krunner/krunner*.so
%{_kf6_qmldir}/org/kde/plasma/activityswitcher
%{_kf6_qmldir}/org/kde/plasma/emoji/
%{_kf6_qmldir}/org/kde/private/desktopcontainment/*
%{_kf6_datadir}/plasma/*
%{_kf6_datadir}/applications/kde-mimeapps.list
%ifnarch s390 s390x
# kcminput
%{_kf6_bindir}/kapplymousetheme
%{_kf6_bindir}/kcm-touchpad-list-devices
%endif
%{_kf6_datadir}/kcmmouse/
%{_kf6_qtplugindir}/plasma/kcminit/kcm_mouse_init.so
%{_datadir}/config.kcfg/*.kcfg
%{_datadir}/kglobalaccel/org.kde.plasma.emojier.desktop
%{_datadir}/kglobalaccel/org.kde.touchpadshortcuts.desktop
%{_datadir}/qlogging-categories6/*.categories
%{_kf6_datadir}/dbus-1/interfaces/org.kde.touchpad.xml
%{_kf6_datadir}/kcmkeys
%{_kf6_datadir}/knsrcfiles/
%{_kf6_datadir}/kcmsolidactions/
%{_kf6_datadir}/solid/devices/*.desktop
%{_kf6_datadir}/dbus-1/system.d/*.conf
%{_kf6_datadir}/knotifications6/*.notifyrc
%{_datadir}/icons/hicolor/*/*/*
%{_kf6_metainfodir}/*.xml
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmclock.policy
%{_sysconfdir}/xdg/autostart/*.desktop
%{_kf6_datadir}/accounts/providers/kde/*.provider
%{_kf6_datadir}/accounts/services/kde/*.service
%{_kf6_datadir}/kcm_recentFiles/workspace/settings/qml/recentFiles/ExcludedApplicationView.qml
# How to include these in the .lang file?
%{_kf6_datadir}/locale/sr/LC_SCRIPTS/kfontinst/kfontinst.js
%{_kf6_datadir}/locale/sr@ijekavian/LC_SCRIPTS/kfontinst/kfontinst.js
%{_kf6_datadir}/locale/sr@ijekavianlatin/LC_SCRIPTS/kfontinst/kfontinst.js
%{_kf6_datadir}/locale/sr@latin/LC_SCRIPTS/kfontinst/kfontinst.js
%{_userunitdir}/plasma-kaccess.service
%{_libdir}/libkglobalaccelmodel.so.6
%{_libdir}/libkglobalaccelmodel.so.%{version}
%{_kf6_qtplugindir}/plasma/applets/org.kde.*.so


%files -n sddm-breeze
%{_datadir}/sddm/themes/breeze/
%{_datadir}/sddm/themes/01-breeze-fedora/


%if 0%{?scim}
%files kimpanel-scim
%{_libexecdir}/kimpanel-scim-panel
%endif

%files doc -f %{name}-doc.lang


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
