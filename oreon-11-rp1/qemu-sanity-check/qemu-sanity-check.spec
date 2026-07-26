%global source0_hash a2122b4fc9b67fbc4b9e3665722ca7e1990f780288fd09092114a06454929c45

%global debug_package %{nil}

# Architectures where the tests should pass.
#
# 2020-09: Fails on power64 because qemu TCG does not support all the
#   features required to boot Fedora.
# 2025-07: Fails on aarch64 because of lack of support for zstd + zboot
#   https://bugzilla.redhat.com/show_bug.cgi?id=2385692
%global test_arches %{s390x} x86_64

Name:           qemu-sanity-check
Version:        1.1.6
Release:        21%{?dist}
Summary:        Simple qemu and Linux kernel sanity checker
License:        GPL-2.0-or-later

ExclusiveArch:  %{kernel_arches}

%if 0%{?rhel} >= 9
# No KVM on POWER in RHEL 9
ExcludeArch:    %{power64}
%endif

URL:            http://people.redhat.com/~rjones/qemu-sanity-check
Source0:        http://people.redhat.com/~rjones/qemu-sanity-check/files/%{name}-%{version}.tar.gz
Source1:        http://people.redhat.com/~rjones/qemu-sanity-check/files/%{name}-%{version}.tar.gz.sig
# Keyring used to verify tarball signature.
Source2:        libguestfs.keyring

# Patches (all upstream).
Patch:          0001-tests-run-qemu-sanity-check-Add-v-flag-for-verbose-m.patch
Patch:          0002-Add-cpu-option.patch
Patch:          0003-Set-RAM-to-something-larger-than-qemu-default.patch
Patch:          0004-Set-console-on-ARM-and-s390.patch
Patch:          0005-Ignore-user-added-local-files-such-as-.-localconfigu.patch
Patch:          0006-Move-the-tests-into-a-subdirectory.patch
Patch:          0007-Move-the-source-files-into-a-subdirectory.patch
Patch:          0008-Attempt-RB_POWER_OFF-before-reboot.patch
Patch:          0009-Make-sure-that-qemu-sanity-check-v-displays-kernel-o.patch
Patch:          0010-Error-out-if-any-kernel-panic-is-seen.patch
Patch:          0011-src-Add-more-information-about-kernel-and-qemu-searc.patch
Patch:          0012-docs-Use-F-around-file-references-in-the-manual.patch
Patch:          0013-src-Look-for-kernels-in-lib-modules-vmlinuz.patch
Patch:          0014-Choose-cpu-max-by-default.patch

# To verify the tarball signature.
BuildRequires:  gnupg2

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake

# For building manual pages.
BuildRequires:  /usr/bin/perldoc

# For building the initramfs.
BuildRequires:  cpio
BuildRequires:  glibc-static

# For testing.
%if !0%{?rhel}
BuildRequires:  qemu
%else
BuildRequires:  qemu-kvm
%endif
BuildRequires:  kernel

# For complicated reasons, this is required so that
# /bin/kernel-install puts the kernel directly into /boot, instead of
# into a /boot/<machine-id> subdirectory (in Fedora >= 23).  Read the
# kernel-install script to understand why.
BuildRequires:  grubby

%if !0%{?rhel}
%ifarch %{ix86} x86_64
Requires:       qemu-system-x86
%global qemu    %{_bindir}/qemu-system-x86_64
%endif
%ifarch armv7hl
Requires:       qemu-system-arm
%global qemu    %{_bindir}/qemu-system-arm
%endif
%ifarch aarch64
Requires:       qemu-system-aarch64
%global qemu    %{_bindir}/qemu-system-aarch64
%endif
%ifarch %{power64}
Requires:       qemu-system-ppc
%global qemu    %{_bindir}/qemu-system-ppc64
%endif
%ifarch %{s390x}
Requires:       qemu-system-s390x
%global qemu    %{_bindir}/qemu-system-s390x
%endif
%else
# RHEL, any arch
Requires:       qemu-kvm
%global qemu    %{_libexecdir}/qemu-kvm
%endif

Requires:       kernel

# Require the -nodeps subpackage.
Requires:       %{name}-nodeps = %{version}-%{release}

%description
Qemu-sanity-check is a short shell script that test-boots a Linux
kernel under qemu, making sure it boots up to userspace.  The idea is
to test the Linux kernel and/or qemu to make sure they are working.

Most users should install the %{name} package.

If you are testing qemu or the kernel in those packages and you want
to avoid a circular dependency on qemu or kernel, you should use
'BuildRequires: %{name}-nodeps' instead.

%package nodeps
Summary:         Simple qemu and Linux kernel sanity checker (no dependencies)
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:         GPL-2.0-or-later

%description nodeps
This is the no-depedencies version of %{name}.  It is exactly the same
as %{name} except that this package does not depend on qemu or kernel.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
autoreconf -fi

%build
# NB: canonical_arch is a variable in the final script, so it
# has to be escaped here.
%configure \
%if 0%{?qemu:1}
    --with-qemu-list="%{qemu}" \
%else
    --with-qemu-list="qemu-system-\$canonical_arch" \
%endif
|| {
    cat config.log
    exit 1
}
make %{?_smp_mflags}

%check
%ifarch %{test_arches}
make check || {
    cat tests/run-qemu-sanity-check.log ||:
    cat tests/test-suite.log ||:
    exit 1
}
%endif

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files
%doc COPYING

%files nodeps
%doc COPYING README
%{_bindir}/qemu-sanity-check
%{_libdir}/qemu-sanity-check
%{_mandir}/man1/qemu-sanity-check.1*

%changelog
%autochangelog
