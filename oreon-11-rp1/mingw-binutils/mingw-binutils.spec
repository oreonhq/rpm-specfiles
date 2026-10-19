%global source0_hash 5fe101e6fe9d18fdec95962d81ed670fdee5f37e3f48f0bef87bddf862513aa5
%global run_testsuite 1
%global mingw_build_ucrt64 1
%define enable_new_dtags 0
Name:           mingw-binutils
Version:        2.45.1
Release:        2%{?dist}
Summary:        Cross-compiled version of binutils for Win32 and Win64 environments
License:        GPL-3.0-or-later AND (GPL-3.0-or-later WITH Bison-exception-2.2) AND (LGPL-2.0-or-later WITH GCC-exception-2.0) AND BSD-3-Clause AND GFDL-1.3-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.0-or-later
URL:            http://www.gnu.org/software/binutils/
Source0:        https://sourceware.org/pub/binutils/releases/binutils-%{version}.tar.xz
Patch02: binutils-version.patch
Patch03: binutils-export-demangle.h.patch
Patch04: binutils-no-config-h-check.patch
Patch05: binutils-revert-PLT-elision.patch
Patch06: binutils-2.27-aarch64-ifunc.patch
Patch07: binutils-do-not-link-with-static-libstdc++.patch
Patch11: binutils-autoconf-version.patch
Patch12: binutils-libtool-no-rpath.patch
Patch14: binutils-testsuite-fixes.patch
Patch15: binutils-riscv-testsuite-fixes.patch
Patch18: binutils-fix-ar-test.patch
Patch19: binutils-aarch64-small-plt0.patch
Patch20:         CVE-2025-11494.patch
Patch21:         CVE-2025-11495.patch
Patch22:         CVE-2025-11082.patch
Patch23:         CVE-2025-11081.patch
Patch24:         CVE-2025-11083.patch
Provides:       bundled(libiberty)
# oreon:deps
BuildRequires:  bison
BuildRequires:  dejagnu
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  sharutils
BuildRequires:  texinfo
BuildRequires:  ucrt64-filesystem
BuildRequires:  zlib-devel
# /oreon:deps
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
Requires:       mingw32-filesystem >= 95
%description -n mingw32-binutils
Cross compiled binutils (utilities like 'strip', 'as', 'ld') which
understand Windows executables and DLLs.

%package -n mingw64-binutils
Summary:        Cross-compiled version of binutils for the Win64 environment
Requires:       mingw-binutils-generic = %{version}-%{release}
Requires:       mingw64-filesystem >= 95
%description -n mingw64-binutils
Cross compiled binutils (utilities like 'strip', 'as', 'ld') which
understand Windows executables and DLLs.

%package -n ucrt64-binutils
Summary:        Cross-compiled version of binutils for the Win64 environment
Requires:       mingw-binutils-generic = %{version}-%{release}
Requires:       ucrt64-filesystem >= 133
%description -n ucrt64-binutils
Cross compiled binutils (utilities like 'strip', 'as', 'ld') which
understand Windows executables and DLLs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n binutils-%{version}

# See Patch02
sed -i -e 's/%''{release}/%{release}/g' bfd/Makefile{.am,.in}

%build

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
rm -rf %{buildroot}%{_infodir}
rm -f %{buildroot}%{_libdir}/libiberty*
rm -f %{buildroot}%{_libdir}/bfd-plugins/libdep.so
mv %{buildroot}/multilib%{_bindir}/%{mingw64_strip} %{buildroot}%{_bindir}/%{mingw_strip}
mv %{buildroot}/multilib%{_bindir}/%{mingw64_objdump} %{buildroot}%{_bindir}/%{mingw_objdump}
mv %{buildroot}/multilib%{_bindir}/%{mingw64_objcopy} %{buildroot}%{_bindir}/%{mingw_objcopy}
mv %{buildroot}/multilib%{_bindir}/%{mingw64_nm} %{buildroot}%{_bindir}/%{mingw_nm}
rm -rf %{buildroot}/multilib
rm -rf %{buildroot}%{_mandir}/man1/*
%oreon_autofiles mingw-binutils-generic usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-binutils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-binutils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ucrt64-binutils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw-binutils-generic -f %{oreon_filedir}/mingw-binutils-generic.list
%files -n mingw32-binutils -f %{oreon_filedir}/mingw32-binutils.list
%files -n mingw64-binutils -f %{oreon_filedir}/mingw64-binutils.list
%files -n ucrt64-binutils -f %{oreon_filedir}/ucrt64-binutils.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.45.1-2
- Prepare for Oreon 11 (RP1)
