
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:          qrca
Version:       25.12.3
Release:	2%{?dist}
License:       CC0-1.0 AND BSD-3-Clause AND BSD-2-Clause AND GPL-2.0-or-later AND LGPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.1-or-later
Summary:       QR code scanner for KDE Plasma
URL:           https://apps.kde.org/%{name}/

Source0:       https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Multimedia)

BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Contacts)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Prison)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6NetworkManagerQt)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6KirigamiAddons)

# Qml Imports
Requires: qt6qml(org.kde.config)
Requires: qt6qml(org.kde.kirigami)
Requires: qt6qml(org.kde.kirigamiaddons.formcard)
Requires: qt6qml(org.kde.prison)

%description
Qrca is a simple application for Plasma Desktop
and Plasma Mobile that lets you scan many barcode
formats and create your own QR code images.

%prep
%autosetup -p1

%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/qrca
%{_kf6_datadir}/applications/org.kde.qrca*.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.qrca.svg
%{_kf6_metainfodir}/org.kde.qrca.appdata.xml

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
