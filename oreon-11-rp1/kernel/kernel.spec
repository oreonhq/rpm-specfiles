# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 8183d475a76a0faffa92d6cd500af421f589dfd0300a0f1060bb875e11d45723
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%bcond thinlto 1

%global kverrel %{version}-%{release}.%{_target_cpu}
%global kmoddir /lib/modules/%{kverrel}
%global develdir %{_usrsrc}/kernels/%{kverrel}

%ifarch x86_64
%global karch x86
%global kimage arch/x86/boot/bzImage
%endif
%ifarch aarch64
%global karch arm64
%global kimage arch/arm64/boot/vmlinuz.efi
%endif

%global kobj ../kbuild
%global kmake %{__make} %{?_smp_mflags} ARCH=%{karch} LLVM=1 LLVM_IAS=1 HOSTLDFLAGS="%{_build_id_flags}" O=%{kobj}
%global tools_make %{__make} CC=%{__cc} HOSTCC=%{__cc} LD=%{__cc}
%ifarch aarch64
%global perf_extra_opts CORESIGHT=1
%endif
%global perf_make %{__make} %{?_smp_mflags} -C tools/perf V=1 CC=%{__cc} CXX=%{__cxx} HOSTCC=%{__cc} LD=%{__cc} CLANG=clang LDFLAGS="-Wl,-E" NO_PERF_READ_VDSO32=1 NO_PERF_READ_VDSOX32=1 WERROR=0 NO_LIBUNWIND=1 HAVE_CPLUS_DEMANGLE=1 NO_GTK2=1 NO_BIONIC=1 %{?perf_extra_opts} prefix=%{_prefix} PYTHON=%{__python3}
%global libperf_make %{__make} %{?_smp_mflags} -C tools/lib/perf V=1 CC=%{__cc} HOSTCC=%{__cc} LD=%{__cc}

%undefine _auto_set_build_flags
%undefine _include_minidebuginfo
%undefine _find_debuginfo_dwz_opts
%undefine _unique_build_ids
%undefine _unique_debug_names
%undefine _unique_debug_srcs
%undefine _debugsource_packages
%undefine _debuginfo_subpackages
%global _find_debuginfo_opts -r --keep-section .BTF --keep-section .rustc
%global _build_id_links alldebug
%global _no_recompute_build_ids 1

%define __modsign_install_post \
  bash %{SOURCE8} %{kobj}/certs/signing_key.pem %{kobj}/certs/signing_key.x509 %{buildroot}%{kmoddir}/ \
  find %{buildroot}%{kmoddir} -type f -name '*.ko' -exec chmod 0644 {} + \
  find %{buildroot}%{kmoddir} -type f -name '*.ko' -print0 | xargs -0 -r -n 16 -P %{_smp_build_ncpus} zstd -q --rm -19 \
%{nil}

%define __spec_install_post \
  %{?__debug_package:%{__debug_install_post}}\
  %{__arch_install_post}\
  %{__os_install_post}\
  %{__modsign_install_post}\
%{nil}

Name: kernel
Version: 7.3.6
Release: 1%{?dist}
Summary: The Linux kernel
License: ((GPL-2.0-only WITH Linux-syscall-note) OR CDDL-1.0) AND ((GPL-2.0-only WITH Linux-syscall-note) OR Linux-OpenIB) AND 0BSD AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSD-3-Clause-Clear AND CC0-1.0 AND GFDL-1.1-no-invariants-or-later AND GPL-1.0-or-later AND (GPL-1.0-or-later WITH Linux-syscall-note) AND GPL-2.0-only AND (GPL-2.0-only OR CDDL-1.0) AND (GPL-2.0-only OR GFDL-1.2-no-invariants-only) AND (GPL-2.0-only OR GFDL-1.2-no-invariants-or-later) AND (GPL-2.0-only WITH Linux-syscall-note) AND GPL-2.0-or-later AND (GPL-2.0-or-later OR CC-BY-4.0) AND (GPL-2.0-or-later WITH GCC-exception-2.0) AND (GPL-2.0-or-later WITH Linux-syscall-note) AND ISC AND LGPL-2.0-or-later AND (LGPL-2.0-or-later WITH Linux-syscall-note) AND LGPL-2.1-only AND (LGPL-2.1-only WITH Linux-syscall-note) AND LGPL-2.1-or-later AND (LGPL-2.1-or-later WITH Linux-syscall-note) AND (Linux-OpenIB OR GPL-2.0-only) AND (Linux-OpenIB OR GPL-2.0-only OR BSD-2-Clause) AND Linux-man-pages-copyleft AND MIT AND (MPL-1.1 OR GPL-2.0-only) AND (X11 OR GPL-2.0-only) AND (X11 OR GPL-2.0-or-later) AND Zlib AND (copyleft-next-0.3.1 OR GPL-2.0-or-later)
URL: https://www.kernel.org/
ExclusiveArch: x86_64 aarch64
Source0: https://cdn.kernel.org/pub/linux/kernel/v7.x/linux-%{version}.tar.xz
Source1: kernel-x86_64-oreon.config
Source2: kernel-aarch64-oreon.config
Source3: filtermods.py
Source4: def_variants.yaml.oreon
Source5: oreonsecureboot-ca.cer
Source6: mod-denylist.sh
Source7: oreonsecureboot-kernel.cer
Source8: mod-sign.sh
BuildRequires: oreon-rpm-macros
BuildRequires: asciidoc
BuildRequires: audit-libs-devel
BuildRequires: bash
BuildRequires: bc
BuildRequires: binutils
BuildRequires: binutils-devel
BuildRequires: bison
BuildRequires: capstone-devel
BuildRequires: clang
BuildRequires: coreutils
BuildRequires: cpio
BuildRequires: diffutils
BuildRequires: dwarves
BuildRequires: elfutils
BuildRequires: elfutils-debuginfod-client-devel
BuildRequires: elfutils-devel
BuildRequires: findutils
BuildRequires: flex
BuildRequires: gawk
BuildRequires: gettext
BuildRequires: hostname
BuildRequires: java-devel
BuildRequires: kmod
BuildRequires: libbabeltrace2-devel
BuildRequires: libbpf-devel
BuildRequires: libcap-devel
BuildRequires: libcap-ng-devel
BuildRequires: libnl3-devel
BuildRequires: libpfm-devel
BuildRequires: libtraceevent-devel
BuildRequires: libtracefs-devel
BuildRequires: lld
BuildRequires: llvm
BuildRequires: m4
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: newt-devel
BuildRequires: numactl-devel
BuildRequires: openssl
BuildRequires: openssl-devel
BuildRequires: pciutils-devel
BuildRequires: perl(ExtUtils::Embed)
BuildRequires: perl-interpreter
BuildRequires: pkgconf
BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: python3-docutils
BuildRequires: python3-pyyaml
BuildRequires: python3-setuptools
BuildRequires: systemd-rpm-macros
BuildRequires: tar
BuildRequires: which
BuildRequires: xmlto
BuildRequires: xz
BuildRequires: xz-devel
BuildRequires: zlib-devel
BuildRequires: zstd
%ifarch aarch64
BuildRequires: opencsd-devel >= 1.0.0
%endif
%if %{without thinlto}
BuildRequires: rust
BuildRequires: rust-src
BuildRequires: bindgen
%endif

