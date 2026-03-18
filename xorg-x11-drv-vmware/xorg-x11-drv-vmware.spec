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

Source0:    https://ftp.x.org/archive/individual/driver/%{tarball}-%{version}.tar.xz

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

Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)
Requires: mesa-compat-libxatracker

%description
X.Org X11 vmware video driver.

%prep
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 13.4.0-12
- Prepare for Oreon 11 (RP1)
