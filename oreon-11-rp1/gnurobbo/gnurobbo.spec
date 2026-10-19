%global source12_hash d60e685228394056657c83378de33adf0ef584cf39538a8fba2c2f201557057d
%global source11_hash 7a3ee7cbc12518246a1427d4ce17f7e3e1fd004c1a2e29df50174b548ecdf0e2
%global source10_hash 3c8da7288a08fa061a242280ecb95c6d22c495230376ceb54bff482ad5046d40
%global source0_hash 3c8da7288a08fa061a242280ecb95c6d22c495230376ceb54bff482ad5046d40
%undefine __cmake_in_source_build
%global rev     415
%global date    20151113
%global readme  README.fedora
Name:           gnurobbo
Version:        0.68
Release:        1%{?dist}
Summary:        Port of an once famous game named Robbo from 1989
License:        GPL-2.0-or-later
URL:            http://%{name}.sf.net/
Source0:        %{name}-%{version}svn%{rev}.tar.xz
Source1:        %{name}-svn-tarball.sh
Patch0:         https://sf.net/p/%{name}/patches/12/attachment/%{name}-cmake.patch
Patch1:         https://sf.net/p/%{name}/patches/13/attachment/%{name}-hardening.patch
Patch2:         gnurobbo-remove-original-levels.patch
Patch3:         %{name}-fno-common.patch
Source10:       https://svn.code.sf.net/p/%{name}/code/%{name}.16.png.bz2
Source11:       https://svn.code.sf.net/p/%{name}/code/%{name}.32.png.bz2
Source12:       https://svn.code.sf.net/p/%{name}/code/%{name}.48.png.bz2
Source20:       %{name}-%{readme}
Requires:       hicolor-icon-theme
Requires:       %{name}-tronic = %{version}-%{release}
Suggests:       %{name}-skin
Obsoletes:      %{name}-data
Obsoletes:      %{name}-fonts
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
# /oreon:deps
%description
GNU Robbo is a free open source port of Janusz Pelc's Robbo
which was distributed by LK Avalon in 1989.

Features (some of them cat not be provided due to legal reasons)
   + Graphical skin support: Oily, Original and Tronic
   + Sound skin support: Default, Free and Oily
   + Support for user supplied music
   + 1113 levels across 28 packs converted from Robbo and Robbo Konstruktor
   + A mouse/stylus driven level designer
   + Support for Alex (a Robbo clone) objects
   + Support for Robbo Millenium objects
   + In-game help
   + Reconfigurable options and controls
   + Support for the mouse/stylus throughout the game
   + Support for keyboards, analogue and digital joysticks
   + Centering of game within any resolution >= 240x240
   + Simple build system to maximize porting potential
   + Support for locales

The game-play of the original is faithfully reproduced with a few modifications
   + Lives has been removed and suicide replaced with level restart
   + Scoring has been removed: goal is level advancement
   + Bears don't endlessly spin around themselves
   + Capsules don't spawn from question marks
   + Solid laser fire is not left live after the gun has been destroyed

Take a look into %{readme} about legal issues cause of missing content.

%package tronic
Summary:        Tronic skin for the game %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-skin
%description tronic
Optional skin named tronic for the game %{name}:
Newly created skin with some vintage science fiction influences.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n%{name}-%{version}svn%{rev}
cp -p %SOURCE10 %SOURCE11 %SOURCE12 .
bunzip2 *.png.bz2
cp -p %SOURCE20 %{readme}

# do not distribute any illegal content
sed -i s,add_subdirectory.data.,, CMakeLists.txt

%build

%cmake -DUSE_FONTS=OFF -DDISABLE_MUSIC=ON
%cmake_build
%install
%cmake_install
rm -v %{buildroot}%{_pkgdocdir}/COPYING %{buildroot}%{_pkgdocdir}/LICENSE*
install -d %{buildroot}%{_datadir}/%{name}
cp -pr data/locales data/levels data/skins data/rob -t%{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=GNU Robbo
Comment=Port of the once famous ATARI game Robbo
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF
install -d %{buildroot}%{_datadir}/icons/hicolor
for size in 16 32 48; do
 install %{name}.$size.png -D %{buildroot}%{_datadir}/icons/hicolor/$size'x'$size/apps/%{name}.png
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%files -f %{oreon_filedir}/main.list
%files -n gnurobbo-tronic -f %{oreon_filedir}/gnurobbo-tronic.list

%changelog

%autochangelog
