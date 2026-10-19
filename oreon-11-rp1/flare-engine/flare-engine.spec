%global source0_hash 2c1bafeaa5ac26c10449bfcb7151b06e8a22547aa7364d2a39bbcb135aa50a09
%global shortname flare
Name:       flare-engine
Version:    1.14
Release:        1%{?dist}
Summary:        A single player, 2D-isometric, action Role-Playing Engine
%global forgeurl https://github.com/flareteam/flare-engine
%global tag v%{version}
%forgemeta
License:    GPL-3.0-or-later AND BSD-3-Clause
URL:        http://www.flarerpg.org
Source0:        %{forgeurl}/archive/%{tag}/%{name}-%{version}.tar.gz
Patch:      0001-Minimum-CMake-version-3.5.patch
Requires:   font(liberationsans)
Requires:   unifont-ttf-fonts
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  font(liberationsans)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  unifont-ttf-fonts
# /oreon:deps
%description
Flare (Free Libre Action Roleplaying Engine) is a simple game engine built to
handle a very specific kind of game: single-player 2D action RPGs. Flare is not
a re-implementation of an existing game or engine. It is a tribute to and
exploration of the action RPG genre.

Rather than building a very abstract, robust game engine, the goal of this
project is to build several real games and harvest an engine from the common,
reusable code. The first game, in progress, is a fantasy dungeon crawl.

Flare uses simple file formats (INI style config files) for most of the game
data, allowing anyone to easily modify game contents. Open formats are
preferred (png, ogg). The game code is C++.

This package contains the engine only.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DBINDIR="bin" -DDATADIR="share/%{shortname}/"
%cmake_build
%install
%cmake_install
rm %{buildroot}%{_datadir}/%{shortname}/mods/default/fonts/LiberationSans-Regular.ttf
ln -s %{_datadir}/fonts/liberation-sans/LiberationSans-Regular.ttf %{buildroot}%{_datadir}/%{shortname}/mods/default/fonts/LiberationSans-Regular.ttf
rm %{buildroot}%{_datadir}/%{shortname}/mods/default/fonts/unifont-10.0.06.ttf
ln -s %{_datadir}/fonts/unifont/unifont.ttf %{buildroot}%{_datadir}/%{shortname}/mods/default/fonts/unifont-10.0.06.ttf
LEFT_FONT_FILES=$(find %{buildroot}%{_datadir}/%{shortname}/ -type f -name "*.ttf" -o -name "*.otf")
if [ -n "$LEFT_FONT_FILES" ]
then
    echo "Found remaining (non-symlinked) fonts: $LEFT_FONT_FILES"  1>&2
    echo "Failing build!" 1>&2
    exit 1
fi
BROKEN_SYMLINKS=$(find %{buildroot}%{_datadir}/%{shortname}/ -type l ! -exec test -e {} \; -print)
if [ -n "$BROKEN_SYMLINKS" ]
then
    echo "Found broken symlinks: $BROKEN_SYMLINKS" 1>&2
    echo "Failing build!" 1>&2
    exit 1
fi
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{shortname}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
