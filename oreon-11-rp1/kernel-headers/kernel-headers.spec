%global released_kernel 1
%define specversion 7.0.9
%define tarfile_release %{specversion}
%define specrelease 200%{?buildid}%{?dist}

%global debug_package %{nil}

Name:           kernel-headers
Summary:        Header files for the Linux kernel for use by glibc
License:        ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-2-Clause) AND ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-3-Clause) AND ((GPL-2.0-only WITH Linux-syscall-note) OR CDDL-1.0) AND ((GPL-2.0-only WITH Linux-syscall-note) OR Linux-OpenIB) AND ((GPL-2.0-only WITH Linux-syscall-note) OR MIT) AND ((GPL-2.0-or-later WITH Linux-syscall-note) OR BSD-3-Clause) AND ((GPL-2.0-or-later WITH Linux-syscall-note) OR MIT) AND BSD-3-Clause AND (GPL-1.0-or-later WITH Linux-syscall-note) AND GPL-2.0-only AND (GPL-2.0-only WITH Linux-syscall-note) AND (GPL-2.0-or-later WITH Linux-syscall-note) AND (LGPL-2.0-or-later WITH Linux-syscall-note) AND (LGPL-2.1-only WITH Linux-syscall-note) AND (LGPL-2.1-or-later WITH Linux-syscall-note) AND MIT
URL:            https://www.kernel.org/
Version:        %{specversion}
Release:        %{specrelease}
Source0:        https://www.kernel.org/pub/linux/kernel/v7.x/linux-%{tarfile_release}.tar.xz

# No gcc/glibc-devel chain: headers_install only runs scripts; pulling gcc would
# require kernel-headers already in the repo (bootstrap deadlock with glibc-devel).
BuildRequires:  make
BuildRequires:  python3
BuildRequires:  perl-interpreter

Obsoletes:      glibc-kernheaders < 3.0-46
Provides:       glibc-kernheaders = 3.0-46

%description
Kernel-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
glibc package.

%package -n kernel-cross-headers
Summary:        Header files for the Linux kernel for use by cross-glibc

%description -n kernel-cross-headers
Kernel-cross-headers includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.  The
header files define structures and constants that are needed for
building most standard programs and are also needed for rebuilding the
cross-glibc package.

%prep
%setup -q -n linux-%{tarfile_release}

%build
# Headers are installed in %%install via headers_install (no kernel image build).

%install
ARCH_LIST="arm arm64 loongarch powerpc riscv s390 x86"
STAGING=%{buildroot}%{_tmppath}/kernel-headers-staging
rm -rf "$STAGING"
mkdir -p "$STAGING"

for karch in $ARCH_LIST; do
  mkdir -p "$STAGING/arch-$karch"
  make ARCH=$karch INSTALL_HDR_PATH="$STAGING/arch-$karch" headers_install %{?_smp_mflags}
done

ARCH=%{_target_cpu}
case $ARCH in
	armv7hl|armv7hnl|arm)
		ARCH=arm
		;;
	aarch64|arm64)
		ARCH=arm64
		;;
	loongarch64*)
		ARCH=loongarch
		;;
	ppc64*|powerpc64*)
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

cd "$STAGING/arch-$ARCH/include"
mkdir -p %{buildroot}%{_includedir}
cp -a asm-generic %{buildroot}%{_includedir}

for karch in $ARCH_LIST; do
	mkdir -p %{buildroot}%{_prefix}/${karch}-linux-gnu/include
	cp -a asm-generic %{buildroot}%{_prefix}/${karch}-linux-gnu/include/
done

rm -rf asm-generic
cp -a * %{buildroot}%{_includedir}/
for karch in $ARCH_LIST; do
	cp -a * %{buildroot}%{_prefix}/${karch}-linux-gnu/include/
done

rm -rf "$STAGING"

%files
%defattr(-,root,root)
%{_includedir}/*

%files -n kernel-cross-headers
%defattr(-,root,root)
%{_prefix}/*-linux-gnu/*

%changelog
* Mon May 18 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.0.9-200
- Add kernel-headers 7.0.9 (matches oreon kernel), build from kernel.org tarball
