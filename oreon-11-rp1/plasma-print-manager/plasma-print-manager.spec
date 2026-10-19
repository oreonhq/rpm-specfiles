%global source1_hash 6871f701fb25c268fe3e005752a739f83f1bf0dbb402e5724474d28fd4abdf4b
%global source0_hash f7ed99b3afaf8ea1faa5c0649f3a704197ac992fcfa5dfc24622e5cf2cb85a4b
%global stable_kf6 stable
%global  base_name print-manager
ExcludeArch: %{ix86}
Name:    plasma-print-manager
Summary:        Printer management for KDE
Version:        23.08.5
Release:        1%{?dist}
License: BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{base_name}
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{base_name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{base_name}-%{version}.tar.xz.sig
Obsoletes:      kde-print-manager < 1:%{version}-%{release}
Provides:       kde-print-manager = 1:%{version}-%{release}
Requires: plasma-workspace
Requires: kf6-kitemmodels%{?_isa}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: cups
Requires: system-config-printer-libs
Recommends: samba-client
# oreon:deps
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami2)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(packagekitqt6)
BuildRequires:  cups
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-kirigami-addons
BuildRequires:  kf6-kitemmodels
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  samba-client
# /oreon:deps
%description
Printer management for KDE.

%package  libs
Summary:  Runtime files for %{name}
Requires: %{name} = %{version}-%{release}
Obsoletes:      kde-print-manager-libs < 1:%{version}-%{release}
Provides:       kde-print-manager-libs = 1:%{version}-%{release}
%description libs
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{base_name}-%{version}

%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.ConfigurePrinter.desktop
%files -f %{oreon_filedir}/main.list
%files -n plasma-print-manager-libs -f %{oreon_filedir}/plasma-print-manager-libs.list

%changelog

%autochangelog
