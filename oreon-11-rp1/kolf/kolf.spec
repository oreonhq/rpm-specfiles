%global source0_hash 6d9359bafd035027516e9c50f64ac25d2718fb4a81141f469d80c7454dc895e8

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kolf
Summary: A miniature golf game
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
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)

%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires: libkdegames-devel >= %{majmin_ver}

BuildRequires: pkgconfig(phonon4qt6)

BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)

Conflicts: kde-l10n < 17.08.3-2

Obsoletes: kolf-libs < 19.12

%description
Kolf is a miniature golf game with 2d top-down view. Courses are
dynamic, and up to 10 people can play at once in competition.

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
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%license COPYING*
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/icons/hicolor/*/*/*
#%%{_kf6_datadir}/kxmlgui6/%{name}*

%changelog
%autochangelog
