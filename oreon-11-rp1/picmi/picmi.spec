%global source0_hash 0ade2dc87a68fd091c550b0e971f02c1642d4f702819e3302d2ae6aab9c6b7b5

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    picmi
Summary: A nonogram logic game
Version: 25.12.3
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
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
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6Crash)

BuildRequires: libappstream-glib
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires: libkdegames-devel >= %{majmin_ver}
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtdeclarative-devel
BuildRequires: qt6-qtsvg-devel

%description
Picmi is a single player puzzle game.  The object of the game is to
color cells according to numbers given at the side of the board.

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
%doc README
%{_kf6_bindir}/%{name}
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/qlogging-categories6/%{name}*

%changelog
%autochangelog
