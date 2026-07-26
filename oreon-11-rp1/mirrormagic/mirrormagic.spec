%global source0_hash c79ad19d461c080011e12f5b9e6b1d3de4b8325e452ef4bb6e8a63a62ce9ffec

Name:           mirrormagic
Version:        3.0.0
Release:        22%{?dist}
Summary:        Puzzle game where you steer a beam of light using mirrors
License:        GPL-1.0-or-later
URL:            http://www.artsoft.org/mirrormagic/
Source0:        http://www.artsoft.org/RELEASES/unix/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}.appdata.xml
Patch0:         %{name}-%{version}-yesno.patch
Patch1:         %{name}-%{version}-fcommon-fix.patch
Patch2:         %{name}-%{version}-c23.patch
BuildRequires:  gcc make
BuildRequires:  SDL2_image-devel SDL2_mixer-devel SDL2_net-devel
BuildRequires:  libappstream-glib desktop-file-utils
Requires:       hicolor-icon-theme

%description
MirrorMagic is a game where you shoot around obstacles to collect energy using
your beam. It is similar to "Mindbender" (Amiga) from the same author. The goal
is to work out how to get around obstacles to shoot energy containers with your
beam, thereby opening the path to the next level. Included are many levels
familiar from the games "Deflektor" and "Mindbender".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
rm levels/Classic_Games/classic_mindbender/*.level.orig
iconv -f ISO_8859-1 -t UTF8 CREDITS > CREDITS.tmp
touch -r CREDITS CREDITS.tmp
mv CREDITS.tmp CREDITS

%build
# parallel build has been disabled because for some unknown reason
# it leads to unknown symbols during the linking of the mirrormagic binary
make PROGBASE=%{name} RO_GAME_DIR=%{_datadir}/%{name} \
  OPTIONS="$RPM_OPT_FLAGS -DUSE_USERDATADIR_FOR_COMMONDATA" \
  EXTRA_LDFLAGS="$RPM_OPT_FLAGS $RPM_LD_FLAGS" sdl2

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
cp -a graphics levels music sounds $RPM_BUILD_ROOT%{_datadir}/%{name}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc CREDITS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%changelog
%autochangelog
