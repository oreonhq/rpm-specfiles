%global source0_hash 9285ebab273ebe788d39a7c1bf19717cc6312cfcaa0bc55d65cf5a8d4f42a545
Summary:        Tethered shooting & control of digital cameras
Name: entangle
Version: 3.0
Release:        1%{?dist}
License: GPL-3.0-or-later
Source0:        https://entangle-photo.org/download/sources/%{name}-%{version}.tar.xz
Patch: 0001-meson-fix-build-for-meson-0.60.0.patch
Patch: 0001-Adapt-to-changing-gexiv2-APIs.patch
Patch: 0001-build-Use-either-libgirepository-2.0-or-libgireposit.patch
Patch: 0001-meson-use-compile-check-for-girepository.patch
Patch: 0001-meson-fix-GExiv2-GIR-name.patch
URL: https://entangle-photo.org/
Requires: adwaita-icon-theme
Requires: libpeas1-loader-python3%{?_isa}
# oreon:deps
BuildRequires:  LibRaw-devel
BuildRequires:  adwaita-icon-theme
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  lcms2-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libgexiv2-devel
BuildRequires:  libgphoto2-devel
BuildRequires:  libgudev1-devel
BuildRequires:  libpeas1-devel
BuildRequires:  meson
# /oreon:deps
%description
Entangle is an application which uses GTK and libgphoto2 to provide a
graphical interface for tethered photography with digital cameras.

It includes control over camera shooting and configuration settings
and 'hands off' shooting directly from the controlling computer.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Denable-gtk-doc=true || ( cat %{_vpath_builddir}/meson-logs/meson-log.txt; exit 1 )
%meson_build
%install
%meson_install
%find_lang %{name}
rm -f %{buildroot}%{_libdir}/libentangle_backend.so
rm -f %{buildroot}%{_libdir}/libentangle_frontend.so
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
