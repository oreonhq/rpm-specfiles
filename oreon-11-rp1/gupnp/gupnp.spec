%global source0_hash a1ee07b7b12673c32d7fc73ca158a50c1a4dc69ab35b65e94d24d38ac875345e
%global apiver 1.6
%global gssdp_version 1.6.2
Name:          gupnp
Version:       1.6.10
Release:        1%{?dist}
Summary:        A framework for creating UPnP devices & control points
License:       LGPL-2.1-or-later
URL:           https://www.gupnp.org/
Source0:        https://download.gnome.org/sources/%{name}/1.6/%{name}-%{version}.tar.xz
Requires: dbus
Requires: gssdp%{?_isa} >= %{gssdp_version}
Requires: libsoup3%{?_isa}
# oreon:deps
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  docbook-style-xsl
BuildRequires:  gi-docgen
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gssdp-1.6)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  vala
# /oreon:deps
%description
GUPnP is an object-oriented open source framework for creating UPnP 
devices and control points, written in C using GObject and libsoup. 
The GUPnP API is intended to be easy to use, efficient and flexible. 

%package devel
Summary: Development package for gupnp
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

%meson --wrap-mode=nofallback \
  -Dcontext_manager=network-manager \
  -Dgtk_doc=true \
  -Dexamples=false \
  %{nil}
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n gupnp-devel -f %{oreon_filedir}/gupnp-devel.list
%files -n gupnp-docs -f %{oreon_filedir}/gupnp-docs.list

%changelog

%autochangelog
