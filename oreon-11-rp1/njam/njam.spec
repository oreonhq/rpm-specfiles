%global source0_hash 8ed3eee3f387ce5ecdab7dd528f98cf77f65971510964000f2f1dfbf8b6f3000

Name:           njam
Version:        1.25
Release:        49%{?dist}
Summary:        Maze-game, eat all the cookies while avoiding the badguys
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://njam.sourceforge.net/
# should be
# http://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.tar.gz
# but that file has got corrupted, hurray for sourceforge :(
Source0:        %{name}-%{version}-src.tar.gz
Source1:        njam.6
Source2:	njam.desktop
Patch0:         njam-1.25-drop-setgid.patch
Patch1:         njam-1.25-html.patch
Patch2:         njam-1.25-leveledit.patch
Patch3:         njam-1.25-gcc45.patch
Patch4:         njam-1.25-rhbz767015.patch
Patch5:         njam-1.25-format-security.patch
Patch6: njam-configure-c99.patch
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  SDL-devel SDL_mixer-devel SDL_image-devel SDL_net-devel 
BuildRequires:  ImageMagick desktop-file-utils
Requires:       hicolor-icon-theme 

%description
Njam is a fast-paced maze-game where you must eat all the cookies while
avoiding the badguys. Special cookies give you the power to freeze or eat the
bad guys. The game features single and multiplayer modes, network play,
duelling and cooperative games, great music and sound effects, customizable
level skins, many different levels and an integrated level editor.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}-src
%patch -P0 -p1 -z .setgid
%patch -P1 -p1
%patch -P2 -p1 -z .leveledit
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1

%build
%configure
make %{?_smp_mflags}
convert -transparent black njamicon.ico %{name}.png

%install
%make_install

# make install installs the docs under /usr/share/njam. We want them in %doc.
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/README
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/levels/readme.txt
rm -fr $RPM_BUILD_ROOT%{_datadir}/%{name}/html

# clean up cruft
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}.*
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/njamicon.ico

# we want the hiscore in /var/lib/games
mkdir -p $RPM_BUILD_ROOT%{_var}/lib/games
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/hiscore.dat \
  $RPM_BUILD_ROOT%{_var}/lib/games/%{name}.hs

# add the manpage (courtesy of Debian)
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man6

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
install -p -m 644 %{name}.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps

%files
%doc COPYING ChangeLog NEWS README TODO levels/readme.txt html
%attr(2755,root,games) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6.gz
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%config(noreplace) %attr (0664,root,games) %{_var}/lib/games/%{name}.hs

%changelog
%autochangelog
