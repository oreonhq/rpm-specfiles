Name:           gupnp-igd
Version:        1.6.0
Release:        9%{?dist}
Summary:        Library to handle UPnP IGD port mapping

License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/GUPnP
Source0:        https://download.gnome.org/sources/%{name}/1.6/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 4099978339ab22126d4968f2a332b6d094fc44c78797860781f1fc2f11771b74
%global source0_file gupnp-igd-1.6.0.tar.xz
# oreon url source checksums end

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gupnp-1.6)
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson

Requires:       gssdp%{?_isa}
Requires:       gupnp%{?_isa}

%description
%{name} is a library to handle UPnP IGD port mapping.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/gupnp-igd-1.6.0.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4099978339ab22126d4968f2a332b6d094fc44c78797860781f1fc2f11771b74" || { echo "oreon: Source0 SHA256 mismatch for gupnp-igd-1.6.0.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1


%build
%meson -Dgtk_doc=true
%meson_build


%install
%meson_install


%files
%license COPYING
%doc NEWS README
%{_libdir}/libgupnp-igd-1.6.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GUPnPIgd-1.6.typelib


%files devel
%{_includedir}/*
%{_libdir}/libgupnp-igd-1.6.so
%{_libdir}/pkgconfig/%{name}-1.6*.pc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/%{name}/
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GUPnPIgd-1.6.gir


%changelog
* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.0-9
- Require gssdp and gupnp for libnice chain

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.0-8
- Prepare for Oreon 11 (RP1)
