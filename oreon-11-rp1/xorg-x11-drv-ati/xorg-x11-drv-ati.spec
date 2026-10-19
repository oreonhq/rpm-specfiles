%global source0_hash c8c8bb56d3f6227c97e59c3a3c85a25133584ceb82ab5bc05a902a743ab7bf6d
%global tarball xf86-video-ati
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir	%{moduledir}/drivers
%undefine _hardened_build
Summary:        Xorg X11 ati video driver
Name:      xorg-x11-drv-ati
Version:   22.0.0
Release:        1%{?dist}
URL:       http://www.x.org
License:   MIT
Source0:        https://www.x.org/pub/individual/driver/%{tarball}-%{version}.tar.xz
Source30:   xserver-sdk-abi-requires
ExcludeArch: s390 s390x
Requires: libdrm >= 2.4.89
Requires: Xorg %(sh %{SOURCE30} ansic)
Requires: Xorg %(sh %{SOURCE30} videodrv)
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libdrm_radeon)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(xorg-server)
# /oreon:deps
%description 
X.Org X11 ati video driver.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{tarball}-%{version}

%build

autoreconf -iv
%configure --disable-static --enable-glamor
%make_build
%install
%make_install
find %{buildroot} -name "*.la" -delete
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 22.0.0-6
- Import
