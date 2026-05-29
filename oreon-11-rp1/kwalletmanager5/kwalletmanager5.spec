%global source0_hash none

%global  base_name kwalletmanager

# replace kde4-based kwalletmanager
%global kwalletmanager 1


# 
ExcludeArch: %{ix86}

Name:    kwalletmanager5
Summary: Manage KDE passwords
Version: 26.04.1
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://apps.kde.org/kwalletmanager5/
Source:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{base_name}-%{version}.tar.xz

# upstream patches

## upstreamable patches
# better/sane defaults (no autoclose mostly)
Patch1: kwalletmanager-15.12.1-defaults.patch

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6DBus)

%if ! 0%{?flatpak}
BuildRequires: cmake(KF6Auth)
%endif
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6StatusNotifierItem)

%if 0%{?kwalletmanager}
Obsoletes: kwalletmanager < 15.04.3-100
Provides:  kwalletmanager = %{version}-%{release}
%endif

%description
KDE Wallet Manager is a tool to manage the passwords on your KDE system.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{base_name}-%{version} -p1


%build
%cmake_kf6 %{?flatpak:-DENABLE_KAUTH=OFF}

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kwalletmanager.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/kwalletmanager5-kwalletd.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kwalletmanager5.appdata.xml


%files -f %{name}.lang
%license LICENSES/*
%{_datadir}/dbus-1/services/org.kde.kwalletmanager.service
%{_kf6_bindir}/kwalletmanager5
%{_kf6_datadir}/applications/kwalletmanager5-kwalletd.desktop
%{_kf6_datadir}/applications/org.kde.kwalletmanager.desktop
%{_kf6_datadir}/icons/hicolor/*/actions/wallet-*
%{_kf6_datadir}/icons/hicolor/*/apps/kwalletmanager*.*
%{_kf6_datadir}/qlogging-categories6/kwalletmanager*
%{_kf6_metainfodir}/org.kde.kwalletmanager5.appdata.xml
%if ! 0%{?flatpak}
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmkwallet5.service
%{_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmkwallet5.conf
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmkwallet5.policy
%{_kf6_libexecdir}/kauth/kcm_kwallet_helper5
%{_kf6_qtplugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kwallet5.so
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.04.1-1
- Import
