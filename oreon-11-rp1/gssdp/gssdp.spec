%global source0_hash 767d2275254ce0efeaeac64419ff9f4f0ad470d134ef672f5c556b2abb786bcb
Name:          gssdp
Version:       1.6.6
Release:        1%{?dist}
Summary:        Resource discovery and announcement over SSDP
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://www.gupnp.org/
Source0:        https://download.gnome.org/sources/%{name}/1.6/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  /usr/bin/pandoc
BuildRequires:  gi-docgen
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  vala
# /oreon:deps
%description
GSSDP implements resource discovery and announcement over SSDP and is part
of gUPnP.  GUPnP is an object-oriented open source framework for creating
UPnP devices and control points, written in C using GObject and libsoup. The
GUPnP API is intended to be easy to use, efficient and flexible.

%package devel
Summary: Development package for gssdp
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Files for development with gssdp.

%package utils
Summary: Various GUI utuls for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description utils
This package contains GUI utilies for %{name}.

%package docs
Summary: Documentation files for %{name}
Requires: %{name} = %{version}-%{release}
Recommends: gi-docgen-fonts
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n gssdp-devel -f %{oreon_filedir}/gssdp-devel.list
%files -n gssdp-utils -f %{oreon_filedir}/gssdp-utils.list
%files -n gssdp-docs -f %{oreon_filedir}/gssdp-docs.list

%changelog

%autochangelog
