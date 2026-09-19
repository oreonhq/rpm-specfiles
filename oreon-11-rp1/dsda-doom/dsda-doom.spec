%global source0_hash f866db79381862080718668f582b0f358811a016db17680e507abb9250afbea5

Name: dsda-doom
Summary: Speedrun-oriented Doom source port

# Most of the files are covered by GPL v2.
# * BSD:
#   - prboom2/src/gl_sky.c
#   - prboom2/src/scanner.cpp
#   - prboom2/src/scanner.h
# * LGPL v2.0 or later:
#   - prboom2/src/umapinfo.cpp
#   - prboom2/src/umapinfo.h
# * LGPL v2.1 or later:
#   - prboom2/src/gl_vertex.c
# * Public domain:
#   - prboom2/src/SDL/SDL_windows_main.c
#   - prboom2/src/md5.c
#   - prboom2/src/md5.h
#   - prboom2/src/win_opendir.c
#   - prboom2/src/win_opendir.h
# * zlib:
#   - prboom2/src/SDL/SDL_windows.h
#
# Note regarding gl_vertex.c: the file has a conditional licensing clause.
# Check the discussion at: https://gitlab.com/fedora/legal/fedora-license-data/-/issues/310
License: GPL-2.0-or-later AND BSD-3-Clause AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LicenseRef-Fedora-Public-Domain AND Zlib

Version: 0.29.4
Release: 2%{?dist}

URL: https://github.com/kraflab/dsda-doom
Source0: %{URL}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: fluidsynth
BuildRequires: gcc-c++
BuildRequires: libzip-tools
BuildRequires: make
BuildRequires: rubygem-rspec

BuildRequires: portmidi-devel

BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(fluidsynth)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(libpcre2-32)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libxmp)
BuildRequires: pkgconfig(libzip)
BuildRequires: pkgconfig(mad)
BuildRequires: pkgconfig(SDL2_image)
BuildRequires: pkgconfig(SDL2_mixer)
BuildRequires: pkgconfig(SDL2_net)
BuildRequires: pkgconfig(sndfile)
BuildRequires: pkgconfig(vorbisfile)

Requires: %{name}-data = %{version}-%{release}

%description
DSDA-Doom is a source port of the 1993 classic DOOM game.
DSDA-Doom is a fork of prboom+, with many added features, including:
- In-game console and scripting
- Full controller support
- Palette-based lightmode for opengl
- Debugging features for testing
- Strict mode for speedrunning
- Various quality of life improvements
- Advanced tools for TASing
- Rewind feature

%package data
Summary: Data files for DSDA-Doom
BuildArch: noarch

%description data
This package contains data files needed to run DSDA-Doom.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
pushd prboom2/
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebugInfo \
	-DCMAKE_FIND_PACKAGE_PREFER_CONFIG=OFF \
	-DDOOMWADDIR=%{_datadir}/doom \
	-DDSDAPWADDIR=%{_datadir}/%{name} \

%cmake_build

%install
pushd prboom2/
	%cmake_install
	desktop-file-install --dir=%{buildroot}%{_datadir}/applications ICONS/%{name}.desktop
	install -Dpm 644 ICONS/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
popd

# docs
ln prboom2/AUTHORS ./
install -m 755 -d %{buildroot}%{_pkgdocdir}
cp -a docs patch_notes AUTHORS README.md %{buildroot}%{_pkgdocdir}

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

%files data
%license prboom2/COPYING
%doc %{_pkgdocdir}
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.png

%changelog
%autochangelog
