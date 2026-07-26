%global source0_hash a4e49cd082972a132ca5f54be52a3c386db37c4cb0e487e017ba00d83a5f985d

%global apiver 1.0

Name:           gst-devtools
Version:        1.28.1
Release:        1%{?dist}
Summary:        Development and debugging tools for GStreamer

License:        LGPL-2.0-or-later
URL:            https://gstreamer.freedesktop.org/src/gst-devtools
Source:         https://gstreamer.freedesktop.org/src/gst-devtools/gst-devtools-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  gobject-introspection-devel
BuildRequires:  json-glib-devel
BuildRequires:  gtk-doc
BuildRequires:  python3-devel
BuildRequires:  cairo-devel
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros >= 24

%description
%{summary}.

%package devel
Summary:        Development libraries and header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       gstreamer1-devel%{?_isa}

%description devel
%{summary}.

%package -n gst-debug-viewer
Summary:        GStreamer Debug Viewer
Requires:       gtk3
Requires:       hicolor-icon-theme
Requires:       python3-gobject
BuildArch:      noarch

%description -n gst-debug-viewer
A simple graphical utility to view and analyze GStreamer debug files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p3

#Uncomment when all deps for dots_viewer are installable.
#%%cargo_prep

#%%generate_buildrequires
#pushd dots-viewer &> /dev/null
#%%cargo_generate_buildrequires
#popd &> /dev/null

%build
%meson -D doc=disabled -D debug_viewer=enabled -D dots_viewer=disabled
%meson_build

%install
%meson_install

%files
%doc validate/README
%license validate/COPYING
%{_bindir}/gst-validate-*
%dir %{_libdir}/girepository-1.0/
%{_libdir}/girepository-1.0/GstValidate-%{apiver}.typelib
%{_libdir}/gstreamer-1.0/libgstvalidatetracer.so
%{_libdir}/libgstvalidate-%{apiver}.so.*
%{_datadir}/gstreamer-1.0/validate/
%{_libdir}/gstreamer-1.0/validate/*.so
%{_libdir}/gst-validate-launcher/
%{_libdir}/libgstvalidate-default-overrides-1.0.so.0*

%files devel
%{_includedir}/gstreamer-1.0/gst/validate/
%{_libdir}/libgstvalidate-%{apiver}.so
%{_libdir}/pkgconfig/gstreamer-validate-%{apiver}.pc
%dir %{_datadir}/gir-1.0/
%{_datadir}/gir-1.0/GstValidate-%{apiver}.gir
%{_libdir}/libgstvalidate-default-overrides-1.0.so

%files -n gst-debug-viewer
%{_bindir}/gst-debug-viewer
%{python3_sitelib}/GstDebugViewer/
%{_datadir}/applications/org.freedesktop.GstDebugViewer.desktop
%{_datadir}/gst-debug-viewer/
%{_datadir}/icons/hicolor/*/apps/gst-debug-viewer.*
%{_metainfodir}/org.freedesktop.GstDebugViewer.appdata.xml

%changelog
%autochangelog
