%global source0_hash none

%define gitshort 9b08a3c4

Name:		vboot-utils
Version:	20230127
Release:	7.git%{gitshort}%{?dist}
Summary:	Verified Boot Utility from Chromium OS
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://chromium.googlesource.com/chromiumos/platform/vboot_reference

ExclusiveArch:	%{arm} aarch64 %{ix86} x86_64

# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  git clone https://git.chromium.org/git/chromiumos/platform/vboot_reference.git
#  cd vboot_reference/
#  git archive --format=tar --prefix=vboot-utils-9b08a3c4/ 9b08a3c4 | xz > vboot-utils-9b08a3c4.tar.xz
Source0:	%{name}-%{gitshort}.tar.xz

# Fix VB2_DEBUG function usage
Patch0:	vboot-utils-9b08a3c4.patch
# Fix linking error with USE_FLASHROM=0
Patch1: flashrom-ensure-flashrom-symbols-are-not-loaded-if-U.patch

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	glibc-static
BuildRequires:	openssl-devel
BuildRequires:	trousers-devel
BuildRequires:	libyaml-devel
BuildRequires:	xz-devel
BuildRequires:	libuuid-devel

%description
Verified boot is a collection of utilities helpful for chromebook computer.
Pack and sign the kernel, manage gpt partitions.

%prep
%autosetup -p1 -n %{name}-%{gitshort}

%build

%ifarch %{arm} aarch64
%global ARCH arm
%endif

%ifarch x86_64
%global ARCH x86_64
%endif

%ifarch i686
%global ARCH i386
%endif

make V=1 ARCH=%{ARCH} COMMON_FLAGS="$RPM_OPT_FLAGS" USE_FLASHROM=0

%install
make install V=1 DESTDIR=%{buildroot} ARCH=%{ARCH} COMMON_FLAGS="$RPM_OPT_FLAGS" USE_FLASHROM=0
mkdir -p %{buildroot}%{_datadir}/vboot/
cp -rf tests/devkeys %{buildroot}%{_datadir}/vboot/

# Remove unneeded build artifacts
rm -rf %{buildroot}/usr/lib/pkgconfig/
rm -rf %{buildroot}/usr/default/
rm -rf %{buildroot}/etc/default/
rm -rf %{buildroot}/usr/share/vboot/bin/
rm -f %{buildroot}/usr/bin/chromeos-tpm-recovery
rm -f %{buildroot}/usr/bin/crossystem
rm -f %{buildroot}/usr/bin/dev_debug_vboot
rm -f %{buildroot}/usr/bin/dumpRSAPublicKey
rm -f %{buildroot}/usr/bin/dump_fmap
rm -f %{buildroot}/usr/bin/dump_kernel_config
rm -f %{buildroot}/usr/bin/enable_dev_usb_boot
rm -f %{buildroot}/usr/bin/gbb_utility
rm -f %{buildroot}/usr/bin/tpm-nvsize
rm -f %{buildroot}/usr/bin/tpmc
rm -f %{buildroot}/usr/bin/vbutil_firmware
rm -f %{buildroot}/usr/bin/vbutil_key
rm -f %{buildroot}/usr/bin/vbutil_keyblock
rm -f %{buildroot}/usr/lib/libvboot_host.a

%files
%license LICENSE
%doc README
%{_bindir}/futility
%{_bindir}/vbutil_kernel
%{_bindir}/cgpt
%{_datadir}/vboot/devkeys/

%changelog
%autochangelog
