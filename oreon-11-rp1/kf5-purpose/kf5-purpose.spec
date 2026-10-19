%global source0_hash 62d66c1a32b614971a52d385be1ea5d218a95b9e65a0b547b7913238c38d1dbc
%global  framework purpose
Name:    kf5-purpose
Summary:        Framework for providing abstractions to get the developer's purposes fulfilled
Version: 5.116.0
Release:        1%{?dist}
License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
Obsoletes:  kf5-purpose-twitter < 5.68.0
%global __provides_exclude_from ^(%{_kf5_qtplugindir}/.*\\.so)$
Requires: kf5-bluez-qt >= %{majmin}
# oreon:deps
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kirigami2-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
# /oreon:deps
%description
Purpose offers the possibility to create integrate services and actions on
any application without having to implement them specifically. Purpose will
offer them mechanisms to list the different alternatives to execute given the
requested action type and will facilitate components so that all the plugins
can receive all the information they need.

%package  devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: cmake(KF5CoreAddons)
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build

%cmake_kf5
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name
rm -fv %{buildroot}%{_datadir}/icons/hicolor/*/actions/kipiplugin_youtube.png
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-purpose-devel -f %{oreon_filedir}/kf5-purpose-devel.list

%changelog

%autochangelog
