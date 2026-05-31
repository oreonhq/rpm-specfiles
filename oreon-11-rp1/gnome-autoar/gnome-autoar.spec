%global source0_hash 838c5306fc38bfaa2f23abe24262f4bf15771e3303fb5dcb74f5b9c7a615dabe

Name:           gnome-autoar
Version:        0.4.5
Release:        4%{?dist}
Summary:        Archive library

License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-autoar
Source0:        https://download.gnome.org/sources/%{name}/0.4/%{name}-%{version}.tar.xz


BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  vala

%description
gnome-autoar is a GObject based library for handling archives.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1


%build
%meson -Dvapi=true \
       -Dgtk_doc=true \
       -Dtests=true \
        %{nil}
%meson_build


%install
%meson_install


%check
%meson_test


%files
%license COPYING
%doc NEWS
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GnomeAutoar-0.1.typelib
%{_libdir}/girepository-1.0/GnomeAutoarGtk-0.1.typelib
%{_libdir}/libgnome-autoar-0.so.0*
%{_libdir}/libgnome-autoar-gtk-0.so.0*

%files devel
%{_includedir}/gnome-autoar-0/
%{_libdir}/pkgconfig/gnome-autoar-0.pc
%{_libdir}/pkgconfig/gnome-autoar-gtk-0.pc
%{_libdir}/*.so
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GnomeAutoar-0.1.gir
%{_datadir}/gir-1.0/GnomeAutoarGtk-0.1.gir
%{_datadir}/gtk-doc/
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gnome-autoar-0.vapi
%{_datadir}/vala/vapi/gnome-autoar-gtk-0.vapi
%{_datadir}/vala/vapi/gnome-autoar-0.deps
%{_datadir}/vala/vapi/gnome-autoar-gtk-0.deps


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.5-4
- Prepare for Oreon 11 (RP1)
