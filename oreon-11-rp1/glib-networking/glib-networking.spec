%global source0_hash 83a75e3d9c36b66ee86d3281c2fc997816101968a5126ba322b2acb9a74dd8c0
%define glib2_version 2.73.3
%global libproxy_version 0.4.16
%global tarball_version %(echo %{version} | tr '~' '.')
%global with_libproxy 1
Name:           glib-networking
Version:        2.90.0
Release:        1%{?dist}
Summary:        Networking support for GLib
License:        LGPL-2.1-or-later WITH cryptsetup-OpenSSL-exception
URL:            https://gitlab.gnome.org/GNOME/glib-networking
Source0:        https://download.gnome.org/sources/%{name}/2.90/%{name}-%{version}.tar.xz
%if 0%{?with_libproxy}
%endif
Requires:       ca-certificates
Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gsettings-desktop-schemas
Recommends:     libproxy-duktape
# oreon:deps
BuildRequires:  ca-certificates
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(p11-kit-1)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n glib-networking-tests -f %{oreon_filedir}/glib-networking-tests.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.80.1-1
- Prepare for Oreon 11 (RP1)
