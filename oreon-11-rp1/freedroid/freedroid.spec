%global source0_hash 3147bd54804e438c7675263d8534979096cd51b5df5528869ffa8ae52579a55c
Name:           freedroid
Summary:        Clone of the C64 game Paradroid
License:        GPL-2.0-or-later
Version:        1.2.3
Release:        1%{?dist}
%global git_tag %{name}-%{version}.apk
URL:            https://github.com/ReinhardPrix/FreedroidClassic/
Source0:        https://github.com/ReinhardPrix/FreedroidClassic/archive/%{git_tag}/%{git_tag}.tar.gz
Source1:        %{name}.desktop
Patch0:         0000-vorbisfile.patch
Requires:       %{name}-data = %{version}
# oreon:deps
BuildRequires:  SDL_gfx-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
# /oreon:deps
%description
This is a clone of the classic game "Paradroid" on Commodore 64
with some improvements and extensions to the classic version.
In this game, you control a robot, depicted by a small white ball with
a few numbers within an interstellar spaceship consisting of several
decks connected by elevators.
The aim of the game is to destroy all enemy robots, depicted by small
black balls with a few numbers, by either shooting them or seizing
control over them by creating connections in a short subgame of
electric circuits.

%package        data
Summary:        Game data files for Freedroid
Requires:       %{name} = %{version}
BuildArch:      noarch
%description    data
This package contains game data files for Freedroid.

%prep

%autosetup -p1 -n FreedroidClassic-%{git_tag}
./autogen.sh

%build

export CFLAGS="${CFLAGS} -fcommon -std=c99"
%configure --disable-dependency-tracking
%make_build
%install
%make_install
rm -rf $RPM_BUILD_ROOT%{_datadir}/freedroid/mac-osx
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
install -Dpm 644 graphics/paraicon_48x48.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/freedroid.png
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n freedroid-data -f %{oreon_filedir}/freedroid-data.list

%changelog

%autochangelog