Requires: kernel-core-uname-r = %{kverrel}
Requires: kernel-modules-uname-r = %{kverrel}
Requires: kernel-modules-core-uname-r = %{kverrel}
Requires: ((kernel-modules-extra-uname-r = %{kverrel}) if kernel-modules-extra-matched)
Provides: installonlypkg(kernel)

%description
The kernel meta package. It pulls in the Linux kernel image and the modules
that match it. This kernel is built with clang and ThinLTO.

%package core
Summary: The Linux kernel image
Provides: kernel = %{version}-%{release}
Provides: kernel-%{_target_cpu} = %{version}-%{release}
Provides: kernel-uname-r = %{kverrel}
Provides: kernel-core-uname-r = %{kverrel}
Provides: installonlypkg(kernel)
Requires: kernel-modules-core-uname-r = %{kverrel}
Requires(pre): coreutils
Requires(pre): systemd >= 203-2
Requires(pre): /usr/bin/kernel-install
Requires(pre): dracut >= 027
Requires(pre): ((linux-firmware >= 20150904-56.git6ebf5d57) if linux-firmware)
Requires(preun): systemd >= 200
Recommends: linux-firmware
AutoReq: no
AutoProv: yes

%description core
The kernel-core package contains the Linux kernel (vmlinuz), the core of any
Linux operating system. The kernel handles the basic functions of the
operating system: memory allocation, process allocation, device input and
output, etc.

%package modules-core
Summary: Core kernel modules to match the core kernel
Provides: kernel-modules-core-%{_target_cpu} = %{version}-%{release}
Provides: kernel-modules-core = %{version}-%{release}
Provides: kernel-modules-core-uname-r = %{kverrel}
Provides: installonlypkg(kernel-module)
Requires: kernel-uname-r = %{kverrel}
AutoReq: no
AutoProv: yes

%description modules-core
This package provides essential kernel modules for the core kernel package.

%package modules
Summary: Kernel modules to match the core kernel
Provides: kernel-modules-%{_target_cpu} = %{version}-%{release}
Provides: kernel-modules = %{version}-%{release}
Provides: kernel-modules-uname-r = %{kverrel}
Provides: installonlypkg(kernel-module)
Requires: kernel-uname-r = %{kverrel}
Requires: kernel-modules-core-uname-r = %{kverrel}
AutoReq: no
AutoProv: yes

%description modules
This package provides commonly used kernel modules for the core kernel package.

%package modules-extra
Summary: Extra kernel modules to match the kernel
Provides: kernel-modules-extra-%{_target_cpu} = %{version}-%{release}
Provides: kernel-modules-extra = %{version}-%{release}
Provides: kernel-modules-extra-uname-r = %{kverrel}
Provides: installonlypkg(kernel-module)
Requires: kernel-uname-r = %{kverrel}
Requires: kernel-modules-uname-r = %{kverrel}
Requires: kernel-modules-core-uname-r = %{kverrel}
AutoReq: no
AutoProv: yes

%description modules-extra
This package provides less commonly used kernel modules for the kernel package.

%package modules-extra-matched
Summary: Meta package which requires modules-extra to be installed for all kernels

%description modules-extra-matched
This meta package provides a single reference that other packages can Require
to have modules-extra installed for all kernels.

%package modules-internal
Summary: Kernel test modules to match the kernel
Provides: kernel-modules-internal-%{_target_cpu} = %{version}-%{release}
Provides: kernel-modules-internal = %{version}-%{release}
Provides: kernel-modules-internal-uname-r = %{kverrel}
Provides: installonlypkg(kernel-module)
Requires: kernel-uname-r = %{kverrel}
Requires: kernel-modules-uname-r = %{kverrel}
Requires: kernel-modules-core-uname-r = %{kverrel}
AutoReq: no
AutoProv: yes

%description modules-internal
This package provides the KUnit and self-test kernel modules for the kernel
package.

%package devel
Summary: Development package for building kernel modules to match the kernel
Provides: kernel-devel-%{_target_cpu} = %{version}-%{release}
Provides: kernel-devel-uname-r = %{kverrel}
Provides: installonlypkg(kernel)
Requires(pre): findutils
Requires: findutils
Requires: perl-interpreter
Requires: openssl-devel
Requires: elfutils-libelf-devel
Requires: bison
Requires: flex
Requires: make
Requires: clang
Requires: lld
Requires: llvm
AutoReqProv: no

%description devel
This package provides kernel headers and makefiles sufficient to build modules
against the kernel package. Out-of-tree modules have to be built with LLVM=1.

%package devel-matched
Summary: Meta package to install matching core and devel packages for a given kernel
Requires: kernel-devel = %{version}-%{release}
Requires: kernel-core = %{version}-%{release}

