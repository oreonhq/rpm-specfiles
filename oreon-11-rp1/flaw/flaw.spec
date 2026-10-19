%global source0_hash 424e53085ecdd60e43b557d1ec0ff73b050fe988bb1ede824c4bc5f9c68c4d77
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}
Name:		flaw
Version:	1.3.2a
Release:        1%{?dist}
Summary:        Free top-down wizard battle game
License:	GPL-3.0-or-later
URL:		http://flaw.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		flaw-aarch64.patch
Requires:	gnu-free-sans-fonts gnu-free-serif-fonts
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  SDL_gfx-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gnu-free-sans-fonts
BuildRequires:  gnu-free-serif-fonts
BuildRequires:  intltool
BuildRequires:  make
# /oreon:deps
%description
FLAW is a free top-down wizard battle game.
It can be played by up to 5 players simultaneously. The goal of the game is to
survive as long as possible while more and more fireballs appear in the arena.
Game play is simple and self-explanatory. It's all about evading the fireballs
and knocking your opponents down. In addition there are collectible magic gems
that provide special abilities.

%prep

%autosetup

# Fix spurious executable permissions
chmod 644 src/*.cc
chmod 644 src/*.h

# Remove deprecated tag Enconding from flaw.desktop
sed -i -e '2d' data/flaw.desktop

%build

%configure --docdir=%{_pkgdocdir}
%make_build
%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Edgar Muniz Berlinck <edgar.vv@gmail.com> -->
<!--
BugReportURL: https://sourceforge.net/p/flaw/feature-requests/3/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">flaw.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Casual Wizards Battle Game</summary>
  <description>
    <p>
      Flaw is a game where you control a wizard and your goal is to survive as
      much as you can.
    </p>
    <p>
      In addition to the fireballs that arise increasingly in larger quantities,
      there are other wizards trying to kill you.
    </p>
    <p>
      The game has some items that give you special abilities to defend yourself or attack your enemies.
    </p>
    <p>
      Flaw can be played on single-player mode or with your friends.
    </p>
  </description>
  <url type="homepage">http://flaw.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://flaw.sourceforge.net/images/ingame1.png</screenshot>
    <screenshot>http://flaw.sourceforge.net/images/ingame3.png</screenshot>
    <screenshot>http://flaw.sourceforge.net/images/ingame2.png</screenshot>
    <screenshot>http://flaw.sourceforge.net/images/menu.png</screenshot>
  </screenshots>
</application>
EOF
%find_lang %{name}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
