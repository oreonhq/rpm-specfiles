%global source0_hash none

%global reltag rc7
%global commit0 f2e0a32368e73a26746b0ac04a9182b23256825f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:       libprojectM
Version:    3.1.12
Release:    14%{?dist}
Summary:    The libraries for the projectM music visualization plugin
License:    LGPLv2+
URL:        https://github.com/projectM-visualizer/projectm
Source0:    https://github.com/projectM-visualizer/projectm/archive/v%{version}/libprojectM-%{version}.tar.gz
#Source0:    https://github.com/projectM-visualizer/projectm/archive/v%%{version}-%%{reltag}/libprojectM-%%{version}-%%{reltag}.tar.gz
#Source0:    https://github.com/projectM-visualizer/projectm/archive/%%{commit0}/%%{name}-%%{shortcommit0}.tar.gz
Patch1:     0001-Build-projectM_qt-shared-lib-instead-static-lib.patch
Patch2:     0002-Generate-libproject-qt.pc.patch
Patch3:     0003-With-shared-lib-libprojectM-qt-we-don-t-need-this-an.patch
#Patch1:     projectM-disable_native_plugins.patch
#Patch3:     projectm-3.1.0-autotools.patch

BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  libgomp
BuildRequires:  pkgconfig(glesv2)
#BuildRequires:  pkgconfig(glew)
#BuildRequires:  pkgconfig(glm)
BuildRequires:  glm-devel
BuildRequires:  pkgconfig(sdl2)
# libprojectM-qt
BuildRequires:  pkgconfig(Qt5Core)
#BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Widgets)
#BuildRequires:  pkgconfig(Qt5Xml)
#BuildRequires:  cmake(Qt5LinguistTools)
#projectM-jack
BuildRequires:  jack-audio-connection-kit-devel
#projectM-libvisual
%if !0%{?rhel}
#BuildRequires:  libvisual-devel = 1:0.4.0
%endif
#projectM-pulseaudio
BuildRequires:  pkgconfig(libpulse)
#BuildRequires:  llvm-devel

BuildRequires:  bitstream-vera-sans-fonts
BuildRequires:  bitstream-vera-sans-mono-fonts
BuildRequires:  make

Requires:       bitstream-vera-sans-fonts
Requires:  bitstream-vera-sans-mono-fonts

Provides:  libprojectM-qt = %{version}-%{release}
Obsoletes: libprojectM-qt < %{version}-%{release}
Obsoletes: projectM-libvisual < %{version}-%{release}

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
# Automatically converted from old format: GPLv2+ - review is highly recommended.
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
#export CXXFLAGS="%{optflags} -Wl,--as-needed"
./autogen.sh
%configure --disable-static --disable-rpath --enable-sdl --enable-threading \
    --enable-gles --with-gnu-ld --with-x

#  --enable-emscripten     Build for web with emscripten
#  --enable-llvm           Support for JIT using LLVM
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete
find %{buildroot} -name "*inl" -exec chmod -x {} ';'
find %{buildroot} -name "*milk" -exec chmod -x {} ';'
find %{buildroot} -name "*prjm" -exec chmod -x {} ';'

desktop-file-validate %{buildroot}%{_datadir}/applications/projectM-pulseaudio.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/projectM-jack.desktop

%files
%doc src/libprojectM/ChangeLog
%doc AUTHORS.txt README.md
%license src/libprojectM/COPYING
%{_libdir}/libprojectM.so.*
%{_datadir}/projectM/

%files devel
%{_bindir}/projectM-unittest
%{_includedir}/libprojectM
%{_libdir}/libprojectM.so
%{_libdir}/pkgconfig/libprojectM.pc

%files qt
%license src/projectM-qt/COPYING
%{_libdir}/libprojectM_qt*.so.*
%{_datadir}/icons/hicolor/scalable/apps/projectM.svg

%files qt-devel
%doc src/projectM-qt/ReadMe
#{_includedir}/%%{name}-qt
%{_libdir}/libprojectM_qt*.so
%{_libdir}/pkgconfig/libprojectM-qt*.pc

%files -n projectM-jack
%doc src/projectM-jack/ChangeLog
%license src/projectM-jack/COPYING
%{_bindir}/projectM-jack
%{_datadir}/applications/projectM-jack.desktop
%{_mandir}/man1/projectM-jack.1*

%files -n projectM-pulseaudio
%doc  src/projectM-pulseaudio/ChangeLog
%license src/projectM-pulseaudio/COPYING
%{_bindir}/projectM-pulseaudio
%{_datadir}/applications/projectM-pulseaudio.desktop
%{_mandir}/man1/projectM-pulseaudio.1*

%files -n projectM-SDL
%{_bindir}/projectMSDL

%if 0 && !0%{?rhel}
%files -n projectM-libvisual
%doc src/projectM-libvisual/AUTHORS src/projectM-libvisual/ChangeLog
%license src/projectM-libvisual/COPYING
%{_libdir}/libvisual-0.4/
%endif

%changelog
%autochangelog
