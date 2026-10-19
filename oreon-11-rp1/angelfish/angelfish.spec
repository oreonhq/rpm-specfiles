%global source0_hash 1283ea5dda7715267b8f66ed0bea214f69db80cbe010ac89b87962351f52f099
%global stable_kf6 stable
%global _ldflags %{?_ldflags} -lavformat
%bcond adblock 0
Name:           angelfish
Version:        26.04.3
Release:        1%{?dist}
Summary:        Plasma Mobile minimal web browser
License:        MIT AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
URL:            https://invent.kde.org/network/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
%if %{with adblock}
%endif
Requires:       hicolor-icon-theme
Requires:       kf6-kirigami%{?_isa}
Requires:       kf6-kirigami-addons%{?_isa}
Requires:       kf6-purpose%{?_isa}
Requires:       kf6-qqc2-desktop-style%{?_isa}
Requires:       qt6-qt5compat%{?_isa}
Requires:       qt6-qtwayland%{?_isa}
Requires:       qt6-qtwebengine%{?_isa}
# oreon:deps
BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  cmake(FutureSQL6)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(QCoro6Core)
BuildRequires:  cmake(QCoro6Quick)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6QmlPrivate)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineQuick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  ffmpeg-free-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# /oreon:deps
%description
Web browser for mobile devices with Plasma integration

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version} -p1
%if %{with adblock}
%endif

%if %{with adblock}
%build

%cmake_kf6
%cmake_build
%if %{with adblock}
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%endif
%install
%cmake_install
%find_lang %{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
