%global source0_hash fae1c417a9807fa8870e14af49d9e49f3c59072474db6b92f7290a8ab127acb6
Name: easyrpg-player
Summary:        Game interpreter for RPG Maker 2000/2003 and EasyRPG games
URL: https://easyrpg.org
License: GPL-3.0-or-later AND CC-BY-SA-4.0 AND (Unlicense OR MIT-0) AND (MIT AND CC0-1.0) AND BSD-3-Clause AND Baekmuk AND LicenseRef-Fedora-Public-Domain AND MIT AND GPL-2.0-or-later WITH Font-exception-2.0
Version: 0.8.1.1
Release:        1%{?dist}
%global repo_owner EasyRPG
%global repo_name Player
Source0:        https://github.com/%{repo_owner}/%{repo_name}/archive/%{version}/%{repo_name}-%{version}.tar.gz
Patch2: 0002-unbundle-dr_wav.patch
Patch3: 0003-dr_wav-0.14.patch
%if %{defined fc42}
%else
%endif
Requires: hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dr_wav-devel
BuildRequires:  fluidsynth
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(liblcf)
BuildRequires:  pkgconfig(liblhasa)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxmp)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(sdl3)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(wildmidi)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  rubygem-asciidoctor
# /oreon:deps
%description
EasyRPG Player is a game interpreter for RPG Maker 2000/2003 and EasyRPG games.

To play a game, run the "%{name}" executable inside
a RPG Maker 2000/2003 game project folder (same place as RPG_RT.exe).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{repo_name}-%{version} -p1

# These are all un-bundled and can be removed
rm src/external/dr_wav.h

%build

%cmake \
	-DPLAYER_BUILD_EXECUTABLE=ON \
	-DPLAYER_BUILD_LIBLCF=OFF \
	-DPLAYER_ENABLE_TESTS=ON \
	-DPLAYER_WITH_LHASA=ON \
	-DPLAYER_TARGET_PLATFORM=SDL3 \
	-DCMAKE_FIND_PACKAGE_PREFER_CONFIG=OFF \
	-DCMAKE_BUILD_TYPE=Release
%cmake_build
%cmake_build --target man
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%cmake_build --target check
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
