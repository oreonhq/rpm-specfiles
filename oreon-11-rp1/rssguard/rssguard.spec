%global source0_hash 71d00187ef2a2c9f78c5e6410268fafcc85f71ae600546314060f2b7411b639f
Name:           rssguard
Version:        5.2.5
Release:        1%{?dist}
Summary:        Simple yet powerful feed reader
License:        GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND LGPL-3.0-or-later AND BSD-3-Clause AND MIT AND AGPL-3.0-or-later AND blessing
URL:            https://github.com/martinrotter/rssguard
Source0:        https://github.com/martinrotter/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  %{qt6_qtwebengine_arches}
Requires:       hicolor-icon-theme
Provides:       bundled(boolinq) = 3.0.1-1
Provides:       bundled(mimesis)
Provides:       bundled(simplecrypt) = 3.1-1
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Core5Compat)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Sql)
BuildRequires:  pkgconfig(Qt6WebEngineCore)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(libsqlite3x)
BuildRequires:  pkgconfig(mpv)
# /oreon:deps
%description
RSS Guard is simple, light and easy-to-use RSS/ATOM feed aggregator developed
using Qt framework which supports online feed synchronization.

%prep

%autosetup -p1 -n %{name}-%{version}
sed -i 's/\r$//' README.md

%build

%cmake -DREVISION_FROM_GIT=OFF \
       -DNO_UPDATE_CHECK=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/*.rssguard.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.rssguard.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
