Name:           game-music-emu
Version:        0.6.4
Release:        3%{?dist}
Provides:       libgme%{?_isa} = %{version}-%{release}
Summary:        Video game music file emulation/playback library
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/libgme/game-music-emu
Source0:        %{url}/archive/%{version}/game-music-emu-%{version}.tar.gz


BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  zlib-devel
# needed to build the player
BuildRequires:  SDL2-devel
BuildRequires: make

%package devel
Summary:        Development files for Game_Music_Emu
Provides:       libgme-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}%{?_isa} = %{version}
Requires:       pkgconfig

%package player
Summary:        Demo player utilizing Game_Music_Emu
# Automatically converted from old format: MIT - review is highly recommended.
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
%setup -q
# add install rule for the player
echo -e "\ninstall(TARGETS gme_player RUNTIME DESTINATION %{_bindir})" >> player/CMakeLists.txt


%build
%cmake -D ENABLE_UBSAN:BOOL=OFF -D GME_BUILD_STATIC:BOOL=OFF
%cmake_build
# explicitly build the player as it has EXCLUDE_FROM_ALL set
%cmake_build --target gme_player


%install
%cmake_install
# explicitly install the player as it has EXCLUDE_FROM_ALL set
pushd %{_vpath_builddir}/player
make install DESTDIR=%{buildroot}
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
* Mon Apr 20 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.6.4-3
- Import from Fedora 43 dist-git for Oreon 11 RP1