%description devel-matched
This meta package is used to install matching core and devel packages for a
given kernel.

%package tools
Summary: Assortment of tools for the Linux kernel
Requires: kernel-tools-libs%{?_isa} = %{version}-%{release}
Provides: cpupowerutils = 1:009-0.6.p1
Provides: cpufreq-utils = 1:009-0.6.p1
Provides: cpufrequtils = 1:009-0.6.p1

%description tools
This package contains the tools/ directory from the kernel source and the
supporting documentation.

%package tools-libs
Summary: Libraries for the kernel-tools

%description tools-libs
This package contains the libraries built from the tools/ directory from the
kernel source.

%package -n perf
Summary: Performance monitoring for the Linux kernel
Requires: bzip2

%description -n perf
This package contains the perf tool, which enables performance monitoring
of the Linux kernel.

%package -n python3-perf
Summary: Python bindings for apps which will manipulate perf events

%description -n python3-perf
The python3-perf package contains a module that permits applications
written in the Python programming language to use the interface
to manipulate perf events.

%package -n libperf
Summary: The perf library from kernel source

%description -n libperf
This package contains the kernel source perf library.

%package -n libperf-devel
Summary: Development files for the perf library from kernel source
Requires: libperf%{?_isa} = %{version}-%{release}

%description -n libperf-devel
This package includes libraries and header files needed for development
of applications which use perf library from kernel source.

%package -n rtla
Summary: Real-Time Linux Analysis tools
Requires: libtraceevent
Requires: libtracefs
Requires: libbpf
Requires: kernel-tools-libs%{?_isa} = %{version}-%{release}

%description -n rtla
The rtla meta-tool includes a set of commands that aims to analyze
the real-time properties of Linux. Instead of testing Linux as a black box,
rtla leverages kernel tracing capabilities to provide precise information
about the properties and root causes of unexpected results.

%package -n rv
Summary: RV: Runtime Verification

%description -n rv
Runtime Verification (RV) is a lightweight (yet rigorous) method that
complements classical exhaustive verification techniques (such as model
checking and theorem proving) with a more practical approach for
complex systems.
The rv tool is the interface for a collection of monitors that aim
to analyze the logical and timing behavior of Linux.

%package tools-libs-devel
Summary: Development files for the kernel-tools libraries
Requires: kernel-tools%{?_isa} = %{version}-%{release}
Requires: kernel-tools-libs%{?_isa} = %{version}-%{release}
Provides: kernel-tools-devel = %{version}-%{release}
Provides: cpupowerutils-devel = 1:009-0.6.p1

%description tools-libs-devel
This package contains the development files for the tools/ directory from the
kernel source.

%prep
%oreon_sha256
%autosetup -p1 -n linux-%{version}
sed -i -e 's/^EXTRAVERSION =.*/EXTRAVERSION = -%{release}.%{_target_cpu}/' Makefile
%py3_shebang_fix scripts/show_delta scripts/diffconfig scripts/bloat-o-meter scripts/jobserver-exec scripts/clang-tools tools Documentation

openssl x509 -inform DER -in %{SOURCE5} -out certs/oreon-secureboot-ca.pem
openssl x509 -inform DER -in %{SOURCE7} -out certs/oreon-secureboot-kernel.pem
cat certs/oreon-secureboot-ca.pem certs/oreon-secureboot-kernel.pem > certs/oreon-secureboot.pem

mkdir -p %{kobj}/certs
cp -p certs/oreon-secureboot.pem %{kobj}/certs/
%ifarch x86_64
cp -p %{SOURCE1} %{kobj}/.config
%endif
%ifarch aarch64
cp -p %{SOURCE2} %{kobj}/.config
%endif
scripts/config --file %{kobj}/.config \
    -d PREEMPT_LAZY -e PREEMPT -e PREEMPT_DYNAMIC \
    -e TCP_CONG_BBR -d DEFAULT_CUBIC -e DEFAULT_BBR \
    -d ZSWAP_COMPRESSOR_DEFAULT_LZO -e ZSWAP_COMPRESSOR_DEFAULT_ZSTD \
    -d ZRAM_DEF_COMP_LZORLE -e ZRAM_DEF_COMP_ZSTD \
    -d MODULE_COMPRESS_XZ -e MODULE_COMPRESS_ZSTD -d MODULE_COMPRESS_ALL \
    --set-str DRM_PANIC_SCREEN_QR_CODE_URL "" \
    --set-str SYSTEM_TRUSTED_KEYS certs/oreon-secureboot.pem \
    --set-str MODULE_SIG_KEY certs/signing_key.pem \
    -e MODULE_SIG_ALL
%if %{with thinlto}
scripts/config --file %{kobj}/.config \
    -d LTO_NONE -e LTO_CLANG_THIN \
    -d RUST -e ANDROID_BINDER_IPC -e ANDROID_BINDERFS \
    --set-str DRM_PANIC_SCREEN user
%endif
%{kmake} olddefconfig

for opt in PREEMPT PREEMPT_DYNAMIC HZ_1000 TCP_CONG_BBR DEFAULT_BBR \
    ZSWAP_COMPRESSOR_DEFAULT_ZSTD ZRAM_DEF_COMP_ZSTD MODULE_COMPRESS_ZSTD \
    LRU_GEN LRU_GEN_ENABLED SCHED_CLASS_EXT DEBUG_INFO_BTF DEBUG_INFO_BTF_MODULES \
    TRANSPARENT_HUGEPAGE_MADVISE MODULE_SIG MODULE_SIG_ALL CPU_MITIGATIONS \
    %{?with_thinlto:LTO_CLANG_THIN ANDROID_BINDER_IPC ANDROID_BINDERFS} %{!?with_thinlto:RUST}; do
    grep -qx "CONFIG_$opt=y" %{kobj}/.config || { echo "CONFIG_$opt is not set" >&2; exit 1; }
