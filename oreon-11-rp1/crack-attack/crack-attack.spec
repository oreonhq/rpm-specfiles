%global source0_hash 0d1691aad9890ae3340ad9e842d78850db7eded2dcc1aff4f52dafc8d25e477d

Summary:        Puzzle action game
Name:           crack-attack
Version:        1.1.14
Release:        58%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.nongnu.org/crack-attack/
Source0:        http://savannah.nongnu.org/download/%{name}/%{name}-%{version}.tar.bz2
Source1:        %{name}-sounds.tar.gz
Source2:        %{name}-music.tar.gz
Patch0:         crack-attack-1.1.14-glutInit.patch
Patch1:         crack-attack-1.1.14-sanitize.patch
Patch2:         crack-attack-1.1.14-audio.patch
Patch3:         crack-attack-1.1.14-gcc43.patch
Patch4:         crack-attack-1.1.14-audio-ppc.patch
Patch5:         crack-attack-1.1.14-format-security.patch
Patch6:         crack-attack-1.1.14-rhbz1065649.patch
Patch7:         crack-attack-configure-c99.patch
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  libstdc++-devel desktop-file-utils ImageMagick
BuildRequires:  SDL-devel gtk2-devel pkgconfig SDL_mixer-devel freeglut-devel
BuildRequires:  mesa-libGLU-devel libXmu-devel
BuildRequires: make

%description
A puzzle/action game in which you rush to eliminate colored blocks
before they fill your screen. Particularly clever eliminations cause
garbage to clutter your opponent's screen. Who will survive the
longest!? Playable both online and off.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 1 -a 2
%patch -P0 -p1 -b .glutinit
%patch -P1 -p1 -b .sanitize
%patch -P2 -p1 -b .audio
%patch -P3 -p1 -b .gcc43
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
# fixup provided desktop file
sed -i -e 's/%{name}\.xpm/%{name}\.png/' \
  -e 's/Application;Games/Game;BlocksGame/' data/%{name}.desktop
echo "Comment=A Puzzle Game" >> data/%{name}.desktop

%build
%configure --enable-sound
make %{?_smp_mflags}

%install
%make_install

#copy Music and Sounds
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds
install -m 644 data/sounds/* $RPM_BUILD_ROOT%{_datadir}/%{name}/sounds
cp -a music $RPM_BUILD_ROOT%{_datadir}/%{name}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
%if 0%{?fedora} && 0%{?fedora} < 19
  --vendor fedora --delete-original \
%endif
  $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps
convert -resize 48x48 $RPM_BUILD_ROOT%{_datadir}/%{name}/logo.tga \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
convert $RPM_BUILD_ROOT%{_datadir}/%{name}/logo.tga \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%files
%doc doc/*.html doc/*.jpg doc/*.xpm AUTHORS COPYING README ChangeLog
%doc music-sound-copyright.txt
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6.gz

%changelog
%autochangelog
