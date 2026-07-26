%global source0_hash 3641d4fd669d1e1818aeff3cf9ffb7887fc5c367850b78c28c775eba4ab6a555

Name:		libgdl
Epoch:		1
Version:	3.40.0
Release:	14%{?dist}
Summary:	GNOME docking library

License:	LGPL-2.1-or-later
URL:		https://gitlab.gnome.org/Archive/gdl
Source0:	https://download.gnome.org/sources/gdl/3.40/gdl-%{version}.tar.xz
# https://gitlab.gnome.org/GNOME/gdl/-/merge_requests/4
Patch0:		libgdl-3.40.0-libxml2-2.12.0-includes.patch
Patch1:         pointers.patch

BuildRequires:	gettext
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	make
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxml-2.0)

%description
GDL adds dockable widgets to GTK+. The user can rearrange those widgets by drag
and drop and layouts can be saved and loaded. Currently it is used by anjuta,
inkscape, gtranslator and others.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
This package contains development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n gdl-%{version} -p1

%build
%configure \
  --disable-silent-rules \
  --disable-static \
  --enable-introspection=yes

# Omit unused direct shared library dependencies.
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build

%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%find_lang gdl-3

%ldconfig_scriptlets

%files -f gdl-3.lang
%license COPYING
%doc AUTHORS
%doc MAINTAINERS
%doc NEWS
%doc README
%{_libdir}/%{name}-3.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Gdl-3.typelib

%files devel
%{_libdir}/%{name}-3.so
%{_libdir}/pkgconfig/gdl-3.0.pc

%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Gdl-3.gir

%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%doc %{_datadir}/gtk-doc/html/gdl-3.0/

%dir %{_includedir}/%{name}-3.0
%{_includedir}/%{name}-3.0/gdl

%changelog
%autochangelog
