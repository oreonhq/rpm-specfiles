%global source0_hash 709c7e657b328a6f7d331298c6264f172528489d28cab107c40c483c392340b2
Name:           amoebax
Version:        0.2.1
Release:        1%{?dist}
Summary:        Action-Puzzle Game
License:        GPL-2.0-or-later AND LAL-1.3
URL:            http://www.emma-soft.com/games/amoebax/
Source0:        http://www.emma-soft.com/games/amoebax/download/amoebax-%{version}.tar.bz2
Patch0:         amoebax-0.2.0-gcc43.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
Amoebax is a cute and addictive action-puzzle game. Due an awful mutation,
some amoeba's species have started to multiply until they take the world if
you can't stop them. Fortunately the mutation made then too unstable and
lining up four or more will make them disappear.

Follow Kim or Tom through 6 levels in their quest to prevent the cute
multiplying amoebas to take the world and become the new Amoeba Master. Watch
out for the cute but amoeba's controlled creatures that will try to put and
end to your quest.

Amoebax is designed with levels for everyone, from children to adults. With
the training mode everybody will quickly become a master and the tournament
mode will let you have a good time with your friends. There is also catchy
music, funny sound effects, and beautiful screens that sure appeal to everyone
in the family.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build

%configure
make %{?_smp_mflags}
%install
%make_install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
EmailAddress:  jordi@emma-soft.com
SentUpstream:  2014-09-17
-->
<application>
  <id type="desktop">amoebax.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A match-4 action puzzle game</summary>
  <description>
    <p>
      Amoebax is a cute action puzzle game where pairs of amoeba fall down,
      and when you match 4 colored amoeba in a row or column they disappear.
      There are 6 levels of difficulty, and also a split-screen mode to battle
      the amoeba-matching fun with a friend.
    </p>
  </description>
  <url type="homepage">http://www.emma-soft.com/games/amoebax/</url>
  <screenshots>
    <screenshot type="default">http://www.emma-soft.com/games/amoebax/screenshots/training.png</screenshot>
    <screenshot>http://www.emma-soft.com/games/amoebax/screenshots/normal.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF
rm $RPM_BUILD_ROOT%{_datadir}/doc/%{name}/manual.pdf
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
mv $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.svg \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
