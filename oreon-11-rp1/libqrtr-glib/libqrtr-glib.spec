%global source0_hash 69ec8883d887a426c6402440b200fa53c41e9da8e098333369f2388d3559e856
Name: libqrtr-glib
Version: 1.2.2
Release:        1%{?dist}
Summary:        Support library to use and manage the QRTR (Qualcomm IPC Router) bus.
License: LGPL-2.1-or-later
URL: https://gitlab.freedesktop.org/mobile-broadband/libqrtr-glib
Source0:        https://gitlab.freedesktop.org/mobile-broadband/libqrtr-glib/-/archive/%{version}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  python3
# /oreon:deps
%description
This package contains the libraries that make it easier to use and
manage the QRTR (Qualcomm IPC Router) bus.

%package devel
Summary: Header files for adding QRTR support to applications that use glib
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: glib2-devel
%description devel
This package contains the header and pkg-config files for development
applications using QRTR functionality from applications that use glib.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
find %{buildroot}%{_datadir}/gtk-doc |xargs touch --reference meson.build
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libqrtr-glib-devel -f %{oreon_filedir}/libqrtr-glib-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.2-9
- Prepare for Oreon 11 (RP1)
