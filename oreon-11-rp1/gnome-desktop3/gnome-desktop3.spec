%global source0_hash 9ebeb9f1769d3c310caeadd921ab34c8f264b92937740518b3bc859a579a6912
%global gdk_pixbuf2_version               2.36.5
%global gtk3_version                      3.3.6
%global gtk4_version                      4.12.0
%global glib2_version                     2.53.0
%global gsettings_desktop_schemas_version 3.27.0
%global po_package                        gnome-desktop-3.0
%global tarball_version %(echo %{version} | tr '~' '.')
Name:    gnome-desktop3
Version: 51.0
Release:        1%{?dist}
Summary:        Library with common API for various GNOME modules
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND GFDL-1.1-or-later
URL:     https://gitlab.gnome.org/GNOME/gnome-desktop
Source0:        https://download.gnome.org/sources/gnome-desktop/51/gnome-desktop-%{version}.tar.xz
%if !0%{?flatpak}
Requires: bubblewrap
%endif
Requires: gdk-pixbuf2%{?_isa} >= %{gdk_pixbuf2_version}
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gsettings-desktop-schemas >= %{gsettings_desktop_schemas_version}
Conflicts: gnome-shell < 3.33.4
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xkbregistry)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  python3
BuildRequires:  python3dist(langtable)
# /oreon:deps
%description
gnome-desktop3 contains the libgnome-desktop library as well as a data
file that exports the "GNOME" version to the Settings Details panel.

The libgnome-desktop library provides API shared by several applications
on the desktop, but that cannot live in the platform for various
reasons. There is no API or ABI guarantee, although we are doing our
best to provide stability. Documentation for the API is available with
gtk-doc.

%package devel
Summary: Libraries and headers for %{name}
License: LGPL-2.0-or-later
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n gnome-desktop4
Summary: Library with common API for various GNOME modules
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND MIT
Provides: bundled(qrcodegen)
Requires: %{name}%{?_isa} = %{version}-%{release}
%description -n gnome-desktop4
gnome-desktop4 contains the libgnome-desktop library.

The libgnome-desktop library provides API shared by several applications
on the desktop, but that cannot live in the platform for various
reasons. There is no API or ABI guarantee, although we are doing our
best to provide stability.

%package -n gnome-desktop4-devel
Summary: Libraries and headers for gnome-desktop4
License: LGPL-2.0-or-later
Requires: gnome-desktop4%{?_isa} = %{version}-%{release}
%description -n gnome-desktop4-devel
The gnome-desktop4-devel package contains libraries and header files for
developing applications that use gnome-desktop4.

%package  tests
Summary:  Tests for the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n gnome-desktop-%{tarball_version}

%build

%meson -Dgtk_doc=true -Dinstalled_tests=true
%meson_build
%install
%meson_install
%find_lang %{po_package} --all-name --with-gnome
%oreon_autofiles gnome-desktop4 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles gnome-desktop4-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gnome-desktop3-devel -f %{oreon_filedir}/gnome-desktop3-devel.list
%files -n gnome-desktop4 -f %{oreon_filedir}/gnome-desktop4.list
%files -n gnome-desktop4-devel -f %{oreon_filedir}/gnome-desktop4-devel.list
%files -n gnome-desktop3-tests -f %{oreon_filedir}/gnome-desktop3-tests.list

%changelog

%autochangelog
