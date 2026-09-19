%global source0_hash e9fce911e96eac14d379b336e89c3e1853a6b350dade865d14c14b769704ffbd

%global base_name    plymouth-kcm

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    plymouth-kcm
Summary: Plymouth configuration module for systemsettings
Version: 6.6.4
Release: 1%{?dist}

License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-or-later
URL:     https://invent.kde.org/plasma/%{base_name}

Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz.sig

## FIXME/TODO: document why this patch is needed, ideally work to make upstreamable
Patch1:         0001-fedora.patch

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  kf6-kcmutils
BuildRequires:  qt6-qtbase-devel
BuildRequires:  plymouth-devel

BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6NewStuffCore)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6KCMUtils)

Requires:   plymouth

%description
This is a System Settings configuration module for configuring the
plymouth splash screen.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{base_name}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang kcm_plymouth --all-name --with-html

%files -f kcm_plymouth.lang
%license LICENSES/*
%{_kf6_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmplymouth.conf
%{_datadir}/knsrcfiles/plymouth.knsrc
%{_bindir}/kplymouththemeinstaller
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_plymouth.so
%{_kf6_libexecdir}/kauth/plymouthhelper
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmplymouth.service
%{_datadir}/applications/kcm_plymouth.desktop
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmplymouth.policy

%changelog
%autochangelog
