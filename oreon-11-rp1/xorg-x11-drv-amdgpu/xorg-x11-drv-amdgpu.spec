%global source0_hash 7653cead024a6820ed1139958503278d78b4b3f80befcacf54ce87a5199b0ce2

%global tarball xf86-video-amdgpu
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/drivers

# Xorg cannot load hardened build
%undefine _hardened_build

Name:       xorg-x11-drv-amdgpu
Version:    25.0.0
Release:    2%{?dist}

Summary:    AMD GPU video driver
License:    MIT

URL:        https://www.x.org/wiki
Source:     https://www.x.org/archive/individual/driver/%{tarball}-%{version}.tar.xz
Source:     https://www.x.org/archive/individual/driver/%{tarball}-%{version}.tar.xz.sig
Source:     0xF1111E4AAF984C9763795FFE4B25B5180522B8D9.gpg

ExcludeArch: s390 s390x

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  kernel-headers
BuildRequires:  meson >= 0.59.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libdrm) >= 2.4.121
BuildRequires:  pkgconfig(libdrm_amdgpu) >= 2.4.121
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xorg-server) >= 1.18
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(xf86driproto)
BuildRequires:  pkgconfig(randrproto)
BuildRequires:  pkgconfig(renderproto)
BuildRequires:  pkgconfig(videoproto)
BuildRequires:  pkgconfig(xextproto) >= 7.0.99.1
BuildRequires:  xorg-x11-util-macros

Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)
Requires: libdrm >= 2.4.121

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

%files
%{driverdir}/amdgpu_drv.so
%{_datadir}/X11/xorg.conf.d/10-amdgpu.conf
%{_mandir}/man4/amdgpu.4*

%changelog
%autochangelog
