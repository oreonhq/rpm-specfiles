%global source0_hash 5915bbe9efbf79713f2b0bb23a3cd33c54272b03739db22b52bcf5e1f9ef82e8
Name: tecnoballz
Version: 0.93.1
Release:        1%{?dist}
Summary:        A Brick Busting game
License: GPL-3.0-or-later
URL: http://linux.tlk.fr/games/TecnoballZ/
Source0:        http://linux.tlk.fr/games/TecnoballZ/download/%{name}-%{version}.tgz
Source1: %{name}.xpm
Source2: %{name}.desktop
Patch0: tecnoballz-0.92-dependecies.patch
Patch1: tecnoballz-0.92-Makefile.patch
Patch2: tecnoballz-0.92-level_data.patch
Patch3: tecnoballz-0.92-texts_dir.patch
Patch4: tecnoballz-0.92-tinyxml.patch
Patch5: tecnoballz-0.92-gcc43.patch
Patch6: tecnoballz-0.92-dropsgid.patch
Patch7: tecnoballz-0.92-gcc6-narrowing.patch
Requires: hicolor-icon-theme
# oreon:deps
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  autoconf
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  mikmod-devel
BuildRequires:  tinyxml-devel
# /oreon:deps
%description
A exciting Brick Breaker with 50 levels of game and 11 special levels, 
distributed on the 2 modes of game to give the player a sophisticated 
system of attack weapons with an enormous power of fire that can be 
build by gaining bonuses. Numerous decors, musics and sounds 
complete this great game. This game was ported from the Commodore Amiga.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
# Patch4 must be called after Patch0
%patch -P4 -p1
%patch -P5 -p2
%patch -P6 -p1
%patch -P7 -p1

%build

autoreconf -fvi
%configure
%make_build CXXFLAGS="$RPM_OPT_FLAGS"
%install
%make_install
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install         \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE2}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
