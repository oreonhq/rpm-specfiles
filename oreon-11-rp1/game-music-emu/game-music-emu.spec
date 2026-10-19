%global source0_hash 8531678502451c2cf04248cda45c8b4645e19fcfb63e6a7ec2549641c47bb392
Name:           game-music-emu
Version:        0.6.5
Release:        1%{?dist}
Provides:       libgme%{?_isa} = %{version}-%{release}
Summary:        Video game music file emulation/playback library
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/libgme/game-music-emu
Source0:        https://github.com/libgme/game-music-emu/archive/refs/tags/0.6.5.tar.gz#/game-music-emu-0.6.4.tar.gz
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%package devel
Summary:        Development files for Game_Music_Emu
Provides:       libgme-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}
Requires:       pkgconfig
%package player
Summary:        Demo player utilizing Game_Music_Emu
License:        MIT
%description
Game_Music_Emu is a collection of video game music file emulators that support
the following formats and systems:

 * AY       ZX Spectrum/Amstrad CPC
 * GBS      Nintendo Game Boy
 * GYM      Sega Genesis/Mega Drive
 * HES      NEC TurboGrafx-16/PC Engine
 * KSS      MSX Home Computer/other Z80 systems (doesn't support FM sound)
 * NSF/NSFE Nintendo NES/Famicom (with VRC 6, Namco 106, and FME-7 sound)
 * SAP      Atari systems using POKEY sound chip
 * SPC      Super Nintendo/Super Famicom
 * VGM/VGZ  Sega Master System/Mark III, Sega Genesis/Mega Drive,BBC Micro

%description devel
This package contains files needed to compile code which uses Game_Music_Emu.

%description player
This package contains the demo player for files supported by Game_Music_Emu.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
# add install rule for the player
echo -e "\ninstall(TARGETS gme_player RUNTIME DESTINATION %{_bindir})" >> player/CMakeLists.txt

%build

%cmake -D ENABLE_UBSAN:BOOL=OFF -D GME_BUILD_STATIC:BOOL=OFF
%cmake_build
%cmake_build --target gme_player
%install
%cmake_install
pushd %{_vpath_builddir}/player
make install DESTDIR=%{buildroot}
popd
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n game-music-emu-devel -f %{oreon_filedir}/game-music-emu-devel.list
%files -n game-music-emu-player -f %{oreon_filedir}/game-music-emu-player.list

%changelog

%autochangelog
