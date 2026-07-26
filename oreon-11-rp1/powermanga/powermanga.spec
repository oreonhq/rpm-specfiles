%global source0_hash da753fce83905a6db3fd8ea65c70c57d662362c86c429d6c6954417144f943e8

Summary: Arcade 2D shoot-them-up game
Name:           powermanga
Version:        0.93.1
Release:        7%{?dist}
License:        GPL-3.0-or-later
URL:            http://linux.tlk.fr/games/Powermanga/

Source0: http://linux.tlk.fr/games/Powermanga/download/powermanga-%{version}.tgz
Source1: powermanga.png
Source2: powermanga.desktop

# install to directories common for Fedora
Patch0:         powermanga-0.93.1-install.patch

# The resulting binary requires libmikmod.so.3 according to ldd, but the
# automatic dependency isn't generated (#577509)
Requires:       libmikmod
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  libmikmod-devel
BuildRequires:  gawk
BuildRequires:  libXt-devel, libXxf86dga-devel, libXxf86vm-devel
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  zlib-devel
BuildRequires:  libpng-devel
BuildRequires:  desktop-file-utils

%description
Powermanga is a vertical scrolling arcade style 2D shoot-them-up game with
41 levels and more than 200 sprites.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1
autoreconf -v -i

%build
# The original configure script sets that mandatory -std=c99
%configure
%make_build

%install
%make_install

# Allow stripping, g+s will be set back in %%files
%{__chmod} g-s %{buildroot}%{_bindir}/powermanga

# Install pixmap for the menu entry
%{__install} -D -p -m 0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/powermanga.png

# Install menu entry
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE2}

# Default to English
echo "Lang=en" > \
    %{buildroot}%{_datadir}/powermanga/texts/config.ini

%files
%doc AUTHORS CHANGES README
%license COPYING
%attr(2755,root,games) %{_bindir}/powermanga
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/powermanga.png
# No _datadir/powermanga/ single line to avoid including config.ini twice
%dir %{_datadir}/powermanga/
%{_datadir}/powermanga/data/
%{_datadir}/powermanga/graphics/
%{_datadir}/powermanga/sound/
%{_datadir}/powermanga/sounds/
%dir %{_datadir}/powermanga/texts/
%{_datadir}/powermanga/texts/*.txt
%config(noreplace) %{_datadir}/powermanga/texts/config.ini
%{_mandir}/man6/powermanga.6*
%{_mandir}/{fr}/man6/powermanga.6*
%config(noreplace) %attr(664,root,games) %{_var}/games/powermanga/powermanga.hi
%config(noreplace) %attr(664,root,games) %{_var}/games/powermanga/powermanga.hi-easy
%config(noreplace) %attr(664,root,games) %{_var}/games/powermanga/powermanga.hi-hard

%changelog
%autochangelog
