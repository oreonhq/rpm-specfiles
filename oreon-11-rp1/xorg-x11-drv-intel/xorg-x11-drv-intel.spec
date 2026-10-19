%global source0_hash 28725d1bb1aa2cc594be2ea9cd886cdd3bb349283c1ca3b317c99451cce2c207
%global commit ce811e78882d9f31636351dfe65351f4ded52c74
%global date 20240506
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers
%undefine _hardened_build
Summary:        Xorg X11 Intel video driver
Name:      xorg-x11-drv-intel
Version:   2.99.917%{!?tag:^%{date}git%{shortcommit}}
Release:        65%{?dist}
URL:       http://www.x.org
License:   MIT
Source0:        https://gitlab.freedesktop.org/xorg/driver/xf86-video-intel/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source30:        xserver-sdk-abi-requires
Patch0:        intel-gcc-pr65873.patch
Patch1:        0001-sna-Avoid-clobbering-output-physical-size-with-xf86O.patch
Patch2:        xvmc-workaround.patch
ExclusiveArch: %{ix86} x86_64
Requires: Xorg %(sh %{SOURCE30} ansic)
Requires: Xorg %(sh %{SOURCE30} videodrv)
Requires: polkit
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  libXfont2-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXv-devel
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libdrm_intel)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xorg-server)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xshmfence)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xvmc)
BuildRequires:  pkgconfig(xxf86vm)
# /oreon:deps
%description
X.Org X11 Intel video driver.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%if 0%{?tag:1}
%autosetup -p1 -n xf86-video-intel-%{version}
%else
%autosetup -p1 -n xf86-video-intel-%{commit}
%endif

%build

%define _lto_cflags %{nil}
%meson \
    -D async-swap=false \
    -D backlight-helper=true \
    -D backlight=true \
    -D default-accel=sna \
    -D default-dri=3 \
    -D dri1=false \
    -D dri2=true \
    -D dri3=true \
    -D internal-debug=no \
    -D kms=true \
    -D present=true \
    -D sna=true \
    -D tearfree=false \
    -D tools=true \
    -D ums=false \
    -D use-create2=false \
    -D uxa=true \
    -D valgrind=false \
    -D xaa=true \
    -D xvmc=true
%meson_build
%install
%meson_install
find %{buildroot} -name "*.la" -delete
rm -f %{buildroot}%{_libdir}/libI*XvMC.so
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.99.917^20240506gitce811e7-65
- Import
