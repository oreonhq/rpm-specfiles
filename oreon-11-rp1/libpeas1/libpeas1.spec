%global source0_hash 297cb9c2cccd8e8617623d1a3e8415b4530b8e5a893e3527bbfd1edd13237b4c
%bcond glade %[!(0%{?rhel} >= 10)]
%global apiver 1.0
%global tarball_name libpeas
Name:           libpeas1
Version:        1.36.0
Release:        1%{?dist}
Summary:        Plug-ins implementation convenience library, API version 1
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/Libpeas
Source0:        https://download.gnome.org/sources/%{tarball_name}/1.36/%{tarball_name}-%{version}.tar.xz
Patch0:        73e25b6059d2fdc090a3feb8341ff902c3ec0d16.patch
Patch1:        4613accc2e22395bb77bdf612fcdf90bf65f230f.patch
%if %{with glade}
%endif
Conflicts:      libpeas < 2.0
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gladeui-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3-devel
# /oreon:deps
%description
libpeas1 is a convenience library making adding plug-ins support
to glib-based applications. For the version based on newer GLib, see the
libpeas package.

%package gtk
Summary:        GTK+ 3 plug-ins support for libpeas1
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      libpeas-gtk < 2.0
Conflicts:      libpeas-gtk < 2.0
Provides:       libpeas-gtk = %{version}-%{release}
Provides:       libpeas-gtk%{?_isa} = %{version}-%{release}
%description gtk
libpeas1-gtk is a convenience library making adding plug-ins support
to GTK+ 3-based applications.

%package loader-python3
Summary:        Python 3 loader for libpeas1
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-gobject
Obsoletes:      libpeas-loader-python3 < 2.0
Conflicts:      libpeas-loader-python3 < 2.0
Provides:       libpeas-loader-python3 = %{version}-%{release}
Provides:       libpeas-loader-python3%{?_isa} = %{version}-%{release}
%description loader-python3
This package contains the Python 3 loader that is needed to
run Python 3 plugins that use libpeas1.

%package devel
Summary:        Development files for libpeas1
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-gtk%{?_isa} = %{version}-%{release}
Recommends:     gi-docgen-fonts
Obsoletes:      libpeas-devel < 2.0
Conflicts:      libpeas-devel < 2.0
%description devel
This package contains development libraries and header files
that are needed to write applications that use libpeas1.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{tarball_name}-%{version}

%build

%meson \
  -Ddemos=false \
  %{!?with_glade:-Dglade_catalog=false} \
  -Dvapi=true \
  -Dgtk_doc=true
%meson_build
%install
%meson_install
%find_lang libpeas-%{apiver}
%oreon_autofiles main usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libpeas1-gtk -f %{oreon_filedir}/libpeas1-gtk.list
%files -n libpeas1-loader-python3 -f %{oreon_filedir}/libpeas1-loader-python3.list
%files -n libpeas1-devel -f %{oreon_filedir}/libpeas1-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.36.0-1
- Import