done
grep -qx 'CONFIG_SYSTEM_TRUSTED_KEYS="certs/oreon-secureboot.pem"' %{kobj}/.config || { echo "CONFIG_SYSTEM_TRUSTED_KEYS is wrong" >&2; exit 1; }
grep -qx 'CONFIG_MODULE_SIG_KEY="certs/signing_key.pem"' %{kobj}/.config || { echo "CONFIG_MODULE_SIG_KEY is wrong" >&2; exit 1; }
if grep -q '^CONFIG_X86_NATIVE_CPU=y' %{kobj}/.config; then
    echo "CONFIG_X86_NATIVE_CPU must stay off" >&2
    exit 1
fi

%build
%{kmake} all
%{__make} %{?_smp_mflags} -C tools/bpf/bpftool LLVM=1 bootstrap
tools/bpf/bpftool/bootstrap/bpftool btf dump file %{kobj}/vmlinux format c > vmlinux.h

chmod +x tools/power/cpupower/utils/version-gen.sh
%{tools_make} %{?_smp_mflags} -C tools/power/cpupower CPUFREQ_BENCH=false DEBUG=false
%ifarch x86_64
%{tools_make} %{?_smp_mflags} -C tools/power/cpupower/debug/x86_64 centrino-decode powernow-k8-decode
%{tools_make} -C tools/power/x86/x86_energy_perf_policy
%{tools_make} -C tools/power/x86/turbostat
%{tools_make} -C tools/power/x86/intel-speed-select
%{tools_make} -C tools/arch/x86/intel_sdsi
%endif
%{tools_make} -C tools/thermal/tmon
%{tools_make} -C tools/bootconfig
%{tools_make} -C tools/iio
%{tools_make} -C tools/gpio
%{tools_make} -C tools/mm slabinfo page_owner_sort
%{tools_make} -C tools/verification/rv
%{tools_make} -C tools/tracing/rtla LDFLAGS="-L../../power/cpupower" INCLUDES="-I../../power/cpupower/lib" SYSTEM_BPFTOOL=$PWD/tools/bpf/bpftool/bootstrap/bpftool
%{perf_make} DESTDIR=%{buildroot} all
%{libperf_make} DESTDIR=%{buildroot}

%install
install -d %{buildroot}/boot %{buildroot}%{kmoddir}
install -m 0755 %{kobj}/%{kimage} %{buildroot}%{kmoddir}/vmlinuz
install -m 0755 %{kobj}/%{kimage} %{buildroot}/boot/vmlinuz-%{kverrel}
install -m 0644 %{kobj}/System.map %{buildroot}%{kmoddir}/System.map
install -m 0644 %{kobj}/System.map %{buildroot}/boot/System.map-%{kverrel}
install -m 0644 %{kobj}/.config %{buildroot}%{kmoddir}/config
install -m 0644 %{kobj}/.config %{buildroot}/boot/config-%{kverrel}
xz --compress --check=crc32 --lzma2=dict=1MiB --stdout < %{kobj}/Module.symvers > %{buildroot}%{kmoddir}/symvers.xz
cp %{buildroot}%{kmoddir}/symvers.xz %{buildroot}/boot/symvers-%{kverrel}.xz
dd if=/dev/zero of=%{buildroot}/boot/initramfs-%{kverrel}.img bs=1M count=40

%{kmake} INSTALL_MOD_PATH=%{buildroot} KERNELRELEASE=%{kverrel} mod-fw= modules_install
%{kmake} INSTALL_MOD_PATH=%{buildroot} KERNELRELEASE=%{kverrel} vdso_install
rm -rf %{buildroot}%{kmoddir}/vdso/.build-id
%ifarch aarch64
mkdir -p %{buildroot}/boot/dtb-%{kverrel}
%{kmake} INSTALL_DTBS_PATH=%{buildroot}/boot/dtb-%{kverrel} dtbs_install
cp -r %{buildroot}/boot/dtb-%{kverrel} %{buildroot}%{kmoddir}/dtb
find %{buildroot}%{kmoddir}/dtb -name '*.dtb' -exec chmod 0644 {} +
%endif

