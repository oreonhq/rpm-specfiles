%global source0_hash 00b781eea055582820a123c47b62411bdf6aabf4f03dc0568faec55faf9667c9

%global commit ce811e78882d9f31636351dfe65351f4ded52c74
%global date 20240506
%global shortcommit %(c=%{commit}; echo ${c:0:7})
#global tag %{version}

%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

%undefine _hardened_build

Summary:   Xorg X11 Intel video driver
Name:      xorg-x11-drv-intel
Version:   2.99.917%{!?tag:^%{date}git%{shortcommit}}
Release:   65%{?dist}
URL:       http://www.x.org
License:   MIT

%if 0%{?tag:1}
Source0:    https://xorg.freedesktop.org/archive/individual/driver/xf86-video-intel-%{version}.tar.bz2
%else
Source0:    https://gitlab.freedesktop.org/xorg/driver/xf86-video-intel/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%endif

Patch0:	    intel-gcc-pr65873.patch
# https://bugs.freedesktop.org/show_bug.cgi?id=96255#c11
Patch1:     0001-sna-Avoid-clobbering-output-physical-size-with-xf86O.patch
# https://gitlab.freedesktop.org/xorg/driver/xf86-video-intel/-/issues/180
Patch2:     xvmc-workaround.patch

ExclusiveArch: %{ix86} x86_64

BuildRequires:  cairo-devel
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  libXfont2-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXv-devel
BuildRequires:  make
BuildRequires:  mesa-libGL-devel >= 6.5-9
BuildRequires:  meson
BuildRequires:  pkgconfig(libdrm) >= 2.4.20
BuildRequires:  pkgconfig(libdrm_intel) >= 2.4.52
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pciaccess) >= 0.10
BuildRequires:  pkgconfig(pixman-1) >= 0.27.1
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
BuildRequires:  pkgconfig(xorg-server) >= 1.6
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xshmfence)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xvmc)
BuildRequires:  pkgconfig(xxf86vm)

Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)
Requires: polkit

%description
X.Org X11 Intel video driver.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%if 0%{?tag:1}
%autosetup -p1 -n xf86-video-intel-%{version}
%else
%autosetup -p1 -n xf86-video-intel-%{commit}
%endif

%build
# This package causes LTO to thrash sucking up enormous amounts of VM.  This
# is almost certainly a GCC bug that will need to be analyzed/fixed.  Until
# then, disable LTO.
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

# libXvMC opens the versioned file name, these are useless
rm -f %{buildroot}%{_libdir}/libI*XvMC.so

%files
%doc COPYING
%{driverdir}/intel_drv.so
%{_libdir}/libIntelXvMC.so.1*
%{_libexecdir}/xf86-video-intel-backlight-helper
%{_datadir}/polkit-1/actions/org.x.xf86-video-intel.backlight-helper.policy
%{_mandir}/man4/i*
%{_bindir}/intel-virtual-output

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.99.917^20240506gitce811e7-65
- Import
