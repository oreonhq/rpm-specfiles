
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:          flatpak-kcm
Version:       6.6.2
Release:	2%{?dist}
License:       BSD-2-Clause and BSD-3-Clause and CC0-1.0 and GPL-2.0-or-later
Summary:       Flatpak Permissions Management KCM
Url:           https://invent.kde.org/plasma/flatpak-kcm

Source0:       https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:       https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils

BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6IconThemes)

BuildRequires: cmake(Qt6Svg)

BuildRequires: pkgconfig(flatpak)

%description
%{summary}.

%prep
%autosetup -p1

%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
desktop-file-validate %{buildroot}%{_datadir}/applications/kcm_app-permissions.desktop
%find_lang kcm_app-permissions

%files -f kcm_app-permissions.lang
%license LICENSES/*
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_app-permissions.so
%{_kf6_datadir}/applications/kcm_app-permissions.desktop

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
