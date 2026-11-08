# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 01710ee01737dac492f1bae52becd057e08d20d11589089aa06accff415c28dd

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
# For a stable, released kernel, released_kernel should be 1. For rawhide
# and/or a kernel built from an rc or git snapshot, released_kernel should
# be 0.
%global released_kernel 1

# define buildid .local
%define specversion 7.2.4
%define tarfile_release 7.2.4
# This is needed to do merge window version magic
# This allows pkg_release to have configurable %%{?dist} tag
%define specrelease 300%{?buildid}%{?dist}

# This package doesn't contain any binary, thus no debuginfo package is needed
%global debug_package %{nil}

Name: kernel-headers
Summary: Header files for the Linux kernel for use by glibc
License: ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-2-Clause) AND ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-3-Clause) AND ((GPL-2.0-only WITH Linux-syscall-note) OR CDDL-1.0) AND ((GPL-2.0-only WITH Linux-syscall-note) OR Linux-OpenIB) AND ((GPL-2.0-only WITH Linux-syscall-note) OR MIT) AND ((GPL-2.0-or-later WITH Linux-syscall-note) OR BSD-3-Clause) AND ((GPL-2.0-or-later WITH Linux-syscall-note) OR MIT) AND BSD-3-Clause AND (GPL-1.0-or-later WITH Linux-syscall-note) AND GPL-2.0-only AND (GPL-2.0-only WITH Linux-syscall-note) AND (GPL-2.0-or-later WITH Linux-syscall-note) AND (LGPL-2.0-or-later WITH Linux-syscall-note) AND (LGPL-2.1-only WITH Linux-syscall-note) AND (LGPL-2.1-or-later WITH Linux-syscall-note) AND MIT
URL: http://www.kernel.org/
Version:        7.2.4
Release:        1%{?dist}
# This is a tarball with headers from the kernel, which should be created
# using create_headers_tarball.sh provided in the kernel source package.
# To create the tarball, you should go into a prepared/patched kernel sources
# directory, or git kernel source repository, and do eg.:
Source0:        https://cdn.kernel.org/pub/linux/kernel/v7.x/linux-%{version}.tar.xz
BuildRequires: make
BuildRequires: gcc
BuildRequires: bc
BuildRequires: flex
BuildRequires: bison
BuildRequires: elfutils-libelf-devel
BuildRequires: openssl-devel
BuildRequires: python3
BuildRequires: rsync
BuildRequires:  oreon-rpm-macros
Obsoletes: glibc-kernheaders < 3.0-46
Provides: glibc-kernheaders = 3.0-46
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
%oreon_sha256

%setup -q -n linux-%{specversion}
mkdir -p _hdr
for arch in arm arm64 loongarch powerpc riscv s390 x86; do
make ARCH=$arch INSTALL_HDR_PATH=$PWD/_hdr/arch-$arch headers_install
done

%build

%install
# List of architectures we support and want to copy their headers
ARCH_LIST="arm arm64 loongarch powerpc riscv s390 x86"

ARCH=%_target_cpu
case $ARCH in
	armv7hl)
		ARCH=arm
		;;
	aarch64)
		ARCH=arm64
		;;
	loongarch64*)
		ARCH=loongarch
		;;
	ppc64*)
		ARCH=powerpc
		;;
	riscv64)
		ARCH=riscv
		;;
	s390x)
		ARCH=s390
		;;
	x86_64|i*86)
		ARCH=x86
		;;
esac

cd _hdr/arch-$ARCH/include
mkdir -p $RPM_BUILD_ROOT%{_includedir}
cp -a asm-generic $RPM_BUILD_ROOT%{_includedir}

# Copy all the architectures we care about to their respective asm directories
for arch in $ARCH_LIST; do
	mkdir -p $RPM_BUILD_ROOT%{_prefix}/${arch}-linux-gnu/include
	cp -a asm-generic $RPM_BUILD_ROOT%{_prefix}/${arch}-linux-gnu/include/
done

# Remove what we copied already
rm -rf asm-generic

# Copy the rest of the headers over
cp -a * $RPM_BUILD_ROOT%{_includedir}/
for arch in $ARCH_LIST; do
cp -a * $RPM_BUILD_ROOT%{_prefix}/${arch}-linux-gnu/include/
done

%files
%defattr(-,root,root)
%{_includedir}/*

%files -n kernel-cross-headers
%defattr(-,root,root)
%{_prefix}/*-linux-gnu/*

