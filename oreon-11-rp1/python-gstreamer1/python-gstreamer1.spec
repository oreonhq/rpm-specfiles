%global source0_hash d47cea95adb95ba10443ed7812c7c5fa0807aef43b98cd1c6d8fb9f9a86f7085

%global gstreamer1_version 1.8.0

Name:           python-gstreamer1
Version:        1.28.1
Release:        1%{?dist}
Summary:        Python bindings for GStreamer

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://gstreamer.freedesktop.org/
Source:         http://gstreamer.freedesktop.org/src/gst-python/gst-python-%{version}.tar.xz

BuildRequires:  meson >= 0.48.0
BuildRequires:  gcc
BuildRequires:  g++
BuildRequires:  python3-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake
BuildRequires:  gstreamer1-devel >= %{gstreamer1_version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{gstreamer1_version}
BuildRequires:  gstreamer1-plugins-bad-free-devel >= %{gstreamer1_version}
BuildRequires:  gstreamer1-rtsp-server-devel >= %{gstreamer1_version}
BuildRequires:  pkgconfig(pygobject-3.0)

# For the benefit of people migrating from the GStreamer-0.10 package,
# which was called gstreamer-python

%global _description\
This module contains PyGObject overrides to make it easier to write\
applications that use GStreamer 1.x in Python.

%description %_description

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

%files -n python3-gstreamer1
%license COPYING
%doc ChangeLog README.md RELEASE
%{python3_sitearch}/gi/overrides/*
%{_libdir}/gstreamer-1.0/libgstpython.*so
%{_libdir}/gstreamer-1.0/python/gesotioformatter.py

%changelog
%autochangelog