rm -f %{buildroot}%{kmoddir}/build %{buildroot}%{kmoddir}/source
mkdir -p %{buildroot}%{kmoddir}/build %{buildroot}%{kmoddir}/updates %{buildroot}%{kmoddir}/weak-updates %{buildroot}%{kmoddir}/systemtap
ln -s build %{buildroot}%{kmoddir}/source
cp --parents $(find . -type f -name "Makefile*" -o -name "Kconfig*") %{buildroot}%{kmoddir}/build
cp %{kobj}/Module.symvers %{kobj}/System.map %{buildroot}%{kmoddir}/build
rm -rf %{buildroot}%{kmoddir}/build/scripts %{buildroot}%{kmoddir}/build/include
cp %{kobj}/.config %{buildroot}%{kmoddir}/build
cp -a scripts %{buildroot}%{kmoddir}/build
rm -rf %{buildroot}%{kmoddir}/build/scripts/tracing
rm -f %{buildroot}%{kmoddir}/build/scripts/spdxcheck.py
cp -a --parents security/selinux/include/classmap.h %{buildroot}%{kmoddir}/build
cp -a --parents security/selinux/include/initial_sid_to_string.h %{buildroot}%{kmoddir}/build
cp -a --parents security/selinux/include/policycap_names.h %{buildroot}%{kmoddir}/build
cp -a --parents security/selinux/include/policycap.h %{buildroot}%{kmoddir}/build
cp -a --parents tools/include/tools/be_byteshift.h %{buildroot}%{kmoddir}/build
cp -a --parents tools/include/tools/le_byteshift.h %{buildroot}%{kmoddir}/build
cp -a --parents tools/include/linux/compiler* %{buildroot}%{kmoddir}/build
cp -a --parents tools/include/linux/types.h %{buildroot}%{kmoddir}/build
cp -a --parents tools/build/Build.include %{buildroot}%{kmoddir}/build
cp --parents tools/build/fixdep.c %{buildroot}%{kmoddir}/build
cp --parents tools/objtool/sync-check.sh %{buildroot}%{kmoddir}/build
cp -a --parents tools/bpf/resolve_btfids %{buildroot}%{kmoddir}/build
cp -a --parents tools/include/asm %{buildroot}%{kmoddir}/build
cp -a --parents tools/include/asm-generic %{buildroot}%{kmoddir}/build
cp -a --parents tools/include/linux %{buildroot}%{kmoddir}/build
cp -a --parents tools/include/uapi/asm %{buildroot}%{kmoddir}/build
cp -a --parents tools/include/uapi/asm-generic %{buildroot}%{kmoddir}/build
cp -a --parents tools/include/uapi/linux %{buildroot}%{kmoddir}/build
cp -a --parents tools/include/vdso %{buildroot}%{kmoddir}/build
cp --parents tools/scripts/utilities.mak %{buildroot}%{kmoddir}/build
cp -a --parents tools/lib/subcmd %{buildroot}%{kmoddir}/build
cp --parents tools/lib/*.c %{buildroot}%{kmoddir}/build
cp --parents tools/objtool/*.[ch] %{buildroot}%{kmoddir}/build
cp --parents tools/objtool/Build %{buildroot}%{kmoddir}/build
cp --parents tools/objtool/include/objtool/*.h %{buildroot}%{kmoddir}/build
cp -a --parents tools/lib/bpf %{buildroot}%{kmoddir}/build
cp --parents tools/lib/bpf/Build %{buildroot}%{kmoddir}/build
if [ -f %{kobj}/tools/objtool/objtool ]; then
    cp -a %{kobj}/tools/objtool/objtool %{buildroot}%{kmoddir}/build/tools/objtool/
fi
if [ -f %{kobj}/tools/objtool/fixdep ]; then
    cp -a %{kobj}/tools/objtool/fixdep %{buildroot}%{kmoddir}/build/tools/objtool/
fi
if ls %{kobj}/rust/*.rmeta >/dev/null 2>&1; then
    mkdir -p %{buildroot}%{kmoddir}/build/rust
    cp -a %{kobj}/rust/*.rmeta %{buildroot}%{kmoddir}/build/rust/
fi
if ls %{kobj}/rust/*.so >/dev/null 2>&1; then
    mkdir -p %{buildroot}%{kmoddir}/build/rust
    cp -a %{kobj}/rust/*.so %{buildroot}%{kmoddir}/build/rust/
fi
if [ -d %{kobj}/arch/%{karch}/scripts ]; then
    cp -a %{kobj}/arch/%{karch}/scripts %{buildroot}%{kmoddir}/build/arch/%{karch}
fi
if [ -d arch/%{karch}/scripts ]; then
    cp -a arch/%{karch}/scripts %{buildroot}%{kmoddir}/build/arch/%{karch}
fi
if ls arch/%{karch}/*lds >/dev/null 2>&1; then
    cp -a arch/%{karch}/*lds %{buildroot}%{kmoddir}/build/arch/%{karch}/
fi
if [ -f arch/%{karch}/kernel/module.lds ]; then
    cp -a --parents arch/%{karch}/kernel/module.lds %{buildroot}%{kmoddir}/build/
fi
cp -a --parents arch/%{karch}/include %{buildroot}%{kmoddir}/build/
cp -a --parents tools/arch/%{karch}/include %{buildroot}%{kmoddir}/build
%ifarch aarch64
cp -a --parents arch/arm/include/asm/xen %{buildroot}%{kmoddir}/build/
cp -a --parents arch/arm/include/asm/opcodes.h %{buildroot}%{kmoddir}/build/
%endif
cp -a include %{buildroot}%{kmoddir}/build/include
cp -a %{kobj}/include/generated %{buildroot}%{kmoddir}/build/include/
cp -a %{kobj}/include/config %{buildroot}%{kmoddir}/build/include/
if [ -d %{kobj}/arch/%{karch}/include/generated ]; then
    cp -a %{kobj}/arch/%{karch}/include/generated %{buildroot}%{kmoddir}/build/arch/%{karch}/include/
fi
cp -a %{kobj}/scripts/. %{buildroot}%{kmoddir}/build/scripts/
if [ -f %{kobj}/tools/bpf/resolve_btfids/resolve_btfids ]; then
    mkdir -p %{buildroot}%{kmoddir}/build/tools/bpf/resolve_btfids
    cp -a %{kobj}/tools/bpf/resolve_btfids/resolve_btfids %{buildroot}%{kmoddir}/build/tools/bpf/resolve_btfids/
fi
cp -a sound/soc/sof/sof-audio.h %{buildroot}%{kmoddir}/build/sound/soc/sof
%ifarch x86_64
cp -a --parents arch/x86/entry/syscalls/syscall_32.tbl %{buildroot}%{kmoddir}/build/
cp -a --parents arch/x86/entry/syscalls/syscall_64.tbl %{buildroot}%{kmoddir}/build/
cp -a --parents arch/x86/tools/relocs_32.c %{buildroot}%{kmoddir}/build/
cp -a --parents arch/x86/tools/relocs_64.c %{buildroot}%{kmoddir}/build/
cp -a --parents arch/x86/tools/relocs.c %{buildroot}%{kmoddir}/build/
cp -a --parents arch/x86/tools/relocs_common.c %{buildroot}%{kmoddir}/build/
cp -a --parents arch/x86/tools/relocs.h %{buildroot}%{kmoddir}/build/
cp -a --parents arch/x86/purgatory/purgatory.c %{buildroot}%{kmoddir}/build/
cp -a --parents arch/x86/purgatory/stack.S %{buildroot}%{kmoddir}/build/
cp -a --parents arch/x86/purgatory/setup-x86_64.S %{buildroot}%{kmoddir}/build/
cp -a --parents arch/x86/purgatory/entry64.S %{buildroot}%{kmoddir}/build/
cp -a --parents arch/x86/boot/string.h %{buildroot}%{kmoddir}/build/
cp -a --parents arch/x86/boot/string.c %{buildroot}%{kmoddir}/build/
cp -a --parents arch/x86/boot/ctype.h %{buildroot}%{kmoddir}/build/
cp -a --parents scripts/syscalltbl.sh %{buildroot}%{kmoddir}/build/
cp -a --parents scripts/syscallhdr.sh %{buildroot}%{kmoddir}/build/
cp -a --parents tools/arch/x86/include/asm %{buildroot}%{kmoddir}/build
cp -a --parents tools/arch/x86/include/uapi/asm %{buildroot}%{kmoddir}/build
if [ -d tools/objtool/arch/x86/lib ]; then
    cp -a --parents tools/objtool/arch/x86/lib %{buildroot}%{kmoddir}/build
fi
cp -a --parents tools/arch/x86/lib/ %{buildroot}%{kmoddir}/build
cp -a --parents tools/arch/x86/tools/gen-insn-attr-x86.awk %{buildroot}%{kmoddir}/build
cp -a --parents tools/objtool/arch/x86/ %{buildroot}%{kmoddir}/build
%endif
find %{buildroot}%{kmoddir}/build/scripts \( -iname "*.o" -o -iname "*.cmd" \) -exec rm -f {} +
find %{buildroot}%{kmoddir}/build/tools \( -iname "*.o" -o -iname "*.cmd" \) -exec rm -f {} +
touch -r %{buildroot}%{kmoddir}/build/Makefile \
    %{buildroot}%{kmoddir}/build/include/generated/uapi/linux/version.h \
    %{buildroot}%{kmoddir}/build/include/config/auto.conf
install -m 0644 vmlinux.h %{buildroot}%{kmoddir}/build/vmlinux.h

mkdir -p %{buildroot}%{_prefix}/lib/debug%{kmoddir}
cp %{kobj}/vmlinux %{buildroot}%{_prefix}/lib/debug%{kmoddir}/vmlinux

find %{buildroot}%{kmoddir} -name '*.ko' -type f > modnames
xargs --no-run-if-empty chmod u+x < modnames
grep -F /drivers/ modnames | xargs --no-run-if-empty nm -upA |
    sed -n 's,^.*/\([^/]*\.ko\):  *U \(.*\)$,\1 \2,p' > drivers.undef
