%global source0_hash 46c1172a53cf974a73dc13a2142d022ec6a8dfa614133815df3aa5ede9af0cc1

%global commit      f240b2ec7d5cdacb8fdcc553703420dc5101ffdb
%global shortcommit %{lua:print(macros.commit:sub(1,7))}

Name:           pqmarble
Version:        2.0.0~^1.%{shortcommit}
Release:        %autorelease
Summary:        Utility library for GNOME apps
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/raggesilver/marble
Source:         %{url}/-/archive/%{commit}/marble-%{shortcommit}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)

%description
PQMarble is a utility library for GNOME apps.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n marble-%{commit}

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%{_libdir}/libpqmarble.so.2*
%{_libdir}/girepository-1.0/PQMarble-2.typelib

%files devel
%{_includedir}/pqmarble.h
%{_libdir}/libpqmarble.so
%{_libdir}/pkgconfig/pqmarble.pc
%{_datadir}/gir-1.0/PQMarble-2.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/pqmarble.deps
%{_datadir}/vala/vapi/pqmarble.vapi

%changelog
%autochangelog
