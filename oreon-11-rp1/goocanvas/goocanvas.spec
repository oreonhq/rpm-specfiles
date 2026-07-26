%global source0_hash 1c072ef88567cad241fb4addee26e9bd96741b1503ff736d1c152fa6d865711e

Name:           goocanvas
Version:        1.0.0
Release:        30%{?dist}
Summary:        A canvas widget for GTK+ that uses cairo for drawing

License:        LGPL-2.0-or-later
URL:            https://wiki.gnome.org/Projects/GooCanvas
Source0:        https://download.gnome.org/sources/%{name}/1.0/%{name}-%{version}.tar.bz2
Patch0:         %{name}-fix-gcc14-build.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig, gettext, gtk2-devel
BuildRequires:  cairo-devel >= 1.4.0
BuildRequires:  make

%description
GooCanvas is a canvas widget for GTK+ that uses the cairo 2D library for
drawing. It has a model/view split, and uses interfaces for canvas items and
views, so you can easily turn any application object into canvas items.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%set_build_flags
%configure
%make_build

%install
%make_install

# remove static libraries and libtool droppings
rm -f $RPM_BUILD_ROOT/%{_libdir}/lib%{name}.{a,la}

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/lib%{name}.so\.*

%package devel
Summary:        A new canvas widget for GTK+ that uses cairo for drawing
Requires:       %{name} = %{version}-%{release} pkgconfig

%description devel
GooCanvas is a new canvas widget for GTK+ that uses the cairo 2D library for
drawing. It has a model/view split, and uses interfaces for canvas items and
views, so you can easily turn any application object into canvas items.

These are the files used for development.

%files devel
%{_includedir}/%{name}-1.0
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gtk-doc/html/%{name}

%changelog
%autochangelog
