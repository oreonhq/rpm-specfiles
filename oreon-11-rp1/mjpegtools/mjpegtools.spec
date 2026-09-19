%global source0_hash b180536d7d9960b05e0023a197b00dcb100929a49aab71d19d55f4a1b210f49a

Name:           mjpegtools
Version:        2.2.1
Release:        12%{?dist}
Summary:        Tools to manipulate MPEG data
# Most sources are GPLv2+ except the following which don't mention "or later":
# mplex/*
# utils/yuv4mpeg_intern.h
# And scripts/lav2mpeg just says "GPL"
License:        GPL-2.0-or-later AND GPL-2.0-only AND GPL-1.0-or-later
URL:            https://mjpeg.sourceforge.io/
Source:         https://downloads.sourceforge.net/mjpeg/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch:          7b1989861157b1af5b98a797bd7a9080609a31f2.patch
Patch:          https://sources.debian.org/data/main/m/mjpegtools/1%3A2.1.0%2Bdebian-8.1/debian/patches/10_usr_local.patch

BuildRequires:  autoconf automake libtool
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig(libquicktime) >= 0.9.8
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libdv) >= 0.9
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.4.0
BuildRequires:  pkgconfig(sdl) >= 1.1.3
BuildRequires:  SDL_gfx-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# mencoder for lav2avi.sh
#Requires:       mencoder%%{?_isa}
# ffmpeg main package, y4mscaler and which for anytovcd.sh
Requires:       /usr/bin/ffmpeg
Requires:       which

%description
The mjpeg programs are a set of tools that can do recording of videos
and playback, simple cut-and-paste editing and the MPEG compression of
audio and video under Linux.  This package contains mjpegtools console
utilities.

%package        gui
Summary:        GUI tools to manipulate MPEG data
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-lav%{?_isa} = %{version}-%{release}

%description    gui
The mjpeg programs are a set of tools that can do recording of videos
and playback, simple cut-and-paste editing and the MPEG compression of
audio and video under Linux.  This package contains mjpegtools GUI
utilities.

%package        libs
Summary:        MJPEGtools libraries

%description    libs
The mjpeg programs are a set of tools that can do recording of videos
and playback, simple cut-and-paste editing and the MPEG compression of
audio and video under Linux.  This package contains libraries which are
used by mjpegtools and also by several other projects.

%package        lav
Summary:        MJPEGtools lavpipe libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    lav
The mjpeg programs are a set of tools that can do recording of videos
and playback, simple cut-and-paste editing and the MPEG compression of
audio and video under Linux.  This package contains libraries used by
mjpegtools.

%package        devel
Summary:        Development files for mjpegtools libraries 
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The mjpeg programs are a set of tools that can do recording of videos
and playback, simple cut-and-paste editing and the MPEG compression of
audio and video under Linux.  This package contains development files
for building applications that use mjpegtools libraries.

%package        lav-devel
Summary:        Development files for mjpegtools lavpipe libraries 
Requires:       %{name}-lav%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    lav-devel
The mjpeg programs are a set of tools that can do recording of videos
and playback, simple cut-and-paste editing and the MPEG compression of
audio and video under Linux.  This package contains development files
for building applications that use mjpegtools lavpipe libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf -fiv

for f in docs/yuvfps.1 ; do
    iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f
done

%build
%configure --disable-static
%make_build

%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
%if 0%{?rhel} && 0%{?rhel} < 10
rm -f %{buildroot}%{_libdir}/*.la
%endif
# too broken/outdated to be useful in 1.[89].0 (and would come with dep chain)
rm -f %{buildroot}%{_bindir}/mpegtranscode
# requires mencoder
rm -f %{buildroot}%{_bindir}/lav2avi.sh

%files
%doc CHANGES ChangeLog AUTHORS BUGS README.lavpipe NEWS TODO
%{_bindir}/anytovcd.sh
%{_bindir}/jpeg2yuv
%{_bindir}/lav*
%{_bindir}/*.flt
%{_bindir}/mjpeg_simd_helper
%{_bindir}/mp*2enc
%{_bindir}/mplex
%{_bindir}/*toy4m
%{_bindir}/png2yuv
%{_bindir}/y4m*
%{_bindir}/ypipe
%{_bindir}/yuv*
%exclude %{_bindir}/glav
%exclude %{_bindir}/lavplay
%exclude %{_bindir}/qttoy4m
%exclude %{_bindir}/y4mhist
%exclude %{_bindir}/y4mtoqt
%exclude %{_bindir}/yuvplay
%{_mandir}/man1/jpeg2yuv.1*
%{_mandir}/man1/lav*.1*
%{_mandir}/man1/mjpegtools.1*
%{_mandir}/man1/mp*2enc.1*
%{_mandir}/man1/mplex.1*
%{_mandir}/man1/*toy4m.1*
%{_mandir}/man1/png2yuv.1*
%{_mandir}/man1/y4m*.1*
%{_mandir}/man1/yuv*.1*
%exclude %{_mandir}/man1/lavplay.1*
%exclude %{_mandir}/man1/yuvplay.1*
%{_mandir}/man5/yuv4mpeg.5*
%{_infodir}/mjpeg-howto.info*

%files gui
%{_bindir}/glav
# lavplay and yuvplay won't save console util users from X11 and SDL
# dependencies as long as liblavplay is in -lav, but they're inherently
# GUI tools -> include them here
%{_bindir}/lavplay
%{_bindir}/qttoy4m
%{_bindir}/y4mhist
%{_bindir}/y4mtoqt
%{_bindir}/yuvplay
%{_mandir}/man1/lavplay.1*
%{_mandir}/man1/yuvplay.1*

%files libs
%license COPYING
%{_libdir}/libmjpegutils-2.2.so.0{,.*}
%{_libdir}/libmpeg2encpp-2.2.so.0{,.*}
%{_libdir}/libmplex2-2.2.so.0{,.*}

%files lav
%{_libdir}/liblavfile-2.2.so.0{,.*}
%{_libdir}/liblavjpeg-2.2.so.0{,.*}
%{_libdir}/liblavplay-2.2.so.0{,.*}

%files devel
%{_includedir}/%{name}
%exclude %{_includedir}/%{name}/*lav*.h
%{_libdir}/libmjpegutils.so
%{_libdir}/libmpeg2encpp.so
%{_libdir}/libmplex2.so
%{_libdir}/pkgconfig/%{name}.pc

%files lav-devel
%{_includedir}/%{name}/*lav*.h
%{_libdir}/liblavfile.so
%{_libdir}/liblavjpeg.so
%{_libdir}/liblavplay.so

%changelog
%autochangelog