collect_modules_list()
{
    sed -r -n -e "s/^([^ ]+) \\.?($2)\$/\\1/p" drivers.undef |
        LC_ALL=C sort -u > %{buildroot}%{kmoddir}/modules.$1
    if [ -n "$3" ]; then
        sed -r -e "/^($3)\$/d" -i %{buildroot}%{kmoddir}/modules.$1
    fi
}
collect_modules_list networking \
    'register_netdev|ieee80211_register_hw|usbnet_probe|phy_driver_register|rt(l_|2x00)(pci|usb)_probe|register_netdevice'
collect_modules_list block \
    'ata_scsi_ioctl|scsi_add_host|scsi_add_host_with_dma|blk_alloc_queue|register_mtd_blktrans|scsi_esp_register|scsi_register_device_handler|blk_queue_physical_block_size' 'dm-mod.ko'
collect_modules_list drm \
    'drm_open'
collect_modules_list modesetting \
    'drm_crtc_init'

if xargs --no-run-if-empty /sbin/modinfo -l < modnames | \
    grep -E -v 'GPL( v2)?$|Dual BSD/GPL$|Dual MPL/GPL$|GPL and additional rights$'; then
    exit 1
fi

mkdir -p kmodlists
%{python3} %{SOURCE3} -q -l kmodlists/filtermods.log sort \
    -d %{buildroot}%{kmoddir}/modules.dep -c %{SOURCE4} -o kmodlists || {
    cat kmodlists/filtermods.log
    exit 1
}

create_module_file_list()
{
    subdir=$1
    relative=$2
    absolute=$3
    alldirs=$4
    denylist=$5
    if [ "$subdir" != kernel ]; then
        sed -e 's|^kernel/||' "$relative" | while read -r kmod; do
            mkdir -p "$(dirname "%{buildroot}%{kmoddir}/$subdir/$kmod")"
            mv "%{buildroot}%{kmoddir}/kernel/$kmod" "%{buildroot}%{kmoddir}/$subdir/$kmod"
        done
    fi
    sed -e "s|^kernel/|%{kmoddir}/$subdir/|" "$relative" > "$absolute"
    if [ "$denylist" -eq 1 ]; then
        bash %{SOURCE6} %{buildroot} lib/modules/%{kverrel} "$absolute"
    fi
    sed -i -e 's/\.ko$/.ko.zst/' "$absolute"
    if [ "$subdir" != kernel ]; then
        echo "%%dir %{kmoddir}/$subdir" >> "$absolute"
    fi
    if [ "$alldirs" -eq 1 ]; then
        (cd %{buildroot} && find lib/modules/%{kverrel}/kernel -mindepth 1 -type d | sort -n) |
            sed -e 's|^lib|%%dir /lib|' >> "$absolute"
    fi
}
create_module_file_list kernel kmodlists/modules-core.list kernel-modules-core.list 1 0
create_module_file_list kernel kmodlists/modules.list kernel-modules.list 0 0
create_module_file_list internal kmodlists/modules-internal.list kernel-modules-internal.list 0 1
create_module_file_list kernel kmodlists/modules-extra.list kernel-modules-extra.list 0 1

rm -f %{buildroot}%{kmoddir}/modules.alias %{buildroot}%{kmoddir}/modules.alias.bin \
    %{buildroot}%{kmoddir}/modules.builtin.alias.bin %{buildroot}%{kmoddir}/modules.builtin.bin \
    %{buildroot}%{kmoddir}/modules.dep %{buildroot}%{kmoddir}/modules.dep.bin \
    %{buildroot}%{kmoddir}/modules.devname %{buildroot}%{kmoddir}/modules.softdep \
    %{buildroot}%{kmoddir}/modules.symbols %{buildroot}%{kmoddir}/modules.symbols.bin \
    %{buildroot}%{kmoddir}/modules.weakdep

