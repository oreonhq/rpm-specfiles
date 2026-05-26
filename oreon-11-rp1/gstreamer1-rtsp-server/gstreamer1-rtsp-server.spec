%global         majorminor      1.0

Name:           gstreamer1-rtsp-server
Version:        1.26.7
Release:        2%{?dist}
Summary:        GStreamer RTSP server library

License:        LGPL-2.0-or-later AND LGPL-2.1-only
URL:            http://gstreamer.freedesktop.org/
Source0:        http://gstreamer.freedesktop.org/src/gst-rtsp/gst-rtsp-server-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 4f234594aea692e3c1bfaa969965039aaf7483bdfc5862b31d614a59e6718abf
%global source0_file gst-rtsp-server-1.26.7.tar.xz
# oreon url source checksums end

BuildRequires:  meson >= 0.48.0
BuildRequires:  gcc
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  gobject-introspection-devel
BuildRequires:  chrpath

Requires:       gstreamer1%{?_isa} >= %{version}
Requires:       gstreamer1-plugins-base%{?_isa} >= %{version}

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/gst-rtsp-server-1.26.7.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4f234594aea692e3c1bfaa969965039aaf7483bdfc5862b31d614a59e6718abf" || { echo "oreon: Source0 SHA256 mismatch for gst-rtsp-server-1.26.7.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n gst-rtsp-server-%{version}

%build
%meson \
	-D doc=disabled -D tests=disabled

%meson_build

%install
%meson_install

# Remove rpath as per https://fedoraproject.org/wiki/Packaging/Guidelines#Beware_of_Rpath
# can't tweak libtool, see:
# https://bugzilla.gnome.org/show_bug.cgi?id=634376#c1
chrpath --delete %{buildroot}%{_libdir}/libgstrtspserver-%{majorminor}.so*

%ldconfig_scriptlets

%files
%license COPYING.LIB
%doc README TODO RELEASE
%dir %{_libdir}/girepository-1.0/
%{_libdir}/libgstrtspserver-%{majorminor}.so.*
%{_libdir}/girepository-1.0/GstRtspServer-%{majorminor}.typelib

%files devel
%dir %{_datadir}/gir-1.0/
%{_includedir}/gstreamer-%{majorminor}/gst/rtsp-server
%{_libdir}/libgstrtspserver-%{majorminor}.so
%{_libdir}/pkgconfig/gstreamer-rtsp-server-%{majorminor}.pc
%{_datadir}/gir-1.0/GstRtspServer-%{majorminor}.gir

%{_libdir}/gstreamer-%{majorminor}/libgstrtspclientsink.so

%if 0
%files devel-docs
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%doc %{_datadir}/gtk-doc/html/gst-rtsp-server-%{majorminor}
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.28.1-1
- Prepare for Oreon 11 (RP1)
