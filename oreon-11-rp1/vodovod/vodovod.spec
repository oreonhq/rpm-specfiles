%global source0_hash 1b788d3b0fd1ad508378ad6ab1ff55d517f98632a6c5afa57059f71ec07d9c32
Name:		vodovod
Version:	1.10r22
Release:        1%{?dist}
Summary:        A pipe connecting game
License:	GPL-2.0-or-later
URL:		http://home.gna.org/vodovod/
Source0:        %{name}-%{version}-src.tar.gz
Patch0:		vodovod-1.10r22-locales.patch
Patch1:		vodovod-1.10r22-format-string.patch
%global fonts font(dejavusansmono)
Requires:	%{fonts}
Requires(post): coreutils
Requires(postun): coreutils
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  desktop-file-utils
BuildRequires:  font(dejavusansmono)
BuildRequires:  fontconfig
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  make
# /oreon:deps
%description
A free cross-platform pipe connecting game. You get a limited number
of pipes on each level and need to combine them to lead the water from
the house at the top of the screen to the storage tank at the bottom.

%description -l cs_CZ.UTF-8
Svobodná, multiplatformní logická hra založená na propojování potrubí.
Každá úroveň začíná s omezeným množstvím trubek, které je potřeba umístit
tak, aby svedly vodu z domku na vrchu obrazovky do nádrže dole.

%description -l sk_SK.UTF-8
Slobodná, multiplatformná logická hra založená na spojovaní potrubia.
Každá úroveň začína s obmedzeným množstvom trubiek, ktoré musíte umiestniť tak,
aby viedli vodu z domčeka v hornej časti obrazovky do nádrže v dolnej časti.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#%%setup -q -n %%{name}-%%{version}-src
%setup -q -n %{name}
# update locales
%patch -P0 -p1
# fix bug #1037377
%patch -P1 -p1

%build

make PREFIX=%{_prefix} HIGHSCOREDIR=%{_localstatedir}/games \
	%{?_smp_mflags} CXX="%{__cxx}" CXXFLAGS="%{optflags}"
cat <<EOF > %{name}.desktop
[Desktop Entry]
Name=Vodovod
GenericName=Logic Game
GenericName[cs]=Logická hra
GenericName[sk]=Logická hra
Comment=A pipe connecting game
Comment[cs]=Propojování potrubí
Comment[sk]=Spojovanie potrubia
Exec=vodovod
Icon=vodovod
Terminal=false
Type=Application
Categories=Game;LogicGame;
EOF
%install
make PREFIX=%{_prefix} DESTDIR=%{buildroot} install
ln -f -s $(fc-match -f "%{file}" "dejavusansmono") \
        %{buildroot}%{_datadir}/%{name}/data/font1.ttf
mkdir -p %{buildroot}%{_localstatedir}/games
touch %{buildroot}%{_localstatedir}/games/%{name}.sco
mkdir -p -m 0755 %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
convert data/abicon.bmp %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/vodovod.xpm
desktop-file-install  \
	--dir=%{buildroot}%{_datadir}/applications %{name}.desktop
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
