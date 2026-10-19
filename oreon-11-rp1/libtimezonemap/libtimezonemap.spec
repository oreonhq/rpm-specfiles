%global source0_hash 7d4896b81f63a3f485a7115381098bd5068c7e36920087cd9adf7372e4328200
Name:           libtimezonemap
Version:        0.4.5.4
Release:        2%{?dist}
Summary:        Time zone map widget for Gtk+
License:        GPL-3.0-only
URL:            https://launchpad.net/timezonemap
Source0:        https://codeberg.org/dashea/timezonemap/archive/%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  json-glib-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libsoup3-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
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
%global oreon_srcdir timezonemap
%oreon_prep
%build

./autogen.sh
%configure --disable-static
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libtimezonemap-devel -f %{oreon_filedir}/libtimezonemap-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.5.4-2
- Import
