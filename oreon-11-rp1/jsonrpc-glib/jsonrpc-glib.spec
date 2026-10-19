%global source0_hash 965496b6e1314f3468b482a5d80340dc3b0340a5402d7783cad24154aee77396
Name:           jsonrpc-glib
Version:        3.44.2
Release:        1%{?dist}
Summary:        A JSON-RPC library for GLib
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/jsonrpc-glib
Source0:        https://download.gnome.org/sources/%{name}/3.44/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gi-docgen
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  vala
# /oreon:deps
%description
Jsonrpc-GLib is a JSON-RPC library for GLib. It includes support for
communicating as both a JSON-RPC client and server. Additionally,
supports upgrading connections to use GVariant for less runtime overhead.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Recommends:     gi-docgen-fonts
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -D enable_gtk_doc=true
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n jsonrpc-glib-devel -f %{oreon_filedir}/jsonrpc-glib-devel.list

%changelog

%autochangelog
