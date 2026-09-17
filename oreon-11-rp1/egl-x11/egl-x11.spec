%global source0_hash 92e22178b3aba63be4cb2bf8953991bdf52ad3e5ec26212143b2df46d16e82d7

Name:           egl-x11
Version:        1.0.5
Release:        %autorelease
Summary:        NVIDIA XLib and XCB EGL Platform Library
License:        Apache-2.0
URL:            https://github.com/NVIDIA/egl-x11

Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Allow building with an older meson:
Patch0:         egl-x11-meson-0.58.patch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(eglexternalplatform) >= 1.2
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm) >= 21.2.0
BuildRequires:  pkgconfig(libdrm) >= 2.4.99
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
# Minimum version 1.17.0 for explicit sync support (Fedora 40+):
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-present)

# Required for directory ownership
Requires:       libglvnd-egl%{?_isa}

%description
This is an EGL platform library for the NVIDIA driver to support XWayland via
xlib (using EGL_KHR_platform_x11) or xcb (using EGL_EXT_platform_xcb).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson \
  -D xcb=true \
  -D xlib=enabled
%meson_build

%install
%meson_install

rm -fv %{buildroot}%{_libdir}/*.so

%files
%license LICENSE
%doc README.md
%{_libdir}/libnvidia-egl-xcb.so.1
%{_libdir}/libnvidia-egl-xcb.so.%{version}
%{_libdir}/libnvidia-egl-xlib.so.1
%{_libdir}/libnvidia-egl-xlib.so.%{version}
%{_datadir}/egl/egl_external_platform.d/20_nvidia_xcb.json
%{_datadir}/egl/egl_external_platform.d/20_nvidia_xlib.json

%changelog
%autochangelog
