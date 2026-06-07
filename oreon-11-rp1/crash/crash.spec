%global source0_hash 73dcdc633ec75ea2fc5329a1c3760407cceb9171428f4d0b885874f943a16797
%global source1_hash bdc1da4a033280ac752e7d34b0418efaa45bed093235cb88e62ea961752a37f8

#
# crash core analysis suite
#
Summary: Kernel analysis utility for live systems, netdump, diskdump, kdump, LKCD or mcore dumpfiles
Name: crash
Version: 9.0.1
Release: 6%{?dist}
License: GPL-3.0-only
Source0:        https://github.com/crash-utility/crash/archive/refs/tags/crash-%{version}.tar.gz#/crash-%{version}.tar.gz
Source1: https://mirrors.kernel.org/gnu/gdb/gdb-16.2.tar.gz
URL: https://crash-utility.github.io
ExclusiveOS: Linux
ExclusiveArch: %{ix86} ia64 x86_64 ppc ppc64 s390 s390x %{arm} aarch64 ppc64le riscv64
BuildRequires: ncurses-devel zlib-devel lzo-devel snappy-devel bison wget patch texinfo libzstd-devel
BuildRequires: make gcc gcc-c++
BuildRequires: gmp-devel mpfr-devel
Requires: binutils
Provides: bundled(libiberty)
Provides: bundled(gdb) = 16.2
Patch0: lzo_snappy_zstd.patch
Patch1: crash-9.0.1_build.patch
Patch2: 0001-Fix-timer-r-option-on-Linux-6.18-and-later-kernels.patch
Patch3: 0002-Fix-typo-uncompess-uncompress.patch
Patch4: 0003-arm64-Fix-vtop-command-to-display-swap-information-o.patch
Patch5: 0004-arm64-Fix-vtop-command-to-display-swap-information-o.patch
Patch6: 0005-make-the-MAX_MALLOC_BUFS-customizable.patch
Patch7: 0006-Doc-add-manual-and-help-entry-for-max-malloc-bufs-op.patch
Patch8: 0007-Add-a-command-line-option-to-retrieve-build-id.patch
Patch9: 0008-Loongarch-update-the-NR_CPUS-to-2048.patch
Patch10: 0009-Resolve-BLK_MQ_F_TAG_HCTX_SHARED-at-runtime.patch
Patch11: 0010-bpf-improve-for-loop-when-searching-for-used_maps.patch
Patch12: 0011-RISCV64-fix-wrong-information-of-PUD-PMD-and-PTE-SA4.patch
Patch13: 0012-RISCV64-fix-wrong-information-of-P4D-PUD-PMD-and-PTE.patch
Patch14: 0013-Fix-for-mod-S-causes-symbols-to-be-incorrect.patch
Patch15: 0014-maple_tree-add-support-for-maple_tree.c-output-to-re.patch
Patch16: 0015-sys-Display-livepatch-transition-status-in-KERNEL-li.patch
Patch17: 0016-Ensure-all-child-processes-are-properly-cleaned-up-i.patch
Patch18: 0017-Fix-prompt-output-interfering-with-piped-commands-in.patch
Patch19: 0018-Fix-external-command-output-not-redirected-to-pipe.patch
Patch20: 0019-memory-Handle-crash-failure-in-linux-next-caused-by-.patch
Patch21: 0020-Fix-pipe-parsing-to-correctly-handle-quotes.patch
Patch22: 0021-Fix-file-redirection-not-working-for-external-comman.patch
Patch23: 0022-Reapply-vmcoreinfo-read-vmcoreinfo-using-vmcoreinfo_.patch
Patch24: 0023-Fix-for-help-r-D-to-display-register-values-and-note.patch

%description
The core analysis suite is a self-contained tool that can be used to
investigate either live systems, kernel core dumps created from the
netdump, diskdump and kdump packages from Red Hat Linux, the mcore kernel patch
offered by Mission Critical Linux, or the LKCD kernel patch.

%package devel
Requires: %{name} = %{version}, zlib-devel
Summary: kernel crash analysis utility for live systems, netdump, diskdump, kdump, LKCD or mcore dumpfiles

%description devel
The core analysis suite is a self-contained tool that can be used to
investigate either live systems, kernel core dumps created from the
netdump, diskdump and kdump packages from Red Hat Linux, the mcore kernel patch
offered by Mission Critical Linux, or the LKCD kernel patch.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -n %{name}-%{version} -q
%patch -P 0 -p1 -b lzo_snappy_zstd.patch
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1
%patch -P 10 -p1
%patch -P 11 -p1
%patch -P 12 -p1
%patch -P 13 -p1
%patch -P 14 -p1
%patch -P 15 -p1
%patch -P 16 -p1
%patch -P 17 -p1
%patch -P 18 -p1
%patch -P 19 -p1
%patch -P 20 -p1
%patch -P 21 -p1
%patch -P 22 -p1
%patch -P 23 -p1
%patch -P 24 -p1

%build

cp %{SOURCE1} .
make -j`nproc` RPMPKG="%{version}-%{release}" CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
%make_install
mkdir -p %{buildroot}%{_mandir}/man8
cp -p crash.8 %{buildroot}%{_mandir}/man8/crash.8
mkdir -p %{buildroot}%{_includedir}/crash
chmod 0644 defs.h
cp -p defs.h %{buildroot}%{_includedir}/crash

%files
%{_bindir}/crash
%{_mandir}/man8/crash.8*
%doc README COPYING3

%files devel
%{_includedir}/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9.0.1-6
- Prepare for Oreon 11 (RP1)
