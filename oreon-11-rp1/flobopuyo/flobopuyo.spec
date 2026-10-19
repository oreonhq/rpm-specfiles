%global source0_hash 46d12af706fba7281e7f92f733e70cc38e9965a550e06a8a38ea4f65620da130
Name:           flobopuyo
Version:        0.20
Release:        1%{?dist}
Summary:        2-player falling bubbles game
License:        GPL-2.0-or-later
URL:            http://www.fovea.cc/flobopuyo-en
Source0:        http://www.fovea.cc/files/flobopuyo/%{name}-%{version}.tgz
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
Patch0:         %{name}-0.20-64bit.patch
Patch1:         %{name}-0.20-Makefile.patch
Patch2:         %{name}-0.20-segfaults.patch
Patch3:         %{name}-0.20-set_window_title.patch
Patch4:         %{name}-0.20-fix_typo.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  bison
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libicns-utils
BuildRequires:  make
# /oreon:deps
%description
A two-player falling bubbles game.  The goal is to make groups of four or more
Puyos (colored bubbles) to make them explode and send bad ghost Puyos to your
opponent.  You win the game if your opponent reaches the top of the board. You
can play against computer or another human.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p0

# Fix end-of-line-encoding
sed -i 's/\r//' COPYING

# Remove AppleDouble files
rm data/sfx/._bi

%build

%set_build_flags macro
make PREFIX=%{_prefix}
%install
%make_install PREFIX=%{_prefix}
install -d -m 755 %{buildroot}%{_mandir}/man6
install -p -m 644 man/%{name}.6 %{buildroot}%{_mandir}/man6
desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
        %{SOURCE1}
icns2png -x mac/icon.icns
install -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -p -m 644 icon_128x128x32.png \
  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -d -m 755 %{buildroot}%{_datadir}/metainfo
install -p -m 644 %{SOURCE2} \
  %{buildroot}%{_datadir}/metainfo
appstream-util validate-relax --nonet \
  %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
