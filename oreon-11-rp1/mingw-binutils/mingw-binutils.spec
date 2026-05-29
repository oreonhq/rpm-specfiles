%global source0_hash none

%global run_testsuite 1
%global mingw_build_ucrt64 1
%define enable_new_dtags 0

Name:           mingw-binutils
Version:        2.45.1
Release:        2%{?dist}
Summary:        Cross-compiled version of binutils for Win32 and Win64 environments

License:        GPL-3.0-or-later AND (GPL-3.0-or-later WITH Bison-exception-2.2) AND (LGPL-2.0-or-later WITH GCC-exception-2.0) AND BSD-3-Clause AND GFDL-1.3-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.0-or-later

URL:            http://www.gnu.org/software/binutils/
Source0:        https://ftp.gnu.org/gnu/binutils/binutils-2.45.1.tar.xz

### Patches from native package
# Purpose:  Use /lib64 and /usr/lib64 instead of /lib and /usr/lib in the
#           default library search path of 64-bit targets.
# Lifetime: Permanent, but it should not be.  This is a bug in the libtool
#           sources used in both binutils and gcc, (specifically the
#           libtool.m4 file).  These are based on a version released in 2009
#           (2.2.6?) rather than the latest version.  (Definitely fixed in
#           libtool version 2.4.6).
# Not needed, mingw does not have lib64
# Patch01: binutils-libtool-lib64.patch

# Purpose:  Appends a RHEL or Fedora release string to the generic binutils
#           version string.
# Lifetime: Permanent.  This is a RHEL/Fedora specific patch.
Patch02: binutils-version.patch

# Purpose:  Exports the demangle.h header file (associated with the libiberty
#           sources) with the binutils-devel rpm.
# Lifetime: Permanent.  This is a RHEL/Fedora specific patch.
Patch03: binutils-export-demangle.h.patch

# Purpose:  Disables the check in the BFD library's bfd.h header file that
#           config.h has been included before the bfd.h header.  See BZ
#           #845084 for more details.
# Lifetime: Permanent - but it should not be.  The bfd.h header defines
#           various types that are dependent upon configuration options, so
#           the order of inclusion is important.
# FIXME:    It would be better if the packages using the bfd.h header were
#           fixed so that they do include the header files in the correct
#           order.
Patch04: binutils-no-config-h-check.patch

# Purpose:  Disable an x86/x86_64 optimization that moves functions from the
#           PLT into the GOTPLT for faster access.  This optimization is
#           problematic for tools that want to intercept PLT entries, such
#           as ltrace and LD_AUDIT.  See BZs 1452111 and 1333481.
# Lifetime: Permanent.  But it should not be.
# FIXME:    Replace with a configure time option.
Patch05: binutils-revert-PLT-elision.patch

# Purpose:  Do not create PLT entries for AARCH64 IFUNC symbols referenced in
#           debug sections.
# Lifetime: Permanent.
# FIXME:    Find related bug.  Decide on permanency.
Patch06: binutils-2.27-aarch64-ifunc.patch

# Purpose:  Stop the binutils from statically linking with libstdc++.
# Lifetime: Permanent.
Patch07: binutils-do-not-link-with-static-libstdc++.patch

# Purpose:  Stop gold from aborting when input sections with the same name
#            have different flags.
# Lifetime: Fixed in 2.43 (maybe)
# Patch08: binutils-gold-mismatched-section-flags.patch

# Purpose:  Change the gold configuration script to only warn about
#            unsupported targets.  This allows the binutils to be built with
#            BPF support enabled.
# Lifetime: Permanent.
# Patch09: binutils-gold-warn-unsupported.patch

# Purpose:  Enable the creation of .note.gnu.property sections by the GOLD
#            linker for x86 binaries.
# Lifetime: Permanent.
# Patch10: binutils-gold-i386-gnu-property-notes.patch

# Purpose:  Allow the binutils to be configured with any (recent) version of
#            autoconf.
# Lifetime: Fixed in 2.44 (maybe ?)
Patch11: binutils-autoconf-version.patch

# Purpose:  Stop libtool from inserting useless runpaths into binaries.
# Lifetime: Who knows.
Patch12: binutils-libtool-no-rpath.patch

