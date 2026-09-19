%global source0_hash 7e524e1ecd08dd876df9333667185200d59dddf2a64c93994d60ef772fd469d9

Name:           zasx
Version:        1.30
Release:        43%{?dist}
Summary:        Asteroid like game with powerups
License:        GPL-2.0-or-later AND Giftware
URL:            https://www.allegro.cc/depot/Zasx/
# Original link (down): http://www.bob.allegronetwork.com/zasx/zasx130s.zip
Source0:        zasx130s.zip
Source1:        zasx.desktop
Source2:        zasx.appdata.xml
Patch0:         zasx-1.30-fixes.patch
Patch1:         zasx-1.30-datadir.patch
Patch2:         zasx-1.30-format-security.patch
Patch3:         zasx-1.30-locale-fix.patch
Patch4:         zasx-1.30-remove-al-fix-aliases.patch
Patch5:         zasx-1.30-Makefile.patch
BuildRequires:  gcc make
BuildRequires:  dumb-devel ImageMagick desktop-file-utils libappstream-glib
Requires:       hicolor-icon-theme

%description
Shoot the asteroids before they hit your ship and collect power ups to restore
your shields and improve your weapons. The game features single and dualplayer 
mode, joystick, music and sound.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Zasx
sed -i 's/\r//' copying.txt readme.txt docs/index.html docs/%{name}.css
mv docs html

%build
make %{?_smp_mflags} PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS -fsigned-char -Wno-deprecated-declarations" \
  LDFLAGS="$RPM_LD_FLAGS"
convert -transparent black -resize 64x64 %{name}.ico %{name}.png

%install
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{name}.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc readme.txt html
%license copying.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

%changelog
%autochangelog
