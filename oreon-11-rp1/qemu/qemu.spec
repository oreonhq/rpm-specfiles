%global source0_hash none
%bcond_without check
%global libfdt_version 1.6.0
%global libseccomp_version 2.4.0
%global libusbx_version 1.0.23
%global meson_version 0.61.3
%global usbredir_version 0.7.1
%global ipxe_version 20200823-5.git4bd064de
%global have_vmsr_helper 0
%global have_memlock_limits 0
%global need_qemu_kvm 0
%ifarch x86_64
%global kvm_package   system-x86
%global need_qemu_kvm 1
%global have_vmsr_helper 1
%endif
%ifarch %{power64}
%global have_memlock_limits 1
%global kvm_package   system-ppc
%endif
%ifarch s390x
%global kvm_package   system-s390x
%endif
%ifarch aarch64
%global kvm_package   system-aarch64
%endif
%ifarch %{mips}
%global kvm_package   system-mips
%endif
%ifarch riscv64
%global kvm_package   system-riscv
%endif
%ifarch loongarch64
%global kvm_package   system-loongarch64
%endif
%global modprobe_kvm_conf %{_sourcedir}/kvm.conf
%ifarch s390x
    %global modprobe_kvm_conf %{_sourcedir}/kvm-s390x.conf
%endif
%ifarch x86_64
    %global modprobe_kvm_conf %{_sourcedir}/kvm-x86.conf
