%global source0_hash b2fb1bf379c345f8754e7e284e65c8ac174099fb63a5130134d164e922af624f

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    katomic
Summary: An educational game built around molecular geometry
Version: 25.12.3
Release: 1%{?dist}

# code GPLv2+, docs GFDL
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

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: kf6-kcompletion-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kconfigwidgets-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kdbusaddons-devel
BuildRequires: kf6-kdeclarative-devel
BuildRequires: kf6-kguiaddons-devel
BuildRequires: kf6-ki18n-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kitemviews-devel
BuildRequires: kf6-kio-devel
BuildRequires: kf6-kjobwidgets-devel
BuildRequires: kf6-knewstuff-devel
BuildRequires: kf6-knotifyconfig-devel
BuildRequires: kf6-knewstuff-devel
BuildRequires: kf6-kservice-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: kf6-kwidgetsaddons-devel
BuildRequires: kf6-kxmlgui-devel
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DocTools)

BuildRequires: perl-generators

BuildRequires: pkgconfig(Qt6Widgets)

%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires: libkdegames-devel >= %{majmin_ver}

%description
KAtomic is a fun and educational game built around molecular geometry.
It employs a simplistic two-dimensional look at the elements which
comprise a molecule. A molecule is disassembled into its separate atoms
and scattered around the playing field. The player must reassemble
the molecule in order to complete the current level and move up to
the next one.

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
%license LICENSES/*
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/knsrcfiles/%{name}.knsrc
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/qlogging-categories6/%{name}*

%changelog
%autochangelog
