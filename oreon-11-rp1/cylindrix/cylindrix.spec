%global source0_hash 276c0ba8f63a5d4f360c78b603579bc2b0213eee266d674033e1f1df5f2f6629

Name: cylindrix
Version:  1.0
Release: 49%{?dist}
Summary: A 3 degrees of freedom combat game

License: LGPL-2.0-only        
URL: http://www.hardgeus.com/cylindrix/
Source0: http://www.hardgeus.com/cylindrix/cylindrix-1.0.tar.bz2
Source1: cylindrix.desktop
Source2: cylindrix.png
Source3: cylindrix.sh
Source4: cylindrix-level10.dat
Patch0: cylindrix-1.0-fix-packing.patch
Patch1: cylindrix-1.0-arch-independ-file-read.patch
Patch2: cylindrix-1.0-use-int-not-long.patch
Patch3: cylindrix-1.0-arch-independ-file-write.patch
Patch4: cylindrix-1.0-object-fopen.patch
Patch5: cylindrix-1.0-configure-c99.patch
Requires: hicolor-icon-theme
BuildRequires:  gcc-c++
BuildRequires: allegro-devel, desktop-file-utils
BuildRequires: make

%description
Cylindrix is a 3-on-3 combat game with 360 degrees of freedom that is
similar to Spectre VR but with a wider variety of ships, as well as the
addition of drivers. Attack and be attacked from all angles as you battle
in huge orbiting arenas that are each unique in physics, atmospheric
conditions, and configuration. You must build your team from 37 warriors
from 10 alien races and select from 8 vehicles, each with unique 
maneuverability, speed, and firepower. The graphics are good, although
structure and ship graphics are a little too monotonous. Gameplay is fast
and furious... so furious, in fact, that it is difficult to differentiate
between friend and foe in the thick of battle. For those who are confident
of their reflexes or have beaten Spectre and Battlezone, though, this game
is worth a try.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p0
%patch -P3 -p0
%patch -P4 -p0
%patch -P5 -p0

%build

%configure
make CFLAGS="$RPM_OPT_FLAGS -Wno-pointer-sign -fcommon -std=gnu17" LIBS="-lm"

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 %{SOURCE3} %{buildroot}%{_bindir}/cylindrix
install -m 755 cylindrix %{buildroot}%{_bindir}/cylindrix-bin

mkdir -p %{buildroot}%{_datadir}/cylindrix

cp -pr 3d_data %{buildroot}%{_datadir}/cylindrix
cp -pr anything.mod %{buildroot}%{_datadir}/cylindrix
cp -pr cylindrx.fli %{buildroot}%{_datadir}/cylindrix
cp -pr gamedata %{buildroot}%{_datadir}/cylindrix
cp -pr pcx_data %{buildroot}%{_datadir}/cylindrix
cp -pr people.dat %{buildroot}%{_datadir}/cylindrix
cp -pr stats %{buildroot}%{_datadir}/cylindrix
cp -pr wav_data %{buildroot}%{_datadir}/cylindrix

#replace broken data file
rm -f %{buildroot}%{_datadir}/cylindrix/gamedata/level10.dat
install -m 644 %{SOURCE4} %{buildroot}%{_datadir}/cylindrix/gamedata/level10.dat

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install            \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps

%files
%{_bindir}/cylindrix*
%{_datadir}/cylindrix/
%license COPYING
%doc AUTHORS
%{_datadir}/applications/cylindrix.desktop
%{_datadir}/icons/hicolor/64x64/apps/cylindrix.png

%changelog
%autochangelog