%endif
%global tools_only 0
%global user_dynamic 1
%global user_static 1
%global have_kvm 0
%if 0%{?kvm_package:1}
%global have_kvm 1
%define obsoletes_package_kvm %{nil}
%else
%define obsoletes_package_kvm Obsoletes: %{name}-kvm < %{evr}
%endif
%global have_numactl 1
%global have_spice 1
%ifnarch x86_64 aarch64 loongarch64
%global have_spice 0
%endif
%global have_xen 0
%global have_liburing 0
%global have_virgl 0
%global have_jack 1
%global have_dbus_display 1
%global have_libblkio 0
%global have_gvnc_devel %{defined fedora}
%global have_sdl_image %{defined fedora}
%global have_brlapi 1
%global have_daxctl 1
%global have_fdt 1
%global have_multipath 1
%global have_opengl 1
%global have_usbredir 1
%global have_xdp 1
%global enable_werror 0
%global have_block_rbd 1
%global have_block_iscsi 1
%global have_block_gluster 1
%global have_block_nfs 0
%global have_librdma 1
%global have_libcacard 1
%global have_rutabaga_gfx 0
%global have_qatzip 0
%ifarch x86_64
%global have_qatzip 1
%endif
%global have_libcbor 1
%global have_igvm 0
%global have_nitro 0
%ifarch x86_64 aarch64
%global have_nitro 1
%endif
%if %{defined flatpak}
%global user_dynamic 0
%global user_static 0
%global have_numactl 0
%global have_xen 0
%global have_liburing 0
%global have_libblkio 0
%global have_brlapi 0
%global have_daxctl 0
%global have_multipath 0
%global have_xdp 0
%global have_block_gluster 0
%global have_block_iscsi 0
%global have_block_rbd 0
%global have_block_nfs 0
%global have_librdma 0
%global have_libcacard 0
%global have_qatzip 0
%global have_libcbor 0
%global have_igvm 0
%endif
%global _lto_cflags %{nil}
%global firmwaredirs "%{_datadir}/qemu-firmware:%{_datadir}/ipxe/qemu:%{_datadir}/seavgabios:%{_datadir}/seabios"
%global qemudocdir %{_docdir}/%{name}
%define evr %{epoch}:%{version}-%{release}
%define requires_block_blkio %{nil}
%define requires_block_curl Requires: %{name}-block-curl = %{evr}
%define requires_block_dmg Requires: %{name}-block-dmg = %{evr}
%define requires_block_gluster %{nil}
%define obsoletes_block_gluster Obsoletes: %{name}-block-gluster < %{evr}
%define requires_block_nfs %{nil}
%define obsoletes_block_nfs Obsoletes: %{name}-block-nfs < %{evr}
%define requires_block_rbd %{nil}
%define obsoletes_block_rbd Obsoletes: %{name}-block-rbd < %{evr}
%define requires_block_iscsi %{nil}
%define obsoletes_block_iscsi Obsoletes: %{name}-block-iscsi < %{evr}
%define requires_block_ssh Requires: %{name}-block-ssh = %{evr}
%define requires_audio_alsa Requires: %{name}-audio-alsa = %{evr}
%define requires_audio_oss Requires: %{name}-audio-oss = %{evr}
%define requires_audio_pa Requires: %{name}-audio-pa = %{evr}
%define requires_audio_pipewire Requires: %{name}-audio-pipewire = %{evr}
%define requires_audio_sdl Requires: %{name}-audio-sdl = %{evr}
%define requires_char_baum %{nil}
%define obsoletes_char_baum Obsoletes: %{name}-char-baum < %{evr}
%define requires_device_uefi_vars Requires: %{name}-device-uefi-vars = %{evr}
%define requires_device_usb_host Requires: %{name}-device-usb-host = %{evr}
%define requires_device_usb_redirect Requires: %{name}-device-usb-redirect = %{evr}
%define requires_ui_curses Requires: %{name}-ui-curses = %{evr}
%define requires_ui_gtk Requires: %{name}-ui-gtk = %{evr}
%define requires_ui_sdl Requires: %{name}-ui-sdl = %{evr}
%define requires_ui_egl_headless Requires: %{name}-ui-egl-headless = %{evr}
%define requires_ui_opengl Requires: %{name}-ui-opengl = %{evr}
%define requires_device_display_virtio_gpu Requires: %{name}-device-display-virtio-gpu = %{evr}
%define requires_device_display_virtio_gpu_pci Requires: %{name}-device-display-virtio-gpu-pci = %{evr}
%define requires_device_display_virtio_gpu_ccw Requires: %{name}-device-display-virtio-gpu-ccw = %{evr}
%define requires_device_display_virtio_vga Requires: %{name}-device-display-virtio-vga = %{evr}
%define requires_package_qemu_pr_helper Requires: qemu-pr-helper
%define requires_package_passt Requires: passt
%define requires_package_virtiofsd Requires: virtiofsd
%define obsoletes_package_virtiofsd %{nil}
%define requires_device_display_vhost_user_gpu Requires: %{name}-device-display-vhost-user-gpu = %{evr}
%define requires_device_display_virtio_gpu_gl Requires: %{name}-device-display-virtio-gpu-gl = %{evr}
%define requires_device_display_virtio_gpu_pci_gl Requires: %{name}-device-display-virtio-gpu-pci-gl = %{evr}
%define requires_device_display_virtio_vga_gl Requires: %{name}-device-display-virtio-vga-gl = %{evr}
%define requires_device_display_virtio_gpu_rutabaga Requires: %{name}-device-display-virtio-gpu-rutabaga = %{evr}
%define requires_device_display_virtio_gpu_pci_rutabaga Requires: %{name}-device-display-virtio-gpu-pci-rutabaga = %{evr}
%define requires_device_display_virtio_vga_rutabaga Requires: %{name}-device-display-virtio-vga-rutabaga = %{evr}
%define requires_audio_jack %{nil}
%define requires_audio_dbus %{nil}
%define requires_ui_dbus %{nil}
%define requires_ui_spice_app %{nil}
%define requires_ui_spice_core %{nil}
%define requires_device_display_qxl %{nil}
%define requires_audio_spice %{nil}
%define requires_char_spice %{nil}
%define requires_device_usb_smartcard %{nil}
%global requires_all_modules \
%{requires_block_blkio} \
%{requires_block_curl} \
%{requires_block_dmg} \
%{requires_block_gluster} \
%{requires_block_iscsi} \
%{requires_block_nfs} \
%{requires_block_rbd} \
%{requires_block_ssh} \
%{requires_audio_alsa} \
%{requires_audio_dbus} \
%{requires_audio_oss} \
%{requires_audio_pa} \
%{requires_audio_pipewire} \
%{requires_audio_sdl} \
%{requires_audio_jack} \
%{requires_audio_spice} \
%{requires_ui_curses} \
%{requires_ui_gtk} \
%{requires_ui_sdl} \
%{requires_ui_egl_headless} \
%{requires_ui_opengl} \
%{requires_ui_spice_app} \
%{requires_ui_spice_core} \
%{requires_char_baum} \
%{requires_char_spice} \
%{requires_device_display_qxl} \
%{requires_device_display_vhost_user_gpu} \
%{requires_device_display_virtio_gpu} \
%{requires_device_display_virtio_gpu_ccw} \
%{requires_device_display_virtio_gpu_gl} \
%{requires_device_display_virtio_gpu_rutabaga} \
%{requires_device_display_virtio_gpu_pci} \
%{requires_device_display_virtio_gpu_pci_gl} \
%{requires_device_display_virtio_gpu_pci_rutabaga} \
%{requires_device_display_virtio_vga} \
%{requires_device_display_virtio_vga_gl} \
%{requires_device_display_virtio_vga_rutabaga} \
%{requires_device_uefi_vars} \
%{requires_device_usb_host} \
%{requires_device_usb_redirect} \
%{requires_device_usb_smartcard} \
%{requires_package_passt} \
%{requires_package_qemu_pr_helper} \
%{requires_package_virtiofsd} \
%global obsoletes_some_modules \
%{obsoletes_block_gluster} \
%{obsoletes_block_rbd} \
%{obsoletes_block_iscsi} \
%{obsoletes_char_baum} \
%{obsoletes_package_virtiofsd} \
%{obsoletes_package_kvm} \
Obsoletes: %{name}-system-cris <= %{evr} \
Obsoletes: %{name}-system-cris-core <= %{evr} \
Obsoletes: %{name}-system-lm32 <= %{evr} \
Obsoletes: %{name}-system-lm32-core <= %{evr} \
Obsoletes: %{name}-system-moxie <= %{evr} \
Obsoletes: %{name}-system-moxie-core <= %{evr} \
Obsoletes: %{name}-system-nios2 <= %{evr} \
Obsoletes: %{name}-system-nios2-core <= %{evr} \
Obsoletes: %{name}-system-unicore32 <= %{evr} \
Obsoletes: %{name}-system-unicore32-core <= %{evr} \
Obsoletes: sgabios-bin <= 1:0.20180715git-10.fc38
Summary:        QEMU is a FAST! processor emulator
Name: qemu
Version: 11.0.0
%if 0%{?rcver:1}
%global rcstr -%{rcver}
Release:        1%{?dist}
%else
Release:        1%{?dist}
%endif
Epoch: 2
License: %{shrink:
    Apache-2.0 AND
    BSD-2-Clause AND
    BSD-3-Clause AND
    FSFAP AND
    GPL-1.0-or-later AND
    GPL-2.0-only AND
    GPL-2.0-or-later AND
    GPL-2.0-or-later WITH GCC-exception-2.0 AND
    LGPL-2.0-only AND
    LGPL-2.0-or-later AND
    LGPL-2.1-only AND
    LGPL-2.1-or-later AND
    MIT AND
    LicenseRef-Fedora-Public-Domain AND
    CC-BY-3.0
}
URL: http://www.qemu.org/
ExcludeArch: %{ix86} %{arm}
%global dlurl https://download.qemu.org
Source0:        %{dlurl}/%{name}-%{version}.tar.xz
Source1: %{dlurl}/%{name}-%{version}%{?rcstr}.tar.xz.sig
Source2: gpgkey-CEACC9E15534EBABB82D3FA03353C9CEF108B584.gpg
Source10: qemu-guest-agent.service
Source11: 99-qemu-guest-agent.rules
Source12: bridge.conf
Source17: qemu-ga.sysconfig
Source21: 95-kvm-memlock.conf
Source26: vhost.conf
Source27: kvm.conf
Source30: kvm-s390x.conf
Source31: kvm-x86.conf
Source36: README.tests
Source37: qemu.sysusers
Patch: 0001-Disable-9p-local-tests-that-fail-on-copr-aarch64.patch
Patch: 0002-TEMPORARY-increase-test-timeout.patch
%ifarch %{valgrind_arches}
%endif
%if "%{toolchain}" == "clang"
%else
%endif
%if %{have_sdl_image}
%endif
%if %{have_gvnc_devel}
%endif
Requires: %{name}-system-arm = %{evr}
Requires: %{name}-system-avr = %{evr}
Requires: %{name}-system-m68k = %{evr}
Requires: %{name}-system-microblaze = %{evr}
Requires: %{name}-system-mips = %{evr}
Requires: %{name}-system-or1k = %{evr}
Requires: %{name}-system-ppc = %{evr}
Requires: %{name}-system-riscv = %{evr}
Requires: %{name}-system-rx = %{evr}
Requires: %{name}-system-sh4 = %{evr}
Requires: %{name}-system-sparc = %{evr}
Requires: %{name}-system-tricore = %{evr}
Requires: %{name}-system-x86 = %{evr}
Requires: %{name}-system-xtensa = %{evr}
Requires: %{name}-img = %{evr}
Requires: %{name}-tools = %{evr}
Requires: %{name}-system-aarch64 = %{evr}
Requires: %{name}-system-alpha = %{evr}
Requires: %{name}-system-loongarch64 = %{evr}
Requires: %{name}-system-s390x = %{evr}
# oreon:deps
BuildRequires:  /usr/bin/dtrace
BuildRequires:  SDL2-devel
BuildRequires:  SDL2_image-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  bison
BuildRequires:  bzip2-devel
BuildRequires:  capstone-devel
BuildRequires:  cyrus-sasl-devel
BuildRequires:  flex
BuildRequires:  fuse-devel
BuildRequires:  fuse3-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  gnupg2
BuildRequires:  gnutls-devel
BuildRequires:  gtk3-devel
BuildRequires:  hostname
BuildRequires:  keyutils-libs-devel
BuildRequires:  libaio-devel
BuildRequires:  libattr-devel
BuildRequires:  libbpf-devel
BuildRequires:  libcap-ng-devel
BuildRequires:  libcurl-devel
BuildRequires:  libfdt-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libselinux-devel
BuildRequires:  libslirp-devel
BuildRequires:  libssh-devel
BuildRequires:  libtasn1-devel
BuildRequires:  libudev-devel
BuildRequires:  libusbx-devel
BuildRequires:  libzstd-devel
BuildRequires:  lzo-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  ncurses-devel
BuildRequires:  pam-devel
BuildRequires:  perl-Test-Harness
BuildRequires:  pipewire-devel
BuildRequires:  pixman-devel
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gvnc-1.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-wheel
BuildRequires:  rutabaga-gfx-ffi-devel
BuildRequires:  snappy-devel
BuildRequires:  systemtap
BuildRequires:  systemtap-sdt-devel
BuildRequires:  usbredir-devel
BuildRequires:  virglrenderer-devel
BuildRequires:  vte291-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
%{name} is an open source virtualizer that provides hardware
emulation for the KVM hypervisor. %{name} acts as a virtual
machine monitor together with the KVM kernel modules, and emulates the
hardware for a full system such as a PC and its associated peripherals.

