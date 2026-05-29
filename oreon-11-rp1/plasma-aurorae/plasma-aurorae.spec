%global source0_hash none

%define base_name aurorae

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    plasma-%{base_name}
Version: 6.6.5
Release: 1%{?dist}
Summary: Window decoration engine for KWin (Aurorae)

License: CC0-1.0 AND GPL-2.0-or-later AND MIT
URL:     https://invent.kde.org/plasma/%{base_name}.git

Source0:        https://download.kde.org/%{stable_kf6}/plasma/6.6.5/aurorae-6.6.5.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  ninja-build

BuildRequires:  cmake(KDecoration3)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  kf6-kconfig-devel
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6Widgets)

Requires:       kf6-filesystem
Requires:       kwin%{?_isa}
# kwin Requires: aurorae%%{?_isa}; this subpackage name is plasma-aurorae upstream
Provides:       aurorae = %{version}-%{release}
Provides:       aurorae%{?_isa} = %{version}-%{release}

%description
Aurorae is a window decoration engine for KWin. It supports QML-based
decoration themes and ships the Plastik Aurorae theme.


%package        devel
Summary:        CMake files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Development files (CMake package config) for Aurorae.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{base_name}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{base_name} --with-qt --all-name


%files -f %{base_name}.lang
%license LICENSES/*
%{_kf6_qtplugindir}/org.kde.kdecoration3.kcm/kcm_auroraedecoration.so
%{_kf6_qtplugindir}/org.kde.kdecoration3/org.kde.kwin.aurorae.so
%{_kf6_qtplugindir}/org.kde.kdecoration3/org.kde.kwin.aurorae.v2.so
%{_kf6_qmldir}/org/kde/kwin/decoration/
%{_kf6_qmldir}/org/kde/kwin/decorations/plastik/
%{_libexecdir}/plasma-apply-aurorae
%{_kf6_datadir}/knsrcfiles/aurorae.knsrc
%{_kf6_datadir}/kwin/aurorae/
%{_kf6_datadir}/kwin/decorations/kwin4_decoration_qml_plastik/

%files devel
%{_kf6_libdir}/cmake/Aurorae/


%changelog
* Mon May 25 2026 Brandon Lester <boostyconnect@oreonproject.org> - 6.6.5-1
- Update to KDE Plasma 6.6.5

* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-1
- Add Plasma Aurorae window decoration engine for KWin
