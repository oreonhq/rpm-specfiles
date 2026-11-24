# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 8531678502451c2cf04248cda45c8b4645e19fcfb63e6a7ec2549641c47bb392
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           game-music-emu
Version:        0.6.5
Release:        1%{?dist}
Provides:       libgme%{?_isa} = %{version}-%{release}
Summary:        Video game music file emulation/playback library
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/libgme/game-music-emu
Source0:        %{url}/archive/%{version}/game-music-emu-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires:  cmake
BuildRequires:  zlib-devel
BuildRequires:  SDL2-devel
BuildRequires: make

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
%oreon_sha256
%setup -q
echo -e "\ninstall(TARGETS gme_player RUNTIME DESTINATION %{_bindir})" >> player/CMakeLists.txt

%build
%cmake -D ENABLE_UBSAN:BOOL=OFF -D GME_BUILD_STATIC:BOOL=OFF
%cmake_build
%cmake_build --target gme_player

%install
%cmake_install
pushd %{_vpath_builddir}/player
DESTDIR=%{buildroot} %__cmake --install .
popd

%ldconfig_scriptlets

%files
%doc changes.txt license.txt readme.txt
%{_libdir}/libgme.so.*

%files devel
%doc design.txt gme.txt
%{_libdir}/libgme.so
%{_includedir}/gme/
%{_libdir}/pkgconfig/libgme.pc

%files player
%{_bindir}/gme_player

%changelog
%autochangelog
