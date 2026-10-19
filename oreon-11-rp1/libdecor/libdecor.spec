%global source0_hash 7fd50f780a4fee90a03f7b2c09055033e488654cbaff4a0c4bbae616bac9cd1c
Name:           libdecor
Version:        0.2.5
Release:        1%{?dist}
Summary:        Wayland client side decoration library
License:        MIT
URL:            https://gitlab.freedesktop.org/libdecor/libdecor
Source0:        https://gitlab.freedesktop.org/libdecor/libdecor/-/releases/0.2.5/downloads/libdecor-0.2.5.tar.xz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gtk3
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)
# /oreon:deps
%description
Libdecor provides a small helper library for providing client side decoration
to Wayland clients.

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

%meson -Ddemo=false
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libdecor-devel -f %{oreon_filedir}/libdecor-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.2.5-2
- Prepare for Oreon 11 (RP1)
