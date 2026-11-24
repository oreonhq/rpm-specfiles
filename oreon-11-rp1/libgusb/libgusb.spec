# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 9df5ef301d6a4b361002aa52cce1165a87a89744055879bdbab31e7e86f1e846
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary:   GLib wrapper around libusb1
Name:      libgusb
Version:   0.4.9
Release:   1%{?dist}
License:   LGPL-2.1-or-later
URL:       https://github.com/hughsie/libgusb
Source0:        https://github.com/hughsie/libgusb/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
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
%oreon_sha256
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
%autochangelog
