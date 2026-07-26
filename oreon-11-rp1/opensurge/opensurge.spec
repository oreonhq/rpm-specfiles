%global source0_hash none

Name: opensurge
Summary: 2D retro platformer inspired by Sonic games

# All of the game's original code is GPLv3.
# There is some third-party code under different licenses.
#
# BSD-3-Clause:
# - src/third_party/fast_draw.c
# - src/third_party/fast_draw.h
# Public domain:
# - src/third_party/ignorecase.c
# - src/third_party/ignorecase.h
# - src/third_party/utf8.c
# - src/third_party/utf8.h
License: GPL-3.0-or-later AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain

Version: 0.6.1.3
Release: 1%{?dist}

URL: https://opensurge2d.org
Source0: https://github.com/alemart/opensurge/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: make

%global allegro_min_ver 5.2.11
BuildRequires: pkgconfig(allegro-5)        >= %allegro_min_ver
BuildRequires: pkgconfig(allegro_acodec-5) >= %allegro_min_ver
BuildRequires: pkgconfig(allegro_audio-5)  >= %allegro_min_ver
BuildRequires: pkgconfig(allegro_dialog-5) >= %allegro_min_ver
BuildRequires: pkgconfig(allegro_image-5)  >= %allegro_min_ver
BuildRequires: pkgconfig(allegro_physfs-5) >= %allegro_min_ver
BuildRequires: pkgconfig(allegro_ttf-5)    >= %allegro_min_ver
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(physfs)
BuildRequires: pkgconfig(surgescript)

%global fontlist font(notosans) font(notosansblack) font(roboto)
BuildRequires: fontconfig
BuildRequires: %{fontlist}

Requires: %{name}-data = %{version}-%{release}

%description
Surge the Rabbit is a fun 2D retro platformer inspired by Sonic games,
and a game creation system that lets you unleash your creativity!

Surge the Rabbit is two projects in one: a game
and a game creation system (game engine).

%package data
Summary: Data files for opensurge
BuildArch: noarch

Requires: %{fontlist}

# Based on src/misc/copyright_data.csv
#
# The above list contains some bundled fonts (Noto and Roboto),
# but we un-bundle them, so they aren't included in the License tag here.
License: CC-BY-SA-4.0 AND CC-BY-SA-3.0 AND CC-BY-4.0 AND CC-BY-3.0 AND CC0-1.0 AND MIT AND Giftware

%description data
Data files (graphics, music, sounds) required by Open Surge.

%prep
%autosetup -p1

%build
# TODO: Please submit an issue to upstream (rhbz#2381341)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake \
	-DALLEGRO_STATIC=OFF  \
	-DALLEGRO_MONOLITH=OFF  \
	-DGAME_BINDIR="%{_bindir}/" \
	-DGAME_DATADIR="%{_datadir}/%{name}"  \
	-DDESKTOP_INSTALL=ON  \
	-DDESKTOP_ENTRY_PATH="%{_datadir}/applications"  \
	-DDESKTOP_ICON_PATH="%{_datadir}/pixmaps"  \
	-DDESKTOP_METAINFO_PATH="%{_metainfodir}"  \
	-DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

# Remove bundled fonts and replace them with symlinks
for NOTO in Black Bold; do
	ln -sf  \
		"$(fc-match -f '%%{file}' "NotoSans:${NOTO}")"  \
		"%{buildroot}/%{_datadir}/%{name}/fonts/NotoSans-${NOTO}.ttf"
done
for ROBOTO in Black Bold Medium; do
	ln -sf  \
		"$(fc-match -f '%%{file}' "Roboto:${ROBOTO}")"  \
		"%{buildroot}/%{_datadir}/%{name}/fonts/Roboto-${ROBOTO}.ttf"
done

# The licenses are not readable inside the game,
# and since we un-bundle the fonts, we might as well remove their licenses
rm %{buildroot}%{_datadir}/%{name}/licenses/Apache2-license.txt
rm %{buildroot}%{_datadir}/%{name}/licenses/OFL-1.1.txt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.appdata.xml

%files
%license licenses/BSD-3-clause.txt
%license licenses/GPL3-license.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png

%files data
%license licenses/CC-BY-3.0-legalcode.txt
%license licenses/CC-BY-4.0-legalcode.txt
%license licenses/CC-BY-SA-3.0-legalcode.txt
%license licenses/CC-BY-SA-4.0-legalcode.txt
%license licenses/CC0-1.0-legalcode.txt
%license licenses/Giftware-license.txt
%license licenses/MIT-license.txt
%{_datadir}/%{name}/

%changelog
%autochangelog
