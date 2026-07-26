%global source0_hash none

Name:           speed-dreams
Version:        2.4.2
Release:        4%{?dist}
Epoch:          1
Summary:        3D Open Racing Simulation

# Speed Dreams source is under GPL-2.0-or-later by default
# https://speed-dreams.net/en/about
License: GPL-2.0-or-later AND LAL-1.3
# Media content: Graphics, sounds, and other artistic works are licensed under LAL-1.3

URL:            https://www.speed-dreams.net
# ------------------------------------------------------------------------------
# retrieve sources and create archive:
# 
# $ git clone --recursive https://forge.a-lec.org/speed-dreams/speed-dreams-code speed-dreams
# $ cd speed-dreams
# $ git checkout tags/v2.4.2
# $ git submodule update --init --recursive
# $ cd ..
# $ mv speed-dreams speed-dreams-2.4.2
# $ tar -cJf speed-dreams-2.4.2.tar.xz speed-dreams-2.4.2
# ------------------------------------------------------------------------------
Source0:        %{name}-%{version}.tar.xz

ExcludeArch:    s390x

Provides:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-robots-base = %{epoch}:%{version}
Requires:       opengl-games-utils
Requires:       bitstream-vera-sans-fonts
Requires:       dejavu-lgc-sans-fonts
BuildRequires:  bitstream-vera-sans-fonts
BuildRequires:  dejavu-lgc-sans-fonts
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  chrpath
BuildRequires:  libcurl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  enet-devel
BuildRequires:  expat-devel
BuildRequires:  freealut-devel
BuildRequires:  freeglut-devel
BuildRequires:  FreeSOLID-devel >= 2.1.2
BuildRequires:  libGL-devel
BuildRequires:  libjpeg-devel
BuildRequires:  zlib-devel
BuildRequires:  libpng-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXrandr-devel
BuildRequires:  plib-devel
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  libogg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  OpenSceneGraph-devel
BuildRequires:  cjson-devel
BuildRequires:  minizip-devel
BuildRequires:  rhash-devel

# Dont provide or require internal libs. Using new rpm builtin filtering,
# see https://docs.fedoraproject.org/en-US/packaging-guidelines/AutoProvidesAndRequiresFiltering/
%global __requires_exclude                       liblearning.so
%global __requires_exclude %{__requires_exclude}|libnetworking.so
%global __requires_exclude %{__requires_exclude}|libraceengine.so
%global __requires_exclude %{__requires_exclude}|librobottools.so
%global __requires_exclude %{__requires_exclude}|libtgf.so
%global __requires_exclude %{__requires_exclude}|libtgfclient.so
%global __requires_exclude %{__requires_exclude}|libtgfdata.so
%global __requires_exclude %{__requires_exclude}|libportability.so
%global __requires_exclude %{__requires_exclude}|libcsnetworking.so

%global __provides_exclude_from %{_libdir}/games/speed-dreams-2/.*\\.so

%description
Speed-Dreams is a 3D racing cars simulator using OpenGL. A Fork of TORCS.
The goal is to have programmed robots drivers racing against each others.
You can also drive yourself with either a wheel, keyboard or mouse.

%package robots-base
Summary:       The Open Racing Car Simulator additional dirt tracks
BuildArch:     noarch
Requires:      %{name} =  %{epoch}:%{version}-%{release}

%description robots-base
This package contains additional tracks for the game.

%package devel
Summary:       The Open Racing Car Simulator development files
Requires:      %{name}%{?_isa} =  %{epoch}:%{version}-%{release}
            
%description devel
This package contains the development files for the game.

%prep
%autosetup -p1 -n %{name}-%{version}

# delete unused header file on arm achitecture
sed -i -e 's|#include "OsgReferenced.h"||g' src/modules/graphic/osggraph/Sky/OsgDome.h

# remove obsolete encoding key from .desktop file
sed -i '/^Encoding=/d' speed-dreams.desktop.in
sed -i '/^Name=/c\Name=/Speed Dreams 2' speed-dreams.desktop.in
sed -i '/^Icon=/c\Icon=/usr/share/games/speed-dreams-2/data/icons/icon.png' speed-dreams.desktop.in

# unbundle freesolid
rm -rf freesolid
rm -rf src/tools/trackeditor

# fixes spurious-executable-perm
# https://sourceforge.net/p/speed-dreams/tickets/605/
find . -name '*.c' -o -name '*.h' -o -name '*.cpp' -o -name '*.hpp' | \
    xargs chmod 644

%build
%cmake -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo       \
       -DCMAKE_SKIP_RPATH:BOOL=OFF                    \
       -DOPTION_DEBUG:STRING=ON                       \
       -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed"  \
       -DSD_BINDIR:PATH=bin                           \
       -DOPTION_3RDPARTY_SOLID:BOOL=ON                \
       -DOPTION_TRACKEDITOR:BOOL=OFF                  \
       -DOPTION_OFFICIAL_ONLY:BOOL=ON                 \
       -DCMAKE_C_FLAGS="%{optflags}"                  \
       -DCMAKE_CXX_FLAGS="%{optflags}"