find %{buildroot}%{kmoddir}/build -name ".*.cmd" -delete
find %{buildroot}%{kmoddir}/build -name "*.mod.c" -delete
mkdir -p %{buildroot}%{_usrsrc}/kernels
mv %{buildroot}%{kmoddir}/build %{buildroot}%{develdir}
ln -sf %{develdir} %{buildroot}%{kmoddir}/build

%{tools_make} -C tools/power/cpupower DESTDIR=%{buildroot} libdir=%{_libdir} libexecdir=%{_libexecdir} mandir=%{_mandir} unitdir=%{_unitdir} CPUFREQ_BENCH=false install
%find_lang cpupower
chmod 0755 %{buildroot}%{_libdir}/libcpupower.so*
%ifarch x86_64
install -m 0755 tools/power/cpupower/debug/x86_64/centrino-decode %{buildroot}%{_bindir}/centrino-decode
install -m 0755 tools/power/cpupower/debug/x86_64/powernow-k8-decode %{buildroot}%{_bindir}/powernow-k8-decode
mkdir -p %{buildroot}%{_mandir}/man8
%{tools_make} -C tools/power/x86/x86_energy_perf_policy DESTDIR=%{buildroot} install
%{tools_make} -C tools/power/x86/turbostat DESTDIR=%{buildroot} install
%{tools_make} -C tools/power/x86/intel-speed-select DESTDIR=%{buildroot} install
%{tools_make} -C tools/arch/x86/intel_sdsi DESTDIR=%{buildroot} BINDIR=%{_sbindir} install
%endif
%{tools_make} -C tools/thermal/tmon INSTALL_ROOT=%{buildroot} install
%{tools_make} -C tools/bootconfig DESTDIR=%{buildroot} install
%{tools_make} -C tools/iio DESTDIR=%{buildroot} install
%{tools_make} -C tools/gpio DESTDIR=%{buildroot} install
install -m 0755 tools/mm/slabinfo %{buildroot}%{_bindir}/slabinfo
install -m 0755 tools/mm/page_owner_sort %{buildroot}%{_bindir}/page_owner_sort
%{tools_make} -C tools/verification/rv DESTDIR=%{buildroot} STRIP=/bin/true install
%{tools_make} -C tools/tracing/rtla DESTDIR=%{buildroot} STRIP=/bin/true install
%{perf_make} DESTDIR=%{buildroot} lib=%{_lib} install-bin
rm -f %{buildroot}%{_bindir}/trace
%{perf_make} DESTDIR=%{buildroot} install-python_ext
mkdir -p %{buildroot}%{_mandir}/man1
%{perf_make} DESTDIR=%{buildroot} install-man
%{libperf_make} DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{_libdir} install install_headers
rm -f %{buildroot}%{_libdir}/libperf.a
mkdir -p %{buildroot}%{_datadir}/doc/kernel-keys/%{kverrel}
install -m 0644 %{SOURCE5} %{buildroot}%{_datadir}/doc/kernel-keys/%{kverrel}/kernel-signing-ca.cer
install -m 0644 %{SOURCE7} %{buildroot}%{_datadir}/doc/kernel-keys/%{kverrel}/kernel-signing.cer

%post core
mkdir -p %{_localstatedir}/lib/rpm-state/%{name}
touch %{_localstatedir}/lib/rpm-state/%{name}/installing_core_%{kverrel}

%posttrans core
rm -f %{_localstatedir}/lib/rpm-state/%{name}/installing_core_%{kverrel}
/bin/kernel-install add %{kverrel} %{kmoddir}/vmlinuz || exit 0
if [ ! -e "/boot/symvers-%{kverrel}.xz" ]; then
    cp "%{kmoddir}/symvers.xz" "/boot/symvers-%{kverrel}.xz"
    if command -v restorecon >/dev/null 2>&1; then
        restorecon "/boot/symvers-%{kverrel}.xz"
    fi
fi

%preun core
/bin/kernel-install remove %{kverrel} || exit 0

%posttrans modules-core
/sbin/depmod -a %{kverrel}

%post modules
/sbin/depmod -a %{kverrel}
if [ -f %{kmoddir}/vmlinuz ] &&
   [ -f /boot/initramfs-%{kverrel}.img ] &&
   [ ! -f %{_localstatedir}/lib/rpm-state/%{name}/installing_core_%{kverrel} ]; then
    mkdir -p %{_localstatedir}/lib/rpm-state/%{name}
    touch %{_localstatedir}/lib/rpm-state/%{name}/need_to_run_dracut_%{kverrel}
fi

%postun modules
/sbin/depmod -a %{kverrel}

%posttrans modules
if [ -f %{_localstatedir}/lib/rpm-state/%{name}/need_to_run_dracut_%{kverrel} ]; then
    rm -f %{_localstatedir}/lib/rpm-state/%{name}/need_to_run_dracut_%{kverrel}
    dracut -f --kver "%{kverrel}" /boot/initramfs-%{kverrel}.img || exit 0
fi

%post modules-extra
/sbin/depmod -a %{kverrel}

%postun modules-extra
/sbin/depmod -a %{kverrel}

%post modules-internal
/sbin/depmod -a %{kverrel}

%postun modules-internal
/sbin/depmod -a %{kverrel}

%post devel
if [ -f /etc/sysconfig/kernel ]; then
    . /etc/sysconfig/kernel || exit 0
fi
if [ "$HARDLINK" != "no" ] && [ -x /usr/bin/hardlink ] && [ ! -e /run/ostree-booted ]; then
    (cd %{develdir} &&
     /usr/bin/find . -type f | while read -r f; do
         hardlink -c /usr/src/kernels/*%{?dist}.*/$f $f > /dev/null
     done
     /usr/bin/find /usr/src/kernels -type f -name '*.hardlink-temporary' -delete
    )
fi

%files

