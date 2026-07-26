%global source0_hash 2057028b51a81ea7d5d1d5de843510829778ac9d2dae49e8990427c21667c8e2

Name:           auriferous
Version:        1.0.1
Release:        48%{?dist}
Summary:        Game inspired by the classic Loderunner
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://auriferous.sourceforge.net/
# This is http://downloads.sourceforge.net/auriferous/auriferous-1.0.1.tar.bz2
# With the nonfree auriferous/music/jungle.ogg song removed
Source0:        %{name}-%{version}-clean.tar.bz2
# Same as in the tarbal with one additional column of transparant pixels added
# to the right, the original is one column to small causing memory corruption
# (clanlib really should complain, but instead it accesses random memory).
Source1:        playerr.png
Source2:        auriferous.desktop
Source3:        auriferous.appdata.xml
Patch0:         auriferous-1.0.1-fixes.patch
Patch1:         auriferous-1.0.1-destdir.patch
Patch2:         auriferous-1.0.1-extra-keys.patch
Patch3:         auriferous-1.0.1-silence-looping-warn.patch
Patch4:         auriferous-1.0.1-gcc8.patch
Patch5:         auriferous-1.0.1-crash-on-exit-fix.patch
Patch6:         auriferous-1.0.1-warnings-fixes.patch
Patch7:         auriferous-configure-c99.patch
BuildRequires:  gcc-c++
BuildRequires:  ClanLib06-devel >= 0.6.5-16
BuildRequires:  desktop-file-utils libappstream-glib
BuildRequires: make
Requires:       hicolor-icon-theme

%description
An arcade style like game. The goal is to fight out all gold from the caves and
go into in the door. Sounds simple, but try it. The challenge: Because some bad
blue Monks want prevent you from that, they bite of your head if the catch you,
good luck. Further the caves(levels) are often like mazes with dangers and
traps, to pass them you need a lot of skill.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
touch -r configure.in auriferous/Makefile.am
cp -a %{SOURCE1} auriferous/pics/game

%build
export CXXFLAGS="$RPM_OPT_FLAGS -Wno-switch -Wno-unused-result -Wno-write-strings"
%configure
%make_build

%install
%make_install
ln -s aqua.ogg $RPM_BUILD_ROOT%{_datadir}/%{name}/music/jungle.ogg

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications  %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 small_%{name}.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -p -m 644 %{name}.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc AUTHORS NEWS README TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
%autochangelog
