%global source0_hash bb78b750e7bce7aa7c11bd35906bb08a49acc7c50bf29629af380eecd153894d
Summary:        3D multi-player tank battle game
Name: bzflag
Version: 2.4.30
Release:        1%{?dist}
License: LicenseRef-Callaway-LGPLv2
URL: http://bzflag.org
Source0:        https://download.bzflag.org/bzflag/source/%{version}/bzflag-%{version}.tar.bz2
Source1: bzflag.desktop
Source2: bzflag.sysconfig
Source3: bzflag.service
Requires: opengl-games-utils
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  c-ares-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  libGLU-devel
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libcurl-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  sed
BuildRequires:  systemd
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles bzflag-maps-sample usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post bzflag.service
%preun

%systemd_preun bzflag.service
%postun

%systemd_postun_with_restart bzflag.service
%files -f %{oreon_filedir}/main.list
%files -n bzflag-maps-sample -f %{oreon_filedir}/bzflag-maps-sample.list

%changelog

%autochangelog
