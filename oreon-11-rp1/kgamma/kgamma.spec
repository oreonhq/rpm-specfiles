%global source0_hash a7d3df14e5e016399e30e06923c0478a2c40a3a915e06abf070bd97e9381f1a3

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kgamma
Summary: A monitor calibration tool
Epoch:   1
Version: 6.6.4
Release: 1%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later
URL:     https://invent.kde.org/%{name}

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

BuildRequires: gcc gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KCMUtils)

BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Qml)
BuildRequires: pkgconfig(Qt6Widgets)

BuildRequires: pkgconfig(xxf86vm)

# when split occurred
Conflicts: kdegraphics < 7:4.6.95-10

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang kcmkgamma --all-name --with-html

%files -f kcmkgamma.lang
%doc ChangeLog
%license LICENSES/*
%{_datadir}/applications/kcm_kgamma.desktop
%{_kf6_datadir}/kgamma/
%{_qt6_plugindir}/plasma/kcminit/kcm_kgamma_init.so
%{_qt6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kgamma.so

%changelog
%autochangelog
