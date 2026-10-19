%global source0_hash none
Name:		alienarena
Summary:        Multiplayer retro sci-fi deathmatch game
Version:	7.71.7
Release:        1%{?dist}
License:	GPL-2.0-or-later AND Zlib
Source0:        alienarena-%{version}.tar.xz
Source2:	GPL.acebot.txt
Source3:	org.alienarena.alienarena.metainfo.xml
Patch3:		alienarena-7.66-no-qglBlitFramebufferEXT.patch
Patch5:		alienarena-7.71.2-svn5674-system-ode-double.patch
Patch6:		alienarena-7.71.4-gcc10.patch
Patch7:		alienarena-c99.patch
Patch9:		alienarena-7.71.6-fix-incompatible-pointer.patch
Patch11:	alienarena-7.71.6-fix-bad-sprintf-use.patch
Patch12:	alienarena-7.71.6-fix-CL_GetLatestGameVersion.patch
Patch13:	alienarena-7.71.7-minizip-fix.patch
URL:		http://red.planetarena.org/
Requires:	%{name}-data = 1:%{version}
Requires:	desktop-file-utils >= 0.9, opengl-games-utils
Requires:	openal-soft%{?_isa}
ExcludeArch:	s390x
# oreon:deps
BuildRequires:  curl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  minizip-devel
BuildRequires:  ode-devel
BuildRequires:  openal-soft-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Alien Arena is a furious frag fest with arenas ranging from the small
to the massive. With game modes such as Capture The Flag and Tactical,
there are terrific team-based experiences to be had as well as 1v1
duels, free-for-all and dozens of mutators to alter the game play to
your liking.

%package server
Summary:	Dedicated server for alienarena, the FPS game
Requires:	%{name}-data = 1:%{version}
%description server
Alien Arena is a furious frag fest with arenas ranging from the small
to the massive. With game modes such as Capture The Flag and Tactical,
there are terrific team-based experiences to be had as well as 1v1
duels, free-for-all and dozens of mutators to alter the game play to
your liking.

This is the dedicated server.

%package data
Summary:	Game Data for alienarena, the FPS game
Epoch:		1
BuildArch:	noarch
License:	GPL-2.0-or-later
%description data
Alien Arena is a furious frag fest with arenas ranging from the small
to the massive. With game modes such as Capture The Flag and Tactical,
there are terrific team-based experiences to be had as well as 1v1
duels, free-for-all and dozens of mutators to alter the game play to
your liking.

This is the game data.

%prep

%setup -q -n %{name}-%{version}

%patch -P3 -p1 -b .no-qglBlitFramebufferEXT
%patch -P5 -p1 -b .ode-double
%patch -P6 -p1 -b .gcc10
%patch -P7 -p1 -b .c99
%patch -P9 -p1 -b .fix-incompatible-pointer
%patch -P11 -p1 -b .fix-bad-sprintf-use
%patch -P12 -p1 -b .fix-CL_GetLatestGameVersion
%patch -P13 -p1 -b .minizip-fix

# We don't want the bundled ode code.
rm -rf source/unix/ode

# Copy license clarification for acebot
cp -p %{SOURCE2} .

# clean up end-line encoding
[[ -e docs/README.txt ]] && %{__sed} -i 's/\r//' docs/README.txt

# So, AlienArena now "uses" openal by dlopening the library, which is hardcoded
# to "libopenal.so". That file only lives in openal-devel, so we need to adjust
# the hardcoding.
LIBOPENAL=`ls %{_libdir}/libopenal.so.? | cut -d "/" -f 4`
sed -i "s|\"libopenal.so\"|\"$LIBOPENAL\"|g" source/unix/qal_unix.c

%build

export PTHREAD_LIBS="-lpthread"
export PTHREAD_CFLAGS="-pthread"
%global optflags %{optflags} -fcommon
%configure  --without-xf86dga --with-system-libode
make %{?_smp_mflags}
%install
%make_install
%{__mkdir_p} %{buildroot}%{_datadir}/metainfo
cp -a %{SOURCE3} %{buildroot}%{_datadir}/metainfo
%{__mkdir_p} %{buildroot}%{_datadir}/applications
sed -i 's|/usr/games/alien-arena --quiet|alienarena-wrapper|g' unix_dist/alien-arena.desktop
sed -i 's|alien-arena.png|alien-arena|g' unix_dist/alien-arena.desktop
desktop-file-install --dir %{buildroot}%{_datadir}/applications	unix_dist/alien-arena.desktop
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
cp -a unix_dist/alien-arena.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
ln -s opengl-game-wrapper.sh %{buildroot}/%{_bindir}/%{name}-wrapper
cp -a GPL.acebot.txt %{buildroot}%{_defaultdocdir}/%{name}/
%oreon_autofiles alienarena-server usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles alienarena-data usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n alienarena-server -f %{oreon_filedir}/alienarena-server.list
%files -n alienarena-data -f %{oreon_filedir}/alienarena-data.list

%changelog

%autochangelog
