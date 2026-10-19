%global source0_hash 370870b0dea12dde0ddac0b77594ff94215cf2694ac0a5ded98f5d2f9864f6e0
Name:           egl-x11
Version:        1.0.6
Release:        1%{?dist}
Summary:        NVIDIA XLib and XCB EGL Platform Library
License:        Apache-2.0
URL:            https://github.com/NVIDIA/egl-x11
Source0:        https://github.com/NVIDIA/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         egl-x11-meson-0.58.patch
Requires:       libglvnd-egl%{?_isa}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(eglexternalplatform)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-present)
# /oreon:deps
%description
This is an EGL platform library for the NVIDIA driver to support XWayland via
xlib (using EGL_KHR_platform_x11) or xcb (using EGL_EXT_platform_xcb).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
  -D xcb=true \
  -D xlib=enabled
%meson_build
%install
%meson_install
rm -fv %{buildroot}%{_libdir}/*.so
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
