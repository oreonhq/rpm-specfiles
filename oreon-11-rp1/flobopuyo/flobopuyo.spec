%global source0_hash 46d12af706fba7281e7f92f733e70cc38e9965a550e06a8a38ea4f65620da130

Name:           flobopuyo
Version:        0.20
Release:        44%{?dist}
Summary:        2-player falling bubbles game

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.fovea.cc/flobopuyo-en
Source0:        http://www.fovea.cc/files/flobopuyo/%{name}-%{version}.tgz
Source1:        %{name}.desktop
Source2:        %{name}.appdata.xml
# Fix building on 64bit
# Patch by Michael Thomas aka Wart <wart at kobold dot org>
# https://lists.fedoraproject.org/archives/list/games@lists.fedoraproject.org/thread/ECMVJBXDAITOV35723OMGQSF3CLXKLZK/
Patch0:         %{name}-0.20-64bit.patch
# Patch by Andrea Musuruane
Patch1:         %{name}-0.20-Makefile.patch
# Fix segfaults on Fedora 24
# Patches by Sebastian Ott
# https://bugzilla.redhat.com/show_bug.cgi?id=1352557
# https://bugzilla.redhat.com/show_bug.cgi?id=1380525
Patch2:         %{name}-0.20-segfaults.patch
# Set proper window title
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=537352
Patch3:         %{name}-0.20-set_window_title.patch
# Fix a typo
# Patch taken from Debian
Patch4:         %{name}-0.20-fix_typo.patch

BuildRequires:  gcc-c++
BuildRequires:  flex 
BuildRequires:  bison 
BuildRequires:  SDL_mixer-devel 
BuildRequires:  SDL_image-devel 
BuildRequires:  libicns-utils
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires: make
Requires:       hicolor-icon-theme

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
# It does not support parallel building
make PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix}

# Install man page
install -d -m 755 %{buildroot}%{_mandir}/man6
install -p -m 644 man/%{name}.6 %{buildroot}%{_mandir}/man6

# Install desktop file
desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
        %{SOURCE1}

# Extract Mac OS X icons
icns2png -x mac/icon.icns

# Install icon
install -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -p -m 644 icon_128x128x32.png \
  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

# Install appdata
install -d -m 755 %{buildroot}%{_datadir}/metainfo
install -p -m 644 %{SOURCE2} \
  %{buildroot}%{_datadir}/metainfo
appstream-util validate-relax --nonet \
  %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%files
%doc TODO Changelog
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man6/%{name}.6*

%changelog
%autochangelog
