%global source0_hash eaaaa0bb455812e2277d14c9be8dd3136e2c607e34efd401a33d4b384b2f0253
%{?mingw_package_header}
%global         api_version      1.0
Name:           mingw-gstreamer1-plugins-base
Version:        1.29.2
Release:        1%{?dist}
Summary:        Cross compiled GStreamer1 media framework base plug-ins
License:        LGPL-2.0-or-later
URL:            http://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-%{version}.tar.xz
Patch0:         gst-plugins-base-build.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  meson
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-gstreamer1
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw32-libogg
BuildRequires:  mingw32-libtheora
BuildRequires:  mingw32-libvorbis
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw32-orc
BuildRequires:  mingw32-pango
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-gstreamer1
BuildRequires:  mingw64-gtk3
BuildRequires:  mingw64-libogg
BuildRequires:  mingw64-libtheora
BuildRequires:  mingw64-libvorbis
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw64-orc
BuildRequires:  mingw64-pango
BuildRequires:  orc-compiler
BuildRequires:  perl-interpreter
# /oreon:deps
%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of well-maintained base plug-ins.

# Win32
%package -n mingw32-gstreamer1-plugins-base
Summary:        Cross compiled GStreamer media framework base plug-ins
Requires:       mingw32-gstreamer1 >= %{version}
%description  -n mingw32-gstreamer1-plugins-base
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of well-maintained base plug-ins.

# Win64
%package -n mingw64-gstreamer1-plugins-base
Summary:        Cross compiled GStreamer media framework base plug-ins
Requires:       mingw64-gstreamer1 >= %{version}
%description  -n mingw64-gstreamer1-plugins-base
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of well-maintained base plug-ins.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gst-plugins-base-%{version}
%oreon_prep
%build

%mingw_meson                                                            \
    -Dpackage-name='Fedora MinGW GStreamer-plugins-base package'        \
    -Dpackage-origin='http://download.fedoraproject.org'                \
    -D doc=disabled \
    -D orc=enabled \
    -D tremor=disabled \
    -D tests=disabled \
    -D examples=disabled
%mingw_ninja
%install
%mingw_ninja_install
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{mingw32_libdir}/gstreamer-%{api_version}/*.dll.a
rm -rf %{buildroot}%{mingw64_libdir}/gstreamer-%{api_version}/*.dll.a
%mingw_find_lang gst-plugins-base-%{api_version}
%oreon_autofiles mingw32-gstreamer1-plugins-base usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-gstreamer1-plugins-base usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-gstreamer1-plugins-base -f %{oreon_filedir}/mingw32-gstreamer1-plugins-base.list
%files -n mingw64-gstreamer1-plugins-base -f %{oreon_filedir}/mingw64-gstreamer1-plugins-base.list

%changelog

%autochangelog
