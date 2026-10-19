%global source0_hash 9d22a27972c25e706b428e78356458446314c70eb31aef07d4a32b843a6dea94
%bcond check 1
%global crate gst-plugin-gtk4
Name:           rust-gst-plugin-gtk4
Version:        0.15.2
Release:        1%{?dist}
Summary:        GStreamer GTK 4 sink element
License:        MPL-2.0
URL:            https://crates.io/crates/gst-plugin-gtk4
Source0:        https://static.crates.io/crates/gst-plugin-gtk4/gst-plugin-gtk4-%{version}.crate
Patch:          gst-plugin-gtk4-fix-metadata-auto.diff
Patch:          gst-plugin-gtk4-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-c
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n gstreamer1-plugin-gtk4
Summary:        GStreamer GTK 4 sink element
License:        MPL-2.0 AND MIT AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
Provides:       %{crate} = %{version}-%{release}
%description -n gstreamer1-plugin-gtk4

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+capi-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+capi-devel

This package contains library source intended for building other packages which
use the "capi" feature of the "%{crate}" crate.

%package     -n %{name}+dmabuf-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+dmabuf-devel

This package contains library source intended for building other packages which
use the "dmabuf" feature of the "%{crate}" crate.

%package     -n %{name}+doc-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+doc-devel

This package contains library source intended for building other packages which
use the "doc" feature of the "%{crate}" crate.

%package     -n %{name}+gdk-wayland-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+gdk-wayland-devel

This package contains library source intended for building other packages which
use the "gdk-wayland" feature of the "%{crate}" crate.

%package     -n %{name}+gdk-x11-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+gdk-x11-devel

This package contains library source intended for building other packages which
use the "gdk-x11" feature of the "%{crate}" crate.

%package     -n %{name}+gst-allocators-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+gst-allocators-devel

This package contains library source intended for building other packages which
use the "gst-allocators" feature of the "%{crate}" crate.

%package     -n %{name}+gst-gl-egl-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+gst-gl-egl-devel

This package contains library source intended for building other packages which
use the "gst-gl-egl" feature of the "%{crate}" crate.

%package     -n %{name}+gst-gl-wayland-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+gst-gl-wayland-devel

This package contains library source intended for building other packages which
use the "gst-gl-wayland" feature of the "%{crate}" crate.

%package     -n %{name}+gst-gl-x11-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+gst-gl-x11-devel

This package contains library source intended for building other packages which
use the "gst-gl-x11" feature of the "%{crate}" crate.

%package     -n %{name}+gtk_v4_10-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+gtk_v4_10-devel

This package contains library source intended for building other packages which
use the "gtk_v4_10" feature of the "%{crate}" crate.

%package     -n %{name}+gtk_v4_12-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+gtk_v4_12-devel

This package contains library source intended for building other packages which
use the "gtk_v4_12" feature of the "%{crate}" crate.

%package     -n %{name}+gtk_v4_14-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+gtk_v4_14-devel

This package contains library source intended for building other packages which
use the "gtk_v4_14" feature of the "%{crate}" crate.

%package     -n %{name}+gtk_v4_16-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+gtk_v4_16-devel

This package contains library source intended for building other packages which
use the "gtk_v4_16" feature of the "%{crate}" crate.

%package     -n %{name}+gtk_v4_18-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+gtk_v4_18-devel

This package contains library source intended for building other packages which
use the "gtk_v4_18" feature of the "%{crate}" crate.

%package     -n %{name}+gtk_v4_20-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+gtk_v4_20-devel

This package contains library source intended for building other packages which
use the "gtk_v4_20" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+static-devel

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

%package     -n %{name}+v1_28-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+v1_28-devel

This package contains library source intended for building other packages which
use the "v1_28" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+wayland-devel

This package contains library source intended for building other packages which
use the "wayland" feature of the "%{crate}" crate.

%package     -n %{name}+waylandegl-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+waylandegl-devel

This package contains library source intended for building other packages which
use the "waylandegl" feature of the "%{crate}" crate.

%package     -n %{name}+x11egl-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+x11egl-devel

This package contains library source intended for building other packages which
use the "x11egl" feature of the "%{crate}" crate.

%package     -n %{name}+x11glx-devel
Summary:        GStreamer GTK 4 sink element
BuildArch:      noarch
%description -n %{name}+x11glx-devel

This package contains library source intended for building other packages which
use the "x11glx" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f dmabuf,gtk_v4_20,v1_28,waylandegl,x11egl,x11glx
%{cargo_license_summary -f dmabuf,gtk_v4_20,v1_28,waylandegl,x11egl,x11glx}
%{cargo_license -f dmabuf,gtk_v4_20,v1_28,waylandegl,x11egl,x11glx} > LICENSE.dependencies
%cargo_cbuild -f dmabuf,gtk_v4_20,v1_28,waylandegl,x11egl,x11glx
%install
%cargo_install -f dmabuf,gtk_v4_20,v1_28,waylandegl,x11egl,x11glx
%cargo_cinstall -f dmabuf,gtk_v4_20,v1_28,waylandegl,x11egl,x11glx
rm -v %{buildroot}/%{_libdir}/gstreamer-1.0/libgstgtk4.a
rm -v %{buildroot}/%{_libdir}/pkgconfig/gstgtk4.pc
%oreon_autofiles gstreamer1-plugin-gtk4 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f dmabuf,gtk_v4_20,v1_28,waylandegl,x11egl,x11glx
%endif
%files -f %{oreon_filedir}/main.list
%files -n gstreamer1-plugin-gtk4 -f %{oreon_filedir}/gstreamer1-plugin-gtk4.list
%files -n rust-gst-plugin-gtk4-devel -f %{oreon_filedir}/rust-gst-plugin-gtk4-devel.list

%changelog

%autochangelog
