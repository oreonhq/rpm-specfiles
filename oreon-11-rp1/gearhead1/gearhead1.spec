%global source0_hash 7f0fa83d745d683b802e3f44cea70a66b6d6a46f1b4e2db49c774f176089e627
Name: gearhead1
%global reponame gearhead-1
%global prettyname GearHead: Arena
%global about_game Roguelike mecha role-playing game
Summary:        Roguelike mecha role-playing game
License: LicenseRef-Callaway-LGPLv2
Version: 1.310
Release:        19%{?dist}
URL: http://gearheadrpg.com
Source0:        https://github.com/jwvhewitt/%{reponame}/archive/v%{version}/%{reponame}-%{version}.tar.gz
Source10: %{name}-icon-128px.png
Source11: %{name}-icon-96px.png
Source12: %{name}-icon-48px.png
Source20: %{name}-sdl.appdata.xml
Patch0: 0000-change-data-paths.patch
ExclusiveArch: %{fpc_arches}
%global fontlist font(bitstreamverasans) font(bitstreamverasansmono) font(bitstreamveraserif)
Requires: %{name}-bin%{?_isa} = %{version}-%{release}
Suggests: %{name}-SDL%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  font(bitstreamverasans)
BuildRequires:  font(bitstreamverasansmono)
BuildRequires:  font(bitstreamveraserif)
BuildRequires:  fontconfig
BuildRequires:  fpc
BuildRequires:  fpc-srpm-macros
BuildRequires:  glibc-devel
BuildRequires:  libappstream-glib
# /oreon:deps
%description
Set a century and a half after nuclear war, in this game you explore a world
where various factions compete to determine the future of the human race.

Features include random plot generation and over two hundred mecha designs.
Pilot a giant robot, a city smashing tank, a living jet fighter, or
anything else that can be built using the game's sophisticated design system.

%package textmode
Summary: %{about_game} (textmode version)
Provides: %{name}-bin%{?_isa} = %{version}-%{release}
Requires: %{name}-data = %{version}-%{release}
%description textmode
Textmode build of %{prettyname}.

%package SDL
Summary: %{about_game} (SDL version)
Provides: %{name}-bin%{?_isa} = %{version}-%{release}
Requires: %{name}-data = %{version}-%{release}
Requires: %{name}-data-gfx = %{version}-%{release}
%description SDL
Graphical build of %{prettyname}, based on the SDL library.

%package data
Summary: Data files for %{name}
BuildArch: noarch
%description data
Data files required to play %{prettyname}.

%package data-gfx
Summary: Graphics and fonts for %{name}-SDL
BuildArch: noarch
Requires: %{name}-data = %{version}-%{release}
Requires: %{fontlist}
Requires: hicolor-icon-theme
%description data-gfx
Images and fonts required to play the graphical version of %{prettyname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{reponame}-%{version}
sed -e "s|__RPM_DATA_DIR__|'%{_datadir}/%{name}'|" -i gears.pp

# Convert files from \r\n to \n
find doc/ -type f -exec dos2unix '{}' ';'
dos2unix readme.md

# Copy over the icons
cp -a %{SOURCE10} %{SOURCE11} %{SOURCE12} ./

# Copy over the appdata.xml file
cp -a %{SOURCE20} ./

# Upsteam does not ship a desktop file
cat > %{name}-sdl.desktop << EOF
[Desktop Entry]
Type=Application
Name=%{prettyname}
Comment=%{about_game}
Exec=%{name}-sdl
Icon=%{name}
Terminal=false
Categories=Game;
EOF

%build

%global buildflags -gw -O2
fpc %{buildflags} -o'gharena-textmode' gharena.pas
rm *.a || true
rm *.o || true
rm *.ppu || true
fpc %{buildflags} -d'SDLMODE' -o'gharena-sdl' gharena.pas
%install
install -m 755 -d %{buildroot}%{_bindir}
for BUILD in textmode sdl; do
	install -m 755  "gharena-${BUILD}"  "%{buildroot}%{_bindir}/%{name}-${BUILD}"
done
install -m 755 -d %{buildroot}%{_datadir}/%{name}
cp -a Design doc GameData Image Series  %{buildroot}%{_datadir}/%{name}
for FONT in  \
	"Vera/Sans:regular" "VeraBd/Sans:bold" "VeraIt/Sans:italic" "VeraBI/Sans:bold:italic"  \
	"VeraMono/Sans Mono:regular" "VeraMoBd/Sans Mono:bold" "VeraMoIt/Sans Mono:italic" "VeraMoBI/Sans Mono:bold:italic"  \
	"VeraSe/Serif:regular" "VeraSeBd/Serif:bold";
do
	FONT_FILE="$(echo "$FONT" | cut '-d/' -f1)"
	FONT_NAME="Bitstream Vera $(echo "$FONT" | cut '-d/' -f2-)"
	ln -sf  \
		"$(fc-match -f "%%{file}" "${FONT_NAME}")"  \
		"%{buildroot}%{_datadir}/%{name}/Image/${FONT_FILE}.ttf"
done
install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 644 %{name}-sdl.desktop %{buildroot}%{_datadir}/applications/
install -m 755 -d %{buildroot}%{_metainfodir}
install -m 644 %{name}-sdl.appdata.xml %{buildroot}%{_metainfodir}/
for SIZE in 128 96 48; do
	ICONDIR="%{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/apps"
	install -m 755 -d "${ICONDIR}"
	install -m 644 "%{name}-icon-${SIZE}px.png" "${ICONDIR}/%{name}.png"
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}-sdl.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-sdl.desktop
%files -f %{oreon_filedir}/main.list
%files -n gearhead1-textmode -f %{oreon_filedir}/gearhead1-textmode.list
%files -n gearhead1-SDL -f %{oreon_filedir}/gearhead1-SDL.list
%files -n gearhead1-data -f %{oreon_filedir}/gearhead1-data.list
%files -n gearhead1-data-gfx -f %{oreon_filedir}/gearhead1-data-gfx.list

%changelog

%autochangelog
