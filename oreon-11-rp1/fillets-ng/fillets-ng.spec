%global source0_hash 329a4d9515d60bebdb657d070824933b993b85864b9d3e302e6361accab992da
Summary:        Fish Fillets Next Generation, a puzzle game with 70 levels
Name: fillets-ng
Version: 1.0.1
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://fillets.sourceforge.net/
Source0:        https://downloads.sf.net/fillets/fillets-ng-%{version}.tar.gz
Source1: fillets.desktop
Source2: fillets.svg
Patch0: fillets-ng-0.8.1-gcc43.patch
Patch1: fillets-ng-1.0.1-lua-5.2.patch
Patch2: fillets-ng-1.0.1-lua-5.4.patch
Patch3: fillets-ng-1.0.1-f35-startup-crash.patch
Requires: fillets-ng-data >= 1.0.1-4
Requires: hicolor-icon-theme
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(lua)
# /oreon:deps
%description
Fish Fillets is strictly a puzzle game. The goal in every of the
seventy levels is always the same: find a safe way out. The fish utter
witty remarks about their surroundings, the various inhabitants of
their underwater realm quarrel among themselves or comment on the
efforts of your fish. The whole game is accompanied by quiet,
comforting music.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .gcc43
%patch -P1 -p0 -b .lua52
%patch -P2 -p1 -b .lua54
%patch -P3 -p1 -b .f35crash

%build

%configure --datadir=%{_datadir}/fillets-ng
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor="" \
    --dir %{buildroot}%{_datadir}/applications \
    %{SOURCE1}
install -D -p -m 0644 %{SOURCE2} \
    %{buildroot}%{_datadir}/icons//hicolor/scalable/apps/fillets.svg
mkdir -p %{buildroot}%{_metainfodir}
cat > %{buildroot}%{_metainfodir}/fillets.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
EmailAddress: ivo@danihelka.net
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">fillets.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>solve the puzzle and help the fish escape</summary>
  <description>
    <p>
      Fish Fillets is a puzzle game where the player has to guide a fish through a series
      of obstacles to escape the maze.
      Fish Fillets features over 70 levels of puzzles and a comforting soundtrack.
    </p>
  </description>
  <url type="homepage">http://fillets.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://fillets.sourceforge.net/img/screenshot/ffng-pyramid.png</screenshot>
    <screenshot>http://fillets.sourceforge.net/img/screenshot/ffng-chest.png</screenshot>
  </screenshots>
</application>
EOF
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/fillets.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
