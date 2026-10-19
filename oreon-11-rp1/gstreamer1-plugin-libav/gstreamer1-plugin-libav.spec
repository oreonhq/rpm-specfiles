%global source0_hash 58da51dd39ecf1cf6faade34cc6412001be2e2e145bca8ae0f45336f60a36ab2
Name:           gstreamer1-plugin-libav
Version:        1.28.7
Release:        1%{?dist}
Summary:        GStreamer FFmpeg/LibAV plugin
License:        LGPLv2+
URL:            https://gstreamer.freedesktop.org/
Source0:        https://gstreamer.freedesktop.org//src/gst-libav/gst-libav-%{version}.tar.xz
Obsoletes:      gstreamer1-libav < 1:1.20.3-4
Provides:       gstreamer1-libav = 1:%{version}-%{release}
Provides:       gstreamer1-libav%{?_isa} = 1:%{version}-%{release}
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  gcc-c++
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  meson
BuildRequires:  orc-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package provides FFmpeg/LibAV GStreamer plugin.

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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
