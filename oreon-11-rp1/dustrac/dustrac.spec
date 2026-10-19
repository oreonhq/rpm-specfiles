%global source0_hash e028a49ad427fb0527b2bf05dad72404cc2d20883da1d330cb1319246bdc423a
Name: dustrac
Summary:        Traditional top-down car racing game
License: GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-3.0-or-later AND MIT
Version: 2.1.1
Release:        1%{?dist}
URL: https://juzzlin.github.io/DustRacing2D/
Source0:        https://github.com/juzzlin/DustRacing2D/archive/%{version}/DustRacing2D-%{version}.tar.gz
Source6: %{name}-game.6
Patch0: 0000-unbundle-libs.patch
%global fontlist font(liberationsans)
Provides: bundled(Argengine) = 0.0.1
Provides: bundled(SimpleLogger) = 1.4.0
Requires: %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(OpenAL)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  font(liberationsans)
BuildRequires:  fontconfig
BuildRequires:  gcc
BuildRequires:  glew-devel
BuildRequires:  glm-devel
BuildRequires:  hardlink
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(vorbisfile)
# /oreon:deps
%description
Dust Racing 2D is a tile-based 2D racing game written with Qt (in C++)
and OpenGL. Dust Racing 2D comes with a Qt-based level editor for level
creation. A separate engine, MiniCore, is used for physics modeling.

%package data
Summary: Data files for Dust Racing 2D
License: CC-BY-SA-3.0
BuildArch: noarch
Requires: hicolor-icon-theme
Requires: %{fontlist}
%description data
This package provides the data files (graphics, sounds, et cetera)
required to play Rust Racing 2D.

%prep

%autosetup -p1 -n DustRacing2D-%{version}

# Remove bundled libs that we want to unbundle
rm -rf src/game/MiniCore/src/Graphics/contrib/

%build

%cmake \
	-DReleaseBuild=1 \
	-DSystemFonts=1 \
	-DDATA_PATH=%{_datadir}/%{name} \
	-DDOC_PATH=%{_docdir}/%{name} \
	-DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build
%install
%cmake_install
hardlink --verbose %{buildroot}%{_datadir}/%{name}/
install -m 755 -d %{buildroot}%{_mandir}/man6/
install -m 644 -p %{SOURCE6} %{buildroot}%{_mandir}/man6/%{name}-game.6
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-game.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-editor.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n dustrac-data -f %{oreon_filedir}/dustrac-data.list

%changelog

%autochangelog
