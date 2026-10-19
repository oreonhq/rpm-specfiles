%global source0_hash 3e123fa2a34f6dfd99897ebe5fec3dfa35d9cf4b192c28fe7fc90c5aafafcf5b
%global api_version 0.4
Name:           libcloudproviders
Summary:        Library for integration of cloud storage providers
Version:        0.4.1
Release:        1%{?dist}
License:        LGPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/libcloudproviders
Source0:        https://ftp.gnome.org/pub/GNOME/sources/%{name}/%{api_version}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gi-docgen
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  vala
# /oreon:deps
%description
Cross desktop library for desktop integration of cloud storage providers
and sync tools.

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

%meson -Denable-gtk-doc=true -Dwrap_mode=nofallback
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libcloudproviders-devel -f %{oreon_filedir}/libcloudproviders-devel.list

%changelog

%autochangelog
