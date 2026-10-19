%global source0_hash b180536d7d9960b05e0023a197b00dcb100929a49aab71d19d55f4a1b210f49a
Name:           mjpegtools
Version:        2.2.1
Release:        12%{?dist}
Summary:        Tools to manipulate MPEG data
License:        GPL-2.0-or-later AND GPL-2.0-only AND GPL-1.0-or-later
URL:            https://mjpeg.sourceforge.io/
Source0:        https://downloads.sourceforge.net/mjpeg/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch:          7b1989861157b1af5b98a797bd7a9080609a31f2.patch
Patch:          https://sources.debian.org/data/main/m/mjpegtools/1%3A2.1.0%2Bdebian-8.1/debian/patches/10_usr_local.patch
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       /usr/bin/ffmpeg
Requires:       which
# oreon:deps
BuildRequires:  SDL_gfx-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libdv)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libquicktime)
BuildRequires:  pkgconfig(sdl)
# /oreon:deps
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
rm -f %{buildroot}%{_bindir}/mpegtranscode
rm -f %{buildroot}%{_bindir}/lav2avi.sh
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mjpegtools-gui -f %{oreon_filedir}/mjpegtools-gui.list
%files -n mjpegtools-libs -f %{oreon_filedir}/mjpegtools-libs.list
%files -n mjpegtools-lav -f %{oreon_filedir}/mjpegtools-lav.list
%files -n mjpegtools-devel -f %{oreon_filedir}/mjpegtools-devel.list
%files -n mjpegtools-lav-devel -f %{oreon_filedir}/mjpegtools-lav-devel.list

%changelog

%autochangelog
