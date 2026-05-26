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
# oreon url source checksums begin
%global source0_sha256 c8c8bb56d3f6227c97e59c3a3c85a25133584ceb82ab5bc05a902a743ab7bf6d
%global source0_file xf86-video-ati-22.0.0.tar.xz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/xf86-video-ati-22.0.0.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c8c8bb56d3f6227c97e59c3a3c85a25133584ceb82ab5bc05a902a743ab7bf6d" || { echo "oreon: Source0 SHA256 mismatch for xf86-video-ati-22.0.0.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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
