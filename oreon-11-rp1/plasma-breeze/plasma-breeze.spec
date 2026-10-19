%global source1_hash 621eecf2e147f4fbd3f1413729e4822fa0ca7e8abb39626c45d53000d5bd28b4
%global source0_hash aa05c0c31c852ed5b137327e7798fd763a54c643875d5d8070625475e0af6976
%global stable_kf6 stable
%global  base_name breeze
%bcond_without kf5
Name:    plasma-breeze
Version:        6.7.5
Release:        1%{?dist}
Summary:        Artwork, styles and assets for the Breeze visual style for the Plasma Desktop
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND MIT
URL:     https://invent.kde.org/plasma/%{base_name}.git
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz.sig
%if %{with kf5}
Requires:       (%{name}-qt5 if qt5-qtbase-gui)
%endif
Requires:       %{name}-qt6
Provides:       %{name}-devel = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake(KDecoration3)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5FrameworkIntegration)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6FrameworkIntegration)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf6-rpm-macros
# /oreon:deps
%description
%{summary}.

%package        qt6
Summary:        Breeze application style for Qt6
Requires:       %{name}-common = %{version}-%{release}
%description    qt6
%{summary}.

%if %{with kf5}
%package        qt5
Summary:        Breeze application style for Qt5
Requires:       %{name}-common = %{version}-%{release}
%description    qt5
%{summary}.
%endif

%package        common
Summary:        Common files shared between Plasma 5 and Plasma 6 versions of the Breeze style
BuildArch:      noarch
%description    common
%{summary}.

%package -n     breeze-cursor-theme
Summary:        Breeze cursor theme
BuildArch:      noarch
Obsoletes:      breeze-icon-theme < 5.17.0
Provides:       breeze-cursor-themes = %{version}-%{release}
%description -n breeze-cursor-theme
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{base_name}-%{version} -p1

%build

mkdir -p qt6build
pushd qt6build
%cmake_kf6 -S .. -DBUILD_QT6=ON -DBUILD_QT5=OFF
%cmake_build
popd
%if %{with kf5}
mkdir -p qt5build
pushd qt5build
%cmake_kf5 -S .. -DBUILD_QT6=OFF -DBUILD_QT5=ON
%cmake_build
popd
%endif
%install
%if %{with kf5}
pushd qt5build
%cmake_install
popd
%endif
pushd qt6build
%cmake_install
popd
%find_lang breeze --all-name
%oreon_autofiles breeze-cursor-theme usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n plasma-breeze-qt6 -f %{oreon_filedir}/plasma-breeze-qt6.list
%files -n plasma-breeze-qt5 -f %{oreon_filedir}/plasma-breeze-qt5.list
%files -n plasma-breeze-common -f %{oreon_filedir}/plasma-breeze-common.list
%files -n breeze-cursor-theme -f %{oreon_filedir}/breeze-cursor-theme.list

%changelog

%autochangelog
