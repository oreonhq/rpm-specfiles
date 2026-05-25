%global tarball xf86-video-ati
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir	%{moduledir}/drivers

%undefine _hardened_build

Summary:   Xorg X11 ati video driver
Name:      xorg-x11-drv-ati
Version:   22.0.0
Release:   6%{?dist}
URL:       http://www.x.org
License:   MIT

Source0:   https://www.x.org/pub/individual/driver/%{tarball}-%{version}.tar.xz

ExcludeArch: s390 s390x

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(pciaccess) >= 0.8.0
BuildRequires:  pkgconfig(gbm) >= 10.6
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libdrm) >= 2.4.89
BuildRequires:  pkgconfig(libdrm_radeon)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xorg-server) >= 1.16

Requires: libdrm >= 2.4.89
Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)

%description 
X.Org X11 ati video driver.

%prep
%setup -q -n %{tarball}-%{version}

%build
autoreconf -iv
%configure --disable-static --enable-glamor
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete

%files
%{driverdir}/ati_drv.so
%{driverdir}/radeon_drv.so
%{_mandir}/man4/ati.4*
%{_mandir}/man4/radeon.4*
%{_datadir}/X11/xorg.conf.d/10-radeon.conf

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 22.0.0-6
- Import
