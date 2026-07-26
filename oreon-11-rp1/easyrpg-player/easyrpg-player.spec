%global source0_hash fae1c417a9807fa8870e14af49d9e49f3c59072474db6b92f7290a8ab127acb6

Name: easyrpg-player
Summary: Game interpreter for RPG Maker 2000/2003 and EasyRPG games
URL: https://easyrpg.org

# EasyRPG Player itself is GPLv3+.
# The program's logos are CC-BY-SA 4.0.
# --
# The program makes use of some header-only libraries:
# * dr_wav: Unlicense OR MIT-0
# * nlohmann_json: MIT AND CC0-1.0
# --
# The program bundles several 3rd-party libraries.
#
# FMMidi files - licensed under the 3-clause BSD license:
# - src/midisequencer.cpp
# - src/midisequencer.h
# - src/midisynth.cpp
# - src/midisynth.h
# --
# The program also uses a couple of 3rd-party fonts. Since these are not
# loaded at runtime, but rather baked into the executable at compile time,
# their licenses are also added to the License tag.
#
# Baekmuk files - licensed under the Baekmuk license:
# - src/resources/shinonome/korean/
#
# Shinonome files - released into the public domain:
# - src/resources/shinonome/
#
# ttyp0 files - licensed under the ttyp0 license,
# a variant of the MIT license:
# - src/resources/ttyp0/
#
# WenQuanYi files - licensed under
# GPLv2-or-later with Font Embedding Exception:
# - src/resources/wenquanyi/
#
# The upstream tarball contains also "Teenyicons", under the MIT license,
# but those are used only for Emscripten builds.
License: GPL-3.0-or-later AND CC-BY-SA-4.0 AND (Unlicense OR MIT-0) AND (MIT AND CC0-1.0) AND BSD-3-Clause AND Baekmuk AND LicenseRef-Fedora-Public-Domain AND MIT AND GPL-2.0-or-later WITH Font-exception-2.0

Version: 0.8.1.1
Release: 5%{?dist}

%global repo_owner EasyRPG
%global repo_name Player
Source0: https://github.com/%{repo_owner}/%{repo_name}/archive/%{version}/%{repo_name}-%{version}.tar.gz

# Unbundle libraries
Patch2: 0002-unbundle-dr_wav.patch

# Update dr_wav to 0.14, adapting to API changes
# https://github.com/EasyRPG/Player/pull/3456
#
# We don’t need to update the bundled dr_wav since we will not use it, so we
# just cherry-pick the following commits:
#
# Adapt to API changes in dr_wav 0.14
# https://github.com/EasyRPG/Player/pull/3456/commits/4420531dfd1726f8f127800344ae3a31df39a6af
# dr_wav: Conditional support for old dr_wav 0.13.x
# https://github.com/EasyRPG/Player/pull/3456/commits/081a06f22cbcd9e115950f09c3e8f8e2e98f40af
Patch3: 0003-dr_wav-0.14.patch

BuildRequires: cmake >= 3.13
BuildRequires: desktop-file-utils
BuildRequires: fluidsynth
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: libappstream-glib
BuildRequires: rubygem-asciidoctor

# This library doesn't have pkgconfig info
# Version 0.14.5 fixes CVE-2026-29022
%if %{defined fc42}
# The fix was backported:
BuildRequires: dr_wav-devel >= 0.13.17^20241216git660795b-4
%else
BuildRequires: dr_wav-devel >= 0.14.5
%endif

BuildRequires: pkgconfig(fluidsynth)
BuildRequires: pkgconfig(fmt)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(ibus-1.0)
BuildRequires: pkgconfig(liblcf) >= 0.8.1
BuildRequires: pkgconfig(liblhasa)
BuildRequires: pkgconfig(libmpg123)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libxmp)
BuildRequires: pkgconfig(nlohmann_json) >= 3.9.1
BuildRequires: pkgconfig(opusfile)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(sdl3)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(speexdsp)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(wildmidi)
BuildRequires: pkgconfig(zlib)

Requires: hicolor-icon-theme

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

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%cmake_build --target check

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.png
%{_metainfodir}/%{name}.metainfo.xml

%changelog
%autochangelog
