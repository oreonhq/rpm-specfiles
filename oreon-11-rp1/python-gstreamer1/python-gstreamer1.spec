%global source0_hash 9c23c5dddfd2c9b94bb1b4e4f5b90ebc6400d84277c77cf91b1dbdb4a8b451f9
%global gstreamer1_version 1.8.0
Name:           python-gstreamer1
Version:        1.28.7
Release:        1%{?dist}
Summary:        Python bindings for GStreamer
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gst-python/gst-python-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  g++
BuildRequires:  gcc
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-bad-free-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gstreamer1-rtsp-server-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3-devel
# /oreon:deps
%description

%package -n python3-gstreamer1
Summary:        Python bindings for GStreamer
Requires:       python3-gobject%{?_isa}
Requires:       gstreamer1%{?_isa} >= %{gstreamer1_version}
%description -n python3-gstreamer1
This module contains PyGObject overrides to make it easier to write
applications that use GStreamer 1.x in Python 3.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n gst-python-%{version} -p0

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles python3-gstreamer1 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-gstreamer1 -f %{oreon_filedir}/python3-gstreamer1.list

%changelog

%autochangelog
