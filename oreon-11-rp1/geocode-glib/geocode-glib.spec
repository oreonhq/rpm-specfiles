%global source0_hash 2d9a6826d158470449a173871221596da0f83ebdcff98b90c7049089056a37aa
%global json_glib_version 0.99.2
Name:           geocode-glib
Version:        3.26.4
Release:        1%{?dist}
Summary:        Geocoding helper library
License:        LGPL-2.0-or-later AND BSD-3-Clause
URL:            http://www.gnome.org/
Source0:        http://download.gnome.org/sources/%{name}/3.26/%{name}-%{version}.tar.xz
Requires:       json-glib%{?_isa} >= %{json_glib_version}
Obsoletes:      geocode-glib-data < %{version}-%{release}
Obsoletes:      geocode-glib2 < %{version}-%{release}
Provides:       geocode-glib2 = %{version}-%{release}
Provides:       geocode-glib2%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)
# /oreon:deps
%description
geocode-glib is a convenience library for the geocoding (finding longitude,
and latitude from an address) and reverse geocoding (finding an address from
coordinates). It uses Nominatim service to achieve that. It also caches
(reverse-)geocoding requests for faster results and to avoid unnecessary server
load.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      geocode-glib2-devel < %{version}-%{release}
Provides:       geocode-glib2-devel = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%meson -Denable-installed-tests=false -Dsoup2=false
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n geocode-glib-devel -f %{oreon_filedir}/geocode-glib-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.26.4-1
- Prepare for Oreon 11 (RP1)