# Purpose:  Stop an abort when using dwp to process a file with no dwo links.
# Lifetime: Fixed in 2.44 (maybe)
# Patch13: binutils-gold-empty-dwp.patch

# Purpose:  Fix binutils testsuite failures.
# Lifetime: Permanent, but varies with each rebase.
Patch14: binutils-testsuite-fixes.patch

# Purpose:  Fix binutils testsuite failures for the RISCV-64 target.
# Lifetime: Permanent, but varies with each rebase.
Patch15: binutils-riscv-testsuite-fixes.patch

# Purpose:  Make the GOLD linker ignore the "-z pack-relative-relocs" command line option.
# Lifetime: Fixed in 2.44 (maybe)
# Patch16: binutils-gold-pack-relative-relocs.patch

# Purpose:  Let the gold lihnker ignore --error-execstack and --error-rwx-segments.
# Lifetime: Fixed in 2.44 (maybe)
# Patch17: binutils-gold-ignore-execstack-error.patch

# Purpose:  Fix the ar test of non-deterministic archives.
# Lifetime: Fixed in 2.44
Patch18: binutils-fix-ar-test.patch

# Purpose:  Fix a seg fault in the AArch64 linker when building u-boot.
# Lifetime: Fixed in 2.45
Patch19: binutils-aarch64-small-plt0.patch

# Backport fix for CVE-2025-11494
# https://sourceware.org/cgit/binutils-gdb/patch/?id=b6ac5a8a5b82f0ae6a4642c8d7149b325f4cc60a
Patch20:         CVE-2025-11494.patch
# Backport fix for CVE-2025-11495
# https://sourceware.org/cgit/binutils-gdb/patch/?id=6b21c8b2ecfef5c95142cbc2c32f185cb1c26ab0
Patch21:         CVE-2025-11495.patch
# Backport fix for CVE-2025-11082
# https://sourceware.org/cgit/binutils-gdb/patch/?id=ea1a0737c7692737a644af0486b71e4a392cbca8
Patch22:         CVE-2025-11082.patch
# Backport fix CVE-2025-11081
# https://sourceware.org/cgit/binutils-gdb/patch/?id=f87a66db645caf8cc0e6fc87b0c28c78a38af59b
Patch23:         CVE-2025-11081.patch
# Backport fix for CVE-2025-11083
# https://sourceware.org/cgit/binutils-gdb/patch/?id=9ca499644a21ceb3f946d1c179c38a83be084490
Patch24:         CVE-2025-11083.patch


BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  texinfo
BuildRequires:  zlib-devel
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  ucrt64-filesystem
%if %{run_testsuite}
BuildRequires:  dejagnu
BuildRequires:  sharutils
%endif
Provides:       bundled(libiberty)


%description
Cross compiled binutils (utilities like 'strip', 'as', 'ld') which
understand Windows executables and DLLs.

%package -n mingw-binutils-generic
Summary:        Utilities which are needed for both the Win32 and Win64 toolchains

%description -n mingw-binutils-generic
Utilities (like strip and objdump) which are needed for
both the Win32 and Win64 toolchains

%package -n mingw32-binutils
Summary:        Cross-compiled version of binutils for the Win32 environment
Requires:       mingw-binutils-generic = %{version}-%{release}

# NB: This must be left in.
Requires:       mingw32-filesystem >= 95

%description -n mingw32-binutils
Cross compiled binutils (utilities like 'strip', 'as', 'ld') which
understand Windows executables and DLLs.

%package -n mingw64-binutils
Summary:        Cross-compiled version of binutils for the Win64 environment
Requires:       mingw-binutils-generic = %{version}-%{release}

# NB: This must be left in.
Requires:       mingw64-filesystem >= 95

%description -n mingw64-binutils
Cross compiled binutils (utilities like 'strip', 'as', 'ld') which
understand Windows executables and DLLs.

%package -n ucrt64-binutils
Summary:        Cross-compiled version of binutils for the Win64 environment
Requires:       mingw-binutils-generic = %{version}-%{release}

# NB: This must be left in.
Requires:       ucrt64-filesystem >= 133

