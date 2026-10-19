%global source0_hash 8b8e1c270ec16a06f665ea841f8e4e167eaa0118d0cbfeeade43745f09198ff7
Name:           gdk-pixbuf2-xlib
Version:        2.40.2
Release:        1%{?dist}
Summary:        Deprecated Xlib integration for gdk-pixbuf2
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/Archive/gdk-pixbuf-xlib
Source0:        https://download.gnome.org/sources/gdk-pixbuf-xlib/2.40/gdk-pixbuf-xlib-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(x11)
# /oreon:deps
%description
gdk-pixbuf2-xlib contains the deprecated API for integrating gdk-pixbuf2 with
Xlib data types.

This library was originally shipped by gdk-pixbuf2, and has
since been moved out of the original repository.

No newly written code should ever use this library.

If your existing code depends on gdk-pixbuf2-xlib, then you're strongly
encouraged to port away from it.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gdk-pixbuf-xlib-%{version}
%oreon_prep
%build

%meson -Dgtk_doc=true
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
