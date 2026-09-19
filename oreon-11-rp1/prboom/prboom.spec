%global source0_hash 226c1c470f8cc983327536404f405a1d026cf0a5188c694a1243cc8630014bae

%define waddir  %{_datadir}/doom

Name:           prboom
Version:        2.5.0
Release:        38%{?dist}
Summary:        Open source port of the DOOM game engine

License:        GPL-2.0-or-later
URL:            http://prboom.sourceforge.net/
Source0:        http://downloads.sourceforge.net/prboom/prboom-2.5.0.tar.gz

Patch0:         pointer-types.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  SDL_mixer-devel SDL_net-devel
BuildRequires:  libGLU-devel
BuildRequires:  autoconf >= 2.69-10

Requires:       freedoom

%description
prboom is an open-source port of Doom, the classic 3D first-person shooter
game.  It totally outclassed any 3D world games that preceded it, with amazing
speed, flexibility, and outstanding gameplay. The specs to the game were
released, and thousands of extra levels were written by fans of the game; even
today new levels are written for Doom faster then any one person could play
them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P 0 -p0

%build
autoreconf -vif
sed -i /HAVE_LIBPNG/d configure
export CPPFLAGS="$CPPFLAGS -fcommon -std=gnu17"
%configure --enable-gl --disable-cpu-opt --program-prefix='' --with-waddir=%{waddir} --disable-i386-asm

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Move the binaries out of the crufty /usr/games directory
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mv $RPM_BUILD_ROOT/usr/games/* $RPM_BUILD_ROOT/%{_bindir}

# Remove the doc files that will get picked up in the files
# section below.
rm -rf $RPM_BUILD_ROOT/%{_docdir}

%files
%license COPYING
%{_bindir}/prboom
%{_bindir}/prboom-game-server
%dir %{waddir}
%{waddir}/prboom.wad
%{_mandir}/man5/*
%{_mandir}/man6/*
%doc NEWS AUTHORS README
%doc doc/README.compat doc/README.demos doc/MBF.txt doc/MBFFAQ.txt doc/boom.txt

%changelog
%autochangelog
