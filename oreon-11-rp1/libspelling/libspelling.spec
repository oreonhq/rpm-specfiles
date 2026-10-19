%global source0_hash 56e3f01a3a18b575beea4c34349f99cdaba316e1f7c271b1231f7bcf5d9af73b
Name:           libspelling
Version:        0.4.10
Release:        1%{?dist}
Summary:        Spellcheck library for GTK 4
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/libspelling
Source0:        https://download.gnome.org/sources/libspelling/0.4/libspelling-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  meson
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  vala
# /oreon:deps
%description
A spellcheck library for GTK 4.  This library is heavily based upon GNOME Text
Editor and GNOME Builder's spellcheck implementation.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libspelling-%{version}
%oreon_prep
%build

%meson -Ddocs=false
%meson_build
%install
%meson_install
%find_lang libspelling
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n libspelling-devel -f %{oreon_filedir}/libspelling-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.10-1
- Prepare for Oreon 11 (RP1)
