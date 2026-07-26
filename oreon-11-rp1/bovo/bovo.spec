%global source0_hash b5ab38158518353360ce95de017236d3a235afe499fe9fd95a692afead80ae15

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    bovo
Summary: Five in a row game
Version: 25.12.3
Release: 1%{?dist}

# code GPLv2+, docs GFDL
License: GPL-2.0-or-later AND GFDL-1.2-or-later
URL:     https://cgit.kde.org/%{name}.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kdeclarative-devel
BuildRequires: kf6-knewstuff-devel
BuildRequires: kf6-kxmlgui-devel
BuildRequires: kf6-knewstuff-devel
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: pkgconfig(Qt6Widgets) pkgconfig(Qt6Qml) pkgconfig(Qt6Quick) pkgconfig(Qt6QuickWidgets) pkgconfig(Qt6Svg) pkgconfig(Qt6Concurrent)
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires: libkdegames-devel >= %{majmin_ver}
%if 0%{?fedora} > 19
BuildRequires: libappstream-glib
%endif

%description
Bovo is a five-in-a-row game for two players, where the opponents alternate
in placing their respective pictogram on the game board. The aim of this
game is to connect five of your own pieces in an unbroken row vertically,
horizontally or diagonally.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop ||:

%files -f %{name}.lang
%doc AUTHORS
%license COPYING*
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/%{name}/

%changelog
%autochangelog