%files core
%license COPYING
%{kmoddir}/vmlinuz
%ghost %attr(0755, root, root) /boot/vmlinuz-%{kverrel}
%{kmoddir}/System.map
%ghost %attr(0644, root, root) /boot/System.map-%{kverrel}
%dir /lib/modules
%dir %{kmoddir}
%{kmoddir}/symvers.xz
%{kmoddir}/config
%{kmoddir}/modules.builtin*
%ghost %attr(0644, root, root) /boot/symvers-%{kverrel}.xz
%ghost %attr(0600, root, root) /boot/initramfs-%{kverrel}.img
%ghost %attr(0644, root, root) /boot/config-%{kverrel}
%dir %{_datadir}/doc/kernel-keys
%{_datadir}/doc/kernel-keys/%{kverrel}
%ifarch aarch64
%{kmoddir}/dtb
%ghost /boot/dtb-%{kverrel}
%endif

%files modules-core -f kernel-modules-core.list
%dir /lib/modules
%dir %{kmoddir}
%dir %{kmoddir}/kernel
%{kmoddir}/build
%{kmoddir}/source
%{kmoddir}/updates
%{kmoddir}/weak-updates
%{kmoddir}/systemtap
%{kmoddir}/vdso
%{kmoddir}/modules.block
%{kmoddir}/modules.drm
%{kmoddir}/modules.modesetting
%{kmoddir}/modules.networking
%{kmoddir}/modules.order
%ghost %attr(0644, root, root) %{kmoddir}/modules.alias
%ghost %attr(0644, root, root) %{kmoddir}/modules.alias.bin
%ghost %attr(0644, root, root) %{kmoddir}/modules.builtin.alias.bin
%ghost %attr(0644, root, root) %{kmoddir}/modules.builtin.bin
%ghost %attr(0644, root, root) %{kmoddir}/modules.dep
%ghost %attr(0644, root, root) %{kmoddir}/modules.dep.bin
%ghost %attr(0644, root, root) %{kmoddir}/modules.devname
%ghost %attr(0644, root, root) %{kmoddir}/modules.softdep
%ghost %attr(0644, root, root) %{kmoddir}/modules.symbols
%ghost %attr(0644, root, root) %{kmoddir}/modules.symbols.bin
%ghost %attr(0644, root, root) %{kmoddir}/modules.weakdep

%files modules -f kernel-modules.list

%files modules-extra -f kernel-modules-extra.list

%files modules-extra-matched

%files modules-internal -f kernel-modules-internal.list

%files devel
%defverify(not mtime)
%{develdir}

%files devel-matched

%files tools -f cpupower.lang
%{_bindir}/cpupower
%{_libexecdir}/cpupower
%{_unitdir}/cpupower.service
%config(noreplace) %{_sysconfdir}/cpupower-service.conf
%{_datadir}/bash-completion/completions/cpupower
%{_mandir}/man[1-8]/cpupower*
%ifarch x86_64
%{_bindir}/centrino-decode
%{_bindir}/powernow-k8-decode
%{_bindir}/x86_energy_perf_policy
%{_mandir}/man8/x86_energy_perf_policy*
%{_bindir}/turbostat
%{_mandir}/man8/turbostat*
%{_bindir}/intel-speed-select
%{_sbindir}/intel_sdsi
%endif
%{_bindir}/tmon
%{_bindir}/bootconfig
%{_bindir}/iio_event_monitor
%{_bindir}/iio_generic_buffer
%{_bindir}/lsiio
%{_bindir}/lsgpio
%{_bindir}/gpio-hammer
%{_bindir}/gpio-event-mon
%{_bindir}/gpio-watch
%{_bindir}/page_owner_sort
%{_bindir}/slabinfo

%files tools-libs
%license COPYING
%{_libdir}/libcpupower.so.1
%{_libdir}/libcpupower.so.1.*

%files -n perf
%{_bindir}/perf
%{_libdir}/libperf-jvmti.so
%dir %{_libexecdir}/perf-core
%{_libexecdir}/perf-core/*
%{_mandir}/man[1-8]/perf*
%{_sysconfdir}/bash_completion.d/perf
%doc tools/perf/Documentation/examples.txt
%{_docdir}/perf-tip/tips.txt
%{_includedir}/perf/perf_dlfilter.h

%files -n python3-perf
%{python3_sitearch}/perf*

%files -n libperf
%{_libdir}/libperf.so.0
%{_libdir}/libperf.so.0.0.1

%files -n libperf-devel
%{_libdir}/libperf.so
%{_libdir}/pkgconfig/libperf.pc
%{_includedir}/internal/*.h
%{_includedir}/perf/bpf_perf.h
%{_includedir}/perf/core.h
%{_includedir}/perf/cpumap.h
%{_includedir}/perf/event.h
%{_includedir}/perf/evlist.h
%{_includedir}/perf/evsel.h
%{_includedir}/perf/mmap.h
%{_includedir}/perf/schedstat-*.h
%{_includedir}/perf/threadmap.h
%{_mandir}/man3/libperf.3*
%{_mandir}/man7/libperf-counting.7*
%{_mandir}/man7/libperf-sampling.7*

%files -n rtla
%{_bindir}/rtla
%{_bindir}/hwnoise
%{_bindir}/osnoise
%{_bindir}/timerlat
%{_mandir}/man1/rtla-hwnoise.1*
%{_mandir}/man1/rtla-osnoise-hist.1*
%{_mandir}/man1/rtla-osnoise-top.1*
%{_mandir}/man1/rtla-osnoise.1*
%{_mandir}/man1/rtla-timerlat-hist.1*
%{_mandir}/man1/rtla-timerlat-top.1*
%{_mandir}/man1/rtla-timerlat.1*
%{_mandir}/man1/rtla.1*

%files -n rv
%{_bindir}/rv
%{_mandir}/man1/rv-list.1*
%{_mandir}/man1/rv-mon-sched.1*
%{_mandir}/man1/rv-mon-stall.1*
%{_mandir}/man1/rv-mon-wip.1*
%{_mandir}/man1/rv-mon-wwnr.1*
%{_mandir}/man1/rv-mon.1*
%{_mandir}/man1/rv.1*

%files tools-libs-devel
%{_libdir}/libcpupower.so
%{_includedir}/cpufreq.h
%{_includedir}/cpuidle.h
%{_includedir}/powercap.h

%changelog
%autochangelog
