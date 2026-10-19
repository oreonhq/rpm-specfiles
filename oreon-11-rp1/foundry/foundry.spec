%global source0_hash 46db0d64436c313611cafdfb4ca0d5cec2b97be7d7a5f1be7ee8d0150d4f25c8
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:           foundry
Version:        1.2.0
Release:        1%{?dist}
Summary:        IDE library and command-line companion tool
License:        LGPL-2.1-or-later AND Apache-2.0
URL:            https://gitlab.gnome.org/GNOME/foundry
Source0:        https://download.gnome.org/sources/%{name}/1.1/%{name}-%{version}.tar.xz
ExcludeArch:    %{ix86}
Requires:       libfoundry%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(jsonrpc-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libcmark)
BuildRequires:  pkgconfig(libdex-1)
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(libpanel-1)
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libspelling-1)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  pkgconfig(template-glib-1.0)
BuildRequires:  pkgconfig(vte-2.91-gtk4)
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildRequires:  pkgconfig(yaml-0.1)
# /oreon:deps
%description

%package      -n libfoundry
Summary:        IDE library and command-line companion tool (shared library)
%description  -n libfoundry
This package contains the shared library.

%package     -n libfoundry-gtk
Summary:        IDE library and command-line companion tool (GTK integration)
Requires:       libfoundry%{?_isa} = %{version}-%{release}
%description -n libfoundry-gtk
This package contains the shared library for GTK integration.

%package     -n libfoundry-devel
Summary:        IDE library and command-line companion tool (development files)
Requires:       libfoundry%{?_isa} = %{version}-%{release}
%description -n libfoundry-devel
This package contains the development headers for libfoundry.

%package     -n libfoundry-gtk-devel
Summary:        IDE library and command-line companion tool (development files)
Requires:       libfoundry-gtk%{?_isa} = %{version}-%{release}
%description -n libfoundry-gtk-devel
This package contains the development headers for libfoundry-gtk.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n foundry-%{tarball_version} -p1

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles libfoundry usr/*/lib*.so.*
%oreon_autofiles libfoundry-gtk usr/*/lib*.so.*
%oreon_autofiles libfoundry-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libfoundry-gtk-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
appstream-util validate-relax --nonet \
    $RPM_BUILD_ROOT/%{_datadir}/metainfo/org.gnome.Foundry.metainfo.xml
%find_lang %{name} --all-name --with-gnome
%files -f %{oreon_filedir}/main.list
%files -n libfoundry -f %{oreon_filedir}/libfoundry.list
%files -n libfoundry-gtk -f %{oreon_filedir}/libfoundry-gtk.list
%files -n libfoundry-devel -f %{oreon_filedir}/libfoundry-devel.list
%files -n libfoundry-gtk-devel -f %{oreon_filedir}/libfoundry-gtk-devel.list

%changelog

%autochangelog