%cmake_build

%install
%cmake_install
find %{buildroot} -type f -name "*.cmake" -delete

install -Dm 0644 packaging/appdata/speed-dreams-2.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

pushd %{buildroot}%{_libdir}/games/%{name}-2
    # Change rpath to refer only private lib dir.
    for lib in $(find . -type f -name \*.so ); do
        # Bug: cmake should make so-files 755 on Fedora by default.
        chmod 755 $lib
        chrpath --replace %{_libdir}/games/%{name}-2/lib $lib
    done

    # Check that %%{buildroot}%%{_libdir}/games/%%{name}-2/lib doesn't 
    # contain unfiltered libs.
    excluded=$( echo '%{__requires_exclude}' | tr '|' ':' )
    for lib in *.so; do
        if [ "${excluded/${lib}/}" = "$excluded" ]; then
            echo "ERROR: $lib not filtered in __requires_exclude" >&2
            exit 2
        fi
    done
popd

# ERROR   0001: file '/usr/bin/speed-dreams-2' contains a standard runpath '/usr/lib64' in [/usr/lib64/games/speed-dreams-2/lib:/usr/lib64]
# ERROR   0001: file '/usr/bin/sd2-accc' contains a standard runpath '/usr/lib64' in [/usr/lib64/games/speed-dreams-2/lib:/usr/lib64]
# ERROR   0001: file '/usr/bin/sd2-nfs2ac' contains a standard runpath '/usr/lib64' in [/usr/lib64/games/speed-dreams-2/lib:/usr/lib64]
# ERROR   0001: file '/usr/bin/sd2-nfsperf' contains a standard runpath '/usr/lib64' in [/usr/lib64/games/speed-dreams-2/lib:/usr/lib64]
# ERROR   0001: file '/usr/bin/sd2-trackgen' contains a standard runpath '/usr/lib64' in [/usr/lib64/games/speed-dreams-2/lib:/usr/lib64]
chrpath -r %{_libdir}/games/speed-dreams-2/lib %{buildroot}%{_bindir}/speed-dreams-2
chrpath -r %{_libdir}/games/speed-dreams-2/lib %{buildroot}%{_bindir}/sd2-accc
chrpath -r %{_libdir}/games/speed-dreams-2/lib %{buildroot}%{_bindir}/sd2-nfs2ac
chrpath -r %{_libdir}/games/speed-dreams-2/lib %{buildroot}%{_bindir}/sd2-nfsperf
chrpath -r %{_libdir}/games/speed-dreams-2/lib %{buildroot}%{_bindir}/sd2-trackgen

# Remove obsolete or unnecessary files from the installation directory
rm -f %{buildroot}%{_includedir}/3D/Makefile.am
rm -f %{buildroot}%{_includedir}/SOLID/Makefile.am

# Replace bundled fonts with symlink to system fonts
ln -sf /usr/share/fonts/dejavu/DejaVuSans.ttf \
       %{buildroot}%{_datadir}/games/speed-dreams-2/data/fonts/DejaVuLGCSans.ttf
ln -sf /usr/share/fonts/bitstream-vera/Vera.ttf \
       %{buildroot}%{_datadir}/games/speed-dreams-2/data/fonts/Vera.ttf
ln -sf /usr/share/fonts/bitstream-vera/VeraBd.ttf \
       %{buildroot}%{_datadir}/games/speed-dreams-2/data/fonts/VeraBd.ttf
ln -sf /usr/share/fonts/bitstream-vera/VeraBI.ttf \
       %{buildroot}%{_datadir}/games/speed-dreams-2/data/fonts/VeraBI.ttf
ln -sf /usr/share/fonts/bitstream-vera/VeraMono.ttf \
       %{buildroot}%{_datadir}/games/speed-dreams-2/data/fonts/VeraMono.ttf
ln -sf ../Vera.ttf \
       %{buildroot}%{_datadir}/games/speed-dreams-2/data/fonts/vera/Vera.ttf

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.appdata.xml

# remove zero length files
find %{buildroot} -size 0 -delete

%files
%license LICENSE
%doc README.md
%{_mandir}/man6/*
%{_bindir}/%{name}-2
%{_bindir}/sd2-*
%{_libdir}/games/%{name}-2/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/games/%{name}-2/
%exclude %{_datadir}/games/%{name}-2/cars/
%exclude %{_datadir}/games/%{name}-2/config/
%exclude %{_datadir}/games/%{name}-2/data/
%exclude %{_datadir}/games/%{name}-2/drivers/
%exclude %{_datadir}/games/%{name}-2/tracks/

%files robots-base
%{_datadir}/games/%{name}-2/cars/
%{_datadir}/games/%{name}-2/config/
%{_datadir}/games/%{name}-2/data/
%{_datadir}/games/%{name}-2/drivers/
%{_datadir}/games/%{name}-2/tracks/

%files devel
%{_includedir}/%{name}-2/

%changelog
%autochangelog
