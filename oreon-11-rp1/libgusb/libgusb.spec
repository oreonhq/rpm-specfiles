%global source0_hash 9df5ef301d6a4b361002aa52cce1165a87a89744055879bdbab31e7e86f1e846
Summary:        GLib wrapper around libusb1
Name:      libgusb
Version:   0.4.9
Release:        1%{?dist}
License:   LGPL-2.1-or-later
URL:       https://github.com/hughsie/libgusb
Source0:        https://github.com/hughsie/libgusb/releases/download/%{version}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gi-docgen
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  json-glib-devel
BuildRequires:  libusb1-devel
BuildRequires:  meson
BuildRequires:  umockdev-devel
BuildRequires:  vala
# /oreon:deps
%description
GUsb is a GObject wrapper for libusb1 that makes it easy to do
asynchronous control, bulk and interrupt transfers with proper
cancellation and integration into a mainloop.

%package devel
Summary: Libraries and headers for gusb
Requires: %{name} = %{version}-%{release}
%description devel
GLib headers and libraries for gusb.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%meson -Dvapi=true -Dtests=true
%meson_build
%install
%meson_install
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libgusb-devel -f %{oreon_filedir}/libgusb-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.9-1
- Prepare for Oreon 11 (RP1)
