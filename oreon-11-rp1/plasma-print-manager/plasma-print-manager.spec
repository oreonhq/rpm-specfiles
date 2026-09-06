%global source0_hash f7ed99b3afaf8ea1faa5c0649f3a704197ac992fcfa5dfc24622e5cf2cb85a4b

%global stable_kf6 stable


%global  base_name print-manager


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    plasma-print-manager
Summary: Printer management for KDE
Version:        23.08.5
Release: 1%{?dist}

License: BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{base_name}

Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{base_name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{base_name}-%{version}.tar.xz.sig

## upstream patches

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: kf6-kitemmodels
BuildRequires: kf6-kirigami-addons
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)

BuildRequires: qt6-qtbase-devel

BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6Qml)

BuildRequires: cmake(Plasma)
BuildRequires: cmake(KF6Declarative)

BuildRequires: cmake(packagekitqt6)

BuildRequires: cups-devel >= 1.5.0
# /usr/bin/smbspool (runtime dep, but checked-for at build-time)
BuildRequires: cups
BuildRequires: samba-client

# Renamed from kde-print-manager
Obsoletes:      kde-print-manager < 1:%{version}-%{release}
Provides:       kde-print-manager = 1:%{version}-%{release}

Requires: plasma-workspace
Requires: kf6-kitemmodels%{?_isa}

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# currently requires local cups for majority of proper function
Requires: cups
# required for the com.redhat.NewPrinterNotification D-Bus service
Requires: system-config-printer-libs
# /usr/bin/smbspool
Recommends: samba-client

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


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.ConfigurePrinter.desktop


%files -f %{name}.lang
%license LICENSES/*
%{_bindir}/configure-printer
%{_bindir}/plasma-print-queue
%{_kf6_qmldir}/org/kde/plasma/printmanager/
%{_kf6_datadir}/qlogging-categories6/pmlogs.categories
%{_kf6_datadir}/knotifications6/printmanager.notifyrc
%{_kf6_datadir}/applications/kcm_printer_manager.desktop
%{_kf6_datadir}/applications/org.kde.ConfigurePrinter.desktop
%{_kf6_datadir}/applications/org.kde.plasma.printqueue.desktop
%{_kf6_metainfodir}/org.kde.print-manager.metainfo.xml
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_printer_manager.so


%files libs
%{_libdir}/libkcups.so
%{_kf6_plugindir}/kded/printmanager.so
%{_kf6_qtplugindir}/plasma/applets/org.kde.plasma.printmanager.so

%changelog
%autochangelog