%package common
Summary: QEMU common files needed by all QEMU targets
Requires(post): /usr/bin/getent
Requires(post): /usr/sbin/groupadd
Requires(post): /usr/sbin/useradd
%{obsoletes_some_modules}
Requires: ipxe-roms-qemu >= %{ipxe_version}
%description common
%{name} is an open source virtualizer that provides hardware emulation for
the KVM hypervisor.

This package provides documentation and auxiliary programs used with %{name}.

%package docs
Summary: %{name} documentation
BuildArch: noarch
%description docs
%{name}-docs provides documentation files regarding %{name}.

%package -n qemu-img
Summary: QEMU command line tool for manipulating disk images
%description -n qemu-img
This package provides a command line tool for manipulating disk images.

%package -n qemu-guest-agent
Summary: QEMU guest agent
%description -n qemu-guest-agent
%{name} is an open source virtualizer that provides hardware emulation for
the KVM hypervisor.

This package provides an agent to run inside guests, which communicates
with the host over a virtio-serial channel named "org.qemu.guest_agent.0"

This package does not need to be installed on the host OS.

%package tools
Summary: %{name} support tools
Recommends: systemtap-client
Recommends: systemtap-devel
%description tools
%{name}-tools provides various tools related to %{name} usage.

%package -n qemu-pr-helper
Summary: qemu-pr-helper utility for %{name}
%description -n qemu-pr-helper
This package provides the qemu-pr-helper utility that is required for certain
SCSI features.

%package tests
Summary: tests for the %{name} package
Requires: %{name} = %{evr}
%define testsdir %{_libdir}/%{name}/tests-src
%description tests
The %{name}-tests rpm contains tests that can be used to verify
the functionality of the installed %{name} package

Install this package if you want access to qemu-iotests.

%package  block-curl
Summary: QEMU CURL block driver
Requires: %{name}-common%{?_isa} = %{evr}
%description block-curl
This package provides the additional CURL block driver for QEMU.

Install this package if you want to access remote disks over
http, https, ftp and other transports provided by the CURL library.

%package  block-ssh
Summary: QEMU SSH block driver
Requires: %{name}-common%{?_isa} = %{evr}
%description block-ssh
This package provides the additional SSH block driver for QEMU.

Install this package if you want to access remote disks using
the Secure Shell (SSH) protocol.

%package  ui-opengl
Summary: QEMU opengl support
Requires: %{name}-common%{?_isa} = %{evr}
Requires: libGL
Requires: libEGL
%description ui-opengl
This package provides opengl support.

# Fedora specific
%package  block-dmg
Summary: QEMU block driver for DMG disk images
Requires: %{name}-common%{?_isa} = %{evr}
%description block-dmg
This package provides the additional DMG block driver for QEMU.

Install this package if you want to open '.dmg' files.

%package  audio-alsa
Summary: QEMU ALSA audio driver
Requires: %{name}-common%{?_isa} = %{evr}
%description audio-alsa
This package provides the additional ALSA audio driver for QEMU.

%package  audio-oss
Summary: QEMU OSS audio driver
Requires: %{name}-common%{?_isa} = %{evr}
%description audio-oss
This package provides the additional OSS audio driver for QEMU.

%package  audio-pa
Summary: QEMU PulseAudio audio driver
Requires: %{name}-common%{?_isa} = %{evr}
%description audio-pa
This package provides the additional PulseAudio audio driver for QEMU.

%package  audio-pipewire
Summary: QEMU Pipewire audio driver
Requires: %{name}-common%{?_isa} = %{evr}
%description audio-pipewire
This package provides the additional Pipewire audio driver for QEMU.

%package  audio-sdl
Summary: QEMU SDL audio driver
Requires: %{name}-common%{?_isa} = %{evr}
%description audio-sdl
This package provides the additional SDL audio driver for QEMU.

%package  ui-curses
Summary: QEMU curses UI driver
Requires: %{name}-common%{?_isa} = %{evr}
%description ui-curses
This package provides the additional curses UI for QEMU.

%package  ui-gtk
Summary: QEMU GTK UI driver
Requires: %{name}-common%{?_isa} = %{evr}
Requires: %{name}-ui-opengl%{?_isa} = %{evr}
%description ui-gtk
This package provides the additional GTK UI for QEMU.

%package  ui-sdl
Summary: QEMU SDL UI driver
Requires: %{name}-common%{?_isa} = %{evr}
Requires: %{name}-ui-opengl%{?_isa} = %{evr}
%description ui-sdl
This package provides the additional SDL UI for QEMU.

%package  ui-egl-headless
Summary: QEMU EGL headless driver
Requires: %{name}-common%{?_isa} = %{evr}
Requires: %{name}-ui-opengl%{?_isa} = %{evr}
%description ui-egl-headless
This package provides the additional egl-headless UI for QEMU.

%package device-display-virtio-gpu
Summary: QEMU virtio-gpu display device
Requires: %{name}-common%{?_isa} = %{evr}
%description device-display-virtio-gpu
This package provides the virtio-gpu display device for QEMU.

%package device-display-virtio-gpu-gl
Summary: QEMU virtio-gpu-gl display device
Requires: %{name}-common%{?_isa} = %{evr}
Requires: %{name}-device-display-virtio-gpu%{?_isa} = %{evr}
%description device-display-virtio-gpu-gl
This package provides the virtio-gpu-gl display device for QEMU.

%package device-display-virtio-gpu-rutabaga
Summary: QEMU virtio-gpu-rutabaga display device
Requires: %{name}-common%{?_isa} = %{evr}
Requires: %{name}-device-display-virtio-gpu%{?_isa} = %{evr}
%description device-display-virtio-gpu-rutabaga
This package provides the virtio-gpu-rutabaga display device for QEMU.

%package device-display-virtio-gpu-pci
Summary: QEMU virtio-gpu-pci display device
Requires: %{name}-common%{?_isa} = %{evr}
Requires: %{name}-device-display-virtio-gpu%{?_isa} = %{evr}
%description device-display-virtio-gpu-pci
This package provides the virtio-gpu-pci display device for QEMU.

%package device-display-virtio-gpu-pci-gl
Summary: QEMU virtio-gpu-pci-gl display device
Requires: %{name}-common%{?_isa} = %{evr}
Requires: %{name}-device-display-virtio-gpu-pci%{?_isa} = %{evr}
Requires: %{name}-device-display-virtio-gpu-gl%{?_isa} = %{evr}
%description device-display-virtio-gpu-pci-gl
This package provides the virtio-gpu-pci-gl display device for QEMU.

