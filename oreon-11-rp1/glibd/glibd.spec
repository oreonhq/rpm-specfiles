%global source0_hash 2020ed4c38376855ab99ea102d0ed3c8246e25c4992e5f7c40c4e057de642975
Name:           glibd
Version:        2.4.3
Release:        7%{?dist}
Summary:        D bindings for the GLib C Utility Library
License:        LGPL-3.0-or-later
URL:            https://github.com/gtkd-developers/GlibD
Source0:        https://github.com/gtkd-developers/GlibD/archive/v%{version}/GlibD-%{version}.tar.gz
ExclusiveArch:  %{ldc_arches}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gir-to-d
BuildRequires:  ldc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
# /oreon:deps
%description
%{summary}.

%package devel
Summary:        Development files for using %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides the development files for building
applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n GlibD-%{version} -p1

# Fix version in meson.build
sed -e "s/    version: '.*'/    version: '%{version}'/" -i meson.build

%build

export LDFLAGS="-Wl,-z,relro"
export DFLAGS="%{_d_optflags}"
%meson
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n glibd-devel -f %{oreon_filedir}/glibd-devel.list

%changelog

%autochangelog
