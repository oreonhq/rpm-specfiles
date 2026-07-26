%global source0_hash 759c1253075d1e72691bc1e770b24cdd51917041fd1857c1daf85b65a6686460

Name:           pingus
Version:        0.7.6
Release:        53%{?dist}
Summary:        Guide the penguins safely home before they drop of the cliff
License:        GPL-2.0-or-later
URL:            http://pingus.seul.org/
Source0:        http://pingus.googlecode.com/files/%{name}-%{version}.tar.bz2
Source1:        pingus.desktop
Source2:        pingus.png
Patch1:         pingus-0.7.6-gcc470-udl.patch
Patch2:         pingus-0.7.6-missing-header.patch
Patch3:         pingus-0.7.6-boost-169.patch
Patch4:         pingus-0.7.6-python3.patch
Patch5:         pingus-gcc13.patch
Patch6:         includes.patch
BuildRequires: make
BuildRequires:  SDL_mixer-devel SDL_image-devel boost-devel libpng-devel
BuildRequires:  physfs-devel python3-scons desktop-file-utils gcc-c++
Requires:       hicolor-icon-theme

%description
You take command in the game of a bunch of small penguins
and have to guide them around in levels. Since the penguins
walk on their own, the player can only influence them by giving them commands,
like build a bridge, dig a hole or redirect all penguins in the other
direction. The goal of each level is to reach the exit, for which multiple
combination of commands are necessary. The game is presented in a 2D site view.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 1 -p0
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p0
%patch -P 5 -p1
%patch -P 6 -p0
iconv -f ISO8859-2 -t UTF8 AUTHORS > AUTHORS.tmp
mv AUTHORS.tmp AUTHORS

%build
scons CCFLAGS="$RPM_OPT_FLAGS -std=gnu++17" LINKFLAGS="$RPM_LD_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
make install PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT
install -p -m 644 doc/man/%{name}.6 $RPM_BUILD_ROOT%{_mandir}/man6/
rm -rf $RPM_BUILD_ROOT%{_mandir}/man1/

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Edgar Muniz Berlinck <edgar.vv@gmail.com> -->
<!--
EmailAddress: grumbel@gmail.com
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">pingus.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Free version of Lemmings Puzzle Game</summary>
  <description>
    <p>
      Pingus is a Puzzle game where you need to save all your little penguins
      using the capabilities provided to you in the current level.
    </p>
    <p>
      The basic game idea is to be like Lemmings game.
      This versions has some other cool
      stuff like a world map and some very cool secret levels.
    </p>
  </description>
  <url type="homepage">http://pingus.seul.org/</url>
  <screenshots>
    <screenshot type="default">http://pingus.seul.org/images/screen_0.7.0-4.jpg</screenshot>
    <screenshot>http://pingus.seul.org/images/screen_0.7.0-3.jpg</screenshot>
  </screenshots>
  <launchable type="desktop-id">pingus.desktop</launchable>
</application>
EOF

%files
%license COPYING
%doc AUTHORS NEWS README TODO
%{_bindir}/%{name}
%{_bindir}/%{name}.bin
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_mandir}/man6/%{name}.6*

%changelog
%autochangelog
