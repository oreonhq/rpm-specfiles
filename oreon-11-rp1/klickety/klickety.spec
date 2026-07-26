%global source0_hash c9f59671ef1f026f9780699e4e1572ee038494caebbf73cab05ee0bf15736faa

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    klickety
Summary: Destroy groups of blocks
Version: 25.12.3
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://invent.kde.org/games/%{name}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-kconfig-devel
BuildRequires:  kf6-kconfigwidgets-devel
BuildRequires:  kf6-kcoreaddons-devel
BuildRequires:  kf6-kdbusaddons-devel
BuildRequires:  kf6-kguiaddons-devel
BuildRequires:  kf6-ki18n-devel
BuildRequires:  kf6-kiconthemes-devel
BuildRequires:  kf6-kio-devel
BuildRequires:  kf6-knotifications-devel
BuildRequires:  kf6-knotifyconfig-devel
BuildRequires:  kf6-kwidgetsaddons-devel
BuildRequires:  kf6-kxmlgui-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)

BuildRequires:  pkgconfig(Qt6Gui) pkgconfig(Qt6Qml) pkgconfig(Qt6Quick)

%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires:  libkdegames-devel >= %{majmin_ver}

BuildRequires:  perl-generators

%description
In Klickety, your goal is to clear the board by clicking on groups to
destroy them. The overall aim is to get the lowest score possible. It
will provide entertainment for all abilities, but a challenge in logical
thought if you want to get a really low score.

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
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.ksame.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/%{name}
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_metainfodir}/org.kde.ksame.appdata.xml
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/applications/org.kde.ksame.desktop
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/kconf_update/%{name}*
%{_kf6_datadir}/sounds/%{name}/

%changelog
%autochangelog
