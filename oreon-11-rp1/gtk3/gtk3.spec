%global source0_hash 80931fa472a77b9a164f6740e3c0b444fac6770054632d35a7ff9d679e5e7b9f
%global with_broadway 0
%global with_cloudproviders 0
%global with_tracker3 0
%global glib2_version 2.57.2
%global pango_version 1.41.0
%global atk_version 2.35.1
%global cairo_version 1.14.0
%global gdk_pixbuf_version 2.30.0
%global xrandr_version 1.5.0
%global wayland_protocols_version 1.17
%global wayland_version 1.14.91
%global epoxy_version 1.4
%global bin_version 3.0.0
%global __provides_exclude_from ^%{_libdir}/gtk-3.0
Name:    gtk3
Version: 3.24.52
Release:        1%{?dist}
Summary:        GTK+ graphical user interface library
License: LGPL-2.0-or-later
URL:     https://gtk.org
Source0:        https://download.gnome.org/sources/gtk/3.24/gtk-%{version}.tar.xz
%if 0%{?with_cloudproviders}
%endif
Requires: adwaita-icon-theme
Requires: hicolor-icon-theme
Requires: gtk-update-icon-cache
Requires: atk%{?_isa} >= %{atk_version}
Requires: cairo%{?_isa} >= %{cairo_version}
Requires: cairo-gobject%{?_isa} >= %{cairo_version}
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: libepoxy%{?_isa} >= %{epoxy_version}
Requires: libwayland-client%{?_isa} >= %{wayland_version}
Requires: libwayland-cursor%{?_isa} >= %{wayland_version}
Requires: libXrandr%{?_isa} >= %{xrandr_version}
Requires: pango%{?_isa} >= %{pango_version}
Requires: colord-libs%{?_isa}
Requires: at-spi2-atk%{?_isa}
Recommends: dconf%{?_isa}
Recommends: libcanberra-gtk3%{?_isa}
Recommends: tracker-miners
Recommends: (ibus-gtk3 if ibus)
# oreon:deps
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(atk-bridge-2.0)
BuildRequires:  pkgconfig(avahi-gobject)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
# /oreon:deps
%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains version 3 of GTK+.

%package -n gtk-update-icon-cache
Summary: Icon theme caching utility
%description -n gtk-update-icon-cache
GTK+ can use the cache files created by gtk-update-icon-cache to avoid a lot of
system call and disk seek overhead when the application starts. Since the
format of the cache files allows them to be mmap()ed shared between multiple
applications, the overall memory consumption is reduced as well.

%package immodules
Summary: Input methods for GTK+
Requires: gtk3%{?_isa} = %{version}-%{release}
Requires: gtk2-immodules%{?_isa}
%description immodules
The gtk3-immodules package contains standalone input methods that
are shipped as part of GTK+ 3.

%package immodule-xim
Summary: XIM support for GTK+
Requires: gtk3%{?_isa} = %{version}-%{release}
%description immodule-xim
The gtk3-immodule-xim package contains XIM support for GTK+ 3.

%package devel
Summary: Development files for GTK+
Requires: gtk3%{?_isa} = %{version}-%{release}
%description devel
This package contains the libraries and header files that are needed
for writing applications with version 3 of the GTK+ widget toolkit. If
you plan to develop applications with GTK+, consider installing the
gtk3-devel-docs package.

%package devel-docs
Summary: Developer documentation for GTK+
Requires: gtk3 = %{version}-%{release}
%description devel-docs
This package contains developer documentation for version 3 of the GTK+
widget toolkit.

%package tests
Summary: Tests for the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gtk-%{version}
%oreon_prep
%build

export CFLAGS='-fno-strict-aliasing %optflags'
%meson \
%if 0%{?with_broadway}
        -Dbroadway_backend=true \
%endif
        -Dbuiltin_immodules=wayland,waylandgtk \
        -Dcolord=yes \
%if 0%{?with_cloudproviders}
        -Dcloudproviders=true \
%else
        -Dcloudproviders=false \
%endif
        -Dgtk_doc=true \
        -Dinstalled_tests=true \
        -Dman=true \
        -Dprofiler=true \
        -Dtracker3=false \
        -Dxinerama=yes \
%meson_build
%install
%meson_install
%find_lang gtk30
%find_lang gtk30-properties
(cd $RPM_BUILD_ROOT%{_bindir}
 mv gtk-query-immodules-3.0 gtk-query-immodules-3.0-%{__isa_bits}
)
echo ".so man1/gtk-query-immodules-3.0.1" > $RPM_BUILD_ROOT%{_mandir}/man1/gtk-query-immodules-3.0-%{__isa_bits}.1
touch $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/%{bin_version}/immodules.cache
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/gtk-3.0
mkdir -p $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/modules
mkdir -p $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/immodules
%oreon_autofiles gtk-update-icon-cache usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%transfiletriggerin -- %{_libdir}/gtk-3.0/3.0.0/immodules
gtk-query-immodules-3.0-%{__isa_bits} --update-cache &>/dev/null || :
%transfiletriggerpostun -- %{_libdir}/gtk-3.0/3.0.0/immodules
gtk-query-immodules-3.0-%{__isa_bits} --update-cache &>/dev/null || :
%files -f %{oreon_filedir}/main.list
%files -n gtk-update-icon-cache -f %{oreon_filedir}/gtk-update-icon-cache.list
%files -n gtk3-immodules -f %{oreon_filedir}/gtk3-immodules.list
%files -n gtk3-immodule-xim -f %{oreon_filedir}/gtk3-immodule-xim.list
%files -n gtk3-devel -f %{oreon_filedir}/gtk3-devel.list
%files -n gtk3-devel-docs -f %{oreon_filedir}/gtk3-devel-docs.list
%files -n gtk3-tests -f %{oreon_filedir}/gtk3-tests.list

%changelog

%autochangelog
