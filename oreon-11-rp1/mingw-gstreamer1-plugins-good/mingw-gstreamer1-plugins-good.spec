%global source0_hash 4ce274d207bd7b404b8b07ed669b4ebac81849b23636e455b23150dee1e3595e
%{?mingw_package_header}
%global         api_version     1.0
Name:           mingw-gstreamer1-plugins-good
Version:        1.29.2
Release:        1%{?dist}
Summary:        Cross compiled GStreamer1 plug-ins good
License:        LGPL-2.0-or-later
URL:            http://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gst-plugins-good/gst-plugins-good-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  meson
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-cairo
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gdk-pixbuf
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-gstreamer1
BuildRequires:  mingw32-gstreamer1-plugins-base
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libsoup
BuildRequires:  mingw32-orc
BuildRequires:  mingw32-speex
BuildRequires:  mingw32-taglib
BuildRequires:  mingw32-wavpack
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-cairo
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gdk-pixbuf
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-gstreamer1
BuildRequires:  mingw64-gstreamer1-plugins-base
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libsoup
BuildRequires:  mingw64-orc
BuildRequires:  mingw64-speex
BuildRequires:  mingw64-taglib
BuildRequires:  mingw64-wavpack
BuildRequires:  pkgconfig
# /oreon:deps
%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

GStreamer Good Plugins is a collection of well-supported plugins of
good quality and under the LGPL license.

# Mingw32
%package -n mingw32-gstreamer1-plugins-good
Summary:        Cross compiled GStreamer1 plug-ins good
Requires:       mingw32-gstreamer1 >= %{version}
Requires:       mingw32-gstreamer1-plugins-base >= %{version}
%description -n mingw32-gstreamer1-plugins-good
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

GStreamer Good Plugins is a collection of well-supported plugins of
good quality and under the LGPL license.

# Mingw64
%package -n mingw64-gstreamer1-plugins-good
Summary:        Cross compiled GStreamer1 plug-ins good
Requires:       mingw64-gstreamer1 >= %{version}
Requires:       mingw64-gstreamer1-plugins-base >= %{version}
%description -n mingw64-gstreamer1-plugins-good
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

GStreamer Good Plugins is a collection of well-supported plugins of
good quality and under the LGPL license.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gst-plugins-good-%{version}
%oreon_prep
%build

%mingw_meson \
    -Dpackage-name='Fedora Mingw gstreamer1-plugins-good package' \
    -Dpackage-origin='http://download.fedora.redhat.com/fedora' \
    -Dexamples=disabled \
    -Dmonoscope=disabled \
    -Daalib=disabled \
    -Dlibcaca=disabled \
    -Dshout2=disabled \
    -Dflac=disabled \
    -Djack=disabled
%mingw_ninja
%install
%mingw_ninja_install
rm -rf %{buildroot}%{mingw32_libdir}/gstreamer-%{api_version}/*.dll.a
rm -rf %{buildroot}%{mingw64_libdir}/gstreamer-%{api_version}/*.dll.a
%mingw_find_lang gstreamer1-plugins-good --all-name
%oreon_autofiles mingw32-gstreamer1-plugins-good usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-gstreamer1-plugins-good usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-gstreamer1-plugins-good -f %{oreon_filedir}/mingw32-gstreamer1-plugins-good.list
%files -n mingw64-gstreamer1-plugins-good -f %{oreon_filedir}/mingw64-gstreamer1-plugins-good.list

%changelog

%autochangelog
