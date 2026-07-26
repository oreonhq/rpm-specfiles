%global source0_hash none

Name:           zaz
Version:        1.0.1
Release:        12%{?dist}
Summary:        A puzzle game where the player has to arrange balls in triplets

# Music released under CC-BY-SA
# Automatically converted from old format: GPLv3+ and CC-BY-SA - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:            http://zaz.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# 128x128px icon by Zbigniew Jędrzejewski-Szmek
Source1:        %{name}.png
# Appdata by Richard Hughes
Source2:        %{name}.appdata.xml
# Debian man page
Source3:        %{name}.6
# Fix jumpy keyboard
# http://bugs.debian.org/649021
Patch0:         %{name}-1.0.0-jumpy_keyboard.patch
# Link with libvorbis
# https://bugs.debian.org/768718
Patch1:         %{name}-1.0.1-libvorbis.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  mesa-libGL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  ftgl-devel >= 2.1.3
BuildRequires:  gettext
BuildRequires:  ImageMagick
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme
Requires:       gnu-free-mono-fonts
Requires:       gnu-free-sans-fonts
Requires:       oflb-dignas-handwriting-fonts

%description
Zaz is an arcade action puzzle game where the goal is to get rid of all 
incoming balls by rearranging their order and making triplets.

A 3D accelerator is needed for decent gameplay.

%prep
%autosetup -p1

# Fix permissions
chmod 644 src/*.{cpp,h}

%build
%configure
%make_build

%install
%make_install

# Symlink system fonts
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/FreeMonoBold.ttf
ln -s %{_datadir}/fonts/gnu-free/FreeMonoBold.ttf \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/FreeMonoBold.ttf
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/FreeSans.ttf
ln -s %{_datadir}/fonts/gnu-free/FreeSans.ttf \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/FreeSans.ttf
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/font1.ttf
ln -s %{_datadir}/fonts/oflb-dignas-handwriting/phranzysko_-_Digna_s_Handwriting.ttf \
    $RPM_BUILD_ROOT%{_datadir}/%{name}/font1.ttf

# Remove docs
rm -r $RPM_BUILD_ROOT/usr/share/doc/

# Remove obsolete pixmap
rm -rf $RPM_BUILD_ROOT%{_datadir}/pixmaps/

# Convert xpm icon to png to appease appdata
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
convert extra/%{name}.xpm \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

# Install 128x128px icon to appease appdata
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 0644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps

# Validate desktop file
desktop-file-validate \
   $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# Install appdata
install -d $RPM_BUILD_ROOT%{_datadir}/metainfo
install -p -m 0644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/metainfo
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/metainfo/*.appdata.xml

# Install man page
install -d $RPM_BUILD_ROOT%{_mandir}/man6
install -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/man6/

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/*
%license COPYING data/copyright.txt
%doc AUTHORS ChangeLog

%changelog
%autochangelog
