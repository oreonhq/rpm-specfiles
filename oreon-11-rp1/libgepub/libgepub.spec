%global source0_hash 5a56695aa8a9132d67c0792a40f252ce0a48d9d032b4e1a8a6ce98af14fd5e1b
%global apiver 0.7
Name:           libgepub
Version:        0.7.3
Release:        1%{?dist}
Summary:        Library for epub documents
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://git.gnome.org/browse/libgepub
Source0:        https://download.gnome.org/sources/libgepub/0.7/libgepub-%{version}.tar.xz
# oreon:deps
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
# /oreon:deps
%description
libgepub is a GObject based library for handling and rendering epub
documents.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libgepub-devel -f %{oreon_filedir}/libgepub-devel.list

%changelog

%autochangelog
