# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 499322e27a55c8183166bf2dd1e47d085eb834143e0d7036baba8427b90c156b
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%define tarball xf86-video-nouveau
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir %{moduledir}/drivers

%undefine _hardened_build

Summary:   Xorg X11 nouveau video driver for NVIDIA graphics chipsets
Name:      xorg-x11-drv-nouveau
# need to set an epoch to get version number in sync with upstream
Epoch:     1
Version:   1.0.17
Release:   14%{?dist}
URL:       http://www.x.org
License:   MIT

Source0: http://xorg.freedesktop.org/archive/individual/driver/xf86-video-nouveau-%{version}.tar.bz2

Patch1: remove-sarea.h.patch
# fixup driver for new X server ABI
Patch2: e80e73ced69b15662103d0fd6837db4ce6c6eb5b.patch
Patch3: 0001-Fixes-warning-nv_driver.c-1443-9-warning-implicit.patch

ExcludeArch: s390 s390x

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  mesa-libGL-devel
BuildRequires:  pkgconfig(xorg-server) >= 1.8
BuildRequires:  pkgconfig(libdrm) >= 2.4.60
BuildRequires:  pkgconfig(libdrm_nouveau) >= 2.4.25
BuildRequires:  pkgconfig(pciaccess) >= 0.10
BuildRequires:  pkgconfig(libudev)

Requires:   Xorg %(xserver-sdk-abi-requires ansic)
Requires:   Xorg %(xserver-sdk-abi-requires videodrv)
Requires:   libdrm >= 2.4.33-0.1

%description 
X.Org X11 nouveau video driver.

%prep
%oreon_verify_sources
%autosetup -p1 -n xf86-video-nouveau-%{version}

%build
autoreconf -v --install --force
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete

%files
%{driverdir}/nouveau_drv.so
%{_mandir}/man4/nouveau.4*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:1.0.17-14
- Import
