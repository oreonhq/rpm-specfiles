
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    plasma-pa
Version: 6.6.2
Release: 1%{?dist}
Summary: Plasma applet for audio volume management using PulseAudio

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6PulseAudioQt)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6StatusNotifierItem)

BuildRequires:  cmake(Plasma)

BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  qt6-qtbase-devel

BuildRequires:  perl-generators

# runtime
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6ItemModels)
Requires: kf6-kirigami
Requires: kf6-kirigami-addons
Requires: kf6-kitemmodels

Requires: pulseaudio-daemon


%description
%{summary}.


%prep
%autosetup


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html
# Not clear why we would need this. Deleting
rm -fv %{buildroot}%{_kf6_libdir}/libplasma-volume.so


%files -f %{name}.lang
%license LICENSES/*
%{_kf6_qmldir}/org/kde/plasma/private/volume/
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_pulseaudio.so
%{_kf6_qtplugindir}/kf6/kded/audioshortcutsservice.so
%{_kf6_qtplugindir}/plasma/applets/org.kde.plasma.volume.so
%{_kf6_datadir}/applications/kcm_pulseaudio.desktop
%{_kf6_libdir}/libplasma-volume.so.6
%{_kf6_libdir}/libplasma-volume.so.%{version}
%{_kf6_datadir}/qlogging-categories6/plasmapa.categories

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
