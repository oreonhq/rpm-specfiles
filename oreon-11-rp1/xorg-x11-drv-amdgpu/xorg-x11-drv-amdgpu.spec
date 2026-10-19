%global source0_hash 7653cead024a6820ed1139958503278d78b4b3f80befcacf54ce87a5199b0ce2
%global tarball xf86-video-amdgpu
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/drivers
%undefine _hardened_build
Name:       xorg-x11-drv-amdgpu
Version:    25.0.0
Release:        2%{?dist}
Summary:        AMD GPU video driver
License:    MIT
URL:        https://www.x.org/wiki
Source0:        https://www.x.org/archive/individual/driver/%{tarball}-%{version}.tar.xz
ExcludeArch: s390 s390x
Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)
Requires: libdrm >= 2.4.121
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  kernel-headers
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libdrm_amdgpu)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xf86driproto)
BuildRequires:  pkgconfig(xorg-server)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  xorg-x11-util-macros
# /oreon:deps
%description
X.Org X11 AMDGPU driver

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%autosetup -p1 -n %{tarball}-%{version}

%build

%meson \
    -D glamor=enabled \
    -D udev=enabled \
%meson_build
%install
%meson_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
