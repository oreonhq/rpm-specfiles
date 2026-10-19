%global source0_hash be0f751a8d0910556380910fcc9ae2a219d7cc74dd2493b396af8edf5b3666a9
Name: opensurge
Summary:        2D retro platformer inspired by Sonic games
License: GPL-3.0-or-later AND BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
Version: 0.6.1.3
Release:        1%{?dist}
URL: https://opensurge2d.org
Source0:        https://github.com/alemart/opensurge/archive/v%{version}/%{name}-%{version}.tar.gz
%global allegro_min_ver 5.2.11
%global fontlist font(notosans) font(notosansblack) font(roboto)
Requires: %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  font(notosans)
BuildRequires:  font(notosansblack)
BuildRequires:  font(roboto)
BuildRequires:  fontconfig
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(allegro-5)
BuildRequires:  pkgconfig(allegro_acodec-5)
BuildRequires:  pkgconfig(allegro_audio-5)
BuildRequires:  pkgconfig(allegro_dialog-5)
BuildRequires:  pkgconfig(allegro_image-5)
BuildRequires:  pkgconfig(allegro_physfs-5)
BuildRequires:  pkgconfig(allegro_ttf-5)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(physfs)
BuildRequires:  pkgconfig(surgescript)
# /oreon:deps
%description
Surge the Rabbit is a fun 2D retro platformer inspired by Sonic games,
and a game creation system that lets you unleash your creativity!

Surge the Rabbit is two projects in one: a game
and a game creation system (game engine).

%package data
Summary: Data files for opensurge
BuildArch: noarch
Requires: %{fontlist}
License: CC-BY-SA-4.0 AND CC-BY-SA-3.0 AND CC-BY-4.0 AND CC-BY-3.0 AND CC0-1.0 AND MIT AND Giftware
%description data
Data files (graphics, music, sounds) required by Open Surge.

%prep
%oreon_prep
%build

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
rm %{buildroot}%{_datadir}/%{name}/licenses/Apache2-license.txt
rm %{buildroot}%{_datadir}/%{name}/licenses/OFL-1.1.txt
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n opensurge-data -f %{oreon_filedir}/opensurge-data.list

%changelog

%autochangelog
