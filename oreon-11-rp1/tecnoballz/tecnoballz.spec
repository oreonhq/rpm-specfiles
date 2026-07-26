%global source0_hash 3ae9d084d7a65af52ef8657c2adbeda0a0747825f9b3b58b8352b7403d5b95b5

Name: tecnoballz
Version: 0.92
Release: 48%{?dist}
Summary: A Brick Busting game

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later
URL: http://linux.tlk.fr/games/TecnoballZ/
Source0: http://linux.tlk.fr/games/TecnoballZ/download/%{name}-%{version}.tgz
Source1: %{name}.xpm
Source2: %{name}.desktop
# Andrea Musuruane
# Fix dependencies
Patch0: tecnoballz-0.92-dependecies.patch
# Andrea Musuruane
# Don't combine explicit and implicit rules for make 3.82
# Set correct gamedir for Fedora
Patch1: tecnoballz-0.92-Makefile.patch
# Debian
# Fix configure.ac Makefile.am to include missing files
Patch2: tecnoballz-0.92-level_data.patch
Patch3: tecnoballz-0.92-texts_dir.patch
# Debian
# Use tinyxml system library
Patch4: tecnoballz-0.92-tinyxml.patch
# Upstream CVS
# Compile with gcc 4.3
Patch5: tecnoballz-0.92-gcc43.patch
# Hans de Goede
# Drop setgid privileges when not needed
Patch6: tecnoballz-0.92-dropsgid.patch
# Raphael Groner/Upstream GIT
# Compile with gcc 6
Patch7: tecnoballz-0.92-gcc6-narrowing.patch

BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: autoconf
BuildRequires: SDL_image-devel
BuildRequires: SDL_mixer-devel
BuildRequires: mikmod-devel
BuildRequires: tinyxml-devel
BuildRequires: desktop-file-utils
Requires: hicolor-icon-theme

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
# FIX: ovverride CXXFLAGS to pick up RPM_OPT_FLAGS
%make_build CXXFLAGS="$RPM_OPT_FLAGS"

%install
%make_install

# install desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install         \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE2}

# install icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm

%files
%attr(2755,root,games) %{_bindir}/tecnoballz
%{_datadir}/tecnoballz
%{_localstatedir}/games/tecnoballz
%attr(-,root,games) %config(noreplace) %{_localstatedir}/games/tecnoballz/tecnoballz.hi
%{_mandir}/man6/%{name}.6*
%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop
%doc AUTHORS CHANGES README
%license COPYING

%changelog
%autochangelog
