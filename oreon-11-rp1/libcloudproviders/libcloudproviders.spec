%global source0_hash 3e123fa2a34f6dfd99897ebe5fec3dfa35d9cf4b192c28fe7fc90c5aafafcf5b

%global api_version 0.4

Name:           libcloudproviders
Summary:        Library for integration of cloud storage providers
Version:        0.4.1
Release:        1%{?dist}
License:        LGPL-3.0-or-later

URL:            https://gitlab.gnome.org/World/libcloudproviders
Source0:        https://ftp.gnome.org/pub/GNOME/sources/libcloudproviders/%{api_version}/libcloudproviders-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  gi-docgen
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

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
%autosetup -p1


%build
%meson -Denable-gtk-doc=true -Dwrap_mode=nofallback
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc CHANGELOG README.md
%{_libdir}/libcloudproviders.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/CloudProviders-%{api_version}.typelib

%files devel
%{_includedir}/cloudproviders/
%{_libdir}/pkgconfig/cloudproviders.pc
%{_libdir}/libcloudproviders.so
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/CloudProviders-%{api_version}.gir
%{_datadir}/gtk-doc/
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/cloudproviders.*


%changelog
%autochangelog
