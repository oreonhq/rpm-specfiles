%global source0_hash bfa91aaca38d0fd8addcdd559e35b7541e3f32a5f410194ec4ba18040defee9b

Name:           gstreamer1-plugin-libav
Version:        1.28.1
Release:        1%{?dist}
Summary:        GStreamer FFmpeg/LibAV plugin
License:        LGPLv2+
URL:            https://gstreamer.freedesktop.org/
Source0:        %{url}/src/gst-libav/gst-libav-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  orc-devel
BuildRequires:  bzip2-devel
BuildRequires:  zlib-devel
BuildRequires:  ffmpeg-free-devel

# Rename from rpmfusion name to match convention in Fedora
Obsoletes:      gstreamer1-libav < 1:1.20.3-4
Provides:       gstreamer1-libav = 1:%{version}-%{release}
Provides:       gstreamer1-libav%{?_isa} = 1:%{version}-%{release}

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package provides FFmpeg/LibAV GStreamer plugin.

%if 0
# gstreamer1 uses hotdoc which isn't provided yet
%package devel-docs
Summary: Development documentation for the libav GStreamer plug-in
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description devel-docs
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains the development documentation for the FFmpeg/LibAV GStreamer
plugin.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p3 -n gst-libav-%{version}

%build
%meson  \
    -D package-name="Fedora GStreamer-plugin-libav package" \
    -D package-origin="http://download.fedoraproject.org" \
    -D doc=disabled

%meson_build

%install
%meson_install

%files
%doc ChangeLog README.md
%license COPYING
%{_libdir}/gstreamer-1.0/libgstlibav.so

%if 0
%files devel-docs
%doc %{_datadir}/gtk-doc/gst-libav-1.0/
%endif

%changelog
%autochangelog
