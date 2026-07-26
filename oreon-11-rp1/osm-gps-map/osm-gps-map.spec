%global source0_hash ddec11449f37b5dffb4bca134d024623897c6140af1f9981a8acc512dbf6a7a5

Name:           osm-gps-map
Version:        1.2.0
Release:        3%{?dist}
Summary:        Gtk+ widget for displaying OpenStreetMap tiles

License:        GPL-2.0-or-later
URL:            https://github.com/nzjrs/%{name}/
Source0:        https://github.com/nzjrs/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gnome-common
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  libsoup-devel

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

%autosetup

%build
%configure --disable-static
%make_build

%install
%make_install

%files
%doc AUTHORS README NEWS ChangeLog
%license COPYING
%exclude %{_libdir}/*.la
%exclude %{_datadir}/gtk-doc/html/libosmgpsmap/
%if 0%{?rhel} <= 7
%exclude %{_datadir}/doc/%{name}/
%endif

%{_libdir}/libosmgpsmap-1.0.so.1{,.*}

%files gobject
%{_libdir}/girepository-1.0/OsmGpsMap-1.0.typelib

%files devel
%{_includedir}/osmgpsmap-1.0
%{_libdir}/libosmgpsmap-1.0.so
%{_libdir}/pkgconfig/osmgpsmap-1.0.pc
%{_datarootdir}/gir-1.0/OsmGpsMap-1.0.gir

%changelog
%autochangelog
