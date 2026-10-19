%global source0_hash 043cb0c23ce99bf99e3f6500403e92d926ae37dce992026e7fc6301eb08270bb
Name:           ballbuster
Version:        1.0
Release:        48%{?dist}
Summary:        Move the paddle to bounce the ball and break all the bricks
License:        GPL-2.0-or-later
Source0:        BallBusterX.zip
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        %{name}.appdata.xml
Patch0:         ballbuster-unix.patch.gz
Patch1:         ballbuster-1.0-gcc43.patch
Patch2:         ballbuster-1.0-gcc6.patch
Patch3:         ballbuster-1.0-better-fullscreen-handling.patch
Patch4:         ballbuster-1.0-html-path-fix.patch
Requires:       hicolor-icon-theme opengl-games-utils
# oreon:deps
BuildRequires:  ClanLib1-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
# /oreon:deps
%description
Game inspired by one of the great classics. The purpose of the game is to
remove all the bricks on the screen, by hitting them with a ball. You can
control the ball by bouncing it back at the bricks with a paddle which you
control with your mouse. The game features: A built in level editor, 20 power
ups and special effects (particle, alpha, rotating, and zooming).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -p1
sed -i 's/\r//g' COPYING credits.txt ExtremeUpdates.txt manual.html html/*

%build

make %{?_smp_mflags} PREFIX=%{_prefix} \
  CFLAGS="$RPM_OPT_FLAGS `pkg-config --cflags clanCore-1.0` -fpermissive"
%install
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
