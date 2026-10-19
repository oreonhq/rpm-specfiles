%global source0_hash d7ea7de896176f0546a64f4b41fa017ef61dc9bafd0cd01b0405088ef2b6b39c
Name:           kommit
Version:        1.8.1
Release:        2%{?dist}
Summary:        Graphical Git Client
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND BSD-3-Clause
URL:            https://apps.kde.org/kommit/
Source0:        https://invent.kde.org/sdk/kommit/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Requires:       kf6-filesystem
Requires:       hicolor-icon-theme
Provides:       gitklient = %{version}-%{release}
Obsoletes:      gitklient < 1.0
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(DolphinVcs)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6Charts)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(libgit2)
# /oreon:deps
%description
%{summary}.

%package devel
Summary:        Development environment for %name
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development package for kommit.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-html
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n kommit-devel -f %{oreon_filedir}/kommit-devel.list

%changelog

%autochangelog
