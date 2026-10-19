%global source0_hash 93918fcf5af529fda5b3d2d9fc3b77cd93df88064939b82f249f5577d8de1c02
Name:          gupnp-av
Version:       0.14.5
Release:        1%{?dist}
Summary:        A collection of helpers for building UPnP AV applications
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://www.gupnp.org/
Source0:        http://download.gnome.org/sources/gupnp-av/0.14/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gi-docgen
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  vala
# /oreon:deps
%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP-AV is a collection of helpers for building AV (audio/video)
applications using GUPnP.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Files for development with %{name}.

%package docs
Summary: Documentation files for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description docs
This package contains developer documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dgtk_doc=true
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n gupnp-av-devel -f %{oreon_filedir}/gupnp-av-devel.list
%files -n gupnp-av-docs -f %{oreon_filedir}/gupnp-av-docs.list

%changelog

%autochangelog
