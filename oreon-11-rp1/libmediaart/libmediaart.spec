%global source0_hash 2b43dd9f54f0d8d0b89e2addb83341ab06d7b98cb1b2e704383584af9c560f6b

Name:           libmediaart
Version:        1.9.7
Release:        4%{?dist}
Summary:        Library for managing media art caches

License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/libmediaart
Source0:        https://download.gnome.org/sources/%{name}/1.9/%{name}-%{version}.tar.xz

# https://gitlab.gnome.org/GNOME/libmediaart/-/merge_requests/21
# move to glycin to avoid https://gitlab.gnome.org/GNOME/gdk-pixbuf/-/issues/293
Patch: 21.patch

BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0) pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glycin-2)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
%if 0%{?rhel} == 8
# Test requires the jpeg gdk-pixbuf loader, which isn't built-in
BuildRequires:  gdk-pixbuf2-modules
%endif
BuildRequires:  vala

# Removed in F34
Obsoletes: libmediaart-tests < 1.9.5

%description
Library tasked with managing, extracting and handling media art caches.


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
%meson -Dimage_library=glycin -Dgtk_doc=true
%meson_build


%install
%meson_install


%check
%meson_test


%files
%license COPYING.LESSER
%doc NEWS
%{_libdir}/libmediaart-2.0.so.0*
%{_libdir}/girepository-1.0/MediaArt-2.0.typelib

%files devel
%{_includedir}/libmediaart-2.0
%{_libdir}/libmediaart-2.0.so
%{_libdir}/pkgconfig/libmediaart-2.0.pc
%{_datadir}/gir-1.0/MediaArt-2.0.gir
%{_datadir}/gtk-doc/html/libmediaart
%{_datadir}/vala/vapi/libmediaart-2.0.deps
%{_datadir}/vala/vapi/libmediaart-2.0.vapi


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9.7-4
- Prepare for Oreon 11 (RP1)
