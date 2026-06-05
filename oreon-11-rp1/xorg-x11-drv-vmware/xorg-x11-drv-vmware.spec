%global source0_hash aed31ee5ed5ecc6e2226705383e7ad06f7602c1376a295305f376b17af3eb81a

%global tarball xf86-video-vmware
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir	%{moduledir}/drivers

%undefine _hardened_build

Summary:    Xorg X11 vmware video driver
Name:       xorg-x11-drv-vmware
Version:    13.4.0
Release:    12%{?dist}
URL:        http://www.x.org
License:    MIT AND X11

Source0:        xf86-video-vmware-13.4.0.tar.xz
Source30:        xserver-sdk-abi-requires

ExclusiveArch: %{ix86} x86_64 ia64

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  mesa-compat-libxatracker-devel
BuildRequires:  pkgconfig(libdrm) >= 2.4.96
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pciaccess) >= 0.8.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xorg-server) >= 1.12

Requires: Xorg %(sh %{SOURCE30} ansic)
Requires: Xorg %(sh %{SOURCE30} videodrv)
Requires: mesa-compat-libxatracker

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

%files
%{driverdir}/vmware_drv.so
%{_mandir}/man4/vmware.4*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 13.4.0-12
- Import
