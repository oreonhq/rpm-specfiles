%global source0_hash ca00c01a636d0a636dd11926dd6a8a018b2018c3877b445eec3cc1617b7f0a69

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kigo
Summary: Go Board game
Version: 25.12.3
Release: 1%{?dist}

# KDE e.V. may determine that future GPL versions are accepted
# Automatically converted from old format: (GPLv2 or GPLv3) and GFDL - review is highly recommended.
License: (GPL-2.0-only OR GPL-3.0-only) AND LicenseRef-Callaway-GFDL
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
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6IconThemes)

%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires: libkdegames-devel >= %{majmin_ver}
BuildRequires: libkdegames-private-devel

BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Svg)

# https://bugzilla.redhat.com/564496
Requires: gnugo

%description
Go is a strategic board game for two players. It is also known as
igo (Japanese), weiqi or wei ch'i (Chinese) or baduk (Korean).
Go is noted for being rich in strategic complexity despite its
simple rules.
The game is played by two players who alternately place black and
white stones (playing pieces, now usually made of glass or plastic)
on the vacant intersections of a grid of 19×19 lines (9x9 or 13x13
lines for easier flavors).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%cmake_kf6

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%license LICENSES/*
%doc README
%{_kf6_bindir}/%{name}*
%{_kf6_datadir}/qlogging-categories6/%{name}*
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/*/*
#{_kf6_datadir}/kxmlgui5/%{name}/
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/config.kcfg/%{name}.kcfg
%{_kf6_datadir}/knsrcfiles/%{name}*.knsrc

%changelog
%autochangelog
