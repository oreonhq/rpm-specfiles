%global kf6_min_version 5.240.0


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           kalk
Version:        25.12.3
Release:	2%{?dist}
License:        BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND GPL-3.0-or-later
Summary:        %{name} is a convergent calculator for Plasma.
Url:            https://apps.kde.org/%{name}/
Source:         https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires: cmake(KF6Config) >= %{kf6_min_version}
BuildRequires: cmake(KF6I18n) >= %{kf6_min_version}
BuildRequires: cmake(KF6CoreAddons) >= %{kf6_min_version}
BuildRequires: cmake(KF6UnitConversion) >= %{kf6_min_version}
BuildRequires: cmake(KF6Kirigami) >= %{kf6_min_version}

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: pkgconfig(libqalculate) > 4.7.0

# QML module dependencies
Requires:  kf6-kcoreaddons%{?_isa}
Requires:  kf6-kirigami%{?_isa}
Requires:  kf6-kirigami-addons%{?_isa}
Requires:  kf6-qqc2-desktop-style%{?_isa}
Requires:  kf6-sonnet%{?_isa}
Requires:  qt6-qt5compat%{?_isa}

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
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

%files -f %{name}.lang
%{_kf6_bindir}/%{name}

%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg

%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

%license LICENSES/*

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
