%global source0_hash 3d93e4c9fab8d1a7a9bde1a6dbbf04d6cf9d347c134b5128b4586a1d90b63cfb

%global somajor 2

Name:           guvcview
Version:        2.1.0
Release:        10%{?dist}
Summary:        GTK+ UVC Viewer and Capturer
License:        GPL-2.0-or-later
URL:            http://guvcview.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.tar.bz2

# Add missing includes to fix build
# https://sourceforge.net/p/guvcview/tickets/75/
Patch:          0001-Add-missing-libavutil-includes-for-av_image_get_buff.patch
# Fix build with FFmpeg 8
Patch:          %{name}-ffmpeg8.patch

BuildRequires:  autoconf automake libtool
BuildRequires:  gettext-devel intltool
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(sfml-graphics)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description
A simple GTK interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.

%package libs
Summary:        Libraries for %{name}

%description libs
A simple GTK interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.

This package contains the libraries for applications to use %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
A simple GTK interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.

This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-src-%{version}
find . \( -name '*.h' -o -name '*.c' \) -exec chmod -x {} \;

%build
autoreconf -fiv
%configure CC=gcc CXX=g++ --disable-debian-menu --disable-silent-rules --disable-static --enable-sfml --disable-sdl2
%make_build

%install
%make_install doc_DATA=

install -D -m0644 %{buildroot}%{_datadir}/pixmaps/%{name}/%{name}.png \
    %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

find %{buildroot} -name "*.la" -delete

%find_lang %{name} --all-name

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.appdata.xml

%files -f %{name}.lang
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*
%{_datadir}/pixmaps/%{name}/
%{_mandir}/man1/%{name}.1*
%{_metainfodir}/%{name}.appdata.xml

%files libs
%license COPYING
%{_libdir}/libgviewaudio-2.2.so.%{somajor}{,.*}
%{_libdir}/libgviewencoder-2.2.so.%{somajor}{,.*}
%{_libdir}/libgviewrender-2.2.so.%{somajor}{,.*}
%{_libdir}/libgviewv4l2core-2.2.so.%{somajor}{,.*}

%files devel
%{_includedir}/%{name}-%{somajor}/
%{_libdir}/libgviewaudio.so
%{_libdir}/libgviewencoder.so
%{_libdir}/libgviewrender.so
%{_libdir}/libgviewv4l2core.so
%{_libdir}/pkgconfig/libgviewaudio.pc
%{_libdir}/pkgconfig/libgviewencoder.pc
%{_libdir}/pkgconfig/libgviewrender.pc
%{_libdir}/pkgconfig/libgviewv4l2core.pc

%changelog
%autochangelog
