%global source0_hash 66097ee05c3cc4dfbdc124dfc9b885085f5c6ba2f1b2e642d0475987f9222939
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:           libshumate
Version:        1.7.0
Release:        1%{?dist}
Summary:        GTK widget to display maps
License:        LGPL-2.1-or-later AND LGPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/libshumate
Source0:        https://download.gnome.org/sources/%{name}/1.6/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  /usr/bin/gperf
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libprotobuf-c)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  pkgconfig(vapigen)
# /oreon:deps
%description
libshumate is a GTK widget displaying interactive maps. Various map
sources can be used together with the possibility to draw custom
overlays, markers and lines on top of the maps. Bindings to other
languages are provided using GObject Introspection.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
License:        LGPL-2.1-or-later AND (Apache-2.0 OR GPL-3.0-or-later) AND MIT
Recommends:     gi-docgen-fonts
BuildArch:      noarch
%description    doc
This package contains developer documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n libshumate-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang shumate1
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libshumate-devel -f %{oreon_filedir}/libshumate-devel.list
%files -n libshumate-doc -f %{oreon_filedir}/libshumate-doc.list

%changelog

%autochangelog
