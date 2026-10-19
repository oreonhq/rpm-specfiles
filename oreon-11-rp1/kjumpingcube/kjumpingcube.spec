%global source0_hash 519f68570fa0152470645caca846c888a348dd2bdefde1c07715ba91ddcb1490
ExcludeArch: %{ix86}
Name:    kjumpingcube
Summary:        Territory capture game
Version: 25.12.3
Release:        1%{?dist}
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://invent.kde.org/games/%{name}
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
# oreon:deps
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-kcompletion-devel
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kconfigwidgets-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kdbusaddons-devel
BuildRequires:  kf6-kdeclarative-devel
BuildRequires:  kf6-kdnssd-devel
BuildRequires:  kf6-kguiaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kiconthemes-devel
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-kitemmodels-devel
BuildRequires:  kf6-kitemviews-devel
BuildRequires:  kf6-kjobwidgets-devel
BuildRequires:  kf6-knewstuff-devel
BuildRequires:  kf6-knotifyconfig-devel
BuildRequires:  kf6-kservice-devel
BuildRequires:  kf6-kwidgetsaddons-devel
BuildRequires:  kf6-kwindowsystem-devel
BuildRequires:  kf6-kxmlgui-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libkdegames-devel
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(phonon4qt6)
# /oreon:deps
%description
KJumpingCube is a simple tactical game. You can play it against the computer
or a friend. The playing area consists of squares containing points. When the
game starts each square has only one point, and no owner. Players move by
clicking on either a vacant square or one of their own squares, thus
increasing the square’s point value by one. When a square’s value reaches
a maximum, the excess points are distributed around the neighboring squares,
taking over ownership of them. The winner is the player who ends up owning
all the squares.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop ||:
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
