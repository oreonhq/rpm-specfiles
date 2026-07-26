%global source0_hash 4ed0d52a072551c6d536f1be68d4fcdb4166454fc9e48567ab2550282086b0f4

%global gtk3_version     3.16.0
%global glib2_version    2.37.3
%global gtk_doc_version  1.9
%global po_package       cinnamon-desktop-3.0

Summary: Shared code among cinnamon-session, nemo, etc
Name:    cinnamon-desktop
Version: 6.6.2
Release: 7%{?dist}
# Automatically converted from old format: GPLv2+ and LGPLv2+ and MIT - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-MIT
URL:     https://github.com/linuxmint/%{name}
Source0: %url/archive/%{version}/%{name}-%{version}.tar.gz
Source1: x-cinnamon-mimeapps.list

ExcludeArch: %{ix86}

Patch0:   set_font_defaults.patch
Patch1:   %url/pull/265.patch#/update-gvc.patch

Requires: redhat-menus

# Make sure to update libgnome schema when changing this
%if 0%{?fedora}
Requires: system-backgrounds-gnome
%endif

BuildRequires: pkgconfig(accountsservice)
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires: pkgconfig(gtk-doc) >= %{gtk_doc_version}
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)  >= %{glib2_version}
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(iso-codes)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xkeyboard-config)
BuildRequires: pkgconfig(xrandr) 
BuildRequires: meson
BuildRequires: gcc
BuildRequires: intltool
BuildRequires: itstool
BuildRequires: python3-packaging

%description
The cinnamon-desktop package contains an internal library
(libcinnamon-desktop) used to implement some portions of the CINNAMON
desktop, and also some data files and other shared components of the
CINNAMON user environment.

%package devel
Summary:  Libraries and headers for libcinnamon-desktop
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:  LicenseRef-Callaway-LGPLv2+
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Libraries and header files for the CINNAMON-internal private library
libcinnamon-desktop.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson -Ddeprecation_warnings=false
%meson_build

%install
%meson_install

mkdir -p %buildroot%{_datadir}/applications/
install -m 644 %SOURCE1 %buildroot%{_datadir}/applications/x-cinnamon-mimeapps.list

%find_lang %{po_package} --all-name --with-gnome

%ldconfig_scriptlets

%files -f %{po_package}.lang
%doc AUTHORS README
%license COPYING COPYING.LIB
%{_datadir}/glib-2.0/schemas/org.cinnamon.*.xml
%{_datadir}/applications/x-cinnamon-mimeapps.list
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/C*.typelib

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/cinnamon-desktop/
%{_datadir}/gir-1.0/C*.gir

%changelog
%autochangelog
