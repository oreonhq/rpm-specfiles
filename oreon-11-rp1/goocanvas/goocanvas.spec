%global source0_hash 1c072ef88567cad241fb4addee26e9bd96741b1503ff736d1c152fa6d865711e
Name:           goocanvas
Version:        3.0.0
Release:        1%{?dist}
Summary:        A canvas widget for GTK+ that uses cairo for drawing
License:        LGPL-2.0-or-later
URL:            https://wiki.gnome.org/Projects/GooCanvas
Source0:        https://download.gnome.org/sources/%{name}/1.0/%{name}-%{version}.tar.bz2
Patch0:         %{name}-fix-gcc14-build.patch
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
GooCanvas is a canvas widget for GTK+ that uses the cairo 2D library for
drawing. It has a model/view split, and uses interfaces for canvas items and
views, so you can easily turn any application object into canvas items.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%set_build_flags
%configure
%make_build
%install
%make_install
rm -f $RPM_BUILD_ROOT/%{_libdir}/lib%{name}.{a,la}
%find_lang %{name}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%package devel
Summary:        A new canvas widget for GTK+ that uses cairo for drawing
Requires:       %{name} = %{version}-%{release} pkgconfig
%description devel
GooCanvas is a new canvas widget for GTK+ that uses the cairo 2D library for
drawing. It has a model/view split, and uses interfaces for canvas items and
views, so you can easily turn any application object into canvas items.

These are the files used for development.

%files -f %{oreon_filedir}/main.list
%files -n goocanvas-devel -f %{oreon_filedir}/goocanvas-devel.list

%changelog

%autochangelog
