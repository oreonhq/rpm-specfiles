%global source0_hash 277d6835220a6a2954e09eb304a8cd6ff49b72542c97c4fc36e53e905f2a747c
Name:           osm-gps-map
Version:        1.2.1
Release:        1%{?dist}
Summary:        Gtk+ widget for displaying OpenStreetMap tiles
License:        GPL-2.0-or-later
URL:            https://github.com/nzjrs/%{name}/
Source0:        https://github.com/nzjrs/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gnome-common
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  libsoup-devel
BuildRequires:  make
# /oreon:deps
%description
A Gtk+ widget that when given GPS co-ordinates, draws a GPS track, and
points of interest on a moving map display. Downloads map data from a
number of websites, including openstreetmap.org.

%package devel
Summary:        Development files for the osm-gps-map Gtk+ widget
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The development files for the osm-gps-map Gtk+ widget

%package gobject
Summary:        GObject introspection bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gobject-introspection
%description gobject
GObject introspection bindings for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
%make_build
%install
%make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n osm-gps-map-devel -f %{oreon_filedir}/osm-gps-map-devel.list
%files -n osm-gps-map-gobject -f %{oreon_filedir}/osm-gps-map-gobject.list

%changelog

%autochangelog
