%global source0_hash 3d53b96f85bc5628d33e367ec9bf2adb38ef2b34d7ad0434a6ba0cf4ad9048e6
Name:          gupnp-dlna
Version:       0.12.0
Release:        1%{?dist}
Summary:        A collection of helpers for building UPnP AV applications
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://www.gupnp.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.12/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gssdp-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gtk-doc
BuildRequires:  gupnp-av-devel
BuildRequires:  gupnp-devel
BuildRequires:  libxml2-devel
BuildRequires:  meson
BuildRequires:  vala
# /oreon:deps
%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP-dlna is a collection of helpers for building DLNA (Digital 
Living Network Alliance) compliant applications using GUPnP.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Contains libraries and header files for developing applications that 
use %{name}.

%package docs
Summary: Development package for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description docs
Contains developer documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%meson -Dgtk_doc=true
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n gupnp-dlna-devel -f %{oreon_filedir}/gupnp-dlna-devel.list
%files -n gupnp-dlna-docs -f %{oreon_filedir}/gupnp-dlna-docs.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.12.0-12
- Prepare for Oreon 11 (RP1)
