%global source0_hash ec434b0a3b48e85ba0132bc46092605fa07b1ed89ebebacf83270f53ecd9cdcd
%global _configure_disable_silent_rules 1
%undefine _hardened_build
Name:           xorg-x11-drv-armada
Version:        0.0.0
Release:        1%{?dist}
Summary:        X.org graphics driver for KMS based systems with pluggable GPU backend
License:        MIT
URL:            http://git.arm.linux.org.uk/cgit/xf86-video-armada.git/
Source0:        xf86-video-armada-%{version}.tar.gz
Patch0:         0001-all-add-the-missing-files-into-the-dist.patch
Patch1:         0002-build-default-to-enable-etnaviv-auto.patch
Patch2:         0003-build-fix-enable-etnadrm-handling.patch
Patch3:         0004-build-align-a-couple-of-configure-options-with-their.patch
Patch4:         0005-build-fix-present.h-detection.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  etnaviv-headers
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(dri2proto)
BuildRequires:  pkgconfig(dri3proto)
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libdrm_armada)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(presentproto)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(xorg-server)
BuildRequires:  pkgconfig(xproto)
# /oreon:deps
%description
The xf86-video-armada module is a 2D graphics driver for the X Window
System as implemented by X.org, supporting Freescale i.MX or Marvell Armada
display controllers with a Vivante Galcore GPU.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n xf86-video-armada-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%build

autoreconf -fi
%configure \
        --disable-vivante \
        --disable-etnaviv \
        --enable-etnadrm \
        --enable-dri2 \
        --enable-dri3 \
        --enable-present
make %{?_smp_mflags}
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
