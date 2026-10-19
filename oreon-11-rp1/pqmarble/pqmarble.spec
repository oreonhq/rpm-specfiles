%global source0_hash 46c1172a53cf974a73dc13a2142d022ec6a8dfa614133815df3aa5ede9af0cc1
%global commit      f240b2ec7d5cdacb8fdcc553703420dc5101ffdb
%global shortcommit %{lua:print(macros.commit:sub(1,7))}
Name:           pqmarble
Version:        2.0.0~^1.%{shortcommit}
Release:        1%{?dist}
Summary:        Utility library for GNOME apps
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/raggesilver/marble
Source0:        https://gitlab.gnome.org/raggesilver/marble/-/archive/%{commit}/marble-f240b2e.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  vala
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n pqmarble-devel -f %{oreon_filedir}/pqmarble-devel.list

%changelog

%autochangelog
