%global source0_hash 20e59f7402f960fbba184b2eb2cdee60e316554fd771bf4d5598ec5e3b9d1002

%global glib2_version 2.66.0
%global gobject_introspection_version 1.66.0
%global gtk3_version 3.20
%global mozjs128_version 128.5.1

Name:          cjs
Epoch:         1
Version:       128.1
Release:       4%{?dist}
Summary:       Javascript Bindings for Cinnamon

# Automatically converted from old format: MIT and (MPLv1.1 or GPLv2+ or LGPLv2+) - review is highly recommended.
License:       LicenseRef-Callaway-MIT AND (LicenseRef-Callaway-MPLv1.1 OR GPL-2.0-or-later OR LicenseRef-Callaway-LGPLv2+)
# The following files contain code from Mozilla which
# is triple licensed under MPL1.1/LGPLv2+/GPLv2+:
# The console module (modules/console.c)
# Stack printer (gjs/stack.c)
URL:           https://github.com/linuxmint/%{name}
Source0:       %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:        pkconfig.patch

ExcludeArch:   %{ix86}

BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: meson
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(gobject-introspection-1.0) >= %{gobject_introspection_version}
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(mozjs-128) >= %{mozjs128_version}
BuildRequires: pkgconfig(readline)
BuildRequires: pkgconfig(sysprof-capture-4)
# For GTK+ 3 tests
BuildRequires: gtk3
# For dbus tests
BuildRequires: dbus-daemon
# Required for checks
BuildRequires: dbus-x11
BuildRequires: mesa-dri-drivers
BuildRequires: mutter
BuildRequires: xwayland-run

Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gobject-introspection%{?_isa} >= %{gobject_introspection_version}
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: mozjs128%{?_isa} >= %{mozjs128_version}

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

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%{shrink:xwfb-run -c mutter -- %meson_test --timeout-multiplier=5}

%files
%doc NEWS README.md
%license COPYING
%{_bindir}/cjs
%{_bindir}/cjs-console
%{_libdir}/*.so.*
%{_libdir}/cjs/

%files devel
%doc examples/*
%{_includedir}/cjs-1.0/
%{_libdir}/pkgconfig/cjs-*1.0.pc
%{_libdir}/*.so
%{_datadir}/cjs-1.0/

%files tests
%{_libexecdir}/installed-tests/
%{_datadir}/installed-tests/
%{_datadir}/glib-2.0/schemas/org.cinnamon.CjsTest.gschema.xml

%changelog
%autochangelog
