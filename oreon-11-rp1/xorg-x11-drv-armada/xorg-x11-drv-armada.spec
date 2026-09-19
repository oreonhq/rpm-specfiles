%global source0_hash ec434b0a3b48e85ba0132bc46092605fa07b1ed89ebebacf83270f53ecd9cdcd

%global _configure_disable_silent_rules 1

# Hardening passws '-z now' to the linker, defeating lazy binding via PLT.
# Xorg's module loading, however, relies on loading modules with unresolved
# symbols that in turn dlopen their own dependencies (such as fb or
# etnadrm_gpu modules). Sigh.
%undefine _hardened_build

Name:           xorg-x11-drv-armada
# This is the version from the configure script.
Version:        0.0.0
# Built from unstable-devel branch that has the etnadrm backend
Release:        17.unstable.20180829git78e7116a5%{?dist}
Summary:        X.org graphics driver for KMS based systems with pluggable GPU backend

License:        MIT
URL:            http://git.arm.linux.org.uk/cgit/xf86-video-armada.git/

# git clone http://git.arm.linux.org.uk/cgit/xf86-video-armada.git/
# cd xf86-video-armada
# git archive --prefix=xf86-video-armada-0.0.0/ 78e7116a5 |
#    gzip -9 >xf86-video-armada-0.0.0.tar.gz
Source0:        xf86-video-armada-%{version}.tar.gz

# These were all sent to the upstream maintainer on 2019-03-26.
Patch0:         0001-all-add-the-missing-files-into-the-dist.patch
Patch1:         0002-build-default-to-enable-etnaviv-auto.patch
Patch2:         0003-build-fix-enable-etnadrm-handling.patch
Patch3:         0004-build-align-a-couple-of-configure-options-with-their.patch
Patch4:         0005-build-fix-present.h-detection.patch

BuildRequires:  gcc make
BuildRequires:  autoconf automake libtool

BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(xorg-server) >= 1.9.99.1
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(libdrm) >= 2.4.47
BuildRequires:  pkgconfig(libdrm_armada) => 2.0.0
BuildRequires:  pkgconfig(dri2proto) >= 2.6
BuildRequires:  pkgconfig(dri3proto) >= 1.0
BuildRequires:  pkgconfig(presentproto) >= 1.0
BuildRequires:  etnaviv-headers

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

%files
%exclude %{_libdir}/xorg/modules/drivers/armada_drv.la
%exclude %{_libdir}/xorg/modules/drivers/etnadrm_gpu.la
%{_libdir}/xorg/modules/drivers/armada_drv.so
%{_libdir}/xorg/modules/drivers/etnadrm_gpu.so
%{_mandir}/man4/armada.4*
%license COPYING
%doc README FAQ
%doc conf/xorg-sample.conf

%changelog
%autochangelog
