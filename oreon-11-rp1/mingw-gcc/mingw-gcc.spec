%global source0_hash none

%global mingw_build_ucrt64 1
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

# Causes build failures
%undefine _auto_set_build_flags

# NOTE See mingw-filesystem/README.md for the build steps!
%global bootstrap 0

%global build_isl 0

%global isl_version 0.16.1

# Run the testsuite
%global enable_tests 0

%global DATE 20260502
%global gcc_version 16.1.1
%global gcc_major 16

Name:           mingw-gcc
Version:        %{gcc_version}
Release:        1%{?dist}
Summary:        MinGW Windows cross-compiler (GCC) for C

# Sync with native 'gcc' package
License: GPL-3.0-or-later AND LGPL-3.0-or-later AND (GPL-3.0-or-later WITH GCC-exception-3.1) AND (GPL-3.0-or-later WITH Texinfo-exception) AND (LGPL-2.1-or-later WITH GCC-exception-2.0) AND (GPL-2.0-or-later WITH GCC-exception-2.0) AND (GPL-2.0-or-later WITH GNU-compiler-exception) AND BSL-1.0 AND GFDL-1.3-or-later AND Linux-man-pages-copyleft-2-para AND SunPro AND BSD-1-Clause AND BSD-2-Clause AND BSD-2-Clause-Views AND BSD-3-Clause AND BSD-4-Clause AND BSD-Source-Code AND Zlib AND MIT AND Apache-2.0 AND (Apache-2.0 WITH LLVM-Exception) AND ZPL-2.1 AND ISC AND LicenseRef-Public-Domain AND HP-1986 AND curl AND Martin-Birgmeier AND HPND-Markus-Kuhn AND dtoa AND SMLNJ AND AMD-newlib AND OAR AND HPND-merchantability-variant AND HPND-Intel
URL:            http://gcc.gnu.org

%global srcdir gcc-%{gcc_major}-%{DATE}
Source0:        https://gcc.gnu.org/pub/gcc/snapshots/%{gcc_major}-%{DATE}/%{srcdir}.tar.xz

# See https://sourceforge.net/p/mingw-w64/mailman/mingw-w64-public/thread/8fd2fb03-9b8a-07e1-e162-0bb48bcc3984%40gmail.com/#msg37200751
Patch0:        0020-libgomp-Don-t-hard-code-MS-printf-attributes.patch
# Add missing stdlib.h include
Patch1:        mingw-gcc_include-stdlib.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  git
BuildRequires:  curl
BuildRequires:  xz
BuildRequires:  texinfo
BuildRequires:  mingw32-filesystem >= 133
BuildRequires:  mingw64-filesystem >= 133
BuildRequires:  ucrt64-filesystem >= 133
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  ucrt64-binutils
BuildRequires:  mingw32-headers
BuildRequires:  mingw64-headers
BuildRequires:  ucrt64-headers
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel
BuildRequires:  libmpc-devel
BuildRequires:  libgomp
BuildRequires:  flex
BuildRequires:  zlib-devel
%if %{build_isl}
BuildRequires: isl = %{isl_version}
BuildRequires: isl-devel = %{isl_version}
%endif
%if 0%{bootstrap} == 0
BuildRequires:  mingw32-crt
BuildRequires:  mingw64-crt
BuildRequires:  ucrt64-crt
BuildRequires:  mingw32-winpthreads
BuildRequires:  mingw64-winpthreads
BuildRequires:  ucrt64-winpthreads
%if 0%{enable_tests}
BuildRequires:  wine
BuildRequires:  autogen
BuildRequires:  dejagnu
BuildRequires:  sharutils
%endif
%endif
Provides: bundled(libiberty)

%description
MinGW Windows cross-compiler (GCC) for C.

###############################################################################
# Mingw32
###############################################################################
%package -n mingw32-gcc
Summary:        MinGW Windows cross-compiler (GCC) for C for the win32 target
Requires:       mingw32-binutils
Requires:       mingw32-headers
Requires:       mingw32-cpp
%if 0%{bootstrap} == 0
Requires:       mingw32-crt
Requires:       mingw32-libgcc
Requires:       mingw32-winpthreads-static
%endif

%description -n mingw32-gcc
MinGW Windows cross-compiler (GCC) for C for the win32 target.


%package -n mingw32-gcc-plugin-devel
Summary:	Support for compiling plugins for MinGW GCC for the win32 target
Requires:	mingw32-gcc = %{version}-%{release}
Requires:	gmp-devel >= 4.1.2-8, mpfr-devel >= 3.1.0, libmpc-devel >= 0.8.1

%description -n mingw32-gcc-plugin-devel
This package contains header files and other support files
for compiling GCC plugins.  The GCC plugin ABI is currently
not stable, so plugins must be rebuilt any time GCC is updated.


%if 0%{bootstrap} == 0
%package -n mingw32-libgcc
Summary:        MinGW Windows GCC runtime libraries for C for the win32 target

%description -n mingw32-libgcc
MinGW Windows GCC runtime libraries for C for the win32 target.


%package -n mingw32-libstdc++
Summary:        MinGW Windows GCC runtime libraries for C++ for the win32 target

%description -n mingw32-libstdc++
MinGW Windows GCC runtime libraries for C++ for the win32 target.


%package -n mingw32-libgomp
Summary:        GCC OpenMP v3.0 shared support library for the win32 target
Requires:       mingw32-gcc = %{version}-%{release}

%description -n mingw32-libgomp
This package contains GCC shared support library which is
needed for OpenMP v3.0 support for the win32 target.
%endif


%package -n mingw32-cpp
Summary:        MinGW Windows cross-C Preprocessor for the win32 target
# NB: Explicit mingw32-filesystem dependency is REQUIRED here.
Requires:       mingw32-filesystem >= 133

%description -n mingw32-cpp
MinGW Windows cross-C Preprocessor for the win32 target.


%package -n mingw32-gcc-c++
Summary:        MinGW Windows cross-compiler for C++ for the win32 target
Requires:       mingw32-gcc = %{version}-%{release}
%if 0%{bootstrap} == 0
Requires:       mingw32-libstdc++ = %{version}-%{release}
%endif

%description -n mingw32-gcc-c++
MinGW Windows cross-compiler for C++ for the win32 target.


