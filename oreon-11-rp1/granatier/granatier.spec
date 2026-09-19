%global source0_hash c5b8814ed4acad3e84edcddfaa9c7fdc380347e50e738c9116de42be07145c95

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    granatier
Summary: Place bombs to kill enemies and remove obstacles
Version: 25.12.3
Release: 1%{?dist}

License: GPL-2.0-or-later AND GFDL-1.2-or-later
URL:     https://invent.kde.org/games/%{name}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: kf6-kguiaddons-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kitemviews-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-knewstuff-devel
BuildRequires: kf6-knotifyconfig-devel
BuildRequires: kf6-kxmlgui-devel
BuildREquires: kf6-knewstuff-devel
BuildRequires: kf6-kwidgetsaddons-devel
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DocTools)

BuildRequires: pkgconfig(Qt6Widgets) pkgconfig(Qt6Svg)

%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires: libkdegames-devel >= %{majmin_ver}

%description
The object of Granatier is to run through an arena, using bombs to clear
out blocks and eliminate your opponents. Several bonuses and handicaps
are hidden underneath the blocks – these can either help or hinder your
progress.

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
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/qlogging-categories6/%{name}*
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/*/%{name}.*
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/config.kcfg/%{name}.kcfg

%changelog
%autochangelog