%package device-display-virtio-gpu-pci-rutabaga
Summary: QEMU virtio-gpu-pci-rutabaga display device
Requires: %{name}-common%{?_isa} = %{evr}
Requires: %{name}-device-display-virtio-gpu-pci%{?_isa} = %{evr}
%description device-display-virtio-gpu-pci-rutabaga
This package provides the virtio-gpu-pci-rutabaga display device for QEMU.

%package device-display-virtio-gpu-ccw
Summary: QEMU virtio-gpu-ccw display device
Requires: %{name}-common%{?_isa} = %{evr}
Requires: %{name}-device-display-virtio-gpu%{?_isa} = %{evr}
%description device-display-virtio-gpu-ccw
This package provides the virtio-gpu-ccw display device for QEMU.

%package device-display-virtio-vga
Summary: QEMU virtio-vga display device
Requires: %{name}-common%{?_isa} = %{evr}
Requires: %{name}-device-display-virtio-gpu%{?_isa} = %{evr}
%description device-display-virtio-vga
This package provides the virtio-vga display device for QEMU.

%package device-display-virtio-vga-gl
Summary: QEMU virtio-vga-gl display device
Requires: %{name}-common%{?_isa} = %{evr}
Requires: %{name}-device-display-virtio-vga%{?_isa} = %{evr}
%description device-display-virtio-vga-gl
This package provides the virtio-vga-gl display device for QEMU.

%package device-display-virtio-vga-rutabaga
Summary: QEMU virtio-vga-rutabaga display device
Requires: %{name}-common%{?_isa} = %{evr}
Requires: %{name}-device-display-virtio-vga%{?_isa} = %{evr}
%description device-display-virtio-vga-rutabaga
This package provides the virtio-vga-rutabaga display device for QEMU.

%package device-uefi-vars
Summary: QEMU UEFI variable service
Requires: %{name}-common%{?_isa} = %{evr}
%description device-uefi-vars
This package provides the UEFI variable service for QEMU.

%package device-usb-host
Summary: QEMU usb host device
Requires: %{name}-common%{?_isa} = %{evr}
%description device-usb-host
This package provides the USB pass through driver for QEMU.

%package device-usb-redirect
Summary: QEMU usbredir device
Requires: %{name}-common%{?_isa} = %{evr}
%description device-usb-redirect
This package provides the usbredir device for QEMU.

%package device-display-vhost-user-gpu
Summary: QEMU QXL display device
Requires: %{name}-common%{?_isa} = %{evr}
%description device-display-vhost-user-gpu
This package provides the vhost-user-gpu display device for QEMU.

%package kvm
Summary: QEMU metapackage for KVM support
Requires: qemu-%{kvm_package} = %{evr}
%description kvm
This is a meta-package that provides a qemu-system-<arch> package for native
architectures where kvm can be enabled. For example, in an x86 system, this
will install qemu-system-x86

%package kvm-core
Summary: QEMU metapackage for KVM support
Requires: qemu-%{kvm_package}-core = %{evr}
%description kvm-core
This is a meta-package that provides a qemu-system-<arch>-core package
for native architectures where kvm can be enabled. For example, in an
x86 system, this will install qemu-system-x86-core

%package system-aarch64
Summary: QEMU system emulator for AArch64
Requires: %{name}-system-aarch64-core = %{evr}
%{requires_all_modules}
%description system-aarch64
This package provides the QEMU system emulator for AArch64.

%package system-aarch64-core
Summary: QEMU system emulator for AArch64
Requires: %{name}-common = %{evr}
Requires: edk2-aarch64
%description system-aarch64-core
This package provides the QEMU system emulator for AArch64.

%package system-alpha
Summary: QEMU system emulator for Alpha
Requires: %{name}-system-alpha-core = %{evr}
%{requires_all_modules}
%description system-alpha
This package provides the QEMU system emulator for Alpha systems.

%package system-alpha-core
Summary: QEMU system emulator for Alpha
Requires: %{name}-common = %{evr}
%description system-alpha-core
This package provides the QEMU system emulator for Alpha systems.

%package system-arm
Summary: QEMU system emulator for ARM
Requires: %{name}-system-arm-core = %{evr}
%{requires_all_modules}
%description system-arm
This package provides the QEMU system emulator for ARM systems.

%package system-arm-core
Summary: QEMU system emulator for ARM
Requires: %{name}-common = %{evr}
Obsoletes: edk2-arm <= 20241117-2.fc42
%description system-arm-core
This package provides the QEMU system emulator for ARM boards.

%package system-avr
Summary: QEMU system emulator for AVR
Requires: %{name}-system-avr-core = %{evr}
%{requires_all_modules}
%description system-avr
This package provides the QEMU system emulator for AVR systems.

%package system-avr-core
Summary: QEMU system emulator for AVR
Requires: %{name}-common = %{evr}
%description system-avr-core
This package provides the QEMU system emulator for AVR systems.

%package system-hppa
Summary: QEMU system emulator for HPPA
Requires: %{name}-system-hppa-core = %{evr}
%{requires_all_modules}
%description system-hppa
This package provides the QEMU system emulator for HPPA.

%package system-hppa-core
Summary: QEMU system emulator for hppa
Requires: %{name}-common = %{evr}
%description system-hppa-core
This package provides the QEMU system emulator for HPPA.

%package system-loongarch64
Summary: QEMU system emulator for LoongArch (LA64)
Requires: %{name}-system-loongarch64-core = %{evr}
%{requires_all_modules}
%description system-loongarch64
This package provides the QEMU system emulator for Loongson boards.

%package system-loongarch64-core
Summary: QEMU system emulator for LoongArch (LA64)
Requires: %{name}-common = %{evr}
Requires: edk2-loongarch64
%description system-loongarch64-core
This package provides the QEMU system emulator for Loongson boards.

%package system-m68k
Summary: QEMU system emulator for ColdFire (m68k)
Requires: %{name}-system-m68k-core = %{evr}
%{requires_all_modules}
%description system-m68k
This package provides the QEMU system emulator for ColdFire boards.

%package system-m68k-core
Summary: QEMU system emulator for ColdFire (m68k)
Requires: %{name}-common = %{evr}
%description system-m68k-core
This package provides the QEMU system emulator for ColdFire boards.

%package system-microblaze
Summary: QEMU system emulator for Microblaze
Requires: %{name}-system-microblaze-core = %{evr}
%{requires_all_modules}
%description system-microblaze
This package provides the QEMU system emulator for Microblaze boards.

%package system-microblaze-core
Summary: QEMU system emulator for Microblaze
Requires: %{name}-common = %{evr}
%description system-microblaze-core
This package provides the QEMU system emulator for Microblaze boards.

%package system-mips
Summary: QEMU system emulator for MIPS
Requires: %{name}-system-mips-core = %{evr}
%{requires_all_modules}
%description system-mips
This package provides the QEMU system emulator for MIPS systems.

%package system-mips-core
Summary: QEMU system emulator for MIPS
Requires: %{name}-common = %{evr}
%description system-mips-core
This package provides the QEMU system emulator for MIPS systems.

%package system-or1k
Summary: QEMU system emulator for OpenRisc32
Requires: %{name}-system-or1k-core = %{evr}
%{requires_all_modules}
%description system-or1k
This package provides the QEMU system emulator for OpenRisc32 boards.

%package system-or1k-core
Summary: QEMU system emulator for OpenRisc32
Requires: %{name}-common = %{evr}
%description system-or1k-core
This package provides the QEMU system emulator for OpenRisc32 boards.

