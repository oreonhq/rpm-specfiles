%global source0_hash afc73f2339b43856cc762a04f61758525093a36378a0aec9429268ba06500427
%global apiver 1.0
Name:           gst-devtools
Version:        1.29.2
Release:        1%{?dist}
Summary:        Development and debugging tools for GStreamer
License:        LGPL-2.0-or-later
URL:            https://gstreamer.freedesktop.org/src/gst-devtools
Source0:        https://gstreamer.freedesktop.org/src/gst-devtools/gst-devtools-%{version}.tar.xz
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  json-glib-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  python3-devel
BuildRequires:  rust
# /oreon:deps
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
%oreon_autofiles gst-debug-viewer usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gst-devtools-devel -f %{oreon_filedir}/gst-devtools-devel.list
%files -n gst-debug-viewer -f %{oreon_filedir}/gst-debug-viewer.list

%changelog

%autochangelog
