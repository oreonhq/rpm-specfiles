%global source0_hash 9c3ad4febe1a92bbec5ad6e2770dc968b810fdafcd08e300c6f8a9fcd510bca3

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    ksirk
Summary: Conquer-the-world strategy game
Version: 25.12.3
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://invent.kde.org/games/%{name}

%global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstreamable patches

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Wallet)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)

BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: libkdegames-devel >= %{majmin_ver}
BuildRequires: libkdegames-private-devel
BuildRequires: cmake(Phonon4Qt6)
BuildRequires: cmake(Qca-qt6)

BuildRequires: zlib-devel

Requires: qca-qt6-ossl%{?_isa}

Conflicts: kde-l10n < 17.08.3-2

%description
The goal of KSirk is to conquer the World. It is done by attacking your
neighbors with your armies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

## unpackaged files
rm -fv %{buildroot}%{_kf6_libdir}/libiris_ksirk.a

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%license COPYING*
%{_kf6_bindir}/%{name}*
%{_kf6_datadir}/qlogging-categories6/%{name}*
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/applications/org.kde.%{name}skineditor.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/%{name}*/
%{_kf6_datadir}/config.kcfg/%{name}*
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}*
#%%{_kf6_datadir}/kxmlgui6/%{name}*/
%{_kf6_datadir}/knsrcfiles/%{name}.knsrc

%changelog
%autochangelog
