%global source0_hash e3dadbf638d0207040f6da6d852db516e463423da710af6cbc35d00572f17d9b
%global glib2_minver 2.28
%global apimajor 1
%global apiver %{apimajor}
%global somajor 1
Name:           msgraph
Version:        0.3.5
Release:        1%{?dist}
Summary:        Library to access MS Graph API for Microsoft 365
License:        LGPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/msgraph
Source0:        https://download.gnome.org/sources/%{name}/0.3/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  /usr/bin/gi-docgen
BuildRequires:  gcc
BuildRequires:  glib-networking
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libuhttpmock-1.0)
BuildRequires:  pkgconfig(rest-1.0)
# /oreon:deps
%description
libmsgraph is a GLib-based library for accessing online service APIs
using the MS Graph protocol.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
Enhances:       %{name}-devel = %{version}-%{release}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains documentation for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n msgraph-devel -f %{oreon_filedir}/msgraph-devel.list
%files -n msgraph-doc -f %{oreon_filedir}/msgraph-doc.list

%changelog

%autochangelog

