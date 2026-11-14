# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d75a94f4d73e7a4086f7513e67e439e8fcdcbb726ffe63f4661744e6256b2cf2

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global run_testsuite 1
%global mingw_build_ucrt64 1
%define enable_new_dtags 0

Name:           mingw-binutils
Version:        2.46.0
Release:        1%{?dist}
Summary:        Cross-compiled version of binutils for Win32 and Win64 environments

License:        GPL-3.0-or-later AND (GPL-3.0-or-later WITH Bison-exception-2.2) AND (LGPL-2.0-or-later WITH GCC-exception-2.0) AND BSD-3-Clause AND GFDL-1.3-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.0-or-later

URL:            https://www.gnu.org/software/binutils/
Source0:        https://mirror.cs.odu.edu/gnu/binutils/binutils-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/binutils/binutils-%{version}.tar.xz.sig
Source2:        binutils-key.asc

Patch02: binutils-version.patch
Patch03: binutils-export-demangle.h.patch
Patch04: binutils-no-config-h-check.patch
Patch05: binutils-revert-PLT-elision.patch
Patch06: binutils-2.27-aarch64-ifunc.patch
Patch07: binutils-do-not-link-with-static-libstdc++.patch
Patch08: binutils-autoconf-version.patch
Patch09: binutils-libtool-no-rpath.patch
Patch10: binutils-testsuite-fixes.patch
Patch11: binutils-riscv-testsuite-fixes.patch
Patch12: binutils-fix-ar-test.patch
Patch13: binutils-aarch64-small-plt0.patch
Patch14: binutils-ld-default-z-text.patch
Patch15: binutils-remove-ld-protected-func-2-test.patch
Patch16: binutils-suppress-ld-align-tests.patch

BuildRequires:  oreon-rpm-macros
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  texinfo
BuildRequires:  gnupg2
BuildRequires:  zlib-devel
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  ucrt64-filesystem
%if %{run_testsuite}
BuildRequires:  dejagnu
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
%oreon_sha256

%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1 -n binutils-%{version}

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
  --disable-werror \
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
  --disable-werror \
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
  --disable-werror \
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
  --disable-werror \
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
%if %{run_testsuite}
pushd build_win32
  make check < /dev/null
popd

pushd build_win64
  make check < /dev/null
popd

pushd build_ucrt64
  make check < /dev/null
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
%{_prefix}/%{mingw32_target}/bin/windres
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
%{_prefix}/%{mingw64_target}/bin/windres
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
%{_prefix}/%{ucrt64_target}/bin/windres
%{_prefix}/%{ucrt64_target}/lib/ldscripts

%changelog
%autochangelog
