%global source0_hash 7b6cb912bb3a22cfa7dcf005925dcb62883024db0c09099486e7d6851185c9b8
Name:          rest
Version:       0.10.2
Release:        1%{?dist}
Summary:        A library for access to RESTful web services
License:       LGPL-2.1-only
URL:           https://gitlab.gnome.org/GNOME/librest
Source0:        https://download.gnome.org/sources/librest/0.10/librest-%{version}.tar.xz
# oreon:deps
BuildRequires:  meson
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
# /oreon:deps
%description
This library was designed to make it easier to access web services that
claim to be "RESTful". A RESTful service should have urls that represent
remote objects, which methods can then be called on. The majority of services
don't actually adhere to this strict definition. Instead, their RESTful end
point usually has an API that is just simpler to use compared to other types
of APIs they may support (XML-RPC, for instance). It is this kind of API that
this library is attempting to support.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Recommends: gi-docgen-fonts
%description devel
Files for development with %{name}.

%package demo
Summary: Demo application for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description demo
Demo application for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir librest-%{version}
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rest-devel -f %{oreon_filedir}/rest-devel.list
%files -n rest-demo -f %{oreon_filedir}/rest-demo.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.10.2-1
- Prepare for Oreon 11 (RP1)
