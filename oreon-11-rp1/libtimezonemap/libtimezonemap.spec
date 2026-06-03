%global source0_hash none

Name:           libtimezonemap
Version:        0.4.5.4
Release:        2%{?dist}
Summary:        Time zone map widget for Gtk+

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://launchpad.net/timezonemap
Source0:        https://codeberg.org/dashea/timezonemap/archive/%{version}.tar.gz

BuildRequires:  autoconf automake libtool
BuildRequires:  glib2-devel >= 2.26
BuildRequires:  gtk3-devel >= 3.1.4
BuildRequires:  json-glib-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  libsoup3-devel >= 3.0.7
BuildRequires:  librsvg2-devel
BuildRequires: make

%description
libtimezonemap is a time zone map widget for Gtk+. The widget displays a world
map with a highlighted region representing the selected time zone, and the
location can be changed by clicking on the map.

This library is a fork of the of the code from gnome-control-center's datetime
panel, which was itself a fork of Ubiquity's timezone map.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
libtimezonemap is a time zone map widget for Gtk+. This package contains header
files used for building applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n timezonemap

%build
./autogen.sh
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%license COPYING
%doc README TODO
%{_libdir}/libtimezonemap.so.*
%{_libdir}/girepository-1.0/TimezoneMap-1.0.typelib
%{_datadir}/%{name}

%files devel
%{_libdir}/libtimezonemap.so
%{_libdir}/pkgconfig/timezonemap.pc
%{_includedir}/timezonemap
%{_datadir}/gir-1.0/TimezoneMap-1.0.gir
%{_datadir}/glade/catalogs/TimezoneMap.xml

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.5.4-2
- Import
