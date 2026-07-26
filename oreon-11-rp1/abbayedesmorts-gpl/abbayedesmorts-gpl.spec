%global source0_hash dd0933e3c48cdd3d6cf7125a0bafd5be806e5708d1e47cf519a3721d7436e1f3

Name:           abbayedesmorts-gpl
Version:        2.0.5
Release:        4%{?dist}
Summary:        Platform game set in 13th century

# Graphics and Sounds are licensed under
# Creative Commons 3.0 Attribution license.
License:        GPL-3.0-only AND CC-BY-3.0
# Original Windows game by locomalito
# https://locomalito.com/abbaye_des_morts.php
URL:            https://github.com/nevat/abbayedesmorts-gpl 
Source0:        https://github.com/nevat/abbayedesmorts-gpl/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme

%description
In the 13th century, the Cathars, who preach about good Christian beliefs, 
were being expelled by the Catholic Church out of the Languedoc region in 
France.

One of them, called Jean Raymond, found an old church in which to hide, not 
knowing that beneath its ruins lay buried an ancient evil.

A style close to Spectrum ZX, with its dark background and bright colors, 
proper fit with the story, because it does look old and somewhat horrifying. 
Also, the gameplay is directly inspired by Manic Miner and Jet Set Willy.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Enable verbose build
sed -i 's/@$(CC)/$(CC)/' Makefile

%build
%set_build_flags
%make_build

%install
%make_install

# Install icons
rm %{buildroot}%{_datadir}/pixmaps/abbaye.png
cp -a abbaye.png abbaye48.png
for px in 48 64 128; do
  install -d %{buildroot}%{_datadir}/icons/hicolor/${px}x${px}/apps
  install -p -m 644 abbaye${px}.png \
    %{buildroot}%{_datadir}/icons/hicolor/${px}x${px}/apps/abbaye.png
done

# Validate desktop file
desktop-file-validate %{buildroot}%{_datadir}/applications/abbaye.desktop

# Validate AppData file
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/abbaye.appdata.xml

%files
%{_bindir}/abbayev2
%{_datadir}/abbayev2
%{_datadir}/appdata/abbaye.appdata.xml
%{_datadir}/applications/abbaye.desktop
%{_datadir}/icons/hicolor/*/apps/abbaye.png
%doc ReadMe.md ChangeLog.md screenshots
%license COPYING

%changelog
%autochangelog
