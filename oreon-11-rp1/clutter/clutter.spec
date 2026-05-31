%global source0_hash 8b48fac159843f556d0a6be3dbfc6b083fc6d9c58a20a49a6b4919ab4263c4e6

%global with_tests 1

%global glib2_version 2.53.4
%global cogl_version 1.21.2
%global json_glib_version 0.12.0
%global cairo_version 1.14.0
%global libinput_version 0.19.0

Name:          clutter
Version:       1.26.4
Release:       19%{?dist}
Summary:       Open Source software library for creating rich graphical user interfaces

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
URL:           http://www.clutter-project.org/
Source0:        https://download.gnome.org/sources/%{name}/1.26/%{name}-%{version}.tar.xz

BuildRequires: gettext
BuildRequires: pkgconfig(atk)
BuildRequires: pkgconfig(cairo-gobject) >= %{cairo_version}
BuildRequires: pkgconfig(cogl-1.0) >= %{cogl_version}
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(gobject-introspection-1.0) >= 1.39.0
BuildRequires: pkgconfig(gdk-3.0)
BuildRequires: pkgconfig(json-glib-1.0) >= %{json_glib_version}
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xi)
BuildRequires: mesa-libEGL-devel
BuildRequires: mesa-libGL-devel
BuildRequires: systemd-devel
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(libinput) >= %{libinput_version}
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: make

Requires:      cairo%{?_isa} >= %{cairo_version}
Requires:      cogl%{?_isa} >= %{cogl_version}
Requires:      glib2%{?_isa} >= %{glib2_version}
Requires:      json-glib%{?_isa} >= %{json_glib_version}
Requires:      libinput%{?_isa} >= %{libinput_version}

Recommends:    mesa-dri-drivers%{?_isa}

%description
Clutter is an open source software library for creating fast,
visually rich graphical user interfaces. The most obvious example
of potential usage is in media center type applications.
We hope however it can be used for a lot more.

%package devel
Summary:       Clutter development environment
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for building a extension library for the
clutter

%package       doc
Summary:       Documentation for %{name}
Requires:      %{name} = %{version}-%{release}

%description   doc
Clutter is an open source software library for creating fast,
visually rich graphical user interfaces. The most obvious example
of potential usage is in media center type applications.
We hope however it can be used for a lot more.

This package contains documentation for clutter.

%if 0%{?with_tests}
%package       tests
Summary:       Tests for the clutter package
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   tests
The clutter-tests package contains tests that can be used to verify
the functionality of the installed clutter package.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%build
%configure \
	--enable-xinput \
        --enable-gdk-backend \
	%{?with_tests:--enable-installed-tests} \
        --enable-egl-backend \
        --enable-evdev-input \
        --enable-wayland-backend \
        --enable-wayland-compositor

make %{?_smp_mflags} V=1

%install
%make_install

#Remove libtool archives.
find %{buildroot} -name '*.la' -delete

%find_lang clutter-1.0

%files -f clutter-1.0.lang
%doc NEWS README.md
%license COPYING
%{_libdir}/*.so.0
%{_libdir}/*.so.0.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/*.typelib

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_datadir}/clutter-1.0
%dir %{_datadir}/clutter-1.0/valgrind
%{_datadir}/clutter-1.0/valgrind/clutter.supp
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/*.gir

%files doc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/clutter

%if 0%{?with_tests}
%files tests
%{_libexecdir}/installed-tests/clutter
%{_datadir}/installed-tests
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.26.4-19
- Prepare for Oreon 11 (RP1)
