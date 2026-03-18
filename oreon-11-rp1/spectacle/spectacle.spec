# For direct library dependencies
%if "%{__isa_bits}" == "64"
%global lib64_suffix ()(64bit)
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    spectacle
Summary: Screenshot capture utility
Epoch:   1
Version: 6.6.2
Release: 2%{?dist}

# Automatically converted from old format: GPLv2 - review is highly recommended.
License: GPL-2.0-only
URL:     https://www.kde.org/applications/graphics/spectacle/

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: https://download.kde.org/%{stable}/plasma/%{maj_ver_kf6}.%{min_ver_kf6}.%{bug_ver_kf6}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable}/plasma/%{maj_ver_kf6}.%{min_ver_kf6}.%{bug_ver_kf6}/%{name}-%{version}.tar.xz.sig

## upstream patches
# Fix crash on quit with a quickly selected region
# https://invent.kde.org/plasma/spectacle/-/commit/e5f1a6ef499d4569db8dc2ddd0a282caa6cf7c60
Patch0: e5f1a6ef499d4569db8dc2ddd0a282caa6cf7c60.patch

## downstream patches
### Local workaround while waiting for a better fix
### Cf. https://bugs.kde.org/show_bug.cgi?id=516162
Patch1001: spectacle-6.6.0-tesseract-fedora-centos-libs.patch

%global majmin %(echo %{version} | cut -d. -f1,2)

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6KirigamiPlatform)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Purpose)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6Prison)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KQuickImageEditor)

BuildRequires: cmake(KPipeWire)
BuildRequires: cmake(LayerShellQt)
BuildRequires: cmake(PlasmaWaylandProtocols)

BuildRequires: qt6-qtbase-private-devel
BuildRequires: cmake(OpenCV)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6QWebpPlugin)
BuildRequires: cmake(ZXing)

BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-util)
BuildRequires: pkgconfig(xcb-xfixes)

# for systemd-related macros
BuildRequires:  systemd-devel

# Animated tray icon: https://pagure.io/fedora-kde/SIG/issue/601
Recommends:     qt6-qtimageformats%{?_isa}
# 6.6.0: Scanning capabilities
# Cf. https://bugs.kde.org/show_bug.cgi?id=516162
Recommends:     (libtesseract.so.5.5%{?lib64_suffix} or libtesseract.so.5.3.4%{?lib64_suffix})

# f26+ upgrade path
%if 0%{?fedora} > 25
Obsoletes: ksnapshot <= 15.08.3
%endif

# translations moved here
Conflicts: kde-l10n < 17.03

%description
%{summary}.


%prep
%autosetup -p1 -n %{name}-%{maj_ver_kf6}.%{min_ver_kf6}.%{bug_ver_kf6}


%build
%cmake_kf6 -DKDE_INSTALL_SYSTEMDUSERUNITDIR=%{_userunitdir}
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html --with-man


%check
# [6.3.1.2] Bypassed. Reason:
# FAILED: • tag-invalid           : <release> versions are not in order [6.3.0 before 24.12.1]
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.spectacle.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.spectacle.desktop

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/spectacle
%{_kf6_datadir}/man/man1/spectacle.1*
%{_kf6_metainfodir}/org.kde.spectacle.appdata.xml
%{_kf6_datadir}/applications/org.kde.spectacle.desktop
%{_kf6_datadir}/dbus-1/interfaces/org.kde.Spectacle.xml
%{_kf6_datadir}/dbus-1/services/org.kde.Spectacle.service
%{_kf6_datadir}/dbus-1/services/org.kde.spectacle.service
%{_kf6_datadir}/icons/hicolor/*/apps/spectacle.*
%{_kf6_datadir}/kglobalaccel/org.kde.spectacle.desktop
%{_kf6_datadir}/knotifications6/spectacle.notifyrc
%{_kf6_datadir}/qlogging-categories6/%{name}*
%{_kf6_libdir}/kconf_update_bin/spectacle*
%{_kf6_datadir}/kconf_update/spectacle*
%{_userunitdir}/app-org.kde.spectacle.service


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-2
- Prepare for Oreon 11 (RP1)
