%global source0_hash e627ca6b3e8971b65ce189ef8f869383daacebe764449336778aa6b59e91cf36
Name:    angband
Version: 4.2.6
Release:        1%{?dist}
Summary:        Popular roguelike role playing game
License: GPL-2.0-only
URL:     https://rephial.org/
Source0:        angband-%{version}-norestricted.tar.gz
Source1: generate-tarball.sh
Source2: fix-restricted.patch
Source3: angband-sdl
Source4: angband-launcher
Patch0: angband-4.2.4-1-chown_fix.patch
Requires: hicolor-icon-theme
Requires: freetype >= 2.11.0-3
Requires: xorg-x11-fonts-misc
Requires: zenity
Requires: %{name}-data = %{version}-%{release}
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_ttf-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  python3-docutils
# /oreon:deps
%description
A roguelike game where you explore a very deep dungeon, kill monsters, try to
equip yourself with the best weapons and armor you can find, and finally face
Morgoth - "The Dark Enemy".

%package data
Summary: Angband data files
License: GPL-2.0-only AND CC-BY-3.0 AND CC-BY-4.0
BuildArch: noarch
%description data
Data files for the Angband game

%package doc
Summary: Angband doc files
%description doc
Documentation about the Angband game

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
./autogen.sh

# file-not-utf8 fix
iconv -f iso8859-1 -t utf-8 \
    docs/version.rst > docs/version.rst.conv && \
    mv -f docs/version.rst.conv docs/version.rst
desktop-file-edit \
    --set-key="Exec" --set-value="angband-sdl" \
    --set-key="TryExec" --set-value="angband-sdl" \
    lib/icons/angband-sdl2.desktop
cp lib/icons/angband-sdl2.desktop \
    lib/icons/angband-launcher.desktop
desktop-file-edit \
    --set-name="Angband Launcher" \
    --set-key="Exec" --set-value="angband-launcher" \
    --set-key="TryExec" --set-value="angband-launcher" \
    lib/icons/angband-launcher.desktop

%build

%configure \
    --with-private-dirs \
    --with-gamedata-in-lib \
    --enable-sdl2 \
    --enable-sdl2-mixer
%make_build PROGNAME=%{name}_homedir
%configure \
    --with-setgid=games \
    --with-gamedata-in-lib \
    --enable-sdl2 \
    --enable-sdl2-mixer
%make_build
%install
%make_install
install -d $RPM_BUILD_ROOT/%{_var}/games/%{name}
install -d $RPM_BUILD_ROOT/%{_var}/games/%{name}/scores
install -d $RPM_BUILD_ROOT/%{_var}/games/%{name}/archive
install -d $RPM_BUILD_ROOT/%{_var}/games/%{name}/save
install -d $RPM_BUILD_ROOT/%{_var}/games/%{name}/panic
desktop-file-install \
    --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
    lib/icons/angband-launcher.desktop
desktop-file-install \
    --dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
    lib/icons/angband-x11.desktop
appstream-util validate-relax --nonet \
    ${RPM_BUILD_ROOT}%{_metainfodir}/angband.metainfo.xml
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6/
install -p -m 644 src/angband.man $RPM_BUILD_ROOT%{_mandir}/man6/angband.6
install -p -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/angband-sdl
install -p -m 755 %{SOURCE4} $RPM_BUILD_ROOT%{_bindir}/angband-launcher
install -p -m 755 src/%{name}_homedir $RPM_BUILD_ROOT/%{_bindir}/%{name}_homedir
%oreon_autofiles angband-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles angband-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n angband-data -f %{oreon_filedir}/angband-data.list
%files -n angband-doc -f %{oreon_filedir}/angband-doc.list

%changelog

%autochangelog
