%global source0_hash 6a1b1348b99e79da957a0d9e237395a54757a09db7e0c0809f6c30668b69da3b
%global somajor 2
Name:           guvcview
Version:        2.2.2
Release:        1%{?dist}
Summary:        GTK+ UVC Viewer and Capturer
License:        GPL-2.0-or-later
URL:            http://guvcview.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.tar.bz2
Patch:          0001-Add-missing-libavutil-includes-for-av_image_get_buff.patch
Patch:          %{name}-ffmpeg8.patch
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(sfml-graphics)
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n guvcview-libs -f %{oreon_filedir}/guvcview-libs.list
%files -n guvcview-devel -f %{oreon_filedir}/guvcview-devel.list

%changelog

%autochangelog
