%global source0_hash 919f529512961a12e81cd4b4b466a48c3933469e7f9a310c6513cd4fb252ba3c
Name:           gdk-pixbuf2-modules-extra
Version:        2.44.8
Release:        1%{?dist}
Summary:        Extra image loaders for gdk-pixbuf2
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/gdk-pixbuf
Source0:        https://download.gnome.org/sources/gdk-pixbuf/2.44/gdk-pixbuf-%{version}.tar.xz
Requires:       gdk-pixbuf2%{?_isa} > 2.43.0
%global contents modules for loading ANI, ICNS, QTIF, XBM, and XPM images
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  shared-mime-info
# /oreon:deps
%description
gdk-pixbuf is an image loading library that can be extended by loadable
modules for new image formats. It is used by toolkits such as GTK+ or
clutter.

This package contains %{contents}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gdk-pixbuf-%{version}
%oreon_prep
%build

%meson \
       -Dpng=disabled \
       -Dtiff=disabled \
       -Djpeg=disabled \
       -Dgif=disabled \
       -Dglycin=disabled \
       -Dandroid=disabled \
       -Dothers=enabled \
       -Dbuiltin_loaders=none \
       -Ddocumentation=false \
       -Dintrospection=disabled \
       -Dman=false \
       -Dinstalled_tests=false \
       -Dthumbnailer=disabled \
       %{nil}
%global _smp_mflags -j1
%meson_build
%check

%meson_test
%install
%meson_install
rm -r $RPM_BUILD_ROOT%{_bindir}
rm -r $RPM_BUILD_ROOT%{_datadir}/locale
rm -r $RPM_BUILD_ROOT%{_includedir}
rm    $RPM_BUILD_ROOT%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-{bmp,ico,pnm,tga}.so
rm    $RPM_BUILD_ROOT%{_libdir}/libgdk_pixbuf-2.0*
rm -r $RPM_BUILD_ROOT%{_libdir}/pkgconfig
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
