%global source0_hash 5150d3038c6d09453d2792219476894b719d51a1b8ed6e5eefdc2086f7e39370
ExcludeArch: %{ix86}
Name:    bomber
Summary:        Arcade bombing game
Version: 25.12.3
Release:        1%{?dist}
License: LGPL-2.0-or-later AND GFDL-1.2-or-later
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
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kconfigwidgets-devel
BuildRequires:  kf6-kdbusaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-kxmlgui-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libkdegames-devel
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(phonon4qt6)
# /oreon:deps
%description
Bomber is a single player arcade game. The player is invading various
cities in a plane that is decreasing in height. The goal of the game is
to destroy all the buildings and advance to the next level. Each level
gets a harder by increasing the speed of the plane and the height of the
buildings.

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
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
