%global source0_hash e56c8356dda01136a6041c6ef832bd0ec99bd2d35dff97832aa5ec10ed014304

# For a stable, released kernel, released_kernel should be 1. For rawhide
# and/or a kernel built from an rc or git snapshot, released_kernel should
# be 0.
%global released_kernel 1

# define buildid .local
%define specversion 7.0.11
%define tarfile_release 7.0.11
# This is needed to do merge window version magic
# This allows pkg_release to have configurable %%{?dist} tag
%define specrelease 200%{?buildid}%{?dist}

# This package doesn't contain any binary, thus no debuginfo package is needed
%global debug_package %{nil}

Name: kernel-headers
Summary: Header files for the Linux kernel for use by glibc
License: ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-2-Clause) AND ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-3-Clause) AND ((GPL-2.0-only WITH Linux-syscall-note) OR CDDL-1.0) AND ((GPL-2.0-only WITH Linux-syscall-note) OR Linux-OpenIB) AND ((GPL-2.0-only WITH Linux-syscall-note) OR MIT) AND ((GPL-2.0-or-later WITH Linux-syscall-note) OR BSD-3-Clause) AND ((GPL-2.0-or-later WITH Linux-syscall-note) OR MIT) AND BSD-3-Clause AND (GPL-1.0-or-later WITH Linux-syscall-note) AND GPL-2.0-only AND (GPL-2.0-only WITH Linux-syscall-note) AND (GPL-2.0-or-later WITH Linux-syscall-note) AND (LGPL-2.0-or-later WITH Linux-syscall-note) AND (LGPL-2.1-only WITH Linux-syscall-note) AND (LGPL-2.1-or-later WITH Linux-syscall-note) AND MIT
URL: http://www.kernel.org/
Version: %{specversion}
Release: %{specrelease}
# This is a tarball with headers from the kernel, which should be created
# using create_headers_tarball.sh provided in the kernel source package.
# To create the tarball, you should go into a prepared/patched kernel sources
# directory, or git kernel source repository, and do eg.:
# For a RHEL package: (...)/create_headers_tarball.sh -m RHEL_RELEASE
# For a Fedora package: kernel/scripts/create_headers_tarball.sh -r <release number>
Source0: https://cdn.kernel.org/pub/linux/kernel/v7.x/linux-%{tarfile_release}.tar.xz#/kernel-headers-%{tarfile_release}.tar.xz
Obsoletes: glibc-kernheaders < 3.0-46
Provides: glibc-kernheaders = 3.0-46
BuildRequires: curl
BuildRequires: tar
BuildRequires: xz
BuildRequires: make
BuildRequires: gcc
BuildRequires: rsync
%if "0%{?variant}"
Obsoletes: kernel-headers < %{specversion}-%{specrelease}
Provides: kernel-headers = %{specversion}-%{specrelease}
%endif

%description
Kernel-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
glibc package.

%package -n kernel-cross-headers
Summary: Header files for the Linux kernel for use by cross-glibc

%description -n kernel-cross-headers
Kernel-cross-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
cross-glibc package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c

%build

%install
KDIR="linux-%{tarfile_release}"
test -d "$KDIR" || { echo "missing $KDIR" >&2; exit 1; }

ARCH=%_target_cpu
case $ARCH in
	armv7hl)
		KARCH=arm
		;;
	aarch64)
		KARCH=arm64
		;;
	loongarch64*)
		KARCH=loongarch
		;;
	ppc64*)
		KARCH=powerpc
		;;
	riscv64)
		KARCH=riscv
		;;
	s390x)
		KARCH=s390
		;;
	x86_64|i*86)
		KARCH=x86
		;;
	*)
		KARCH=$ARCH
		;;
esac

make -C "$KDIR" ARCH=$KARCH INSTALL_HDR_PATH=%{buildroot}/usr headers_install
find %{buildroot}/usr/include \
	\( -name .install -o -name .check -o -name ..install.cmd -o -name ..check.cmd \) -delete

HDR_ARCH_LIST="arm arm64 loongarch powerpc riscv s390 x86"
mkdir -p %{buildroot}/usr/tmp-headers
for arch in $HDR_ARCH_LIST; do
	mkdir -p %{buildroot}/usr/tmp-headers/arch-${arch}
	make -C "$KDIR" ARCH=${arch} INSTALL_HDR_PATH=%{buildroot}/usr/tmp-headers/arch-${arch} headers_install
done
find %{buildroot}/usr/tmp-headers \
	\( -name .install -o -name .check -o -name ..install.cmd -o -name ..check.cmd \) -delete
for arch in $HDR_ARCH_LIST; do
	mkdir -p %{buildroot}%{_prefix}/${arch}-linux-gnu/include
	cp -a %{buildroot}/usr/tmp-headers/arch-${arch}/include/. %{buildroot}%{_prefix}/${arch}-linux-gnu/include/
done
rm -rf %{buildroot}/usr/tmp-headers

%files
%defattr(-,root,root)
%{_includedir}/*

%files -n kernel-cross-headers
%defattr(-,root,root)
%{_prefix}/*-linux-gnu/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.0.6-200
- Import
