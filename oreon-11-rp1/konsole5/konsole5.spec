%global source0_hash c6fb20753ac27a46bce62e31f7b105b6b99497035830b34a7bba1bc60260c1ca

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

%global  base_name konsole

Name:    konsole5
Summary: KDE Terminal emulator
Version: 23.08.5
Release: 7%{?dist}

# sources: MIT and LGPLv2 and LGPLv2+ and GPLv2+
License: GPL-2.0-only AND GFDL-1.1-or-later
URL:     http://www.kde.org/applications/system/konsole/
#URL:    http://konsole.kde.org/

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: https://download.kde.org/%{stable}/release-service/%{version}/src/%{base_name}-%{version}.tar.xz

## upstreamable patches

## upstream patches
# 21.08 branch fixes

## downstream patches
Patch200: konsole-history_location_default.patch
# custom konsolerc that sets default to cache as well
Source10: konsolerc

Obsoletes: konsole < 14.12
Provides:  konsole = %{version}-%{release}

%global maj_ver %(echo %{version} | cut -d. -f1)

BuildRequires: make
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(zlib)

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(KF5Bookmarks)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5GlobalAccel)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5NewStuff)
BuildRequires: cmake(KF5NewStuffCore)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5NotifyConfig)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5Pty)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5XmlGui)

BuildRequires: libappstream-glib
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: libicu-devel

%if 0%{?tests}
BuildRequires: appstream
BuildRequires: xorg-x11-server-Xvfb dbus-x11
%endif

# translations moved here
Conflicts: kde-l10n < 17.03

Requires: %{name}-part%{?_isa} = %{version}-%{release}
Requires: keditbookmarks

%description
%{summary}.

%package part
Summary: Konsole5 kpart plugin
%description part
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{base_name}-%{version} -p1

%build
%cmake_kf5 \
  %{?flatpak:-DINSTALL_ICONS:BOOL=ON} \
  %{?tests:-DBUILD_TESTING:BOOL=ON}

%cmake_build

%install
%cmake_install

install -m644 -p -D %{SOURCE10} %{buildroot}%{_kf5_sysconfdir}/xdg/konsolerc

%find_lang konsole --with-html

# add startupWMClass=konsole if not already present
grep 'StartupWMClass=' %{buildroot}%{_kf5_datadir}/applications/org.kde.konsole.desktop >& /dev/null || \
desktop-file-edit --set-key=StartupWMClass --set-value=konsole %{buildroot}%{_kf5_datadir}/applications/org.kde.konsole.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.konsole.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.konsole.desktop
%if 0%{?tests}
test "$(xvfb-run -a %{_target_platform}/src/konsole --version)" = "konsole %{version}" ||:
export CTEST_OUTPUT_ON_FAILURE=1
DBUS_SESSION_BUS_ADDRESS=
xvfb-run -a \
make test -C %{_target_platform} ARGS="--output-on-failure --timeout 30" ||:
%endif

%files -f konsole.lang
%dir %{_kf5_datadir}/knsrcfiles/
%doc README*
%config(noreplace) %{_kf5_sysconfdir}/xdg/konsolerc
%{_kf5_datadir}/konsole/
%{_kf5_bindir}/konsole
%{_kf5_bindir}/konsoleprofile
%{_kf5_datadir}/applications/org.kde.konsole.desktop
%{_kf5_datadir}/kglobalaccel/org.kde.konsole.desktop
%{_kf5_datadir}/kconf_update/konsole.upd
%{_kf5_datadir}/kconf_update/konsole_add_hamburgermenu_to_toolbar.sh
%{_kf5_datadir}/kio/servicemenus/konsolerun.desktop
%{_kf5_datadir}/knotifications5/konsole.notifyrc
%{_kf5_datadir}/knsrcfiles/konsole.knsrc
%{_kf5_datadir}/kservicetypes5/terminalemulator.desktop
%{_kf5_datadir}/qlogging-categories5/konsole.*
%{_kf5_datadir}/zsh/site-functions/_konsole
%{_kf5_libdir}/kconf_update_bin/konsole_globalaccel
%{_kf5_libdir}/kconf_update_bin/konsole_show_menubar
%{_kf5_metainfodir}/org.kde.konsole.appdata.xml
%if 0%{?flatpak}
%{_kf5_datadir}/icons/hicolor/*/apps/utilities-terminal.*
%endif

%ldconfig_scriptlets part

%files part
%{_kf5_libdir}/libkonsoleapp.so.*
%{_kf5_libdir}/libkonsoleprivate.so.*
%{_kf5_qtplugindir}/konsolepart.so
%{_kf5_qtplugindir}/konsoleplugins/
%{_kf5_datadir}/kservices5/konsolepart.desktop

%changelog
%autochangelog