%package system-ppc
Summary: QEMU system emulator for PPC
Requires: %{name}-system-ppc-core = %{evr}
%{requires_all_modules}
%description system-ppc
This package provides the QEMU system emulator for PPC and PPC64 systems.

%package system-ppc-core
Summary: QEMU system emulator for PPC
Requires: %{name}-common = %{evr}
Requires: openbios
Requires: SLOF
Requires: seavgabios-bin
%description system-ppc-core
This package provides the QEMU system emulator for PPC and PPC64 systems.

%package system-riscv
Summary: QEMU system emulator for RISC-V
Requires: %{name}-system-riscv-core = %{evr}
%{requires_all_modules}
%description system-riscv
This package provides the QEMU system emulator for RISC-V systems.

%package system-riscv-core
Summary: QEMU system emulator for RISC-V
Requires: %{name}-common = %{evr}
Requires: edk2-riscv64
%description system-riscv-core
This package provides the QEMU system emulator for RISC-V systems.

%package system-rx
Summary: QEMU system emulator for RX
Requires: %{name}-system-rx-core = %{evr}
%{requires_all_modules}
%description system-rx
This package provides the QEMU system emulator for RX systems.

%package system-rx-core
Summary: QEMU system emulator for RX
Requires: %{name}-common = %{evr}
%description system-rx-core
This package provides the QEMU system emulator for RX systems.

%package system-s390x
Summary: QEMU system emulator for S390
Requires: %{name}-system-s390x-core = %{evr}
%{requires_all_modules}
%description system-s390x
This package provides the QEMU system emulator for S390 systems.

%package system-s390x-core
Summary: QEMU system emulator for S390
Requires: %{name}-common = %{evr}
%description system-s390x-core
This package provides the QEMU system emulator for S390 systems.

%package system-sh4
Summary: QEMU system emulator for SH4
Requires: %{name}-system-sh4-core = %{evr}
%{requires_all_modules}
%description system-sh4
This package provides the QEMU system emulator for SH4 boards.

%package system-sh4-core
Summary: QEMU system emulator for SH4
Requires: %{name}-common = %{evr}
%description system-sh4-core
This package provides the QEMU system emulator for SH4 boards.

%package system-sparc
Summary: QEMU system emulator for SPARC
Requires: %{name}-system-sparc-core = %{evr}
%{requires_all_modules}
%description system-sparc
This package provides the QEMU system emulator for SPARC and SPARC64 systems.

%package system-sparc-core
Summary: QEMU system emulator for SPARC
Requires: %{name}-common = %{evr}
Requires: openbios
%description system-sparc-core
This package provides the QEMU system emulator for SPARC and SPARC64 systems.

%package system-tricore
Summary: QEMU system emulator for tricore
Requires: %{name}-system-tricore-core = %{evr}
%{requires_all_modules}
%description system-tricore
This package provides the QEMU system emulator for Tricore.

%package system-tricore-core
Summary: QEMU system emulator for tricore
Requires: %{name}-common = %{evr}
%description system-tricore-core
This package provides the QEMU system emulator for Tricore.

%package system-x86
Summary: QEMU system emulator for x86
Requires: %{name}-system-x86-core = %{evr}
%{requires_all_modules}
%description system-x86
This package provides the QEMU system emulator for x86. When being run in a x86
machine that supports it, this package also provides the KVM virtualization
platform.

%package system-x86-core
Summary: QEMU system emulator for x86
Requires: %{name}-common = %{evr}
Requires: seabios-bin
Requires: seavgabios-bin
Requires: edk2-ovmf
%description system-x86-core
This package provides the QEMU system emulator for x86. When being run in a x86
machine that supports it, this package also provides the KVM virtualization
platform.

%package system-xtensa
Summary: QEMU system emulator for Xtensa
Requires: %{name}-system-xtensa-core = %{evr}
%{requires_all_modules}
%description system-xtensa
This package provides the QEMU system emulator for Xtensa boards.

%package system-xtensa-core
Summary: QEMU system emulator for Xtensa
Requires: %{name}-common = %{evr}
%description system-xtensa-core
This package provides the QEMU system emulator for Xtensa boards.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gpgv2 --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}

%autosetup -n qemu-%{version}%{?rcstr} -S git_am

%global qemu_kvm_build qemu_kvm_build
mkdir -p %{qemu_kvm_build}
%global static_builddir static_builddir
mkdir -p %{static_builddir}

%build

%define disable_everything         \\\
  --audio-drv-list=                \\\
  --disable-af-xdp                 \\\
  --disable-alsa                   \\\
  --disable-asan                   \\\
  --disable-attr                   \\\
  --disable-auth-pam               \\\
  --disable-blkio                  \\\
  --disable-block-drv-whitelist-in-tools \\\
  --disable-bochs                  \\\
  --disable-bpf                    \\\
  --disable-brlapi                 \\\
  --disable-bsd-user               \\\
  --disable-bzip2                  \\\
  --disable-cap-ng                 \\\
  --disable-capstone               \\\
  --disable-cfi                    \\\
  --disable-cfi-debug              \\\
  --disable-cloop                  \\\
  --disable-cocoa                  \\\
  --disable-colo-proxy             \\\
  --disable-coreaudio              \\\
  --disable-coroutine-pool         \\\
  --disable-crypto-afalg           \\\
  --disable-curl                   \\\
  --disable-curses                 \\\
  --disable-dbus-display           \\\
  --disable-debug-graph-lock       \\\
  --disable-debug-info             \\\
  --disable-debug-mutex            \\\
  --disable-debug-remap            \\\
  --disable-debug-tcg              \\\
  --disable-dmg                    \\\
  --disable-docs                   \\\
  --disable-download               \\\
  --disable-dsound                 \\\
  --disable-fdt                    \\\
  --disable-fuse                   \\\
  --disable-fuse-lseek             \\\
  --disable-gcrypt                 \\\
  --disable-gettext                \\\
  --disable-gio                    \\\
  --disable-glusterfs              \\\
  --disable-gnutls                 \\\
  --disable-gtk                    \\\
  --disable-gtk-clipboard          \\\
  --disable-guest-agent            \\\
  --disable-guest-agent-msi        \\\
  --disable-hv-balloon             \\\
  --disable-hvf                    \\\
  --disable-iconv                  \\\
  --disable-igvm                   \\\
  --disable-jack                   \\\
  --disable-kvm                    \\\
  --disable-l2tpv3                 \\\
  --disable-libcbor                \\\
  --disable-libdaxctl              \\\
  --disable-libdw                  \\\
  --disable-libkeyutils            \\\
  --disable-libiscsi               \\\
  --disable-libnfs                 \\\
  --disable-libpmem                \\\
  --disable-libssh                 \\\
  --disable-libudev                \\\
  --disable-libusb                 \\\
  --disable-linux-aio              \\\
  --disable-linux-io-uring         \\\
  --disable-linux-user             \\\
  --disable-lto                    \\\
  --disable-lzfse                  \\\
  --disable-lzo                    \\\
  --disable-malloc-trim            \\\
  --disable-membarrier             \\\
  --disable-modules                \\\
  --disable-module-upgrades        \\\
  --disable-mpath                  \\\
  --disable-mshv                   \\\
  --disable-multiprocess           \\\
  --disable-nitro                  \\\
  --disable-netmap                 \\\
  --disable-nettle                 \\\
  --disable-numa                   \\\
  --disable-nvmm                   \\\
  --disable-opengl                 \\\
  --disable-oss                    \\\
  --disable-pa                     \\\
  --disable-parallels              \\\
  --disable-passt                  \\\
  --disable-pie                    \\\
  --disable-pipewire               \\\
  --disable-pixman                 \\\
  --disable-plugins                \\\
  --disable-pvg                    \\\
  --disable-qcow1                  \\\
  --disable-qed                    \\\
  --disable-qom-cast-debug         \\\
  --disable-qpl                    \\\
  --disable-rbd                    \\\
  --disable-rdma                   \\\
  --disable-relocatable            \\\
  --disable-replication            \\\
  --disable-rust                   \\\
  --disable-rutabaga-gfx           \\\
  --disable-rng-none               \\\
  --disable-safe-stack             \\\
  --disable-sdl                    \\\
  --disable-sdl-image              \\\
  --disable-seccomp                \\\
  --disable-selinux                \\\
  --disable-slirp                  \\\
  --disable-slirp-smbd             \\\
  --disable-smartcard              \\\
  --disable-snappy                 \\\
  --disable-sndio                  \\\
  --disable-sparse                 \\\
  --disable-spice                  \\\
  --disable-spice-protocol         \\\
  --disable-strict-rust-lints      \\\
  --disable-strip                  \\\
  --disable-system                 \\\
  --disable-tcg                    \\\
  --disable-tools                  \\\
  --disable-tpm                    \\\
  --disable-tsan                   \\\
  --disable-uadk                   \\\
  --disable-u2f                    \\\
  --disable-ubsan                  \\\
  --disable-usb-redir              \\\
  --disable-user                   \\\
  --disable-valgrind               \\\
  --disable-vpc                    \\\
  --disable-vde                    \\\
  --disable-vdi                    \\\
  --disable-vfio-user-server       \\\
  --disable-vhdx                   \\\
  --disable-vhost-crypto           \\\
  --disable-vhost-kernel           \\\
  --disable-vhost-net              \\\
  --disable-vhost-user             \\\
  --disable-vhost-user-blk-server  \\\
  --disable-vhost-vdpa             \\\
  --disable-virglrenderer          \\\
  --disable-virtfs                 \\\
  --disable-vnc                    \\\
  --disable-vnc-jpeg               \\\
  --disable-png                    \\\
  --disable-vnc-sasl               \\\
  --disable-vte                    \\\
  --disable-vvfat                  \\\
  --disable-werror                 \\\
  --disable-whpx                   \\\
  --disable-xen                    \\\
  --disable-xen-pci-passthrough    \\\
  --disable-xkbcommon              \\\
  --disable-zstd                   \\\
  --without-default-devices
