%global source0_hash 081c1fb5091cb8a1660ea9c152b689de9ba191d10a1109df503f5754f318af7e
Summary:        A GObject library for interacting with oVirt REST API
Name: libgovirt
Version: 0.3.11
Release:        1%{?dist}
License: LGPL-2.1-or-later
Source0:        http://download.gnome.org/sources/libgovirt/0.3/%{name}-%{version}.tar.xz
URL: https://gitlab.gnome.org/GNOME/libgovirt
# oreon:deps
BuildRequires:  dconf
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  glib-networking
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(rest-1.0)
# /oreon:deps
%description
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

%package devel
Summary: Libraries, includes, etc. to compile with the libgovirt library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Requires: glib2-devel
%description devel
libgovirt is a library that allows applications to use oVirt REST API
to list VMs managed by an oVirt instance, and to get the connection
parameters needed to make a SPICE/VNC connection to them.

Libraries, includes, etc. to compile with the libgovirt library

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n libgovirt-devel -f %{oreon_filedir}/libgovirt-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.11-1
- Prepare for Oreon 11 (RP1)
