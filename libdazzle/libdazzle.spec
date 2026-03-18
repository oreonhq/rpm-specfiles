%global glib2_version 2.57.2
%global gtk3_version 3.24.0

Name:           libdazzle
Version:        3.44.0
Release:        11%{?dist}
Summary:        Experimental new features for GTK+ and GLib

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/libdazzle
Source0:        https://download.gnome.org/sources/%{name}/3.42/%{name}-%{version}.tar.xz

BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gmodule-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}

# for tests
BuildRequires:  tigervnc-server-minimal
BuildRequires:  words

Requires:       glib2%{?_isa} >= %{glib2_version}
Requires:       gtk3%{?_isa} >= %{gtk3_version}

%description
libdazzle is a collection of fancy features for GLib and Gtk+ that aren't quite
ready or generic enough for use inside those libraries. This is often a proving
ground for new widget prototypes. Applications such as Builder tend to drive
development of this project.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
%meson -D enable_gtk_doc=true
%meson_build


%install
%meson_install

%find_lang libdazzle-1.0


%check
Xvnc :99 -nolisten tcp &
export DISPLAY=:99
%meson_test


%files -f libdazzle-1.0.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/dazzle-list-counters
%{_libdir}/libdazzle-1.0.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Dazzle-1.0.typelib

%files devel
%doc CONTRIBUTING.md examples
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Dazzle-1.0.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libdazzle
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libdazzle-1.0.*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libdazzle-1.0.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.44.0-11
- Prepare for Oreon 11 (RP1)
