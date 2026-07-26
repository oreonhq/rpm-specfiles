%global source0_hash 1446a4c2a92ff5d78d88e85a599f0038441d53333236f0c72d72f21a9c132497

%{?mingw_package_header}

%global         api_version      1.0

Name:           mingw-gstreamer1-plugins-base
Version:        1.28.1
Release:        1%{?dist}
Summary:        Cross compiled GStreamer1 media framework base plug-ins

License:        LGPL-2.0-or-later
URL:            http://gstreamer.freedesktop.org/
Source:         http://gstreamer.freedesktop.org/src/gst-plugins-base/gst-plugins-base-%{version}.tar.xz
# Fix build
Patch0:         gst-plugins-base-build.patch

BuildArch:      noarch

BuildRequires:  gettext
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  orc-compiler

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gstreamer1 >= %{version}
BuildRequires:  mingw32-libogg >= 1.0
BuildRequires:  mingw32-libvorbis >= 1.0
BuildRequires:  mingw32-libtheora
BuildRequires:  mingw32-orc
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw32-pango
BuildRequires:  mingw32-libxml2

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gstreamer1 >= %{version}
BuildRequires:  mingw64-libogg >= 1.0
BuildRequires:  mingw64-libvorbis >= 1.0
BuildRequires:  mingw64-libtheora
BuildRequires:  mingw64-orc
BuildRequires:  mingw64-gtk3
BuildRequires:  mingw64-pango
BuildRequires:  mingw64-libxml2

BuildRequires:  perl-interpreter
# We need glib-mkenums
BuildRequires:  glib2-devel

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

%autosetup -p1 -n gst-plugins-base-%{version}

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

# Drop man pages
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}

# Drop import libs for plugins
rm -rf %{buildroot}%{mingw32_libdir}/gstreamer-%{api_version}/*.dll.a
rm -rf %{buildroot}%{mingw64_libdir}/gstreamer-%{api_version}/*.dll.a

%mingw_find_lang gst-plugins-base-%{api_version}

# Win32
%files -n mingw32-gstreamer1-plugins-base -f mingw32-gst-plugins-base-%{api_version}.lang
%license COPYING
%doc README.md

%{mingw32_bindir}/gst-device-monitor-%{api_version}.exe
%{mingw32_bindir}/gst-play-%{api_version}.exe
%{mingw32_bindir}/gst-discoverer-%{api_version}.exe
%{mingw32_bindir}/libgstallocators-%{api_version}-0.dll
%{mingw32_bindir}/libgstapp-%{api_version}-0.dll
%{mingw32_bindir}/libgstaudio-%{api_version}-0.dll
%{mingw32_bindir}/libgstfft-%{api_version}-0.dll
%{mingw32_bindir}/libgstgl-%{api_version}-0.dll
%{mingw32_bindir}/libgstpbutils-%{api_version}-0.dll
%{mingw32_bindir}/libgstriff-%{api_version}-0.dll
%{mingw32_bindir}/libgstrtp-%{api_version}-0.dll
%{mingw32_bindir}/libgstrtsp-%{api_version}-0.dll
%{mingw32_bindir}/libgstsdp-%{api_version}-0.dll
%{mingw32_bindir}/libgsttag-%{api_version}-0.dll
%{mingw32_bindir}/libgstvideo-%{api_version}-0.dll

%{mingw32_includedir}/gstreamer-%{api_version}/

%{mingw32_libdir}/gstreamer-%{api_version}/*.dll
%{mingw32_libdir}/gstreamer-%{api_version}/include
%{mingw32_libdir}/libgstallocators-%{api_version}.dll.a
%{mingw32_libdir}/libgstapp-%{api_version}.dll.a
%{mingw32_libdir}/libgstaudio-%{api_version}.dll.a
%{mingw32_libdir}/libgstfft-%{api_version}.dll.a
%{mingw32_libdir}/libgstgl-%{api_version}.dll.a
%{mingw32_libdir}/libgstpbutils-%{api_version}.dll.a
%{mingw32_libdir}/libgstriff-%{api_version}.dll.a
%{mingw32_libdir}/libgstrtp-%{api_version}.dll.a
%{mingw32_libdir}/libgstrtsp-%{api_version}.dll.a
%{mingw32_libdir}/libgstsdp-%{api_version}.dll.a
%{mingw32_libdir}/libgsttag-%{api_version}.dll.a
%{mingw32_libdir}/libgstvideo-%{api_version}.dll.a

%{mingw32_libdir}/pkgconfig/*.pc

%{mingw32_datadir}/gst-plugins-base

# Win64
%files -n mingw64-gstreamer1-plugins-base -f mingw64-gst-plugins-base-%{api_version}.lang
%license COPYING
%doc README.md

%{mingw64_bindir}/gst-device-monitor-%{api_version}.exe
%{mingw64_bindir}/gst-play-%{api_version}.exe
%{mingw64_bindir}/gst-discoverer-%{api_version}.exe
%{mingw64_bindir}/libgstallocators-%{api_version}-0.dll
%{mingw64_bindir}/libgstapp-%{api_version}-0.dll
%{mingw64_bindir}/libgstaudio-%{api_version}-0.dll
%{mingw64_bindir}/libgstfft-%{api_version}-0.dll
%{mingw64_bindir}/libgstgl-%{api_version}-0.dll
%{mingw64_bindir}/libgstpbutils-%{api_version}-0.dll
%{mingw64_bindir}/libgstriff-%{api_version}-0.dll
%{mingw64_bindir}/libgstrtp-%{api_version}-0.dll
%{mingw64_bindir}/libgstrtsp-%{api_version}-0.dll
%{mingw64_bindir}/libgstsdp-%{api_version}-0.dll
%{mingw64_bindir}/libgsttag-%{api_version}-0.dll
%{mingw64_bindir}/libgstvideo-%{api_version}-0.dll

%{mingw64_includedir}/gstreamer-%{api_version}/

%{mingw64_libdir}/gstreamer-%{api_version}/*.dll
%{mingw64_libdir}/gstreamer-%{api_version}/include
%{mingw64_libdir}/libgstallocators-%{api_version}.dll.a
%{mingw64_libdir}/libgstapp-%{api_version}.dll.a
%{mingw64_libdir}/libgstaudio-%{api_version}.dll.a
%{mingw64_libdir}/libgstfft-%{api_version}.dll.a
%{mingw64_libdir}/libgstgl-%{api_version}.dll.a
%{mingw64_libdir}/libgstpbutils-%{api_version}.dll.a
%{mingw64_libdir}/libgstriff-%{api_version}.dll.a
%{mingw64_libdir}/libgstrtp-%{api_version}.dll.a
%{mingw64_libdir}/libgstrtsp-%{api_version}.dll.a
%{mingw64_libdir}/libgstsdp-%{api_version}.dll.a
%{mingw64_libdir}/libgsttag-%{api_version}.dll.a
%{mingw64_libdir}/libgstvideo-%{api_version}.dll.a

%{mingw64_libdir}/pkgconfig/*.pc

%{mingw64_datadir}/gst-plugins-base

%changelog
%autochangelog
