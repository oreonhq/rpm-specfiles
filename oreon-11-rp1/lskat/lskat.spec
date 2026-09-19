%global source0_hash 211188dceb5d84d39af70cd66d43ec26908834d1ebc682c0902492fd9481cfcf

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    lskat
Summary: A fun and engaging card game
Version: 25.12.3
Release: 1%{?dist}

# Automatically converted from old format: LGPLv2 and GFDL - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2 AND LicenseRef-Callaway-GFDL
URL:     https://invent.kde.org/plasma/%{name}

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
BuildRequires: cmake(KF6XmlGui)

BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6OpenGL)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)

%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires: libkdegames-devel >= %{majmin_ver}

BuildRequires: cmake(Phonon4Qt6)

%description
Lieutenant Skat (from German Offiziersskat) is a fun and engaging card
game for two players, where the second player is either live opponent,
or builtin artificial intelligence.

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
%license LICENSES/*
%{_kf6_bindir}/%{name}*
%{_kf6_datadir}/qlogging-categories6/%{name}*
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/%{name}/

%changelog
%autochangelog