%package -n mingw32-gcc-objc
Summary:        MinGW Windows cross-compiler support for Objective C for the win32 target
Requires:       mingw32-gcc = %{version}-%{release}

%description -n mingw32-gcc-objc
MinGW Windows cross-compiler support for Objective C for the win32 target.


%package -n mingw32-gcc-objc++
Summary:        MinGW Windows cross-compiler support for Objective C++ for the win32 target
Requires:       mingw32-gcc-c++ = %{version}-%{release}
Requires:       mingw32-gcc-objc = %{version}-%{release}

%description -n mingw32-gcc-objc++
MinGW Windows cross-compiler support for Objective C++ for the win32 target.


%package -n mingw32-gcc-gfortran
Summary:        MinGW Windows cross-compiler for FORTRAN for the win32 target
Requires:       mingw32-gcc = %{version}-%{release}

%description -n mingw32-gcc-gfortran
MinGW Windows cross-compiler for FORTRAN for the win32 target.


###############################################################################
# Mingw64
###############################################################################
%package -n mingw64-gcc
Summary:        MinGW Windows cross-compiler (GCC) for C for the win64 target
Requires:       mingw64-binutils
Requires:       mingw64-headers
Requires:       mingw64-cpp
%if 0%{bootstrap} == 0
Requires:       mingw64-crt
Requires:       mingw64-libgcc
Requires:       mingw64-winpthreads-static
%endif

%description -n mingw64-gcc
MinGW Windows cross-compiler (GCC) for C for the win64 target.


%package -n mingw64-gcc-plugin-devel
Summary:	Support for compiling plugins for MinGW GCC for the win64 target
Requires:	mingw64-gcc = %{version}-%{release}
Requires:	gmp-devel >= 4.1.2-8, mpfr-devel >= 3.1.0, libmpc-devel >= 0.8.1

%description -n mingw64-gcc-plugin-devel
This package contains header files and other support files
for compiling GCC plugins.  The GCC plugin ABI is currently
not stable, so plugins must be rebuilt any time GCC is updated.


%if 0%{bootstrap} == 0
%package -n mingw64-libgcc
Summary:        MinGW Windows GCC runtime libraries for C for the win64 target

%description -n mingw64-libgcc
MinGW Windows GCC runtime libraries for C for the win64 target.


%package -n mingw64-libstdc++
Summary:        MinGW Windows GCC runtime libraries for C++ for the win64 target

%description -n mingw64-libstdc++
MinGW Windows GCC runtime libraries for C++ for the win64 target.


%package -n mingw64-libgomp
Summary:        GCC OpenMP v3.0 shared support library for the win64 target
Requires:       mingw64-gcc = %{version}-%{release}

%description -n mingw64-libgomp
This package contains GCC shared support library which is
needed for OpenMP v3.0 support for the win32 target.
%endif


%package -n mingw64-cpp
Summary:        MinGW Windows cross-C Preprocessor for the win64 target.
# NB: Explicit mingw64-filesystem dependency is REQUIRED here.
Requires:       mingw64-filesystem >= 133

%description -n mingw64-cpp
MinGW Windows cross-C Preprocessor for the win64 target


%package -n mingw64-gcc-c++
Summary:        MinGW Windows cross-compiler for C++ for the win64 target
Requires:       mingw64-gcc = %{version}-%{release}
%if 0%{bootstrap} == 0
Requires:       mingw64-libstdc++ = %{version}-%{release}
%endif

%description -n mingw64-gcc-c++
MinGW Windows cross-compiler for C++ for the win64 target.


%package -n mingw64-gcc-objc
Summary:        MinGW Windows cross-compiler support for Objective C for the win64 target
Requires:       mingw64-gcc = %{version}-%{release}

%description -n mingw64-gcc-objc
MinGW Windows cross-compiler support for Objective C for the win64 target.


%package -n mingw64-gcc-objc++
Summary:        MinGW Windows cross-compiler support for Objective C++ for the win64 target
Requires:       mingw64-gcc-c++ = %{version}-%{release}
Requires:       mingw64-gcc-objc = %{version}-%{release}

%description -n mingw64-gcc-objc++
MinGW Windows cross-compiler support for Objective C++ for the win64 target.


%package -n mingw64-gcc-gfortran
Summary:        MinGW Windows cross-compiler for FORTRAN for the win64 target
Requires:       mingw64-gcc = %{version}-%{release}

%description -n mingw64-gcc-gfortran
MinGW Windows cross-compiler for FORTRAN for the win64 target.


###############################################################################
# UCRT64
###############################################################################
%package -n ucrt64-gcc
Summary:        MinGW Windows cross-compiler (GCC) for C for the win64 target
Requires:       ucrt64-binutils
Requires:       ucrt64-headers
Requires:       ucrt64-cpp
%if 0%{bootstrap} == 0
Requires:       ucrt64-crt
Requires:       ucrt64-libgcc
Requires:       ucrt64-winpthreads-static
%endif


%description -n ucrt64-gcc
MinGW Windows cross-compiler (GCC) for C for the win64 target.


%package -n ucrt64-gcc-plugin-devel
Summary:	Support for compiling plugins for MinGW GCC for the win64 target
Requires:	ucrt64-gcc = %{version}-%{release}
Requires:	gmp-devel >= 4.1.2-8, mpfr-devel >= 3.1.0, libmpc-devel >= 0.8.1

%description -n ucrt64-gcc-plugin-devel
This package contains header files and other support files
for compiling GCC plugins.  The GCC plugin ABI is currently
not stable, so plugins must be rebuilt any time GCC is updated.


%if 0%{bootstrap} == 0
%package -n ucrt64-libgcc
Summary:        MinGW Windows GCC runtime libraries for C for the win64 target

%description -n ucrt64-libgcc
MinGW Windows GCC runtime libraries for C for the win64 target.


%package -n ucrt64-libstdc++
Summary:        MinGW Windows GCC runtime libraries for C++ for the win64 target

%description -n ucrt64-libstdc++
MinGW Windows GCC runtime libraries for C++ for the win64 target.


%package -n ucrt64-libgomp
Summary:        GCC OpenMP v3.0 shared support library for the win64 target
Requires:       ucrt64-gcc = %{version}-%{release}

