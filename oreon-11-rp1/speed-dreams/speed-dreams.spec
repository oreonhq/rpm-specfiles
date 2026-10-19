%global source0_hash none
Name:           speed-dreams
Version:        2.4.2
Release:        4%{?dist}
Epoch:          1
Summary:        3D Open Racing Simulation
License: GPL-2.0-or-later AND LAL-1.3
URL:            https://www.speed-dreams.net
Source0:        %{name}-%{version}.tar.xz
ExcludeArch:    s390x
Provides:       %{name} = %{epoch}:%{version}-%{release}
Requires:       %{name}-robots-base = %{epoch}:%{version}
Requires:       opengl-games-utils
Requires:       bitstream-vera-sans-fonts
Requires:       dejavu-lgc-sans-fonts
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
# oreon:deps
BuildRequires:  FreeSOLID-devel
BuildRequires:  OpenSceneGraph-devel
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_mixer-devel
BuildRequires:  bitstream-vera-sans-fonts
BuildRequires:  chrpath
BuildRequires:  cjson-devel
BuildRequires:  cmake
BuildRequires:  dejavu-lgc-sans-fonts
BuildRequires:  desktop-file-utils
BuildRequires:  enet-devel
BuildRequires:  expat-devel
BuildRequires:  freealut-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libGL-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libappstream-glib
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libogg-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  minizip-devel
BuildRequires:  plib-devel
BuildRequires:  rhash-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
    for lib in $(find . -type f -name \*.so ); do
        chmod 755 $lib
        chrpath --replace %{_libdir}/games/%{name}-2/lib $lib
    done
    excluded=$( echo '%{__requires_exclude}' | tr '|' ':' )
    for lib in *.so; do
        if [ "${excluded/${lib}/}" = "$excluded" ]; then
            echo "ERROR: $lib not filtered in __requires_exclude" >&2
            exit 2
        fi
    done
popd
chrpath -r %{_libdir}/games/speed-dreams-2/lib %{buildroot}%{_bindir}/speed-dreams-2
chrpath -r %{_libdir}/games/speed-dreams-2/lib %{buildroot}%{_bindir}/sd2-accc
chrpath -r %{_libdir}/games/speed-dreams-2/lib %{buildroot}%{_bindir}/sd2-nfs2ac
chrpath -r %{_libdir}/games/speed-dreams-2/lib %{buildroot}%{_bindir}/sd2-nfsperf
chrpath -r %{_libdir}/games/speed-dreams-2/lib %{buildroot}%{_bindir}/sd2-trackgen
rm -f %{buildroot}%{_includedir}/3D/Makefile.am
rm -f %{buildroot}%{_includedir}/SOLID/Makefile.am
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.appdata.xml
find %{buildroot} -size 0 -delete
%files -f %{oreon_filedir}/main.list
%files -n speed-dreams-robots-base -f %{oreon_filedir}/speed-dreams-robots-base.list
%files -n speed-dreams-devel -f %{oreon_filedir}/speed-dreams-devel.list

%changelog

%autochangelog
