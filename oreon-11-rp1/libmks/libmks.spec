%global source0_hash 1093b9053dd8d98c3d8e03d03ae56bb6f11df67bb2cab5432eae594e41fba0ff
%global glib2_version 2.76.0
%global gtk4_version  4.12.0
%global api_version 1
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:		libmks
Version:	0.1.5
Release:        1%{?dist}
Summary:        Mouse, Keyboard, and Screen to QEMU
License:	LGPL-2.1-or-later
URL:		https://gitlab.gnome.org/GNOME/libmks
Source0:        https://download.gnome.org/sources/%{name}/0.1/%{name}-%{version}.tar.xz
Requires:		glib2%{?_isa} >= %{glib2_version}
Requires:		gtk4%{?_isa} >= %{gtk4_version}
Recommends:		qemu-ui-dbus
Recommends:		qemu-ui-opengl
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  vala
# /oreon:deps
%description
This library provides a "Mouse, Keyboard, and Screen" to QEMU using the
D-Bus device support in QEMU and GTK 4.

%package devel
Summary:		Development files for %{name}
Requires:		%{name}%{?_isa} = %{version}-%{release}
Recommends:		%{name}-doc = %{version}-%{release}
%description devel
This package contains the libraries and header files that are needed
for writing applications using %{name}.

%package doc
Summary:		Documentation files for %{name}
BuildArch:		noarch
Recommends:		%{name}-devel = %{version}-%{release}
Recommends:		gi-docgen-fonts
%description doc
Documentation files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson -Dinstall-tools=true -Ddocs=true -Dintrospection=enabled
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libmks-devel -f %{oreon_filedir}/libmks-devel.list
%files -n libmks-doc -f %{oreon_filedir}/libmks-doc.list

%changelog

%autochangelog
