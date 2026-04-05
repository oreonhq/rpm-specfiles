
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           qmlkonsole
Version:        25.12.3
Release:	2%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Summary:        Terminal app for Plasma Mobile
Url:            https://invent.kde.org/plasma-mobile/qmlkonsole
Source:         https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  appstream

BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Pty)
BuildRequires:  cmake(KF6WindowSystem)

Requires:       kf6-kirigami
Requires:       kf6-kirigami-addons
Recommends:     dejavu-fonts-all

%description
%{summary}.

%prep
%autosetup

%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%license LICENSES/GPL-2.0-or-later.txt
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/config.kcfg/terminalsettings.kcfg

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
