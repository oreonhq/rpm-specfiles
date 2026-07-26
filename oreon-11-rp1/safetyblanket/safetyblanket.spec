%global source0_hash 60d0f4e684439ac79bcaa44bd24c7ff56ed631d8d5ed826252025d701601d667

Name:           safetyblanket
Version:        1.01
Release:        21%{?dist}
Summary:        Creepy blanket simulator

#See LICENSE.txt file in source for details
#All code is zlib excluding slam.lua and AnAL.lua, which is MIT
#All assets are CC-BY 4.0, excluding font, which is CC-BY 3.0
# Automatically converted from old format: zlib and MIT and CC-BY - review is highly recommended.
License:        Zlib AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-CC-BY
URL:            http://tangramgames.dk/games/safetyblanket/
Source0:        https://github.com/SimonLarsen/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Patch for appdata, manpage, execution script, and desktop file
Patch0:         %{name}-appdata.patch
#Patch for LOVE v0.10.2
#https://github.com/SimonLarsen/safetyblanket/commit/5a3387b73bb5bd85718742ab813d9df44d075cd0
Patch1:         0001-Updated-for-L-VE-11.0.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildArch:      noarch
Requires:       love

# List the arches that love builds on
ExclusiveArch: %{arm} %{ix86} x86_64 aarch64 ppc64le

#From the website (see URL above)
%description
Safety Blanket was developed in 48 hours for the Ludum Dare 29 game jam.
It’s bed time, the monsters are out to get you, and your blanket is just too
small to cover your body!
Cover your exposed limbs to fend off the approaching tentacles.
The tentacles will only go for your feet, hands and head.
If the tentacles reach you it’s game over!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i 's/VERSION/%{version}/g' appdata/%{name}.6

%build
#love "binary" files are just zipped sources, but should exclude appdata/docs
zip -r %{name}.love . -x appdata/* -x appdata/ -x LICENSE.txt

%install
#Install love file
install -p -D -m 0644 %{name}.love \
  %{buildroot}/%{_datadir}/%{name}/%{name}.love
#Install execution script
install -p -D -m 0755 appdata/%{name} \
  %{buildroot}/%{_bindir}/%{name}
#Install manpage
install -p -D -m 0644 appdata/%{name}.6 \
  %{buildroot}/%{_mandir}/man6/%{name}.6
#Install appdata.xml and verify
install -p -D -m 0644 appdata/%{name}.appdata.xml \
  %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet \
  %{buildroot}/%{_datadir}/appdata/*.appdata.xml
#Install desktop, icon:
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  appdata/%{name}.desktop
install -p -D -m 0644 res/gfx/title_text1.png \
  %{buildroot}/%{_datadir}/pixmaps/%{name}.png

%files
%license LICENSE.txt
%{_mandir}/man6/%{name}.*
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/*.appdata.xml

%changelog
%autochangelog