%description -n ucrt64-binutils
Cross compiled binutils (utilities like 'strip', 'as', 'ld') which
understand Windows executables and DLLs.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n binutils-%{version}

# See Patch02
sed -i -e 's/%''{release}/%{release}/g' bfd/Makefile{.am,.in}


%build
# We call configure directly rather than via macros, thus if
# we are using LTO, we have to manually fix the broken configure
# scripts
[ %{_lto_cflags}x != x ] && %{_fix_broken_configure_for_lto}


mkdir build_win32
pushd build_win32
CFLAGS="%{optflags}" \
../configure \
  --build=%_build --host=%_host \
  --target=%{mingw32_target} \
  --disable-nls \
  --with-sysroot=%{mingw32_sysroot} \
  --prefix=%{_prefix} \
  --bindir=%{_bindir} \
  --includedir=%{_includedir} \
  --libdir=%{_libdir} \
  --mandir=%{_mandir} \
  --infodir=%{_infodir}

%make_build
popd

mkdir build_win64
pushd build_win64
CFLAGS="%{optflags}" \
../configure \
  --build=%_build --host=%_host \
  --target=%{mingw64_target} \
  --disable-nls \
  --with-sysroot=%{mingw64_sysroot} \
  --prefix=%{_prefix} \
  --bindir=%{_bindir} \
  --includedir=%{_includedir} \
  --libdir=%{_libdir} \
  --mandir=%{_mandir} \
  --infodir=%{_infodir}

%make_build
popd

mkdir build_ucrt64
pushd build_ucrt64
CFLAGS="%{optflags}" \
../configure \
  --build=%_build --host=%_host \
  --target=%{ucrt64_target} \
  --disable-nls \
  --with-sysroot=%{ucrt64_sysroot} \
  --prefix=%{_prefix} \
  --bindir=%{_bindir} \
  --includedir=%{_includedir} \
  --libdir=%{_libdir} \
  --mandir=%{_mandir} \
  --infodir=%{_infodir}

%make_build
popd

# Create multilib versions for the tools strip, objdump nm, and objcopy
mkdir build_multilib
pushd build_multilib
CFLAGS="%{optflags}" \
../configure \
  --build=%_build --host=%_host \
  --target=%{mingw64_target} \
  --enable-targets=%{mingw64_target},%{mingw32_target},%{ucrt64_target} \
  --disable-nls \
  --with-sysroot=%{mingw64_sysroot} \
  --prefix=%{_prefix} \
  --bindir=%{_bindir} \
  --includedir=%{_includedir} \
  --libdir=%{_libdir} \
  --mandir=%{_mandir} \
  --infodir=%{_infodir}

%make_build
popd


%check
%if !%{run_testsuite}
echo ====================TESTSUITE DISABLED=========================
%else
pushd build_win32
  make -k check < /dev/null || :
  echo ====================TESTING WIN32 =========================
  cat {gas/testsuite/gas,ld/ld,binutils/binutils}.sum
  echo ====================TESTING WIN32 END=====================
  for file in {gas/testsuite/gas,ld/ld,binutils/binutils}.{sum,log}
  do
    ln $file binutils-%{mingw32_target}-$(basename $file) || :
  done
  tar cjf binutils-%{mingw32_target}.tar.bz2 binutils-%{mingw32_target}-*.{sum,log}
  uuencode binutils-%{mingw32_target}.tar.bz2 binutils-%{mingw32_target}.tar.bz2
  rm -f binutils-%{mingw32_target}.tar.bz2 binutils-%{mingw32_target}-*.{sum,log}
popd

pushd build_win64
  make -k check < /dev/null || :
  echo ====================TESTING WIN64 =========================
  cat {gas/testsuite/gas,ld/ld,binutils/binutils}.sum
  echo ====================TESTING WIN64 END=====================
  for file in {gas/testsuite/gas,ld/ld,binutils/binutils}.{sum,log}
  do
    ln $file binutils-%{mingw64_target}-$(basename $file) || :
  done
  tar cjf binutils-%{mingw64_target}.tar.bz2 binutils-%{mingw64_target}-*.{sum,log}
  uuencode binutils-%{mingw64_target}.tar.bz2 binutils-%{mingw64_target}.tar.bz2
  rm -f binutils-%{mingw64_target}.tar.bz2 binutils-%{mingw64_target}-*.{sum,log}
