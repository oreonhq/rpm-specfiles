%global source0_hash de43a59a0c89a14eb1c14ae8e81e5b45c4e9d7b1f930b0ebaad360f9b5e0b5c4
%global         majorminor      1.0
Name:           gstreamer1-rtsp-server
Version:        1.28.7
Release:        1%{?dist}
Summary:        GStreamer RTSP server library
License:        LGPL-2.0-or-later AND LGPL-2.1-only
URL:            http://gstreamer.freedesktop.org/
Source0:        https://gstreamer.freedesktop.org/src/gst-rtsp-server/gst-rtsp-server-%{version}.tar.xz
Requires:       gstreamer1%{?_isa} >= %{version}
Requires:       gstreamer1-plugins-base%{?_isa} >= %{version}
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  gcc
BuildRequires:  gobject-introspection-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  meson
# /oreon:deps
%description
A GStreamer-based RTSP server library.

%package devel
Summary:        Development files for %{name}
Requires:       gstreamer1-devel%{?_isa} >= %{version}
Requires:       gstreamer1-plugins-base-devel%{?_isa} >= %{version}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for %{name}, the GStreamer RTSP server library.

%package devel-docs
Summary:         Developer documentation for GStreamer-based RTSP server library
Requires:        %{name} = %{version}-%{release}
BuildArch:       noarch
%description devel-docs
This %{name}-devel-docs contains developer documentation for the
GStreamer-based RTSP server library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n gst-rtsp-server-%{version}

%build

%meson \
	-D doc=disabled -D tests=disabled
%meson_build
%install
%meson_install
chrpath --delete %{buildroot}%{_libdir}/libgstrtspserver-%{majorminor}.so*
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gstreamer1-rtsp-server-devel -f %{oreon_filedir}/gstreamer1-rtsp-server-devel.list
%files -n gstreamer1-rtsp-server-devel-docs -f %{oreon_filedir}/gstreamer1-rtsp-server-devel-docs.list

%changelog

%autochangelog