run_configure() {
    ../configure  \
        --cc=%{__cc} \
        --cxx=/bin/false \
        --prefix="%{_prefix}" \
        --libdir="%{_libdir}" \
        --datadir="%{_datadir}" \
        --sysconfdir="%{_sysconfdir}" \
        --interp-prefix=%{_prefix}/qemu-%M \
        --localstatedir="%{_localstatedir}" \
        --docdir="%{_docdir}" \
        --libexecdir="%{_libexecdir}" \
        --extra-ldflags="%{build_ldflags}" \
        --extra-cflags="%{optflags}" \
        --with-pkgversion="%{name}-%{version}-%{release}" \
        --with-suffix="%{name}" \
        --firmwarepath="%firmwaredirs" \
        --enable-trace-backends=dtrace \
        --with-coroutine=ucontext \
        --tls-priority=@QEMU,SYSTEM \
        %{disable_everything} \
        "$@" \
    || ( cat config.log ; exit 1 )
    echo "config-host.mak contents:"
    echo "==="
    cat config-host.mak
    echo "==="
}
pushd %{qemu_kvm_build}
run_configure \
%if %{defined target_list}
  --target-list="%{target_list}" \
%endif
%if %{defined block_drivers_rw_list}
  --block-drv-rw-whitelist=%{block_drivers_rw_list} \
%endif
%if %{defined block_drivers_ro_list}
  --block-drv-ro-whitelist=%{block_drivers_ro_list} \
%endif
  --enable-alsa \
  --enable-attr \
  --enable-bpf \
  --enable-cap-ng \
  --enable-capstone \
  --enable-coroutine-pool \
  --enable-curl \
  --enable-debug-info \
  --enable-docs \
  --enable-passt \
  --enable-fdt=system \
  --enable-gettext \
  --enable-gnutls \
  --enable-guest-agent \
  --enable-iconv \
  --enable-kvm \
  --enable-l2tpv3 \
  --enable-libssh \
  --enable-libusb \
  --enable-libudev \
  --enable-linux-aio \
%if "%{_lto_cflags}" != "%{nil}"
  --enable-lto \
%endif
  --enable-lzo \
  --enable-malloc-trim \
  --enable-modules \
  --enable-opengl \
  --enable-oss \
  --enable-pa \
  --enable-pie \
  --enable-pipewire \
  --enable-pixman \
  --enable-relocatable \
  --enable-seccomp \
  --enable-selinux \
  --enable-slirp \
  --enable-slirp-smbd \
  --enable-snappy \
  --enable-system \
  --enable-tcg \
  --enable-tools \
  --enable-tpm \
  --enable-usb-redir \
  --enable-vhost-kernel \
  --enable-vhost-net \
  --enable-vhost-user \
  --enable-vhost-user-blk-server \
  --enable-vhost-vdpa \
  --enable-vnc \
  --enable-png \
  --enable-vnc-sasl \
  --enable-xkbcommon \
  \
  \
  --audio-drv-list=pipewire,pa,sdl,alsa,%{?jack_drv}oss \
  --target-list-exclude=moxie-softmmu \
  --with-default-devices \
  --enable-auth-pam \
  --enable-bochs \
  --enable-bzip2 \
  --enable-cloop \
  --enable-curses \
  --enable-dmg \
  --enable-fuse \
  --enable-gio \
  --enable-gtk \
  --enable-hv-balloon \
  --enable-libdw \
  --enable-libkeyutils \
  --enable-multiprocess \
  --enable-nitro \
  --enable-parallels \
  --enable-qcow1 \
  --enable-qed \
  --enable-qom-cast-debug \
  --enable-replication \
  --enable-rutabaga-gfx \
  --enable-sdl \
%if %{have_sdl_image}
  --enable-sdl-image \
%endif
%ifarch %{valgrind_arches}
  --enable-valgrind \
%endif
  --enable-vdi \
  --enable-vhost-crypto \
  --enable-virglrenderer \
  --enable-vhdx \
  --enable-virtfs \
  --enable-vpc \
  --enable-vnc-jpeg \
  --enable-vte \
  --enable-vvfat \
  --enable-zstd
