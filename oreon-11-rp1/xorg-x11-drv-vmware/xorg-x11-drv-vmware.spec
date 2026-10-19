%global source0_hash aed31ee5ed5ecc6e2226705383e7ad06f7602c1376a295305f376b17af3eb81a
%global tarball xf86-video-vmware
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir	%{moduledir}/drivers
%undefine _hardened_build
Summary:        Xorg X11 vmware video driver
Name:       xorg-x11-drv-vmware
Version:    13.4.0
Release:        1%{?dist}
URL:        http://www.x.org
License:    MIT AND X11
Source0:        https://xorg.freedesktop.org/releases/individual/driver/xf86-video-vmware-13.4.0.tar.xz#/xorg-x11-drv-vmware-13.4.0.tar.gz
Source30:        xserver-sdk-abi-requires
ExclusiveArch: %{ix86} x86_64 ia64
Requires: Xorg %(sh %{SOURCE30} ansic)
Requires: Xorg %(sh %{SOURCE30} videodrv)
Requires: mesa-compat-libxatracker
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mesa-compat-libxatracker-devel
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xorg-server)
# /oreon:deps
%description
X.Org X11 vmware video driver.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{tarball}-%{version}

%build

autoreconf -vif
%configure --disable-static
%make_build
%install
%make_install
find %{buildroot} -name "*.la" -delete
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 13.4.0-12
- Import