popd

pushd build_ucrt64
  make -k check < /dev/null || :
  echo ====================TESTING UCRT64 =========================
  cat {gas/testsuite/gas,ld/ld,binutils/binutils}.sum
  echo ====================TESTING UCRT64 END=====================
  for file in {gas/testsuite/gas,ld/ld,binutils/binutils}.{sum,log}
  do
    ln $file binutils-%{ucrt64_target}-$(basename $file) || :
  done
  tar cjf binutils-%{ucrt64_target}.tar.bz2 binutils-%{ucrt64_target}-*.{sum,log}
  uuencode binutils-%{ucrt64_target}.tar.bz2 binutils-%{ucrt64_target}.tar.bz2
  rm -f binutils-%{ucrt64_target}.tar.bz2 binutils-%{ucrt64_target}-*.{sum,log}
popd
%endif


%install
%mingw_make_install
make -C build_multilib DESTDIR=%{buildroot}/multilib install

# These files conflict with ordinary binutils.
rm -rf %{buildroot}%{_infodir}
rm -f %{buildroot}%{_libdir}/libiberty*
rm -f %{buildroot}%{_libdir}/bfd-plugins/libdep.so

# Keep the multilib versions of the strip, objdump and objcopy commands
# We need these for the RPM integration as these tools must be able to
# both process win32 and win64 binaries
mv %{buildroot}/multilib%{_bindir}/%{mingw64_strip} %{buildroot}%{_bindir}/%{mingw_strip}
mv %{buildroot}/multilib%{_bindir}/%{mingw64_objdump} %{buildroot}%{_bindir}/%{mingw_objdump}
mv %{buildroot}/multilib%{_bindir}/%{mingw64_objcopy} %{buildroot}%{_bindir}/%{mingw_objcopy}
mv %{buildroot}/multilib%{_bindir}/%{mingw64_nm} %{buildroot}%{_bindir}/%{mingw_nm}
rm -rf %{buildroot}/multilib