%if !%{tools_only}
%make_build
popd
%endif
%install
install -D -m 0644 %{_sourcedir}/qemu-guest-agent.service %{buildroot}%{_unitdir}/qemu-guest-agent.service
install -D -m 0644 %{_sourcedir}/qemu-ga.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/qemu-ga
install -D -m 0644 %{_sourcedir}/99-qemu-guest-agent.rules %{buildroot}%{_udevrulesdir}/99-qemu-guest-agent.rules
mkdir -p %{buildroot}%{_sysconfdir}/qemu-ga/fsfreeze-hook.d
install -p scripts/qemu-guest-agent/fsfreeze-hook %{buildroot}%{_sysconfdir}/qemu-ga/fsfreeze-hook
mkdir -p %{buildroot}%{_datadir}/%{name}/qemu-ga/fsfreeze-hook.d/
install -p -m 0644 scripts/qemu-guest-agent/fsfreeze-hook.d/*.sample %{buildroot}%{_datadir}/%{name}/qemu-ga/fsfreeze-hook.d/
mkdir -p -v %{buildroot}%{_localstatedir}/log/qemu-ga/
%if !%{tools_only}
install -D -m 0644 %{_sourcedir}/bridge.conf %{buildroot}%{_sysconfdir}/%{name}/bridge.conf
install -m 0644 contrib/systemd/qemu-pr-helper.service %{buildroot}%{_unitdir}
install -m 0644 contrib/systemd/qemu-pr-helper.socket %{buildroot}%{_unitdir}
install -m 0644 contrib/systemd/qemu-vmsr-helper.service %{buildroot}%{_unitdir}
install -m 0644 contrib/systemd/qemu-vmsr-helper.socket %{buildroot}%{_unitdir}
install -D -p -m 644 %{_sourcedir}/95-kvm-memlock.conf %{buildroot}%{_sysconfdir}/security/limits.d/95-kvm-memlock.conf
install -D -p -m 0644 %{_sourcedir}/vhost.conf %{buildroot}%{_sysconfdir}/modprobe.d/vhost.conf
install -D -p -m 0644 %{modprobe_kvm_conf} %{buildroot}%{_sysconfdir}/modprobe.d/kvm.conf
install -D -p -m 0644 -t %{buildroot}%{qemudocdir} README.rst COPYING COPYING.LIB LICENSE docs/interop/qmp-spec.rst
install -D -p -m 0644 qemu.sasl %{buildroot}%{_sysconfdir}/sasl2/%{name}.conf
install -m 0644 scripts/dump-guest-memory.py %{buildroot}%{_datadir}/%{name}
install -m 0755 scripts/simpletrace.py %{buildroot}%{_datadir}/%{name}/simpletrace.py
mkdir -p %{buildroot}%{_datadir}/%{name}/tracetool
install -m 0644 -t %{buildroot}%{_datadir}/%{name}/tracetool scripts/tracetool/*.py
mkdir -p %{buildroot}%{_datadir}/%{name}/tracetool/backend
install -m 0644 -t %{buildroot}%{_datadir}/%{name}/tracetool/backend scripts/tracetool/backend/*.py
mkdir -p %{buildroot}%{_datadir}/%{name}/tracetool/format
install -m 0644 -t %{buildroot}%{_datadir}/%{name}/tracetool/format scripts/tracetool/format/*.py
mkdir -p %{buildroot}%{_datadir}/%{name}/vhost-user
mkdir -p %{buildroot}%{testsdir}/python
mkdir -p %{buildroot}%{testsdir}/tests
mkdir -p %{buildroot}%{testsdir}/tests/qemu-iotests
mkdir -p %{buildroot}%{testsdir}/scripts/qmp
cp -R %{qemu_kvm_build}/python/qemu %{buildroot}%{testsdir}/python
cp -R %{qemu_kvm_build}/scripts/qmp/* %{buildroot}%{testsdir}/scripts/qmp
install -p -m 0755 tests/Makefile.include %{buildroot}%{testsdir}/tests/
cp -R tests/qemu-iotests/* %{buildroot}%{testsdir}/tests/qemu-iotests/
cp -ur %{qemu_kvm_build}/tests/qemu-iotests/* %{buildroot}%{testsdir}/tests/qemu-iotests/
install -p -m 0644 %{_sourcedir}/README.tests %{buildroot}%{testsdir}/README
pushd %{qemu_kvm_build}
%make_install
popd
chmod +x %{buildroot}%{_libdir}/%{name}/*.so
find %{buildroot}%{qemudocdir} -name .buildinfo -delete
rm -rf %{buildroot}%{qemudocdir}/specs
rm -rf %{buildroot}%{_datadir}/%{name}/openbios-ppc
rm -rf %{buildroot}%{_datadir}/%{name}/openbios-sparc32
rm -rf %{buildroot}%{_datadir}/%{name}/openbios-sparc64
rm -rf %{buildroot}%{_datadir}/%{name}/slof.bin
rm -rf %{buildroot}%{_datadir}/%{name}/pxe*rom
rm -rf %{buildroot}%{_datadir}/%{name}/efi*rom
rm -rf %{buildroot}%{_datadir}/%{name}/vgabios*bin
rm -rf %{buildroot}%{_datadir}/%{name}/bios*.bin
rm -rf %{buildroot}%{_datadir}/%{name}/edk2*
rm -rf %{buildroot}%{_datadir}/%{name}/firmware
%find_lang %{name}
chmod -x %{buildroot}%{_mandir}/man1/*
for emu in %{buildroot}%{_bindir}/qemu-system-*; do
    ln -sf qemu.1.gz %{buildroot}%{_mandir}/man1/$(basename $emu).1.gz
 done
ln -sf qemu.1.gz %{buildroot}%{_mandir}/man1/qemu-kvm.1.gz
ln -sf qemu-system-x86_64 %{buildroot}%{_bindir}/qemu-kvm
%endif
install -m0644 -D %{SOURCE37} %{buildroot}%{_sysusersdir}/qemu.conf
%oreon_autofiles qemu-img usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qemu-guest-agent usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qemu-pr-helper usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export MTESTARGS="--no-suite block"
%define timeout_multiplier 1
%ifarch riscv64 loongarch64
%define timeout_multiplier 3
%endif
%if %{with check}
%if !%{tools_only}
pushd %{qemu_kvm_build}
./qemu-system-i386 -help
./qemu-img -help
echo "Testing %{name}-build"
echo "######## unit tests ########"
%make_build check-unit
echo "######## QAPI schema tests ########"
%make_build check-qapi-schema
echo "######## DecodeTree tests ########"
%make_build check-decodetree
echo "######## Soft Float tests ########"
%make_build check-softfloat
echo "######## QTest tests ########"
%ifnarch ppc64le
%make_build check-qtest TIMEOUT_MULTIPLIER=%{timeout_multiplier}
%endif
echo "######## Block I/O tests ########"
%make_build check-block TIMEOUT_MULTIPLIER=%{timeout_multiplier}
echo "######## Functional tests ########"
%ifnarch ppc64le
%make_build check-func-quick TIMEOUT_MULTIPLIER=%{timeout_multiplier}
%endif
popd
%endif
%endif
%post -n qemu-guest-agent

%systemd_post qemu-guest-agent.service
%preun -n qemu-guest-agent

%systemd_preun qemu-guest-agent.service
%postun -n qemu-guest-agent

%systemd_postun_with_restart qemu-guest-agent.service
%if !%{tools_only}
%endif
%files -f %{oreon_filedir}/main.list
%files -n qemu-common -f %{oreon_filedir}/qemu-common.list
%files -n qemu-docs -f %{oreon_filedir}/qemu-docs.list
%files -n qemu-img -f %{oreon_filedir}/qemu-img.list
%files -n qemu-guest-agent -f %{oreon_filedir}/qemu-guest-agent.list
%files -n qemu-tools -f %{oreon_filedir}/qemu-tools.list
%files -n qemu-pr-helper -f %{oreon_filedir}/qemu-pr-helper.list
%files -n qemu-tests -f %{oreon_filedir}/qemu-tests.list
%files -n qemu-block-curl -f %{oreon_filedir}/qemu-block-curl.list
%files -n qemu-block-ssh -f %{oreon_filedir}/qemu-block-ssh.list
%files -n qemu-ui-opengl -f %{oreon_filedir}/qemu-ui-opengl.list
%files -n qemu-block-dmg -f %{oreon_filedir}/qemu-block-dmg.list
%files -n qemu-audio-alsa -f %{oreon_filedir}/qemu-audio-alsa.list
%files -n qemu-audio-oss -f %{oreon_filedir}/qemu-audio-oss.list
%files -n qemu-audio-pa -f %{oreon_filedir}/qemu-audio-pa.list
%files -n qemu-audio-pipewire -f %{oreon_filedir}/qemu-audio-pipewire.list
%files -n qemu-audio-sdl -f %{oreon_filedir}/qemu-audio-sdl.list
%files -n qemu-ui-curses -f %{oreon_filedir}/qemu-ui-curses.list
%files -n qemu-ui-gtk -f %{oreon_filedir}/qemu-ui-gtk.list
%files -n qemu-ui-sdl -f %{oreon_filedir}/qemu-ui-sdl.list
%files -n qemu-ui-egl-headless -f %{oreon_filedir}/qemu-ui-egl-headless.list
%files -n qemu-device-display-virtio-gpu -f %{oreon_filedir}/qemu-device-display-virtio-gpu.list
%files -n qemu-device-display-virtio-gpu-gl -f %{oreon_filedir}/qemu-device-display-virtio-gpu-gl.list
%files -n qemu-device-display-virtio-gpu-rutabaga -f %{oreon_filedir}/qemu-device-display-virtio-gpu-rutabaga.list
%files -n qemu-device-display-virtio-gpu-pci -f %{oreon_filedir}/qemu-device-display-virtio-gpu-pci.list
%files -n qemu-device-display-virtio-gpu-pci-gl -f %{oreon_filedir}/qemu-device-display-virtio-gpu-pci-gl.list
%files -n qemu-device-display-virtio-gpu-pci-rutabaga -f %{oreon_filedir}/qemu-device-display-virtio-gpu-pci-rutabaga.list
%files -n qemu-device-display-virtio-gpu-ccw -f %{oreon_filedir}/qemu-device-display-virtio-gpu-ccw.list
%files -n qemu-device-display-virtio-vga -f %{oreon_filedir}/qemu-device-display-virtio-vga.list
%files -n qemu-device-display-virtio-vga-gl -f %{oreon_filedir}/qemu-device-display-virtio-vga-gl.list
%files -n qemu-device-display-virtio-vga-rutabaga -f %{oreon_filedir}/qemu-device-display-virtio-vga-rutabaga.list
%files -n qemu-device-uefi-vars -f %{oreon_filedir}/qemu-device-uefi-vars.list
%files -n qemu-device-usb-host -f %{oreon_filedir}/qemu-device-usb-host.list
%files -n qemu-device-usb-redirect -f %{oreon_filedir}/qemu-device-usb-redirect.list
%files -n qemu-device-display-vhost-user-gpu -f %{oreon_filedir}/qemu-device-display-vhost-user-gpu.list
%files -n qemu-kvm -f %{oreon_filedir}/qemu-kvm.list
%files -n qemu-kvm-core -f %{oreon_filedir}/qemu-kvm-core.list
%files -n qemu-system-aarch64 -f %{oreon_filedir}/qemu-system-aarch64.list
%files -n qemu-system-aarch64-core -f %{oreon_filedir}/qemu-system-aarch64-core.list
%files -n qemu-system-alpha -f %{oreon_filedir}/qemu-system-alpha.list
%files -n qemu-system-alpha-core -f %{oreon_filedir}/qemu-system-alpha-core.list
%files -n qemu-system-arm -f %{oreon_filedir}/qemu-system-arm.list
%files -n qemu-system-arm-core -f %{oreon_filedir}/qemu-system-arm-core.list
%files -n qemu-system-avr -f %{oreon_filedir}/qemu-system-avr.list
%files -n qemu-system-avr-core -f %{oreon_filedir}/qemu-system-avr-core.list
%files -n qemu-system-hppa -f %{oreon_filedir}/qemu-system-hppa.list
%files -n qemu-system-hppa-core -f %{oreon_filedir}/qemu-system-hppa-core.list
%files -n qemu-system-loongarch64 -f %{oreon_filedir}/qemu-system-loongarch64.list
%files -n qemu-system-loongarch64-core -f %{oreon_filedir}/qemu-system-loongarch64-core.list
%files -n qemu-system-m68k -f %{oreon_filedir}/qemu-system-m68k.list
%files -n qemu-system-m68k-core -f %{oreon_filedir}/qemu-system-m68k-core.list
%files -n qemu-system-microblaze -f %{oreon_filedir}/qemu-system-microblaze.list
%files -n qemu-system-microblaze-core -f %{oreon_filedir}/qemu-system-microblaze-core.list
%files -n qemu-system-mips -f %{oreon_filedir}/qemu-system-mips.list
%files -n qemu-system-mips-core -f %{oreon_filedir}/qemu-system-mips-core.list
%files -n qemu-system-or1k -f %{oreon_filedir}/qemu-system-or1k.list
%files -n qemu-system-or1k-core -f %{oreon_filedir}/qemu-system-or1k-core.list
%files -n qemu-system-ppc -f %{oreon_filedir}/qemu-system-ppc.list
%files -n qemu-system-ppc-core -f %{oreon_filedir}/qemu-system-ppc-core.list
%files -n qemu-system-riscv -f %{oreon_filedir}/qemu-system-riscv.list
%files -n qemu-system-riscv-core -f %{oreon_filedir}/qemu-system-riscv-core.list
%files -n qemu-system-rx -f %{oreon_filedir}/qemu-system-rx.list
%files -n qemu-system-rx-core -f %{oreon_filedir}/qemu-system-rx-core.list
%files -n qemu-system-s390x -f %{oreon_filedir}/qemu-system-s390x.list
%files -n qemu-system-s390x-core -f %{oreon_filedir}/qemu-system-s390x-core.list
%files -n qemu-system-sh4 -f %{oreon_filedir}/qemu-system-sh4.list
%files -n qemu-system-sh4-core -f %{oreon_filedir}/qemu-system-sh4-core.list
%files -n qemu-system-sparc -f %{oreon_filedir}/qemu-system-sparc.list
%files -n qemu-system-sparc-core -f %{oreon_filedir}/qemu-system-sparc-core.list
%files -n qemu-system-tricore -f %{oreon_filedir}/qemu-system-tricore.list
%files -n qemu-system-tricore-core -f %{oreon_filedir}/qemu-system-tricore-core.list
%files -n qemu-system-x86 -f %{oreon_filedir}/qemu-system-x86.list
%files -n qemu-system-x86-core -f %{oreon_filedir}/qemu-system-x86-core.list
%files -n qemu-system-xtensa -f %{oreon_filedir}/qemu-system-xtensa.list
%files -n qemu-system-xtensa-core -f %{oreon_filedir}/qemu-system-xtensa-core.list

%changelog

%autochangelog