%description -n ucrt64-libgomp
This package contains GCC shared support library which is
needed for OpenMP v3.0 support for the win32 target.
%endif


%package -n ucrt64-cpp
Summary:        MinGW Windows cross-C Preprocessor for the win64 target.
# NB: Explicit ucrt64-filesystem dependency is REQUIRED here.
Requires:       ucrt64-filesystem >= 133

%description -n ucrt64-cpp
MinGW Windows cross-C Preprocessor for the win64 target


%package -n ucrt64-gcc-c++
Summary:        MinGW Windows cross-compiler for C++ for the win64 target
Requires:       ucrt64-gcc = %{version}-%{release}
%if 0%{bootstrap} == 0
Requires:       ucrt64-libstdc++ = %{version}-%{release}
%endif

%description -n ucrt64-gcc-c++
MinGW Windows cross-compiler for C++ for the win64 target.


%package -n ucrt64-gcc-objc
Summary:        MinGW Windows cross-compiler support for Objective C for the win64 target
Requires:       ucrt64-gcc = %{version}-%{release}

%description -n ucrt64-gcc-objc
MinGW Windows cross-compiler support for Objective C for the win64 target.


%package -n ucrt64-gcc-objc++
Summary:        MinGW Windows cross-compiler support for Objective C++ for the win64 target
Requires:       ucrt64-gcc-c++ = %{version}-%{release}
Requires:       ucrt64-gcc-objc = %{version}-%{release}

%description -n ucrt64-gcc-objc++
MinGW Windows cross-compiler support for Objective C++ for the win64 target.


%package -n ucrt64-gcc-gfortran
Summary:        MinGW Windows cross-compiler for FORTRAN for the win64 target
Requires:       ucrt64-gcc = %{version}-%{release}

%description -n ucrt64-gcc-gfortran
MinGW Windows cross-compiler for FORTRAN for the win64 target.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{srcdir}
echo 'Fedora MinGW %{version}-%{release}' > gcc/DEV-PHASE

%build
# Default configure arguments
configure_args="\
    --prefix=%{_prefix} \
    --bindir=%{_bindir} \
    --includedir=%{_includedir} \
    --mandir=%{_mandir} \
    --infodir=%{_infodir} \
    --datadir=%{_datadir} \
    --build=%_build --host=%_host \
    --with-gnu-as --with-gnu-ld --verbose \
    --without-newlib \
    --disable-multilib \
    --disable-libcc1 \
    --with-system-zlib \
    --disable-nls --without-included-gettext \
    --disable-win32-registry \
    --enable-languages="c,c++,objc,obj-c++,fortran" \
    --with-bugurl=http://bugzilla.redhat.com/bugzilla \
    --enable-threads=posix"

# PPL/CLOOG optimalisations are only available on Fedora
%if %{build_isl}
configure_args="$configure_args --with-isl"
%else
configure_args="$configure_args --without-isl"
%endif

# When bootstrapping, disable LTO support as it causes errors while building any binary
# $ i686-w64-mingw32-gcc -o conftest    conftest.c  >&5
# i686-w64-mingw32-gcc: fatal error: -fuse-linker-plugin, but liblto_plugin.so not found
%if 0%{bootstrap}
configure_args="$configure_args --disable-lto"
%else
configure_args="$configure_args --enable-libgomp"
%endif

# The %%configure macro can't be used for out of source builds
# without overriding other variables and causes unwanted side
# effects so make sure the right compiler flags are used
export CC="%{__cc} ${RPM_OPT_FLAGS}"

# Win32
mkdir build_win32
pushd build_win32
    ../configure $configure_args --target=%{mingw32_target} --with-sysroot=%{mingw32_sysroot} --with-gxx-include-dir=%{mingw32_includedir}/c++ --disable-sjlj-exceptions --with-dwarf2
popd

# Win64
mkdir build_win64
pushd build_win64
    ../configure $configure_args --target=%{mingw64_target} --with-sysroot=%{mingw64_sysroot} --with-gxx-include-dir=%{mingw64_includedir}/c++
popd

# ucrt64
mkdir build_ucrt64
pushd build_ucrt64
    ../configure $configure_args --target=%{ucrt64_target} --with-sysroot=%{ucrt64_sysroot} --with-gxx-include-dir=%{ucrt64_includedir}/c++
popd

# If we're bootstrapping, only build the GCC core
%if 0%{bootstrap}
%mingw_make_build all-gcc
%else
%mingw_make_build all
%endif


%if 0%{enable_tests}
%check
# Win32
# Create a seperate wine prefix
export WINEPREFIX=/tmp/.wine_gcc_testsuite
rm -rf $WINEPREFIX
mkdir $WINEPREFIX

# The command below will fail, but that's intentional
# We only have to call a wine binary which triggers
# the generation and population of a wine prefix
winecfg || :

# Copy the GCC DLL's inside the wine prefix
SYSTEM32_DIR=$WINEPREFIX/drive_c/windows/syswow64
if [ ! -d $SYSTEM32_DIR ] ; then
    SYSTEM32_DIR=$WINEPREFIX/drive_c/windows/system32
fi
cp build_win32/i686-w64-mingw32/libquadmath/.libs/libquadmath-0.dll $SYSTEM32_DIR
cp build_win32/i686-w64-mingw32/libgfortran/.libs/libgfortran-5.dll $SYSTEM32_DIR
cp build_win32/i686-w64-mingw32/libobjc/.libs/libobjc-4.dll $SYSTEM32_DIR
cp build_win32/i686-w64-mingw32/libssp/.libs/libssp-0.dll $SYSTEM32_DIR
cp build_win32/i686-w64-mingw32/libstdc++-v3/src/.libs/libstdc++-6.dll $SYSTEM32_DIR
cp build_win32/i686-w64-mingw32/libgcc/shlib/libgcc_s_dw2-1.dll $SYSTEM32_DIR
%if 0%{bootstrap} == 0
cp %{mingw32_bindir}/libwinpthread-1.dll $SYSTEM32_DIR
cp build_win32/i686-w64-mingw32/libgomp/.libs/libgomp-1.dll $SYSTEM32_DIR
%endif

