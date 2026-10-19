%global source0_hash 919f529512961a12e81cd4b4b466a48c3933469e7f9a310c6513cd4fb252ba3c
%global glib2_version 2.56.0
%global glycin_version 2.0.1
%global __meson_auto_features disabled
Name:           gdk-pixbuf2
Version:        2.44.8
Release:        1%{?dist}
Summary:        An image loading library
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/gdk-pixbuf
Source0:        https://download.gnome.org/sources/gdk-pixbuf/2.44/gdk-pixbuf-%{version}.tar.xz
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: glycin-libs%{?_isa} >= %{glycin_version}
Requires: shared-mime-info
Obsoletes: %{name}-modules < %{version}-%{release}
Obsoletes: avif-pixbuf-loader <= 1.1.1-4
Provides:  avif-pixbuf-loader
Obsoletes: heif-pixbuf-loader <= 1.20.1-2
Provides:  heif-pixbuf-loader
Obsoletes: jxl-pixbuf-loader <= 0.11.1-4
Provides:  jxl-pixbuf-loader
Obsoletes: rsvg-pixbuf-loader <= 2.61.0-1
Provides:  rsvg-pixbuf-loader
Obsoletes: webp-pixbuf-loader <= 0.2.7-4
Provides:  webp-pixbuf-loader
# oreon:deps
BuildRequires:  /usr/bin/rst2man
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glycin-2)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  shared-mime-info
# /oreon:deps
%description
gdk-pixbuf is an image loading library that can be extended by loadable
modules for new image formats. It is used by toolkits such as GTK+ or
clutter.

%package devel
Summary: Development files for gdk-pixbuf2
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: glib2-devel%{?_isa} >= %{glib2_version}
Recommends: gi-docgen-fonts
%description devel
This package contains the libraries and header files that are needed
for writing applications that are using gdk-pixbuf2.

%package tests
Summary: Tests for the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gdk-pixbuf-%{version}
%oreon_prep
%build

%meson \
       -Ddocumentation=true \
       -Dintrospection=enabled \
       -Dglycin=enabled \
       -Dlegacy_xpm=enabled \
       %{nil}
%meson_build
%install
%meson_install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders
touch $RPM_BUILD_ROOT%{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders.cache
(cd $RPM_BUILD_ROOT%{_bindir}
 mv gdk-pixbuf-query-loaders gdk-pixbuf-query-loaders-%{__isa_bits}
)
sed -i -e 's/gdk-pixbuf-query-loaders/gdk-pixbuf-query-loaders-%{__isa_bits}/' \
    $RPM_BUILD_ROOT%{_libdir}/pkgconfig/gdk-pixbuf-2.0.pc
%find_lang gdk-pixbuf
%transfiletriggerin -- %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders
gdk-pixbuf-query-loaders-%{__isa_bits} --update-cache
%transfiletriggerpostun -- %{_libdir}/gdk-pixbuf-2.0/2.10.0/loaders
gdk-pixbuf-query-loaders-%{__isa_bits} --update-cache
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gdk-pixbuf2-devel -f %{oreon_filedir}/gdk-pixbuf2-devel.list
%files -n gdk-pixbuf2-tests -f %{oreon_filedir}/gdk-pixbuf2-tests.list

%changelog

%autochangelog
