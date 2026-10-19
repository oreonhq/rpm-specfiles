%global source0_hash 19262df1df00de75bdc419d31d544953a3589e6369e5dff1a4ebcee465c6d046
Name:           egl-wayland2
Version:        1.0.2
Release:        1%{?dist}
Summary:        Dma-buf-based Wayland external platform library
License:        Apache-2.0 and GPL-2.0
URL:            https://github.com/NVIDIA/%{name}
Source0:        https://github.com/NVIDIA/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:       libglvnd-egl%{?_isa}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(eglexternalplatform)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl-backend)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
# /oreon:deps
%description
This is a new implementation of the EGL External Platform Library for Wayland
(EGL_KHR_platform_wayland), using the NVIDIA driver's new platform surface
interface, which simplifies a lot of the library and improves window resizing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
find %{buildroot} -name '*.la' -delete
rm -f %{buildroot}%{_libdir}/libnvidia-egl-wayland2.so
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
