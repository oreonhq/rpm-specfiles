%global source0_hash 2020ed4c38376855ab99ea102d0ed3c8246e25c4992e5f7c40c4e057de642975

Name:           glibd
Version:        2.4.3
Release:        7%{?dist}
Summary:        D bindings for the GLib C Utility Library

License:        LGPL-3.0-or-later
URL:            https://github.com/gtkd-developers/GlibD
Source0:        %{url}/archive/v%{version}/GlibD-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  ldc
# Cf. rhbz#1813529
BuildRequires:  meson > 0.53.2-1

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  gir-to-d >= 0.23.2

ExclusiveArch:  %{ldc_arches}

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
# Drop '-specs=/usr/lib/rpm/redhat/redhat-hardened-ld' as LDC doesn't support it
export LDFLAGS="-Wl,-z,relro"
# Export DFLAGS
export DFLAGS="%{_d_optflags}"
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%{_libdir}/*.so.*

%files devel
%doc AUTHORS README.md
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_d_includedir}/glibd-2/

%changelog
%autochangelog
