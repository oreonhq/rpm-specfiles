%global source0_hash bcc2b7fc8719a8e055969c8eac099b7c40b9d68f36ba1f83d690216bdcdd51f6

%global pkgversion %(echo %version|sed s/\\\\\.//g) 

Name:           whichwayisup
Version:        0.7.9
Release:        25%{?dist}
Summary:        2D platform game with a slight rotational twist

# All game content, sounds and graphics are licensed under
# Creative Commons 3.0 Attribution license.
# Automatically converted from old format: GPLv2 and CC-BY - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-CC-BY
URL:            http://www.oletus.fi/static/whichwayisup/
Source0:        http://www.oletus.fi/static/whichwayisup/%{name}_b%{pkgversion}.zip
# Desktop file taken from Debian
Source1:        %{name}.desktop
# AppData file provided by Iwicki Artur
Source2:        %{name}.appdata.xml
# Man page taken from Debian
Source3:        %{name}.6
# Under certain circumstances whichwayisup detected keyboards as joysticks
# http://bugs.debian.org/710162
Patch0:         %{name}-0.7.9-check_for_joystick_axes_not_null.patch
# Initialize only required pygame modules
# http://bugs.debian.org/432015
Patch1:         %{name}-0.7.9-initialize_only_required_pygame_modules.patch
# Port game to python3
# https://bugs.debian.org/912500
Patch2:         %{name}-0.7.9-python3.patch

BuildArch:      noarch

BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       python3-pygame
Requires:       bitstream-vera-sans-fonts
Requires:       hicolor-icon-theme

%description
A traditional and challenging 2D platform game with a slight rotational 
twist. Help a mysterious big-eared salaryman named Guy find his keys in a 
labyrinth of dangers and bad dialogue.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name} -p1

# Fix script interpreter
sed -i 's!/usr/bin/env python3!/usr/bin/python3!' run_game.py

# Change data path
sed -i "s!libdir = .*!libdir = '%{_datadir}/%{name}/lib'!" run_game.py

# Fix end-of-line encoding
sed -i 's/\r//' changelog.txt

# Remove Thumbs.db
rm data/pictures/Thumbs.db

%build
# Empty

%install
# Install launcher script
install -d %{buildroot}%{_bindir}
install -m 755 -p run_game.py %{buildroot}%{_bindir}/%{name}

# Install game and data
install -d %{buildroot}%{_datadir}/%{name}
cp -pr data lib %{buildroot}%{_datadir}/%{name}

# Install icons
for i in 0 1 2 ; do
  px=$(expr 64 - ${i} \* 16)
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${px}x${px}/apps
  convert lib/whichway.ico[${i}] \
    %{buildroot}%{_datadir}/icons/hicolor/${px}x${px}/apps/%{name}.png
done

# Install desktop file
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

# Install AppData file
install -d %{buildroot}%{_datadir}/metainfo
install -p -m 644 %{SOURCE2} %{buildroot}%{_datadir}/metainfo
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.appdata.xml

# Install man page
install -d %{buildroot}%{_mandir}/man6
install -p -m 644 %{SOURCE3} %{buildroot}%{_mandir}/man6/

# Symlink system font
rm %{buildroot}%{_datadir}/%{name}/data/misc/Vera.ttf
ln -s %{_datadir}/fonts/bitstream-vera-sans-fonts/Vera.ttf \
    %{buildroot}%{_datadir}/%{name}/data/misc/Vera.ttf

%files
%doc README.txt changelog.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6*

%changelog
%autochangelog
