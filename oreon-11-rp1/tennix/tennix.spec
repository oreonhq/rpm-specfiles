%global source0_hash d60bba4ca34a4d532012955bf682fb474da3f845b98f47fb5699924feccb9f97

Name:           tennix
Version:        1.3.4
Release:        7%{?dist}
Summary:        A simple tennis game

License:        GPL-2.0-or-later
URL:            http://icculus.org/tennix/
Source0:        https://repo.or.cz/tennix.git/snapshot/tennix-%{version}.tar.gz
Patch1:		tennix-1.0-tnxpath.patch

BuildRequires:  SDL2-devel SDL2_mixer-devel SDL2_image-devel SDL2_ttf-devel SDL2_gfx-devel SDL2_net-devel
BuildRequires:  desktop-file-utils gcc-c++ make

%description
Tennix! is a SDL port of a simple tennis game.
It features a two-player game mode and a single-player mode
against the computer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn tennix-tennix-1.3.4-9c8f18e

%patch -P 1 -p0

%build
./configure --prefix %{_prefix} --disable-python
CFLAGS="%{optflags}" make LIBS="-lm -lSDL2 -lSDL2_mixer -lSDL2_ttf -lSDL2_image -lSDL2_net"
make %{?_smp_mflags}

%install
PREFIX=%{_prefix} make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications           \
                     data/%{name}.desktop

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/scalable/apps/
cp $RPM_BUILD_ROOT/%{_datadir}/pixmaps/%{name}.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/scalable/apps/%{name}.png

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
<!-- Copyright 2014 Your Name <email@address.com> -->
<!--
EmailAddress: m@thp.io
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">tennix.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Tennis simulator</summary>
  <description>
    <p>
      Tennix is a overhead view tennis simulator for one or two players.
      It features locations from all 4 Grand Slam tournaments in Australia,
      France, the USA and England.
    </p>
  </description>
  <url type="homepage">http://icculus.org/tennix/</url>
  <screenshots>
    <screenshot type="default">http://icculus.org/tennix/screenshots/2011/tennix-ingame-2011.png</screenshot>
  </screenshots>
</application>
EOF

%files
%license COPYING
%doc README HACKING TODO
%attr(2755,root,games) %{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man6/%{name}.*
%attr(0664,root,games) /usr/share/tennix/tennix.tnx

%changelog
%autochangelog
