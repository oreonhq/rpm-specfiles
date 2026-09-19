%global source0_hash 80d7b8e83596678b4c7274922e2b1db2f4e8af6d19a20edb0e3b102c884dd93f

Name:           shippy
Version:        1.5.5
Release:        %autorelease
Summary:        Space invaders / Galaxians like game with powerups
License:        GPL-2.0-or-later
URL:            http://www.identicalsoftware.com/shippy1984
Source0:        http://www.identicalsoftware.com/shippy1984/%{name}-%{version}.tgz
BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  SDL2_mixer-devel SDL2_ttf-devel fontconfig-devel libgamerzilla-devel
BuildRequires:  desktop-file-utils libappstream-glib
Obsoletes:      shippy-common < 1.5.0-10
Obsoletes:      shippy-allegro < 1.5.0-10

%description
Shippy1984 is a small, portable game designed to bring back nostalgia for the
ways games used to be made--addicting as hell! Mash buttons on your way to the
high score! Shippy1984 is designed from the ground up for the avid casual
gamer who feels left behind by the technological overload of today's games!
No longer! Shippy1984 is the game you have been waiting for!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
mv docs html

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc html
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

%changelog
%autochangelog
