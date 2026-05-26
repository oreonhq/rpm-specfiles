# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 9df5ef301d6a4b361002aa52cce1165a87a89744055879bdbab31e7e86f1e846
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Summary:   GLib wrapper around libusb1
Name:      libgusb
Version:   0.4.9
Release:   %autorelease
License:   LGPL-2.1-or-later
URL:       https://github.com/hughsie/libgusb
Source0:   https://github.com/hughsie/libgusb/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires: glib2-devel >= 2.38.0
BuildRequires: json-glib-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gi-docgen
BuildRequires: libusb1-devel >= 1.0.19
BuildRequires: umockdev-devel
BuildRequires: meson
BuildRequires: vala

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
%oreon_verify_sources
%setup -q

%build
%meson -Dvapi=true -Dtests=true

%meson_build

%install
%meson_install

%ldconfig_scriptlets

%files
%doc README.md AUTHORS NEWS COPYING
%{_libdir}/libgusb.so.?
%{_libdir}/libgusb.so.?.0.*
%{_libdir}/girepository-1.0/GUsb-1.0.typelib

%files devel
%{_includedir}/gusb-1
%{_bindir}/gusbcmd
%{_libdir}/libgusb.so
%{_libdir}/pkgconfig/gusb.pc
%{_datadir}/doc/libgusb
%{_datadir}/gir-1.0/GUsb-1.0.gir
%{_datadir}/vala/vapi/gusb.deps
%{_datadir}/vala/vapi/gusb.vapi

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.9-1
- Prepare for Oreon 11 (RP1)