SYSTEM64_DIR=$WINEPREFIX/drive_c/windows/system32
cp build_win64/x86_64-w64-mingw32/libquadmath/.libs/libquadmath-0.dll $SYSTEM64_DIR
cp build_win64/x86_64-w64-mingw32/libgfortran/.libs/libgfortran-5.dll $SYSTEM64_DIR
cp build_win64/x86_64-w64-mingw32/libobjc/.libs/libobjc-4.dll $SYSTEM64_DIR
cp build_win64/x86_64-w64-mingw32/libssp/.libs/libssp-0.dll $SYSTEM64_DIR
cp build_win64/x86_64-w64-mingw32/libstdc++-v3/src/.libs/libstdc++-6.dll $SYSTEM64_DIR
cp build_win64/x86_64-w64-mingw32/libgcc/shlib/libgcc_s_seh-1.dll $SYSTEM64_DIR
%if 0%{bootstrap} == 0
cp %{mingw64_bindir}/libwinpthread-1.dll $SYSTEM64_DIR
cp build_win64/x86_64-w64-mingw32/libgomp/.libs/libgomp-1.dll $SYSTEM64_DIR
%endif

# According to Kai Tietz (of the mingw-w64 project) it's recommended
# to set the environment variable GCOV_PREFIX_STRIP
export GCOV_PREFIX_STRIP=1000

# Run the testsuite
# Code taken from the native Fedora GCC package to collect testsuite results
pushd build_win32
    make -k check %{?_smp_mflags} || :
    echo ====================TESTING WIN32=========================
    ( LC_ALL=C ../contrib/test_summary || : ) 2>&1 | sed -n '/^cat.*EOF/,/^EOF/{/^cat.*EOF/d;/^EOF/d;/^LAST_UPDATED:/d;p;}'
    echo ====================TESTING WIN32 END=====================
    mkdir testlogs-%{mingw32_target}-%{version}-%{release}
    for i in `find . -name \*.log | grep -F testsuite/ | grep -v 'config.log\|acats.*/tests/'`; do
        ln $i testlogs-%{mingw32_target}-%{version}-%{release}/ || :
    done
    tar cf - testlogs-%{mingw32_target}-%{version}-%{release} | bzip2 -9c \
        | uuencode testlogs-%{mingw32_target}.tar.bz2 || :
    rm -rf testlogs-%{mingw32_target}-%{version}-%{release}
popd

pushd build_win64
    make -k check %{?_smp_mflags} || :
    echo ====================TESTING WIN64=========================
    ( LC_ALL=C ../contrib/test_summary || : ) 2>&1 | sed -n '/^cat.*EOF/,/^EOF/{/^cat.*EOF/d;/^EOF/d;/^LAST_UPDATED:/d;p;}'
    echo ====================TESTING WIN64 END=====================
    mkdir testlogs-%{mingw64_target}-%{version}-%{release}
    for i in `find . -name \*.log | grep -F testsuite/ | grep -v 'config.log\|acats.*/tests/'`; do
        ln $i testlogs-%{mingw64_target}-%{version}-%{release}/ || :
    done
    tar cf - testlogs-%{mingw64_target}-%{version}-%{release} | bzip2 -9c \
        | uuencode testlogs-%{mingw64_target}.tar.bz2 || :
    rm -rf testlogs-%{mingw64_target}-%{version}-%{release}
popd

%endif


%install
%if 0%{bootstrap}
%mingw_make DESTDIR=%{buildroot} install-gcc
%else
%mingw_make_install
%endif

