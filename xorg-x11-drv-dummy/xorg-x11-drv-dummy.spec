%global tarball xf86-video-dummy
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/drivers

%undefine _hardened_build

Summary:   Xorg X11 dummy video driver
Name:      xorg-x11-drv-dummy
Version:   0.4.1
Release:   8%{?dist}
URL:       http://www.x.org
License:   MIT AND X11

Source0:   https://xorg.freedesktop.org/archive/individual/driver/%{tarball}-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(xorg-server) >= 1.4.99.901

Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)

%description 
X.Org X11 dummy video driver.

%prep
%setup -q -n %{tarball}-%{version}

%build
autoreconf -vif
%configure --disable-static
%make_build

%install
%make_install

find %{buildroot} -name "*.la" -delete

%files
%doc README.md
%{driverdir}/dummy_drv.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.4.1-8
- Prepare for Oreon 11 (RP1)
