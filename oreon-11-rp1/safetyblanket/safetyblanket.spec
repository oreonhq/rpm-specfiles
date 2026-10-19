%global source0_hash 60d0f4e684439ac79bcaa44bd24c7ff56ed631d8d5ed826252025d701601d667
Name:           safetyblanket
Version:        1.01
Release:        21%{?dist}
Summary:        Creepy blanket simulator
License:        Zlib AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-CC-BY
URL:            http://tangramgames.dk/games/safetyblanket/
Source0:        https://github.com/SimonLarsen/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-appdata.patch
Patch1:         0001-Updated-for-L-VE-11.0.patch
BuildArch:      noarch
Requires:       love
ExclusiveArch: %{arm} %{ix86} x86_64 aarch64 ppc64le
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
# /oreon:deps
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

zip -r %{name}.love . -x appdata/* -x appdata/ -x LICENSE.txt
%install
install -p -D -m 0644 %{name}.love \
  %{buildroot}/%{_datadir}/%{name}/%{name}.love
install -p -D -m 0755 appdata/%{name} \
  %{buildroot}/%{_bindir}/%{name}
install -p -D -m 0644 appdata/%{name}.6 \
  %{buildroot}/%{_mandir}/man6/%{name}.6
install -p -D -m 0644 appdata/%{name}.appdata.xml \
  %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
appstream-util validate-relax --nonet \
  %{buildroot}/%{_datadir}/appdata/*.appdata.xml
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  appdata/%{name}.desktop
install -p -D -m 0644 res/gfx/title_text1.png \
  %{buildroot}/%{_datadir}/pixmaps/%{name}.png
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