# These files conflict with existing installed files.
rm -rf %{buildroot}%{_infodir}
rm -f %{buildroot}%{_libdir}/libiberty*
rm -f %{buildroot}%{_mandir}/man7/*
rm -rf %{buildroot}%{_datadir}/gcc-%{version}/python

%if 0%{bootstrap} == 0
# Move the DLL's manually to the correct location
mkdir -p %{buildroot}%{mingw32_bindir}
mv    %{buildroot}%{_prefix}/%{mingw32_target}/lib/libatomic-1.dll \
      %{buildroot}%{_prefix}/%{mingw32_target}/lib/libgcc_s_dw2-1.dll \
      %{buildroot}%{_prefix}/%{mingw32_target}/lib/libssp-0.dll \
      %{buildroot}%{_prefix}/%{mingw32_target}/lib/libstdc++-6.dll \
      %{buildroot}%{_prefix}/%{mingw32_target}/lib/libobjc-4.dll \
      %{buildroot}%{_prefix}/%{mingw32_target}/lib/libgfortran-5.dll \
      %{buildroot}%{_prefix}/%{mingw32_target}/lib/libquadmath-0.dll \
%if 0%{bootstrap} == 0
      %{buildroot}%{_prefix}/%{mingw32_target}/lib/libgomp-1.dll \
%endif
      %{buildroot}%{mingw32_bindir}

mkdir -p %{buildroot}%{mingw64_bindir}
mv    %{buildroot}%{_prefix}/%{mingw64_target}/lib/libatomic-1.dll \
      %{buildroot}%{_prefix}/%{mingw64_target}/lib/libgcc_s_seh-1.dll \
      %{buildroot}%{_prefix}/%{mingw64_target}/lib/libssp-0.dll \
      %{buildroot}%{_prefix}/%{mingw64_target}/lib/libstdc++-6.dll \
      %{buildroot}%{_prefix}/%{mingw64_target}/lib/libobjc-4.dll \
      %{buildroot}%{_prefix}/%{mingw64_target}/lib/libgfortran-5.dll \
      %{buildroot}%{_prefix}/%{mingw64_target}/lib/libquadmath-0.dll \
%if 0%{bootstrap} == 0
      %{buildroot}%{_prefix}/%{mingw64_target}/lib/libgomp-1.dll \
%endif
      %{buildroot}%{mingw64_bindir}

mkdir -p %{buildroot}%{ucrt64_bindir}
mv    %{buildroot}%{_prefix}/%{ucrt64_target}/lib/libatomic-1.dll \
      %{buildroot}%{_prefix}/%{ucrt64_target}/lib/libgcc_s_seh-1.dll \
      %{buildroot}%{_prefix}/%{ucrt64_target}/lib/libssp-0.dll \
      %{buildroot}%{_prefix}/%{ucrt64_target}/lib/libstdc++-6.dll \
      %{buildroot}%{_prefix}/%{ucrt64_target}/lib/libobjc-4.dll \
      %{buildroot}%{_prefix}/%{ucrt64_target}/lib/libgfortran-5.dll \
      %{buildroot}%{_prefix}/%{ucrt64_target}/lib/libquadmath-0.dll \
%if 0%{bootstrap} == 0
      %{buildroot}%{_prefix}/%{ucrt64_target}/lib/libgomp-1.dll \
%endif
      %{buildroot}%{ucrt64_bindir}


# Various import libraries are placed in the wrong folder
mkdir -p %{buildroot}%{mingw32_libdir}
mkdir -p %{buildroot}%{mingw64_libdir}
mkdir -p %{buildroot}%{ucrt64_libdir}
mv %{buildroot}%{_prefix}/%{mingw32_target}/lib/* %{buildroot}%{mingw32_libdir}
mv %{buildroot}%{_prefix}/%{mingw64_target}/lib/* %{buildroot}%{mingw64_libdir}
mv %{buildroot}%{_prefix}/%{ucrt64_target}/lib/* %{buildroot}%{ucrt64_libdir}

# Don't want the *.la files.
find %{buildroot} -name '*.la' -delete

%endif

# For some reason there are wrapper libraries created named $target-$target-gcc-$tool
# Drop those files for now as this looks like a bug in GCC
rm -f %{buildroot}%{_bindir}/%{mingw32_target}-%{mingw32_target}-*
rm -f %{buildroot}%{_bindir}/%{mingw64_target}-%{mingw64_target}-*
rm -f %{buildroot}%{_bindir}/%{ucrt64_target}-%{ucrt64_target}-*

%if 0%{bootstrap} == 0
# HACK symlink libssp dll over import lib, otherwise linking with -lssp failes for mysterious reasons
# Needed to build gdb and everything which adds -D_FORTIFY_SOURCES=... and -fstack-protector
ln -sf %{mingw32_bindir}/libssp-0.dll %{buildroot}%{mingw32_libdir}/libssp.dll.a
ln -sf %{mingw64_bindir}/libssp-0.dll %{buildroot}%{mingw64_libdir}/libssp.dll.a
ln -sf %{ucrt64_bindir}/libssp-0.dll %{buildroot}%{ucrt64_libdir}/libssp.dll.a
%endif


%files -n mingw32-gcc
%license gcc/COPYING* COPYING.RUNTIME
%{_bindir}/%{mingw32_target}-gcc
%{_bindir}/%{mingw32_target}-gcc-%{version}
%{_bindir}/%{mingw32_target}-gcc-ar
%{_bindir}/%{mingw32_target}-gcc-nm
%{_bindir}/%{mingw32_target}-gcc-ranlib
%{_bindir}/%{mingw32_target}-gcov
%{_bindir}/%{mingw32_target}-gcov-dump
%{_bindir}/%{mingw32_target}-gcov-tool
%dir %{_prefix}/lib/gcc/%{mingw32_target}/%{version}
%{_prefix}/lib/gcc/%{mingw32_target}/%{version}/include/
%{_prefix}/lib/gcc/%{mingw32_target}/%{version}/include-fixed/
%{_prefix}/lib/gcc/%{mingw32_target}/%{version}/install-tools/
%{_libexecdir}/gcc/%{mingw32_target}/%{version}/collect2
%{_libexecdir}/gcc/%{mingw32_target}/%{version}/lto-wrapper
%{_libexecdir}/gcc/%{mingw32_target}/%{version}/install-tools
%{_mandir}/man1/%{mingw32_target}-gcc.1*
%{_mandir}/man1/%{mingw32_target}-gcov.1*
%{_mandir}/man1/%{mingw32_target}-gcov-dump.1*
%{_mandir}/man1/%{mingw32_target}-gcov-tool.1*

# Non-bootstrap files
%if 0%{bootstrap} == 0
%{_bindir}/%{mingw32_target}-lto-dump
%{mingw32_libdir}/libatomic.a
%{mingw32_libdir}/libatomic.dll.a
%{mingw32_libdir}/libatomic_asneeded.a
%{mingw32_libdir}/libgcc_s.a
%{mingw32_libdir}/libssp.a
%{mingw32_libdir}/libssp.dll.a
%{mingw32_libdir}/libssp_nonshared.a
%{mingw32_libdir}/libstdc++fs.a
%{mingw32_libdir}/libstdc++exp.a
%{mingw32_libdir}/libstdc++.modules.json
%{_prefix}/lib/gcc/%{mingw32_target}/%{version}/crtbegin.o
%{_prefix}/lib/gcc/%{mingw32_target}/%{version}/crtend.o
%{_prefix}/lib/gcc/%{mingw32_target}/%{version}/crtfastmath.o
%{_prefix}/lib/gcc/%{mingw32_target}/%{version}/libcaf_shmem.a
%{_prefix}/lib/gcc/%{mingw32_target}/%{version}/libgcc.a
%{_prefix}/lib/gcc/%{mingw32_target}/%{version}/libgcc_eh.a
%{_prefix}/lib/gcc/%{mingw32_target}/%{version}/libgcov.a
%dir %{_prefix}/lib/gcc/%{mingw32_target}/%{version}/include/ssp
%{_prefix}/lib/gcc/%{mingw32_target}/%{version}/include/ssp/*.h
%{_libexecdir}/gcc/%{mingw32_target}/%{version}/g++-mapper-server
%{_libexecdir}/gcc/%{mingw32_target}/%{version}/lto1
%{_libexecdir}/gcc/%{mingw32_target}/%{version}/liblto_plugin.so*
%{_mandir}/man1/%{mingw32_target}-lto-dump.1*
%endif

%files -n mingw64-gcc
%license gcc/COPYING* COPYING.RUNTIME
%{_bindir}/%{mingw64_target}-gcc
%{_bindir}/%{mingw64_target}-gcc-%{version}
%{_bindir}/%{mingw64_target}-gcc-ar
%{_bindir}/%{mingw64_target}-gcc-nm
%{_bindir}/%{mingw64_target}-gcc-ranlib
%{_bindir}/%{mingw64_target}-gcov
%{_bindir}/%{mingw64_target}-gcov-dump
%{_bindir}/%{mingw64_target}-gcov-tool
%dir %{_prefix}/lib/gcc/%{mingw64_target}/%{version}
%{_prefix}/lib/gcc/%{mingw64_target}/%{version}/include/
%{_prefix}/lib/gcc/%{mingw64_target}/%{version}/include-fixed/
%{_prefix}/lib/gcc/%{mingw64_target}/%{version}/install-tools/
%{_libexecdir}/gcc/%{mingw64_target}/%{version}/collect2
%{_libexecdir}/gcc/%{mingw64_target}/%{version}/lto-wrapper
%{_libexecdir}/gcc/%{mingw64_target}/%{version}/install-tools
%{_mandir}/man1/%{mingw64_target}-gcc.1*
%{_mandir}/man1/%{mingw64_target}-gcov.1*
%{_mandir}/man1/%{mingw64_target}-gcov-dump.1*
%{_mandir}/man1/%{mingw64_target}-gcov-tool.1*

# Non-bootstrap files
%if 0%{bootstrap} == 0
%{_bindir}/%{mingw64_target}-lto-dump
%{mingw64_libdir}/libatomic.a
%{mingw64_libdir}/libatomic.dll.a
%{mingw64_libdir}/libatomic_asneeded.a
%{mingw64_libdir}/libgcc_s.a
%{mingw64_libdir}/libssp.a
%{mingw64_libdir}/libssp.dll.a
%{mingw64_libdir}/libssp_nonshared.a
%{mingw64_libdir}/libstdc++fs.a
%{mingw64_libdir}/libstdc++exp.a
%{mingw64_libdir}/libstdc++.modules.json
%{_prefix}/lib/gcc/%{mingw64_target}/%{version}/crtbegin.o
%{_prefix}/lib/gcc/%{mingw64_target}/%{version}/crtend.o
%{_prefix}/lib/gcc/%{mingw64_target}/%{version}/crtfastmath.o
%{_prefix}/lib/gcc/%{mingw64_target}/%{version}/libcaf_shmem.a
%{_prefix}/lib/gcc/%{mingw64_target}/%{version}/libgcc.a
%{_prefix}/lib/gcc/%{mingw64_target}/%{version}/libgcc_eh.a
%{_prefix}/lib/gcc/%{mingw64_target}/%{version}/libgcov.a
%dir %{_prefix}/lib/gcc/%{mingw64_target}/%{version}/include/ssp
%{_prefix}/lib/gcc/%{mingw64_target}/%{version}/include/ssp/*.h
%{_libexecdir}/gcc/%{mingw64_target}/%{version}/g++-mapper-server
%{_libexecdir}/gcc/%{mingw64_target}/%{version}/lto1
%{_libexecdir}/gcc/%{mingw64_target}/%{version}/liblto_plugin.so*
%{_mandir}/man1/%{mingw64_target}-lto-dump.1*
%endif

%files -n ucrt64-gcc
%license gcc/COPYING* COPYING.RUNTIME
%{_bindir}/%{ucrt64_target}-gcc
%{_bindir}/%{ucrt64_target}-gcc-%{version}
%{_bindir}/%{ucrt64_target}-gcc-ar
%{_bindir}/%{ucrt64_target}-gcc-nm
%{_bindir}/%{ucrt64_target}-gcc-ranlib
%{_bindir}/%{ucrt64_target}-gcov
%{_bindir}/%{ucrt64_target}-gcov-dump
%{_bindir}/%{ucrt64_target}-gcov-tool
%dir %{_prefix}/lib/gcc/%{ucrt64_target}/%{version}
%{_prefix}/lib/gcc/%{ucrt64_target}/%{version}/include/
%{_prefix}/lib/gcc/%{ucrt64_target}/%{version}/include-fixed/
%{_prefix}/lib/gcc/%{ucrt64_target}/%{version}/install-tools/
%{_libexecdir}/gcc/%{ucrt64_target}/%{version}/collect2
%{_libexecdir}/gcc/%{ucrt64_target}/%{version}/lto-wrapper
%{_libexecdir}/gcc/%{ucrt64_target}/%{version}/install-tools
%{_mandir}/man1/%{ucrt64_target}-gcc.1*
%{_mandir}/man1/%{ucrt64_target}-gcov.1*
%{_mandir}/man1/%{ucrt64_target}-gcov-dump.1*
%{_mandir}/man1/%{ucrt64_target}-gcov-tool.1*

# Non-bootstrap files
%if 0%{bootstrap} == 0
%{_bindir}/%{ucrt64_target}-lto-dump
%{ucrt64_libdir}/libatomic.a
%{ucrt64_libdir}/libatomic.dll.a
%{ucrt64_libdir}/libatomic_asneeded.a
%{ucrt64_libdir}/libgcc_s.a
%{ucrt64_libdir}/libssp.a
%{ucrt64_libdir}/libssp.dll.a
%{ucrt64_libdir}/libssp_nonshared.a
%{ucrt64_libdir}/libstdc++fs.a
%{ucrt64_libdir}/libstdc++exp.a
%{ucrt64_libdir}/libstdc++.modules.json
%{_prefix}/lib/gcc/%{ucrt64_target}/%{version}/crtbegin.o
%{_prefix}/lib/gcc/%{ucrt64_target}/%{version}/crtend.o
%{_prefix}/lib/gcc/%{ucrt64_target}/%{version}/crtfastmath.o
%{_prefix}/lib/gcc/%{ucrt64_target}/%{version}/libcaf_shmem.a
%{_prefix}/lib/gcc/%{ucrt64_target}/%{version}/libgcc.a
%{_prefix}/lib/gcc/%{ucrt64_target}/%{version}/libgcc_eh.a
%{_prefix}/lib/gcc/%{ucrt64_target}/%{version}/libgcov.a
%dir %{_prefix}/lib/gcc/%{ucrt64_target}/%{version}/include/ssp
%{_prefix}/lib/gcc/%{ucrt64_target}/%{version}/include/ssp/*.h
%{_libexecdir}/gcc/%{ucrt64_target}/%{version}/g++-mapper-server
%{_libexecdir}/gcc/%{ucrt64_target}/%{version}/lto1
%{_libexecdir}/gcc/%{ucrt64_target}/%{version}/liblto_plugin.so*
%{_mandir}/man1/%{ucrt64_target}-lto-dump.1*
%endif

%files -n mingw32-gcc-plugin-devel
%dir %{_prefix}/lib/gcc/%{mingw32_target}
%dir %{_prefix}/lib/gcc/%{mingw32_target}/%{version}
%dir %{_prefix}/lib/gcc/%{mingw32_target}/%{version}/plugin
%{_prefix}/lib/gcc/%{mingw32_target}/%{version}/plugin/gtype.state
%{_prefix}/lib/gcc/%{mingw32_target}/%{version}/plugin/include
%dir %{_libexecdir}/gcc/%{mingw32_target}
%dir %{_libexecdir}/gcc/%{mingw32_target}/%{version}
%{_libexecdir}/gcc/%{mingw32_target}/%{version}/plugin

%files -n mingw64-gcc-plugin-devel
%dir %{_prefix}/lib/gcc/%{mingw64_target}
%dir %{_prefix}/lib/gcc/%{mingw64_target}/%{version}
%dir %{_prefix}/lib/gcc/%{mingw64_target}/%{version}/plugin
%{_prefix}/lib/gcc/%{mingw64_target}/%{version}/plugin/gtype.state
%{_prefix}/lib/gcc/%{mingw64_target}/%{version}/plugin/include
%dir %{_libexecdir}/gcc/%{mingw64_target}
%dir %{_libexecdir}/gcc/%{mingw64_target}/%{version}
%{_libexecdir}/gcc/%{mingw64_target}/%{version}/plugin

%files -n ucrt64-gcc-plugin-devel
%dir %{_prefix}/lib/gcc/%{ucrt64_target}
%dir %{_prefix}/lib/gcc/%{ucrt64_target}/%{version}
%dir %{_prefix}/lib/gcc/%{ucrt64_target}/%{version}/plugin
%{_prefix}/lib/gcc/%{ucrt64_target}/%{version}/plugin/gtype.state
%{_prefix}/lib/gcc/%{ucrt64_target}/%{version}/plugin/include
%dir %{_libexecdir}/gcc/%{ucrt64_target}
%dir %{_libexecdir}/gcc/%{ucrt64_target}/%{version}
%{_libexecdir}/gcc/%{ucrt64_target}/%{version}/plugin

%if 0%{bootstrap} == 0
%files -n mingw32-libgcc
%license gcc/COPYING* COPYING.RUNTIME
%{mingw32_bindir}/libatomic-1.dll
%{mingw32_bindir}/libgcc_s_dw2-1.dll
%{mingw32_bindir}/libssp-0.dll

%files -n mingw64-libgcc
%license gcc/COPYING* COPYING.RUNTIME
%{mingw64_bindir}/libatomic-1.dll
%{mingw64_bindir}/libgcc_s_seh-1.dll
%{mingw64_bindir}/libssp-0.dll

%files -n ucrt64-libgcc
%license gcc/COPYING* COPYING.RUNTIME
%{ucrt64_bindir}/libatomic-1.dll
%{ucrt64_bindir}/libgcc_s_seh-1.dll
%{ucrt64_bindir}/libssp-0.dll

%files -n mingw32-libstdc++
%license gcc/COPYING* COPYING.RUNTIME
%{mingw32_bindir}/libstdc++-6.dll

%files -n mingw64-libstdc++
%license gcc/COPYING* COPYING.RUNTIME
%{mingw64_bindir}/libstdc++-6.dll

%files -n ucrt64-libstdc++
%license gcc/COPYING* COPYING.RUNTIME
%{ucrt64_bindir}/libstdc++-6.dll

%files -n mingw32-libgomp
%{mingw32_bindir}/libgomp-1.dll
%{mingw32_libdir}/libgomp.a
%{mingw32_libdir}/libgomp.dll.a
%{mingw32_libdir}/libgomp.spec

%files -n mingw64-libgomp
%{mingw64_bindir}/libgomp-1.dll
%{mingw64_libdir}/libgomp.a
%{mingw64_libdir}/libgomp.dll.a
%{mingw64_libdir}/libgomp.spec

%files -n ucrt64-libgomp
%{ucrt64_bindir}/libgomp-1.dll
%{ucrt64_libdir}/libgomp.a
%{ucrt64_libdir}/libgomp.dll.a
%{ucrt64_libdir}/libgomp.spec
%endif

%files -n mingw32-cpp
%{_bindir}/%{mingw32_target}-cpp
%{_mandir}/man1/%{mingw32_target}-cpp.1*
%dir %{_prefix}/lib/gcc/%{mingw32_target}
%dir %{_prefix}/lib/gcc/%{mingw32_target}/%{version}
%dir %{_libexecdir}/gcc/%{mingw32_target}/%{version}
%dir %{_libexecdir}/gcc/%{mingw32_target}
%{_libexecdir}/gcc/%{mingw32_target}/%{version}/cc1

%files -n mingw64-cpp
%{_bindir}/%{mingw64_target}-cpp
%{_mandir}/man1/%{mingw64_target}-cpp.1*
%dir %{_prefix}/lib/gcc/%{mingw64_target}
%dir %{_prefix}/lib/gcc/%{mingw64_target}/%{version}
%dir %{_libexecdir}/gcc/%{mingw64_target}/%{version}
%dir %{_libexecdir}/gcc/%{mingw64_target}
%{_libexecdir}/gcc/%{mingw64_target}/%{version}/cc1

%files -n ucrt64-cpp
%{_bindir}/%{ucrt64_target}-cpp
%{_mandir}/man1/%{ucrt64_target}-cpp.1*
%dir %{_prefix}/lib/gcc/%{ucrt64_target}
%dir %{_prefix}/lib/gcc/%{ucrt64_target}/%{version}
%dir %{_libexecdir}/gcc/%{ucrt64_target}/%{version}
%dir %{_libexecdir}/gcc/%{ucrt64_target}
%{_libexecdir}/gcc/%{ucrt64_target}/%{version}/cc1

%files -n mingw32-gcc-c++
%{_bindir}/%{mingw32_target}-g++
%{_bindir}/%{mingw32_target}-c++
%{_mandir}/man1/%{mingw32_target}-g++.1*
%{_libexecdir}/gcc/%{mingw32_target}/%{version}/cc1plus

# Non-bootstrap files
%if 0%{bootstrap} == 0
%{mingw32_includedir}/c++/
%{mingw32_libdir}/libstdc++.a
%{mingw32_libdir}/libstdc++.dll.a
%{mingw32_libdir}/libstdc++.dll.a-gdb.py
%{mingw32_libdir}/libsupc++.a
%endif

%files -n mingw64-gcc-c++
%{_bindir}/%{mingw64_target}-g++
%{_bindir}/%{mingw64_target}-c++
%{_mandir}/man1/%{mingw64_target}-g++.1*
%{_libexecdir}/gcc/%{mingw64_target}/%{version}/cc1plus

# Non-bootstrap files
%if 0%{bootstrap} == 0
%{mingw64_includedir}/c++/
%{mingw64_libdir}/libstdc++.a
%{mingw64_libdir}/libstdc++.dll.a
%{mingw64_libdir}/libstdc++.dll.a-gdb.py
%{mingw64_libdir}/libsupc++.a
%endif

%files -n ucrt64-gcc-c++
%{_bindir}/%{ucrt64_target}-g++
%{_bindir}/%{ucrt64_target}-c++
%{_mandir}/man1/%{ucrt64_target}-g++.1*
%{_libexecdir}/gcc/%{ucrt64_target}/%{version}/cc1plus

# Non-bootstrap files
%if 0%{bootstrap} == 0
%{ucrt64_includedir}/c++/
%{ucrt64_libdir}/libstdc++.a
%{ucrt64_libdir}/libstdc++.dll.a
%{ucrt64_libdir}/libstdc++.dll.a-gdb.py
%{ucrt64_libdir}/libsupc++.a
%endif

%files -n mingw32-gcc-objc
%{_libexecdir}/gcc/%{mingw32_target}/%{version}/cc1obj
%if 0%{bootstrap} == 0
%{_prefix}/lib/gcc/%{mingw32_target}/%{version}/include/objc/
%{mingw32_bindir}/libobjc-4.dll
%{mingw32_libdir}/libobjc.a
%{mingw32_libdir}/libobjc.dll.a
%endif

%files -n mingw64-gcc-objc
%{_libexecdir}/gcc/%{mingw64_target}/%{version}/cc1obj
%if 0%{bootstrap} == 0
%{_prefix}/lib/gcc/%{mingw64_target}/%{version}/include/objc/
%{mingw64_bindir}/libobjc-4.dll
%{mingw64_libdir}/libobjc.a
%{mingw64_libdir}/libobjc.dll.a
%endif

%files -n ucrt64-gcc-objc
%{_libexecdir}/gcc/%{ucrt64_target}/%{version}/cc1obj
%if 0%{bootstrap} == 0
%{_prefix}/lib/gcc/%{ucrt64_target}/%{version}/include/objc/
%{ucrt64_bindir}/libobjc-4.dll
%{ucrt64_libdir}/libobjc.a
%{ucrt64_libdir}/libobjc.dll.a
%endif

%files -n mingw32-gcc-objc++
%{_libexecdir}/gcc/%{mingw32_target}/%{version}/cc1objplus

%files -n mingw64-gcc-objc++
%{_libexecdir}/gcc/%{mingw64_target}/%{version}/cc1objplus

%files -n ucrt64-gcc-objc++
%{_libexecdir}/gcc/%{ucrt64_target}/%{version}/cc1objplus

%files -n mingw32-gcc-gfortran
%{_bindir}/%{mingw32_target}-gfortran
%{_mandir}/man1/%{mingw32_target}-gfortran.1*
%{_libexecdir}/gcc/%{mingw32_target}/%{version}/f951
%if 0%{bootstrap} == 0
%{mingw32_bindir}/libgfortran-5.dll
%{mingw32_bindir}/libquadmath-0.dll
%{mingw32_libdir}/libgfortran.a
%{mingw32_libdir}/libgfortran.dll.a
%{mingw32_libdir}/libgfortran.spec
%{mingw32_libdir}/libquadmath.a
%{mingw32_libdir}/libquadmath.dll.a
%{_prefix}/lib/gcc/%{mingw32_target}/%{version}/libcaf_single.a
%{_prefix}/lib/gcc/%{mingw32_target}/%{version}/finclude
%endif

%files -n mingw64-gcc-gfortran
%{_bindir}/%{mingw64_target}-gfortran
%{_mandir}/man1/%{mingw64_target}-gfortran.1*
%{_libexecdir}/gcc/%{mingw64_target}/%{version}/f951
%if 0%{bootstrap} == 0
%{mingw64_bindir}/libgfortran-5.dll
%{mingw64_bindir}/libquadmath-0.dll
%{mingw64_libdir}/libgfortran.a
%{mingw64_libdir}/libgfortran.dll.a
%{mingw64_libdir}/libgfortran.spec
%{mingw64_libdir}/libquadmath.a
%{mingw64_libdir}/libquadmath.dll.a
%{_prefix}/lib/gcc/%{mingw64_target}/%{version}/libcaf_single.a
%{_prefix}/lib/gcc/%{mingw64_target}/%{version}/finclude
%endif

%files -n ucrt64-gcc-gfortran
%{_bindir}/%{ucrt64_target}-gfortran
%{_mandir}/man1/%{ucrt64_target}-gfortran.1*
%{_libexecdir}/gcc/%{ucrt64_target}/%{version}/f951
%if 0%{bootstrap} == 0
%{ucrt64_bindir}/libgfortran-5.dll
%{ucrt64_bindir}/libquadmath-0.dll
%{ucrt64_libdir}/libgfortran.a
%{ucrt64_libdir}/libgfortran.dll.a
%{ucrt64_libdir}/libgfortran.spec
%{ucrt64_libdir}/libquadmath.a
%{ucrt64_libdir}/libquadmath.dll.a
%{_prefix}/lib/gcc/%{ucrt64_target}/%{version}/libcaf_single.a
%{_prefix}/lib/gcc/%{ucrt64_target}/%{version}/finclude
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 16.1.1-1
- Import