# Drop man pages, they are a duplicate of those of the native tools
rm -rf %{buildroot}%{_mandir}/man1/*


%files -n mingw-binutils-generic
%license COPYING
%{_bindir}/%{mingw_strip}
%{_bindir}/%{mingw_objdump}
%{_bindir}/%{mingw_objcopy}
%{_bindir}/%{mingw_nm}

%files -n mingw32-binutils
%{_bindir}/%{mingw32_target}-addr2line
%{_bindir}/%{mingw32_target}-ar
%{_bindir}/%{mingw32_target}-as
%{_bindir}/%{mingw32_target}-c++filt
%{_bindir}/%{mingw32_target}-dlltool
%{_bindir}/%{mingw32_target}-dllwrap
%{_bindir}/%{mingw32_target}-elfedit
%{_bindir}/%{mingw32_target}-gprof
%{_bindir}/%{mingw32_target}-ld
%{_bindir}/%{mingw32_target}-ld.bfd
%{_bindir}/%{mingw32_target}-nm
%{_bindir}/%{mingw32_target}-objcopy
%{_bindir}/%{mingw32_target}-objdump
%{_bindir}/%{mingw32_target}-ranlib
%{_bindir}/%{mingw32_target}-readelf
%{_bindir}/%{mingw32_target}-size
%{_bindir}/%{mingw32_target}-strings
%{_bindir}/%{mingw32_target}-strip
%{_bindir}/%{mingw32_target}-windmc
%{_bindir}/%{mingw32_target}-windres
%{_prefix}/%{mingw32_target}/bin/ar
%{_prefix}/%{mingw32_target}/bin/as
%{_prefix}/%{mingw32_target}/bin/dlltool
%{_prefix}/%{mingw32_target}/bin/ld
%{_prefix}/%{mingw32_target}/bin/ld.bfd
%{_prefix}/%{mingw32_target}/bin/nm
%{_prefix}/%{mingw32_target}/bin/objcopy
%{_prefix}/%{mingw32_target}/bin/objdump
%{_prefix}/%{mingw32_target}/bin/ranlib
%{_prefix}/%{mingw32_target}/bin/readelf
%{_prefix}/%{mingw32_target}/bin/strip
%{_prefix}/%{mingw32_target}/lib/ldscripts

%files -n mingw64-binutils
%{_bindir}/%{mingw64_target}-addr2line
%{_bindir}/%{mingw64_target}-ar
%{_bindir}/%{mingw64_target}-as
%{_bindir}/%{mingw64_target}-c++filt
%{_bindir}/%{mingw64_target}-dlltool
%{_bindir}/%{mingw64_target}-dllwrap
%{_bindir}/%{mingw64_target}-elfedit
%{_bindir}/%{mingw64_target}-gprof
%{_bindir}/%{mingw64_target}-ld
%{_bindir}/%{mingw64_target}-ld.bfd
%{_bindir}/%{mingw64_target}-nm
%{_bindir}/%{mingw64_target}-objcopy
%{_bindir}/%{mingw64_target}-objdump
%{_bindir}/%{mingw64_target}-ranlib
%{_bindir}/%{mingw64_target}-readelf
%{_bindir}/%{mingw64_target}-size
%{_bindir}/%{mingw64_target}-strings
%{_bindir}/%{mingw64_target}-strip
%{_bindir}/%{mingw64_target}-windmc
%{_bindir}/%{mingw64_target}-windres
%{_prefix}/%{mingw64_target}/bin/ar
%{_prefix}/%{mingw64_target}/bin/as
%{_prefix}/%{mingw64_target}/bin/dlltool
%{_prefix}/%{mingw64_target}/bin/ld
%{_prefix}/%{mingw64_target}/bin/ld.bfd
%{_prefix}/%{mingw64_target}/bin/nm
%{_prefix}/%{mingw64_target}/bin/objcopy
%{_prefix}/%{mingw64_target}/bin/objdump
%{_prefix}/%{mingw64_target}/bin/ranlib
%{_prefix}/%{mingw64_target}/bin/readelf
%{_prefix}/%{mingw64_target}/bin/strip
%{_prefix}/%{mingw64_target}/lib/ldscripts

%files -n ucrt64-binutils
%{_bindir}/%{ucrt64_target}-addr2line
%{_bindir}/%{ucrt64_target}-ar
%{_bindir}/%{ucrt64_target}-as
%{_bindir}/%{ucrt64_target}-c++filt
%{_bindir}/%{ucrt64_target}-dlltool
%{_bindir}/%{ucrt64_target}-dllwrap
%{_bindir}/%{ucrt64_target}-elfedit
%{_bindir}/%{ucrt64_target}-gprof
%{_bindir}/%{ucrt64_target}-ld
%{_bindir}/%{ucrt64_target}-ld.bfd
%{_bindir}/%{ucrt64_target}-nm
%{_bindir}/%{ucrt64_target}-objcopy
%{_bindir}/%{ucrt64_target}-objdump
%{_bindir}/%{ucrt64_target}-ranlib
%{_bindir}/%{ucrt64_target}-readelf
%{_bindir}/%{ucrt64_target}-size
%{_bindir}/%{ucrt64_target}-strings
%{_bindir}/%{ucrt64_target}-strip
%{_bindir}/%{ucrt64_target}-windmc
%{_bindir}/%{ucrt64_target}-windres
%{_prefix}/%{ucrt64_target}/bin/ar
%{_prefix}/%{ucrt64_target}/bin/as
%{_prefix}/%{ucrt64_target}/bin/dlltool
%{_prefix}/%{ucrt64_target}/bin/ld
%{_prefix}/%{ucrt64_target}/bin/ld.bfd
%{_prefix}/%{ucrt64_target}/bin/nm
%{_prefix}/%{ucrt64_target}/bin/objcopy
%{_prefix}/%{ucrt64_target}/bin/objdump
%{_prefix}/%{ucrt64_target}/bin/ranlib
%{_prefix}/%{ucrt64_target}/bin/readelf
%{_prefix}/%{ucrt64_target}/bin/strip
%{_prefix}/%{ucrt64_target}/lib/ldscripts


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.45.1-2
- Prepare for Oreon 11 (RP1)
