%global stable_kf6 stable
%global source0_hash 063f6ea38dc33c7296af7075cd800f81b5c490e2c54e1d7017fd45067c2dbbf5
%global commit f0f617cdb948b8788ea8bfd2c141d6cb46bf1b0e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20251213
%global app_id  org.kde.atlantik
Name:           atlantik
Version:        0.7.80%{?gitdate:~%{gitdate}.git%{shortcommit}}
Release:        1%{?dist}
Summary:        KDE monopd game client
License:        GPL-2.0-only
URL:            https://apps.kde.org/atlantik/
%if 0%{?gitdate:1}
Source0:        https://invent.kde.org/games/%{name}/-/archive/%{commit}/%{name}-%{commit}.tar.bz2
%else
Source0:        https://invent.kde.org/games/%{name}/-/archive/%{commit}/%{name}-%{commit}.tar.bz2
%endif
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  cmake(KDEGames6)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# /oreon:deps
%description
Purpose of the Atlantic board game is to acquire land in major cities in
North America and Europe while being a transatlantic traveller. One of the
game modes plays like the popular real estate board game based on Atlantic
City street names.

%package libs
Summary:        KDE monopd client libraries
License:        LGPL-2.1-only
Obsoletes:      kdeaddons-atlantikdesigner < 4
%description libs
%{summary}.

%package devel
Summary:        Development files for KDE monopd client libraries
License:        LGPL-2.1-only
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      kdegames3-devel < 3.5.10-47
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup %{?gitdate:-n %{name}-%{commit}}

%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-html --with-man
%oreon_autofiles atlantik-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles atlantik-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/%{app_id}.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n atlantik-libs -f %{oreon_filedir}/atlantik-libs.list
%files -n atlantik-devel -f %{oreon_filedir}/atlantik-devel.list

%changelog

%autochangelog
