# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ea95636590098355a05e3027579dba1a9a950b05e456b2488ea03d82e4b6c18a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%define glib2_version 2.73.3
%global libproxy_version 0.4.16

%global tarball_version %(echo %{version} | tr '~' '.')

%global with_libproxy 1

Name:           glib-networking
Version:        2.90.1
Release:        1%{?dist}
Summary:        Networking support for GLib

License:        LGPL-2.1-or-later WITH cryptsetup-OpenSSL-exception
URL:            https://gitlab.gnome.org/GNOME/glib-networking
Source0:        https://download.gnome.org/sources/glib-networking/2.90/%{name}-%{tarball_version}.tar.xz
BuildRequires: oreon-rpm-macros
BuildRequires:  ca-certificates
BuildRequires:  clang
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
%if 0%{?with_libproxy}
BuildRequires:  pkgconfig(libproxy-1.0) >= %{libproxy_version}
%endif
BuildRequires:  pkgconfig(p11-kit-1)
BuildRequires:  systemd-rpm-macros

Requires:       ca-certificates
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gsettings-desktop-schemas

Recommends:     libproxy-duktape

%description
This package contains modules that extend the networking support in
GIO. In particular, it contains libproxy- and GSettings-based
GProxyResolver implementations and a gnutls-based GTlsConnection
implementation.

%package tests
Summary: Tests for the glib-networking package
License: LGPL-2.1-or-later WITH cryptsetup-OpenSSL-exception AND Apache-2.0 AND LicenseRef-RSA
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
The glib-networking-tests package contains tests that can be used to verify
the functionality of the installed glib-networking package.

%prep
%oreon_sha256
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson \
%if !0%{?with_libproxy}
  -Dlibproxy=disabled \
  -Denvironment_proxy=enabled \
%endif
  -Dinstalled_tests=true \
  %nil
%meson_build

%install
%meson_install

%find_lang %{name}

%check
%meson_test

%files -f %{name}.lang
%license COPYING LICENSE_EXCEPTION
%doc NEWS README
%{_libdir}/gio/modules/libgiognomeproxy.so
%{_libdir}/gio/modules/libgiognutls.so
%if 0%{?with_libproxy}
%{_libdir}/gio/modules/libgiolibproxy.so
%{_libexecdir}/glib-pacrunner
%{_datadir}/dbus-1/services/org.gtk.GLib.PACRunner.service
%{_userunitdir}/glib-pacrunner.service
%else
%{_libdir}/gio/modules/libgioenvironmentproxy.so
%endif

%files tests
%{_libexecdir}/installed-tests/glib-networking
%{_datadir}/installed-tests

%changelog
%autochangelog
