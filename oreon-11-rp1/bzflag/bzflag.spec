%global source0_hash 5dd3a4a92ba934e620954123aebb4bf05ad20cf3ff744fd4e1e8c723bc5cabcd

Summary: 3D multi-player tank battle game
Name: bzflag
Version: 2.4.28
Release: 4%{?dist}
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2
URL: http://bzflag.org
Source0: https://download.bzflag.org/bzflag/source/%{version}/bzflag-%{version}.tar.bz2
Source1: bzflag.desktop
Source2: bzflag.sysconfig
Source3: bzflag.service
BuildRequires: libXxf86vm-devel
BuildRequires: libXext-devel
BuildRequires: libSM-devel
BuildRequires: libICE-devel
BuildRequires: libX11-devel
BuildRequires: libGLU-devel
BuildRequires: make
BuildRequires: glew-devel
BuildRequires: gcc-c++
BuildRequires: desktop-file-utils
BuildRequires: SDL2-devel
BuildRequires: ncurses-devel
BuildRequires: libcurl-devel
BuildRequires: c-ares-devel
BuildRequires: zlib-devel
BuildRequires: sed
BuildRequires: systemd
Requires: opengl-games-utils

%description
BZFlag is a 3D multi-player tank battle game  that  allows users to play
against each other in a networked environment.  There are five teams: red,
green, blue, purple and rogue (rogue tanks are black).  Destroying a player
on another team  scores a win, while being destroyed or destroying a teammate
scores a loss.  Rogues have no teammates (not even other rogues), so they
cannot shoot teammates and they do not have a team score.
There are two main styles of play: capture-the-flag and free-for-all.

%package maps-sample
Summary: Sample maps for bzflag
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch: noarch

%description maps-sample
This package contains sample world maps for bzflag.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}

# Create a sysusers.d config file
cat >bzflag.sysusers.conf <<EOF
u bzflag - 'BZFlag game server' %{_datadir}/bzflag -
EOF

%build
# Use PIE because bzflag/bzfs are networked server applications
CFLAGS='-fPIC %{optflags} -fno-strict-aliasing' \
CXXFLAGS='-fPIC %{optflags} -fno-strict-aliasing' \
LDFLAGS='-pie' \
SDL_CFLAGS='-I%{_prefix}/include/SDL -D_GNU_SOURCE=1 -D_REENTRANT' \
%configure --libdir=%{_libdir}/%{name} --with-SDL=2 \
    --prefix=%{_prefix} --exec-prefix=%{_prefix} \
    --with-sdl-prefix=%{_prefix} --with-sdl-exec-prefix=%{_prefix}
%make_build

%install
%make_install
install -D -m 644 package/rpm/bzflag-m.xpm \
    %{buildroot}%{_datadir}/pixmaps/bzflag.xpm
install -D -m 644 misc/art/bzicon-red.svg \
    %{buildroot}%{_datadir}/pixmaps/bzflag.svg
mkdir -p %{buildroot}%{_datadir}/bzflag/maps
install -m 644 misc/maps/*.bzw %{buildroot}%{_datadir}/bzflag/maps
rm -f %{buildroot}%{_libdir}/bzflag/*.la
rm -f %{buildroot}%{_datadir}/bzflag/bzflag.desktop

ln -snf opengl-game-wrapper.sh %{buildroot}%{_bindir}/bzflag-wrapper
sed 's:^Exec=\(.*\)$:Exec=\1-wrapper:g' < %{SOURCE1} > bzflag.desktop

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --dir %{buildroot}%{_datadir}/applications bzflag.desktop

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
<!-- Copyright 2014 Ravi Srinivasan <ravishankar.srinivasan@gmail.com> -->
<!--
BugReportURL: https://sourceforge.net/p/bzflag/bugs/601/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">bzflag.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>An online multiplayer 3D tank battle game</summary>
  <description>
    <p>
      bzflag is a multiplayer tank battle game with "retro" 3D style graphics.
    </p>
  </description>
  <url type="homepage">http://bzflag.org</url>
  <screenshots>
    <screenshot type="default">http://bzflag.org/resources/screenshots/dantes_inferno_01.jpg</screenshot>
    <screenshot>http://bzflag.org/resources/screenshots/aa_bridge_crossing_01.jpg</screenshot>
    <screenshot>http://bzflag.org/resources/screenshots/pandemonium_01.jpg</screenshot>
  </screenshots>
</application>
EOF

install -Dp -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/bzflag
install -Dp -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/bzflag.service
install -D -m0644 bzflag.sysusers.conf %{buildroot}%{_sysusersdir}/bzflag.conf

%post
%systemd_post bzflag.service

%preun
%systemd_preun bzflag.service

%postun
%systemd_postun_with_restart bzflag.service

%files
%license COPYING
%doc AUTHORS ChangeLog README README.Linux
%{_bindir}/bzadmin
%{_bindir}/bzflag
%{_bindir}/bzflag-wrapper
%{_bindir}/bzfs
%dir %{_libdir}/bzflag
%{_libdir}/bzflag/*.so
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/bzflag
%exclude %{_datadir}/bzflag/maps/*
%{_datadir}/pixmaps/bzflag.xpm
%{_datadir}/pixmaps/bzflag.svg
%{_mandir}/man*/*
%{_sysconfdir}/sysconfig/bzflag
%{_unitdir}/bzflag.service
%{_sysusersdir}/bzflag.conf

%files maps-sample
%{_datadir}/bzflag/maps/*

%changelog
%autochangelog
