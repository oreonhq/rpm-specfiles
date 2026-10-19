%global source0_hash fd0fc479f983a8c05313f13e9c36330fe6651cf725396748c40d5cd93fa1e6a4
%global released_kernel 1
%define specversion 7.2.11
%define tarfile_release 7.2.11
%define specrelease 200%{?buildid}%{?dist}
%global debug_package %{nil}
Name: kernel-headers
Summary:        Header files for the Linux kernel for use by glibc
License: ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-2-Clause) AND ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-3-Clause) AND ((GPL-2.0-only WITH Linux-syscall-note) OR CDDL-1.0) AND ((GPL-2.0-only WITH Linux-syscall-note) OR Linux-OpenIB) AND ((GPL-2.0-only WITH Linux-syscall-note) OR MIT) AND ((GPL-2.0-or-later WITH Linux-syscall-note) OR BSD-3-Clause) AND ((GPL-2.0-or-later WITH Linux-syscall-note) OR MIT) AND BSD-3-Clause AND (GPL-1.0-or-later WITH Linux-syscall-note) AND GPL-2.0-only AND (GPL-2.0-only WITH Linux-syscall-note) AND (GPL-2.0-or-later WITH Linux-syscall-note) AND (LGPL-2.0-or-later WITH Linux-syscall-note) AND (LGPL-2.1-only WITH Linux-syscall-note) AND (LGPL-2.1-or-later WITH Linux-syscall-note) AND MIT
URL: http://www.kernel.org/
Version: %{specversion}
Release:        1%{?dist}
Source0:        https://cdn.kernel.org/pub/linux/kernel/v7.x/linux-%{version}.tar.xz#/%{name}-%{version}.tar.xz
Obsoletes: glibc-kernheaders < 3.0-46
Provides: glibc-kernheaders = 3.0-46
%if "0%{?variant}"
Obsoletes: kernel-headers < %{specversion}-%{specrelease}
Provides: kernel-headers = %{specversion}-%{specrelease}
%endif
# oreon:deps
BuildRequires:  curl
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  rsync
BuildRequires:  tar
BuildRequires:  xz
# /oreon:deps
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
%oreon_autofiles kernel-cross-headers usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n kernel-cross-headers -f %{oreon_filedir}/kernel-cross-headers.list

%changelog

* Mon Jul 27 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.1.5-200
- Linux v7.1.5
* Sat Jul  5 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.1.3-200
- Linux v7.1.3
* Sat Jun 20 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.1.1-200
- Linux v7.1.1
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.0.6-200
- Import
