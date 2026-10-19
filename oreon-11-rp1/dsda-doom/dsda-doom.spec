%global source0_hash 5ce3401f2975b330936c0739b62910ae3b193f0d8f323b7b246bb242e1987e19
Name: dsda-doom
Summary:        Speedrun-oriented Doom source port
License: GPL-2.0-or-later AND BSD-3-Clause AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LicenseRef-Fedora-Public-Domain AND Zlib
Version: 0.30.0
Release:        1%{?dist}
URL: https://github.com/kraflab/dsda-doom
Source0:        https://github.com/kraflab/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
Requires: %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fluidsynth
BuildRequires:  gcc-c++
BuildRequires:  libzip-tools
BuildRequires:  make
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libpcre2-32)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxmp)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  portmidi-devel
BuildRequires:  rubygem-rspec
# /oreon:deps
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
%oreon_prep
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
ln prboom2/AUTHORS ./
install -m 755 -d %{buildroot}%{_pkgdocdir}
cp -a docs patch_notes AUTHORS README.md %{buildroot}%{_pkgdocdir}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n dsda-doom-data -f %{oreon_filedir}/dsda-doom-data.list

%changelog

%autochangelog
