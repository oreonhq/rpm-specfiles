%global source0_hash 132575f3ef2712cd0fc8a7f0c9287ff5c4264d75921953220dd2089911272946
%global glib2_version 2.45.8
%global json_glib_version 1.1.2
%global gdk_pixbuf_version 2.31.5
Summary:        Library for AppStream metadata
Name:      libappstream-glib
Version:   0.8.4
Release:        1%{?dist}
License:   LGPL-2.1-or-later
URL:       http://people.freedesktop.org/~hughsient/appstream-glib/
Source0:        http://people.freedesktop.org/~hughsient/appstream-glib/releases/appstream-glib-%{version}.tar.xz
Requires: gdk-pixbuf2%{?_isa} >= %{gdk_pixbuf_version}
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: json-glib%{?_isa} >= %{json_glib_version}
Obsoletes: appdata-tools < 0.1.9
Provides: appdata-tools
Obsoletes: libappstream-glib-builder-devel < 0.7.15
%define as_plugin_version               5
# oreon:deps
BuildRequires:  docbook-style-xsl
BuildRequires:  docbook-utils
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gperf
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  json-glib-devel
BuildRequires:  libarchive-devel
BuildRequires:  libcurl-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  pango-devel
BuildRequires:  rpm-devel
# /oreon:deps
%description
This library provides GObjects and helper methods to make it easy to read and
write AppStream metadata. It also provides a simple DOM implementation that
makes it easy to edit nodes and convert to and from the standardized XML
representation.

%package devel
Summary: GLib Libraries and headers for appstream-glib
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
GLib headers and libraries for appstream-glib.

%package builder
Summary: Library and command line tools for building AppStream metadata
Requires: %{name}%{?_isa} = %{version}-%{release}
Recommends: pngquant
%description builder
This library and command line tool is used for building AppStream metadata
from a directory of packages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir appstream-glib-%{version}
%oreon_prep
%build

%meson \
    -Dgtk-doc=true \
    -Ddep11=false
%meson_build
%install
%meson_install
%find_lang appstream-glib
%ldconfig_scriptlets
%ldconfig_scriptlets builder
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libappstream-glib-devel -f %{oreon_filedir}/libappstream-glib-devel.list
%files -n libappstream-glib-builder -f %{oreon_filedir}/libappstream-glib-builder.list

%changelog

%autochangelog
