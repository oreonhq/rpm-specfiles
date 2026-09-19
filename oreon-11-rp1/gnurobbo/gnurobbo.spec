%global source0_hash 3c8da7288a08fa061a242280ecb95c6d22c495230376ceb54bff482ad5046d40

%undefine __cmake_in_source_build

%global rev     415
%global date    20151113

%global readme  README.fedora

Name:           gnurobbo
Version:        0.68
Release:        28.%{date}svn%{rev}%{?dist}
Summary:        Port of an once famous game named Robbo from 1989

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://%{name}.sf.net/

# Make source tarball from svn with $ ./%{name}-svn-tarball.sh %{rev}
Source0:        %{name}-%{version}svn%{rev}.tar.xz
Source1:        %{name}-svn-tarball.sh

Patch0:         https://sf.net/p/%{name}/patches/12/attachment/%{name}-cmake.patch
Patch1:         https://sf.net/p/%{name}/patches/13/attachment/%{name}-hardening.patch
Patch2:         gnurobbo-remove-original-levels.patch
# Fix the build with -fno-common, the GCC 10 default
Patch3:         %{name}-fno-common.patch

# icons additionally
Source10:       https://svn.code.sf.net/p/%{name}/code/%{name}.16.png.bz2
Source11:       https://svn.code.sf.net/p/%{name}/code/%{name}.32.png.bz2
Source12:       https://svn.code.sf.net/p/%{name}/code/%{name}.48.png.bz2

# information about legal issues
Source20:       %{name}-%{readme}

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  SDL-devel SDL_image-devel
# FIXME fonts and sounds are disabled and so deps should be removed
BuildRequires:  SDL_ttf-devel SDL_mixer-devel

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  desktop-file-utils

Requires:       hicolor-icon-theme

#Bug 1171461 - due to legal reasons only the tronic skin has left
#and therefore we need to depend on it unless someone finds a better solution
Requires:       %{name}-tronic = %{version}-%{release}
Suggests:       %{name}-skin

Obsoletes:      %{name}-data
Obsoletes:      %{name}-fonts

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
# fonts and sounds are not redistributable, ignore them
%cmake -DUSE_FONTS=OFF -DDISABLE_MUSIC=ON
%cmake_build

%install
%cmake_install
# skip misplaced license texts, they get replaced via %license
rm -v %{buildroot}%{_pkgdocdir}/COPYING %{buildroot}%{_pkgdocdir}/LICENSE*

# legal content parts
install -d %{buildroot}%{_datadir}/%{name}
cp -pr data/locales data/levels data/skins data/rob -t%{buildroot}%{_datadir}/%{name}

# desktop
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

# icons
install -d %{buildroot}%{_datadir}/icons/hicolor
for size in 16 32 48; do
 install %{name}.$size.png -D %{buildroot}%{_datadir}/icons/hicolor/$size'x'$size/apps/%{name}.png
done
#install -d %{buildroot}%{_datadir}/pixmaps
#ln -s ../icons/hicolor/48x48/apps/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license COPYING LICENSE-ttf LICENSE-sound
%doc AUTHORS Bugs ChangeLog NEWS README TODO
# distribution is only allowed for legal content
%doc %{readme}
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/levels/
%{_datadir}/%{name}/locales/
%{_datadir}/%{name}/rob/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
#%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/%{name}/skins

%files tronic
%{_datadir}/%{name}/skins/tronic/

%changelog
%autochangelog
