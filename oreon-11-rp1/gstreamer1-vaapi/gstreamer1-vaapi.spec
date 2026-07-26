%global source0_hash 64633e188d0b6005847fd8e3ad70c0c20c86caeeae4f211f3e383b1455fc5d09

Name:           gstreamer1-vaapi
Version:        1.26.10
Release:        2%{?dist}
Summary:        GStreamer plugins to use VA API video acceleration

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://cgit.freedesktop.org/gstreamer/gstreamer-vaapi
Source0:        https://gstreamer.freedesktop.org/src/gstreamer-vaapi/gstreamer-vaapi-%{version}.tar.xz

BuildRequires:  meson >= 0.48.0
BuildRequires:  gcc
BuildRequires:  glib2-devel >= 2.40
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  gstreamer1-plugins-bad-free-devel >= %{version}
BuildRequires:  libva-devel >= 1.1.0
BuildRequires:  libdrm-devel
BuildRequires:  libudev-devel
BuildRequires:  libGL-devel
BuildRequires:  pkgconfig(egl)
BuildRequires:  libvpx-devel
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  gtk3-devel

%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  wayland-devel >= 1.11.0
BuildRequires:  wayland-protocols-devel >= 1.15
BuildRequires:  pkgconfig(wayland-client)  >= 1.11.0
BuildRequires:  pkgconfig(wayland-scanner) >= 1.11.0
BuildRequires:  pkgconfig(wayland-cursor)  >= 1.11.0
BuildRequires:  pkgconfig(wayland-egl)     >= 1.11.0
BuildRequires:  pkgconfig(wayland-server)  >= 1.11.0
%endif

%ifnarch s390x
Recommends:     mesa-va-drivers%{?_isa}
%endif

# We can't provide encoders or decoders unless we know what VA-API drivers
# are on the system. Just filter them out, so they're not suggested by
# PackageKit et al.
%global __provides_exclude gstreamer1\\(decoder|gstreamer1\\(encoder

%description
A collection of GStreamer plugins to let you make use of VA API video
acceleration from GStreamer applications.

Includes elements for video decoding, display, encoding and post-processing
using VA API (subject to hardware limitations).

%package devel
Summary:        GStreamer VA API Development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files
for developing applications that use %{name}.

%package        devel-docs
Summary:        Developer documentation for GStreamer VA API video acceleration plugins
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

Provides:       gstreamer1-vaapi-devel = %{version}-%{release}
Obsoletes:      gstreamer1-vaapi-devel < 0.6.1-3

%description	devel-docs
The %{name}-devel-docs package contains developer documentation
for the GStreamer VA API video acceleration plugins

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n gstreamer-vaapi-%{version}

%build

%meson \
	-D doc=disabled

%meson_build

%install
%meson_install

%check
%ldconfig_scriptlets

%files
%doc AUTHORS NEWS README
%license COPYING.LIB
%{_libdir}/gstreamer-1.0/*.so

%files devel

%files devel-docs
%doc AUTHORS NEWS README
%if 0
%doc %{_datadir}/gtk-doc
%endif

%changelog
%autochangelog
