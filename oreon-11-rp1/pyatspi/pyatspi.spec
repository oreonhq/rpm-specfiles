%global source0_hash 24590e5b60fec8dfb59fcd27d2a90de7034060be318ca3f7770e0f984f1f94e2
%global debug_package %{nil}
%global major_minor_version %(echo %{version} | cut -d "." -f 1-2)
Name:           pyatspi
Version:        2.58.2
Release:        1%{?dist}
Summary:        Python bindings for at-spi
License:        LGPL-2.0-or-later AND GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/pyatspi2/
Source0:        https://download.gnome.org/sources/%{name}/%{major_minor_version}/%{name}-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3-dbus
BuildRequires:  python3-devel
# /oreon:deps
%description
at-spi allows assistive technologies to access GTK-based
applications. Essentially it exposes the internals of applications for
automation, so tools such as screen readers, magnifiers, or even
scripting interfaces can query and interact with GUI controls.

This package includes a python3 client library for at-spi.

%package -n python3-pyatspi
Summary:        Python3 bindings for at-spi
Requires:       at-spi2-core
Requires:       python3-gobject
%description -n python3-pyatspi
at-spi allows assistive technologies to access GTK-based
applications. Essentially it exposes the internals of applications for
automation, so tools such as screen readers, magnifiers, or even
scripting interfaces can query and interact with GUI controls.

This package includes a python3 client library for at-spi.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Denable_tests=true
%meson_build
%install
%meson_install
sed -i '1s|^#!/usr/bin/python|#!%{__python3}|' examples/magFocusTracker.py
%oreon_autofiles python3-pyatspi usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n python3-pyatspi -f %{oreon_filedir}/python3-pyatspi.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.58.2-1
- Import
