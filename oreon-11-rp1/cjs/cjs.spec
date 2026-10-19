%global source0_hash 1e223ce6229a7dc926b5ec3ee42040f6848e466ab51eb36c415c283b0b03098c
%global glib2_version 2.66.0
%global gobject_introspection_version 1.66.0
%global gtk3_version 3.20
%global mozjs128_version 128.5.1
Name:          cjs
Epoch:         1
Version:       140.1
Release:        1%{?dist}
Summary:        Javascript Bindings for Cinnamon
License:       LicenseRef-Callaway-MIT AND (LicenseRef-Callaway-MPLv1.1 OR GPL-2.0-or-later OR LicenseRef-Callaway-LGPLv2+)
URL:           https://github.com/linuxmint/%{name}
Source0:        https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
ExcludeArch:   %{ix86}
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gobject-introspection%{?_isa} >= %{gobject_introspection_version}
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: mozjs128%{?_isa} >= %{mozjs128_version}
# oreon:deps
BuildRequires:  dbus-daemon
BuildRequires:  dbus-x11
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtk3
BuildRequires:  mesa-dri-drivers
BuildRequires:  meson
BuildRequires:  mutter
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(mozjs-128)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  xwayland-run
# /oreon:deps
%description
Cjs allows using Cinnamon libraries from Javascript. It's based on the
Spidermonkey Javascript engine from Mozilla and the GObject introspection
framework.

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{?epoch}:%{version}-%{release}
%description devel
Files for development with %{name}.

%package tests
Summary: Tests for the cjs package
Requires: %{name}%{?_isa} = %{?epoch}:%{version}-%{release}
%description tests
The cjs-tests package contains tests that can be used to verify
the functionality of the installed cjs package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles cjs-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cjs-tests usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{shrink:xwfb-run -c mutter -- %meson_test --timeout-multiplier=5}
%files -f %{oreon_filedir}/main.list
%files -n cjs-devel -f %{oreon_filedir}/cjs-devel.list
%files -n cjs-tests -f %{oreon_filedir}/cjs-tests.list

%changelog

%autochangelog
