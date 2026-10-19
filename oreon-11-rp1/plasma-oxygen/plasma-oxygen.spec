%global source1_hash 594b9e41137687d4ed40712a6df3dca9b76cb85b5bb24e16e9456d7967bc1ebf
%global source0_hash ffa4b969197f6e09a6ee4f468925e67223666d761ee9801a8ea612e09b756037
%global stable_kf6 stable
%global         base_name oxygen
%bcond kf5 %[%{undefined rhel} || 0%{?rhel} < 10]
ExcludeArch: %{ix86}
Name:    plasma-%{base_name}
Version:        6.7.5
Release:        1%{?dist}
Summary:        Plasma and Qt widget style and window decorations for Plasma
License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:     https://invent.kde.org/plasma/%{base_name}
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz.sig
%if %{with kf5}
Requires:       (%{name}-qt5 if qt5-qtbase-gui)
%endif
Requires:       kf6-filesystem
Requires:       %{name}-qt6
Requires:       oxygen-cursor-themes >= %{version}
Requires:       oxygen-sound-theme
Requires:       oxygen-icon-theme
Obsoletes:      kwin-oxygen < 5.1.95-1
Obsoletes:      plasma-oxygen < 5.1.1-2
Conflicts:      plasma-desktop < 5.16.90
# oreon:deps
BuildRequires:  cmake(KDecoration3)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5FrameworkIntegration)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6FrameworkIntegration)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KirigamiPlatform)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf6-rpm-macros
BuildRequires:  libxcb-devel
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
%description
%{summary}.

%if %{with kf5}
%package        qt5
Summary:        Oxygen widget style for Qt 5
Obsoletes:      qt5-style-oxygen < %{version}-%{release}
Provides:       qt5-style-oxygen = %{version}-%{release}
%description    qt5
%{summary}.
%endif

%package        qt6
Summary:        Oxygen widget style for Qt 6
%description    qt6
%{summary}.

%package -n     oxygen-cursor-themes
Summary:        Oxygen cursor themes
BuildArch:      noarch
Obsoletes:      plasma-oxygen-common < 5.1.1-2
%description -n oxygen-cursor-themes
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
pushd qt6build
%cmake_install
popd
%if %{with kf5}
pushd qt5build
%cmake_install
popd
%endif
%find_lang oxygen --with-qt --all-name
%oreon_autofiles oxygen-cursor-themes usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n plasma-oxygen-qt5 -f %{oreon_filedir}/plasma-oxygen-qt5.list
%files -n plasma-oxygen-qt6 -f %{oreon_filedir}/plasma-oxygen-qt6.list
%files -n oxygen-cursor-themes -f %{oreon_filedir}/oxygen-cursor-themes.list

%changelog

%autochangelog
