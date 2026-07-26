%global source0_hash 67d697df9092a98aa79e50eefb079d80f66c48974a68b36a82241161dbcc6e51

Summary:         Drive and jump with some kind of car across the moon
Name:            moon-buggy
Version:         1.0.51
Release:         40%{?dist}
License:         GPL-1.0-or-later
URL:             https://seehuhn.de/pages/%{name}
Source0:         https://seehuhn.de/media/programs/%{name}-%{version}.tar.gz
Source1:         https://seehuhn.de/media/programs/%{name}-sound-%{version}.tar.gz
Source2:         %{name}.desktop
Source3:         %{name}-sound.desktop
Patch0:          moon-buggy-1.0.51-pause.patch
Patch1:          moon-buggy-1.0.51-sound.patch
Patch2:          https://github.com/seehuhn/moon-buggy/commit/c929f2c1bdd173686b295a003e4f6dda5f0fa98a.patch#/moon-buggy-1.0.51-c23.patch
BuildRequires:   gcc, make, ncurses-devel, texinfo
%if 0%{!?_without_sound:1}
BuildRequires:   esound-devel, desktop-file-utils, autoconf, automake
%endif

%description
Moon-buggy is a simple character graphics game where you drive some kind
of car across the moon's surface. Unfortunately there are dangerous craters
there. Fortunately your car can jump over them! 

The game has some resemblance of the classic arcade game moon-patrol which
was released in 1982. A clone of this game was released for the Commodore
C64 in 1983. The present, ASCII art version of moon-buggy was written many
years later by Jochen Voss.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -a 1
%patch -P0 -p1 -b .pause
%if 0%{!?_without_sound:1}
%patch -P1 -p1 -b .sound
%patch -P2 -p1 -b .c23
mv -f %{name}-%{version}/* .
autoreconf -f -i
%endif

%build
%configure --sharedstatedir=%{_localstatedir}/games
%make_build

%install
%make_install

# Create zero-sized highscore file
touch $RPM_BUILD_ROOT%{_localstatedir}/games/%{name}/mbscore

# Install working *.desktop files and an icon
%if 0%{!?_without_sound:1}
desktop-file-install --vendor "" --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
desktop-file-install --vendor "" --dir=$RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE3}

install -D -p -m 644 %{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
%endif

# Some file cleanups
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

# Convert everything to UTF-8
iconv -f iso-8859-1 -t utf-8 -o ChangeLog.utf8 ChangeLog
sed -i 's|\r$||g' ChangeLog.utf8
touch -c -r ChangeLog ChangeLog.utf8
mv -f ChangeLog.utf8 ChangeLog

iconv -f iso-8859-1 -t utf-8 -o TODO.utf8 TODO
sed -i 's|\r$||g' TODO.utf8
touch -c -r TODO TODO.utf8
mv -f TODO.utf8 TODO

%files 
%license COPYING
%doc ANNOUNCE AUTHORS ChangeLog README THANKS
%if 0%{!?_without_sound:1}
%doc README.sound
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-sound.desktop
%endif
%attr(2755,root,games) %{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%{_infodir}/%{name}.info.*
%attr(0775,root,games) %{_localstatedir}/games/%{name}
%verify(not md5 size mtime) %config(noreplace) %attr(664,root,games) %{_localstatedir}/games/%{name}/mbscore

%changelog
%autochangelog
