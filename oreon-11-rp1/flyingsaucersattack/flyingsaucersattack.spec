%global source0_hash 06d8f2e1d9329049d96ad87507203ea89e947d99dfd646f117c645ef1e281915
Name:           flyingsaucersattack
Version:        1.20h
Release:        1%{?dist}
Summary:        Shoot down the attacking UFOs and to save the city
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-CC-BY-SA
URL:            http://www.dennisbusch.de/fsa.php
Source0:        http://www.dennisbusch.de/software/fsa/fuga120h.zip
Source1:        %{name}.png
Source2:        %{name}.desktop
Source3:        %{name}.appdata.xml
Patch0:         flyingsaucersattack-1.20h-unixify.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  allegro-devel
BuildRequires:  desktop-file-utils
BuildRequires:  dumb-devel
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
# /oreon:deps
%description
F.S.A. (Flying Saucers Attack) aka F.U.G.A. (Fliegende Untertassen greifen an)
is a kind of mixture between two old Atari2600 games.
It comes in German and English language.

You'll see a screen with your city that you have to save against 30 Alien
attack waves in three different difficulty levels.

You shoot attacking UFOs with two cannons positioned at the left and right
borders of the screen. The UFOs will first bomb away all your buildings then
send in little green men to dig tunnels to blow your cannons which results
in a game over.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n fuga120h
%patch -P0 -p1 -b .unix
for i in docs/*; do
  sed -i 's/\r//' $i;
done

%build

%make_build -C sources \
  CFLAGS="$RPM_OPT_FLAGS -Wno-deprecated-declarations -Wno-deprecated -Wno-write-strings -Wno-unused-result -Wno-format-security"
%install
%make_install -C sources
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
