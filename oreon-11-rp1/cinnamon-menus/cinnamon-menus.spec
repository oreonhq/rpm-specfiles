%global source0_hash 87596380720077991f58afdbbabe72d9afd10f56d64043076cf7b09bc6b0f3c1

Summary: A menu system for the Cinnamon project
Name:    cinnamon-menus
Version: 6.6.0
Release: 3%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://github.com/linuxmint/%{name} 
Source0: %url/archive/%{version}/%{name}-%{version}.tar.gz

ExcludeArch:   %{ix86}

BuildRequires: intltool
BuildRequires: meson
BuildRequires: gcc
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: python3

%description
cinnamon-menus is an implementation of the draft "Desktop
Menu Specification" from freedesktop.org. This package
also contains the Cinnamon menu layout configuration files,
.directory files and assorted menu related utility programs,
Python bindings, and a simple menu editor.

%package devel
Summary: Libraries and include files for the Cinnamon menu system
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the necessary development libraries for
writing applications that use the Cinnamon menu system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson \
 -Ddeprecated_warnings=false \
 -Denable_debug=false

%meson_build

%install
%meson_install

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS
%license COPYING COPYING.LIB
%{_libdir}/lib*.so.*
%{_libdir}/girepository-1.0/CMenu-3.0.typelib

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/cinnamon-menus-3.0
%{_datadir}/gir-1.0/CMenu-3.0.gir

%changelog
%autochangelog
