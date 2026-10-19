%global source0_hash 28ba4ac1c04f86eac09b79a163cb163a4c2b54442d9f7eccc04679062a581044
%global glib2_version 2.84.0
%global pango_version 1.56.0
%global cairo_version 1.18.0
%global gdk_pixbuf_version 2.30.0
%global gstreamer_version 1.28.0
%global harfbuzz_version 8.4
%global wayland_protocols_version 1.31
%global wayland_version 1.21.0
%global epoxy_version 1.4
%global bin_version 4.0.0
%global __provides_exclude_from ^%{_libdir}/gtk-4.0
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%ifarch %{ix86}
%global build_type_safety_c 1
%endif
%endif
Name:           gtk4
Version:        4.24.0
Release:        1%{?dist}
Summary:        GTK graphical user interface library
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later AND Apache-2.0 AND CC0-1.0 AND MIT AND MIT-open-group AND HPND-sell-variant AND GPL-2.0-or-later AND GPL-3.0-or-later AND OFL-1.1
URL:            https://www.gtk.org
Source0:        https://download.gnome.org/sources/gtk/4.24/gtk-%{version}.tar.xz
Requires: adwaita-icon-theme
Requires: hicolor-icon-theme
Requires: gtk-update-icon-cache
Requires: shared-mime-info
Requires: cairo%{?_isa} >= %{cairo_version}
Requires: cairo-gobject%{?_isa} >= %{cairo_version}
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: harfbuzz%{?_isa} >= %{harfbuzz_version}
Requires: libepoxy%{?_isa} >= %{epoxy_version}
Requires: gstreamer1-plugins-bad-free-libs%{?_isa} >= %{gstreamer_version}
Requires: libwayland-client%{?_isa} >= %{wayland_version}
Requires: libwayland-cursor%{?_isa} >= %{wayland_version}
Requires: pango%{?_isa} >= %{pango_version}
Recommends: dconf%{?_isa}
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/rst2man
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  glslc
BuildRequires:  meson
BuildRequires:  pkgconfig(avahi-gobject)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(graphene-gobject-1.0)
BuildRequires:  pkgconfig(gstreamer-play-1.0)
BuildRequires:  pkgconfig(gstreamer-player-1.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:  pkgconfig(vulkan)
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
BuildRequires:  python3-gobject
# /oreon:deps
%description
GTK is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK is suitable for
projects ranging from small one-off tools to complete application
suites.

This package contains version 4 of GTK.

%package devel
Summary: Development files for GTK
Requires: gtk4%{?_isa} = %{version}-%{release}
%description devel
This package contains the libraries and header files that are needed
for writing applications with version 4 of the GTK widget toolkit.

%package devel-docs
Summary: Developer documentation for GTK
BuildArch: noarch
Requires: gtk4 = %{version}-%{release}
Recommends: gi-docgen-fonts
%description devel-docs
This package contains developer documentation for version 4 of the GTK
widget toolkit.

%package devel-tools
Summary: Developer tools for GTK
Requires: gtk4%{?_isa} = %{version}-%{release}
%description devel-tools
This package contains helpful applications for developers using GTK.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gtk-%{version}
%oreon_prep
%build

export CFLAGS='-std=c11 -fno-strict-aliasing -DG_DISABLE_CAST_CHECKS -DG_DISABLE_ASSERT %optflags'
%meson --wrap-mode=nofallback \
%if 0%{?with_broadway}
        -Dbroadway-backend=true \
%endif
        -Dsysprof=enabled \
        -Dtracker=enabled \
        -Dcolord=enabled \
        -Ddocumentation=true \
        -Dman-pages=true \
        -Dbuild-testsuite=false \
        -Dbuild-tests=false \
        -Dbuild-examples=false
%meson_build
%install
%meson_install
%find_lang gtk40
%if !0%{?with_broadway}
rm $RPM_BUILD_ROOT%{_mandir}/man1/gtk4-broadwayd.1*
%endif
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/gtk-4.0
mkdir -p $RPM_BUILD_ROOT%{_libdir}/gtk-4.0/modules
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/*.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n gtk4-devel -f %{oreon_filedir}/gtk4-devel.list
%files -n gtk4-devel-docs -f %{oreon_filedir}/gtk4-devel-docs.list
%files -n gtk4-devel-tools -f %{oreon_filedir}/gtk4-devel-tools.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.22.1-1
- Prepare for Oreon 11 (RP1)
