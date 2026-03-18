Name:          plasma-camera
Version:       2.1.1
Release:       4%{?dist}
License:       BSD-3-Clause AND GPL-2.0-or-later AND CC0-1.0 AND GPL-3.0-or-later
Summary:       Camera application for Plasma Mobile
URL:           https://apps.kde.org/plasma.camera/

Source0:       https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

# libcamera does not currently build on these architectures
ExcludeArch: s390x ppc64le

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
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Sensors)
BuildRequires: cmake(Qt6Multimedia)

BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Config)

BuildRequires: pkgconfig(libcamera)
BuildRequires: pkgconfig(exiv2)

%description
%{summary}.
It supports different resolutions, different white balance modes and
switching between different camera devices.


%prep
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-man --with-qt --all-name

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.plasma.camera.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%{_bindir}/plasma-camera
%{_kf6_datadir}/applications/org.kde.plasma.camera.desktop
%{_metainfodir}/org.kde.plasma.camera.appdata.xml

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.1-4
- Prepare for Oreon 11 (RP1)
