%global source0_hash 4099978339ab22126d4968f2a332b6d094fc44c78797860781f1fc2f11771b74
Name:           gupnp-igd
Version:        1.6.0
Release:        1%{?dist}
Summary:        Library to handle UPnP IGD port mapping
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/GUPnP
Source0:        https://download.gnome.org/sources/%{name}/1.6/%{name}-%{version}.tar.xz
Requires:       gssdp%{?_isa}
Requires:       gupnp%{?_isa}
# oreon:deps
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gupnp-1.6)
# /oreon:deps
%description
%{name} is a library to handle UPnP IGD port mapping.

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

%meson -Dgtk_doc=true
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gupnp-igd-devel -f %{oreon_filedir}/gupnp-igd-devel.list

%changelog

* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.0-9
- Require gssdp and gupnp for libnice chain

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.0-8
- Prepare for Oreon 11 (RP1)
