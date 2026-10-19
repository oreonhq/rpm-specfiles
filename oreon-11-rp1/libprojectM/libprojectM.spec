%global source0_hash 3733c6bf1873cb6af5e2a5d24e678f525970c63ad994355fa9d375115663b8f7
%global reltag rc7
%global commit0 f2e0a32368e73a26746b0ac04a9182b23256825f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Name:       libprojectM
Version:    4.1.7
Release:        1%{?dist}
Summary:        The libraries for the projectM music visualization plugin
License:    LGPLv2+
URL:        https://github.com/projectM-visualizer/projectm
Source0:        https://github.com/projectM-visualizer/projectm/archive/v%{version}/libprojectM-%{version}.tar.gz
Patch1:     0001-Build-projectM_qt-shared-lib-instead-static-lib.patch
Patch2:     0002-Generate-libproject-qt.pc.patch
Patch3:     0003-With-shared-lib-libprojectM-qt-we-don-t-need-this-an.patch
Requires:       bitstream-vera-sans-fonts
Requires:  bitstream-vera-sans-mono-fonts
Provides:  libprojectM-qt = %{version}-%{release}
Obsoletes: libprojectM-qt < %{version}-%{release}
Obsoletes: projectM-libvisual < %{version}-%{release}
# oreon:deps
BuildRequires:  bitstream-vera-sans-fonts
BuildRequires:  bitstream-vera-sans-mono-fonts
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libgomp
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(sdl2)
# /oreon:deps
%description
projectM is an awesome music visualizer. There is nothing better in the world
of Unix. projectM's greatness comes from the hard work of the community. Users
like you can create presets that connect music with incredible visuals.
projectM is an LGPL'ed reimplementation of Milkdrop under OpenGL. All projectM
requires is a video card with 3D acceleration and your favorite music.

%package    devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}, pkgconfig
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package qt
Summary:    The Qt frontend to the projectM visualization plugin
License:    GPL-2.0-or-later
%description qt
projectM-qt is a GUI designed to enhance the projectM user and preset writer
experience.  It provides a way to browse, search, rate presets and setup
preset playlists for projectM-jack and projectM-pulseaudio.

%package qt-devel
Summary:    Development files for %{name}-qt
Requires:   %{name}-qt = %{version}-%{release}
Requires:   pkgconfig libprojectM-devel qt-devel
%description qt-devel
The %{name}-qt-devel package contains libraries and header files for
developing applications that use %{name}-qt.

%package -n projectM-jack
Summary:    The projectM visualization plugin for jack
License:    GPLv2+ and MIT
%description -n projectM-jack
This package allows the use of the projectM visualization plugin through any
JACK compatible applications.

%package -n projectM-pulseaudio
Summary:    The projectM visualization plugin for pulseaudio
License:    GPLv2+ and MIT
%description -n projectM-pulseaudio
This package allows the use of the projectM visualization plugin through any
pulseaudio compatible applications.

%package -n projectM-libvisual
Summary:    The projectM visualization plugin for libvisual
License:    GPLv2+ and LGPLv2+ and MIT
%description -n projectM-libvisual
This package allows the use of the projectM visualization plugin through any
libvisual compatible applications.

%package -n projectM-SDL
Summary:    The projectM visualization plugin for SDL
License:    GPLv2+ and LGPLv2+ and MIT
%description -n projectM-SDL
This package allows the use of the projectM visualization plugin through any
SDL2 compatible applications.

%prep

#setup -q -n projectm-%%{commit0}
#setup -q -n projectm-%%{version}-%{reltag}
%autosetup -p1 -n projectm-%{version}

#replace by symlink
rm -r fonts/*
ln -s %{_datadir}/fonts/bitstream-vera-sans-mono-fonts/VeraMono.ttf fonts/
ln -s %{_datadir}/fonts/bitstream-vera-sans-fonts/Vera.ttf fonts/

chmod -x LICENSE.txt
chmod -x presets/tests/README.md

find -name "*.?pp" -type f -exec chmod -x {} ';'
find -name "*.c" -exec chmod -x {} ';'
find -name "*.h" -exec chmod -x {} ';'
find -name "*inl" -exec chmod -x {} ';'

%build

./autogen.sh
%configure --disable-static --disable-rpath --enable-sdl --enable-threading \
    --enable-gles --with-gnu-ld --with-x
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -delete
find %{buildroot} -name "*inl" -exec chmod -x {} ';'
find %{buildroot} -name "*milk" -exec chmod -x {} ';'
find %{buildroot} -name "*prjm" -exec chmod -x {} ';'
desktop-file-validate %{buildroot}%{_datadir}/applications/projectM-pulseaudio.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/projectM-jack.desktop
%oreon_autofiles projectM-jack usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles projectM-pulseaudio usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles projectM-libvisual usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles projectM-SDL usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libprojectM-devel -f %{oreon_filedir}/libprojectM-devel.list
%files -n libprojectM-qt -f %{oreon_filedir}/libprojectM-qt.list
%files -n libprojectM-qt-devel -f %{oreon_filedir}/libprojectM-qt-devel.list
%files -n projectM-jack -f %{oreon_filedir}/projectM-jack.list
%files -n projectM-pulseaudio -f %{oreon_filedir}/projectM-pulseaudio.list
%files -n projectM-libvisual -f %{oreon_filedir}/projectM-libvisual.list
%files -n projectM-SDL -f %{oreon_filedir}/projectM-SDL.list

%changelog

%autochangelog
