%global source0_hash 438fd996826b0c82485a29da03a72d71d6e3541a83ec702df4271f6fe025d24e
%global source100_hash 1e5ee8ea4a6a1f7249a44134c67ad466dd68d7bbbadbf1da2bd860756cbd531f

%global ghdlver 5.1.1
%global ghdldate 20250618
%global ghdlcommit 91725e47fdded6a3ac2e4e5ee5fa1adb4b8b4f6f
%global ghdlshortcommit %(c=%{ghdlcommit}; echo ${c:0:7})
%global ghdlgitrev %{ghdldate}git%{ghdlshortcommit}

%ifarch %{ix86} x86_64
%bcond_without mcode
%else
%bcond_with mcode
%endif

#workaround for another compiler error
#bcond_without llvm

%ifarch x86_64 ppc64le
%bcond_without llvm
%else
%bcond_with llvm
%endif

%bcond_with gnatwae

%global gcc_version 15.2.0
%global gcc_major 15
# Note, gcc_release must be integer, if you want to add suffixes to
# %%{release}, append them after %%{gcc_release} on Release: line.
%global gcc_release 1
# Hardening slows the compiler way too much.
%undefine _hardened_build
%if 0%{?fedora} > 27 || 0%{?rhel} > 7
# Until annobin is fixed (#1519165).
%undefine _annotated_build
%endif
%global build_isl 1

Summary: A VHDL simulator, using the GCC technology
Name: ghdl
Version: %{ghdlver}
Release: 2.%{ghdlgitrev}%{?dist}
# Automatically converted from old format: GPLv2+ and GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD - review is highly recommended.
License: GPL-2.0-or-later AND GPL-3.0-or-later AND LicenseRef-Callaway-GPLv3+-with-exceptions AND LicenseRef-Callaway-GPLv2+-with-exceptions AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-BSD
URL: http://ghdl.free.fr/
Source0: https://ftp.gnu.org/gnu/gcc/gcc-%{gcc_version}/gcc-%{gcc_version}.tar.xz
%global isl_version 0.16.1

Patch0: gcc15-hack.patch
Patch3: gcc15-libgomp-omp_h-multilib.patch
Patch4: gcc15-libtool-no-rpath.patch
Patch5: gcc15-isl-dl.patch
Patch6: gcc15-isl-dl2.patch
Patch8: gcc15-no-add-needed.patch
Patch9: gcc15-Wno-format-security.patch
Patch10: gcc15-rh1574936.patch
Patch12: gcc15-pr119006.patch

Source100: https://github.com/ghdl/ghdl/archive/%{ghdlcommit}/%{name}-%{ghdlshortcommit}.tar.gz
Patch102: ghdl-gcc15.patch
Patch103: ghdl-gcc15-ortho.patch
# From: Thomas Sailer <t.sailer@alumni.ethz.ch>
# To: ghdl-discuss@gna.org
# Date: Thu, 02 Apr 2009 15:36:00 +0200
# https://gna.org/bugs/index.php?13390
Patch110: ghdl-ppc64abort.patch
Requires: gcc

BuildRequires: binutils >= 2.31
BuildRequires: zlib-devel, gettext, bison, flex
BuildRequires: texinfo
BuildRequires: gmp-devel >= 4.1.2-8, mpfr-devel >= 2.2.1, libmpc-devel >= 0.8.1
BuildRequires: gcc, gcc-c++
# Make sure pthread.h doesn't contain __thread tokens
# Make sure glibc supports stack protector
# Make sure glibc supports DT_GNU_HASH
BuildRequires: glibc-devel >= 2.4.90-13
BuildRequires: elfutils-devel >= 0.147
BuildRequires: elfutils-libelf-devel >= 0.147
%if %{build_isl}
BuildRequires: isl = %{isl_version}
BuildRequires: isl-devel = %{isl_version}
%if 0%{?__isa_bits} == 64
Requires: libisl.so.15()(64bit)
%else
Requires: libisl.so.15
%endif
%endif
Requires: binutils >= 2.31
Requires: libgcc >= %{gcc_version}

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: gcc-gnat
# for x86, we also build the mcode version; if on x86_64, we need some 32bit libraries
%if %{with llvm}
BuildRequires: libedit-devel
BuildRequires: clang
BuildRequires: llvm
BuildRequires: llvm-devel
BuildRequires: llvm-static
%endif
BuildRequires: make

Requires: ghdl-grt = %{version}-%{release}
Provides: bundled(libiberty)

# gcc-gnat only available on these:
ExclusiveArch: %{GNAT_arches}

# the following arches are not supported by the base compiler:
# plus https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: armv7hl %{ix86}

# Make sure we don't use clashing namespaces
%global _vendor fedora_ghdl

%global _gnu %{nil}
%global gcc_target_platform %{_target_platform}

# do not strip libgrt.a -- makes debugging tedious otherwise
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's#/usr/lib/rpm/redhat/brp-strip-static-archive .*##g')

%description
GHDL is the open-source analyzer, compiler, simulator and (experimental)
synthesizer for VHDL, a Hardware Description Language (HDL). GHDL implements
the VHDL language according to the 1987, 1993 and 2002 versions of the IEEE
1076 VHDL standard, and partial for 2008. It compiles VHDL files and creates
a binary that simulates (or executes) your design. GHDL can also translate
a design into a VHDL 1993 netlist, or it can be plugged into Yosys for
open-source synthesis.

Since GHDL is a compiler (i.e., it generates object files), you can call
functions or procedures written in a foreign language, such as C, C++, Ada95
or Python.

%package grt
Summary: GHDL runtime libraries
# rhbz #316311
Requires: zlib-devel, libgnat >= 4.3

%description grt
This package contains the runtime libraries needed to link ghdl-compiled
object files into simulator executables. grt contains the simulator kernel
that tracks signal updates and schedules processes.

%ifarch %{ix86} x86_64
%if %{with mcode}
%package mcode
Summary: GHDL with mcode backend
Requires: ghdl-mcode-grt = %{version}-%{release}

%description mcode
This package contains the ghdl compiler with the mcode backend. The mcode
backend provides for faster compile time at the expense of longer run time.

%package mcode-grt
Summary: GHDL mcode runtime libraries

%description mcode-grt
This package contains the runtime libraries needed to link ghdl-mcode-compiled
object files into simulator executables. mcode-grt contains the simulator kernel
that tracks signal updates and schedules processes.
%endif
%endif

%if %{with llvm}
%package llvm
Summary: GHDL with LLVM backend
Requires: ghdl-llvm-grt = %{version}-%{release}

%description llvm
This package contains the ghdl compiler with the LLVM backend. The LLVM
backend is experimental.

%package llvm-grt
Summary: GHDL LLVM runtime libraries

%description llvm-grt
This package contains the runtime libraries needed to link ghdl-llvm-compiled
object files into simulator executables. llvm-grt contains the simulator kernel
that tracks signal updates and schedules processes.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source100_hash}" = "none" || { f="%{SOURCE100}"; test -f "$f" || { echo "oreon: missing Source100 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source100_hash}" || { echo "oreon: Source100 hash mismatch" >&2; exit 1; }; }

%setup -q -n gcc-%{gcc_version} -a 100
%patch -P 0 -p0 -b .hack~
%patch -P 3 -p0 -b .libgomp-omp_h-multilib~
%patch -P 4 -p0 -b .libtool-no-rpath~
%if %{build_isl}
%patch -P 5 -p0 -b .isl-dl~
%patch -P 6 -p0 -b .isl-dl2~
%endif
%patch -P 8 -p0 -b .no-add-needed~
%patch -P 9 -p0 -b .Wno-format-security~
%if 0%{?fedora} >= 29 || 0%{?rhel} > 7
%patch -P 10 -p0 -b .rh1574936~
%endif
%patch -P 12 -p0 -b .pr119006~

echo 'Red Hat GHDL %{version}-%{release}' > gcc/DEV-PHASE

cp -a libstdc++-v3/config/cpu/i{4,3}86/atomicity.h

./contrib/gcc_update --touch

LC_ALL=C sed -i -e 's/\xa0/ /' gcc/doc/options.texi

sed -i -e 's/Common Driver Var(flag_report_bug)/& Init(1)/' gcc/common.opt

# ghdl
mv ghdl-%{ghdlcommit} ghdl

pushd ghdl
%patch -P 102 -p1 -b .gcc15~
%patch -P 103 -p1 -b .gcc15-ortho~
popd

# fix library and include path
pushd ghdl
sed -i.orig -e 's|\"include\"|\"include/ghdl\"|' src/ghdldrv/ghdlsynth.adb
sed -i.orig -e 's|\"include\"|\"include/ghdl\"|' src/ghdldrv/ghdlvpi.adb
popd

%if %{with mcode}
cp -r ghdl ghdl-mcode
pushd ghdl-mcode
perl -i -pe 's,^libdirsuffix=.*$,libdirsuffix=lib/ghdl/mcode,' configure
perl -i -pe 's,^libdirreverse=.*$,libdirreverse=../../..,' configure
popd
%endif

%if %{with llvm}
cp -r ghdl ghdl-llvm
pushd ghdl-llvm
perl -i -pe 's,^libdirsuffix=.*$,libdirsuffix=lib/ghdl/llvm,' configure
perl -i -pe 's,^libdirreverse=.*$,libdirreverse=../../..,' configure
popd
%endif

echo 'Red Hat %{version}-%{gcc_release}' > gcc/DEV-PHASE

pushd ghdl
./configure \
%if %{without gnatwae}
	--disable-werror \
%endif
	--prefix=/usr --with-gcc=..
make copy-sources
popd

%patch -P 110 -p0 -b .ppc64abort

# workaround for GCC 14 build system
touch gcc/vhdl/lang.opt.urls

%build

# build mcode on x86
%if %{with mcode}
pushd ghdl-mcode
./configure \
%if %{without gnatwae}
	--disable-werror \
%endif
	--prefix=/usr
make %{?_smp_mflags}
popd
%endif

%if %{with llvm}
pushd ghdl-llvm
./configure --prefix=/usr \
%if %{without gnatwae}
	--disable-werror \
%endif
	--with-llvm-config=/usr/bin/llvm-config
make %{?_smp_mflags} LDFLAGS=-Wl,--build-id
popd
%endif

# Undo the broken autoconf change in recent Fedora versions
export CONFIG_SITE=NONE

CC=gcc
CXX=g++
OPT_FLAGS=`echo %{optflags}|sed -e 's/\(-Wp\)\?,-D_FORTIFY_SOURCE=[123]//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-flto=auto//g;s/-flto//g;s/-ffat-lto-objects//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-m64//g;s/-m32//g;s/-m31//g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-mfpmath=sse/-mfpmath=sse -msse2/g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/ -pipe / /g'`
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-Werror=format-security/-Wformat-security/g'`
%ifarch %{ix86}
OPT_FLAGS=`echo $OPT_FLAGS|sed -e 's/-march=i.86//g'`
%endif
OPT_FLAGS=`echo "$OPT_FLAGS" | sed -e 's/[[:blank:]]\+/ /g'`
case "$OPT_FLAGS" in
  *-fasynchronous-unwind-tables*)
    sed -i -e 's/-fno-exceptions /-fno-exceptions -fno-asynchronous-unwind-tables /' \
      libgcc/Makefile.in
    ;;
esac

rm -rf obj-%{gcc_target_platform}
mkdir obj-%{gcc_target_platform}
pushd obj-%{gcc_target_platform}

CONFIGURE_OPTS="\
	--prefix=%{_prefix} --mandir=%{_mandir} --infodir=%{_infodir} \
	--with-bugurl=http://bugzilla.redhat.com/bugzilla \
	--enable-shared --enable-threads=posix --enable-checking=release \
	--disable-multilib \
	--with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions \
	--enable-gnu-unique-object --enable-linker-build-id --with-gcc-major-version-only \
	--with-linker-hash-style=gnu \
	--enable-plugin --enable-initfini-array \
%if %{build_isl}
	--with-isl \
%else
	--without-isl \
%endif
%ifarch %{arm}
	--disable-sjlj-exceptions \
%endif
%ifarch ppc64le
	--enable-secureplt \
%endif
%ifarch ppc64le s390x
	--with-long-double-128 \
%endif
%ifarch ppc64le
	--with-cpu-32=power8 --with-tune-32=power8 --with-cpu-64=power8 --with-tune-64=power8 \
%endif
%ifarch %{ix86} x86_64
	--enable-cet \
	--with-tune=generic \
%endif
%if 0%{?rhel} >= 7
%ifarch %{ix86}
	--with-arch=x86-64 \
%endif
%ifarch x86_64
	--with-arch_32=x86-64 \
%endif
%else
%ifarch %{ix86}
	--with-arch=i686 \
%endif
%ifarch x86_64
	--with-arch_32=i686 \
%endif
%endif
%ifarch s390 s390x
%if 0%{?rhel} >= 7
%if 0%{?rhel} > 7
	--with-arch=zEC12 --with-tune=z13 \
%else
	--with-arch=z196 --with-tune=zEC12 \
%endif
%else
%if 0%{?fedora} >= 26
	--with-arch=zEC12 --with-tune=z13 \
%else
	--with-arch=z9-109 --with-tune=z10 \
%endif
%endif
	--enable-decimal-float \
%endif
%ifarch armv7hl
	--with-tune=generic-armv7-a --with-arch=armv7-a \
	--with-float=hard --with-fpu=vfpv3-d16 --with-abi=aapcs-linux \
%endif
	--build=%{gcc_target_platform} \
	"

CC="$CC" CXX="$CXX" CFLAGS="$OPT_FLAGS" \
	CXXFLAGS="`echo " $OPT_FLAGS " | sed 's/ -Wall / /g;s/ -fexceptions / /g' \
		  | sed 's/ -Wformat-security / -Wformat -Wformat-security /'`" \
	XCFLAGS="$OPT_FLAGS" TCFLAGS="$OPT_FLAGS" \
	../configure --enable-bootstrap=no \
	--enable-languages=vhdl \
	$CONFIGURE_OPTS

make %{?_smp_mflags}

pushd gcc/vhdl
gnatmake -c -aI%{_builddir}/gcc-%{gcc_version}/gcc/vhdl ortho_gcc-main \
  -cargs -g -Wall -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 \
%ifarch %{ix86} x86_64
  -mtune=generic \
%endif
%ifarch ppc64le
  -mcpu=power8 -mtune=power8 \
%endif
  -gnata -gnat05 -gnaty3befhkmr
#-gnatwae
popd

popd

PBINDIR=`pwd`/obj-%{gcc_target_platform}/gcc/
pushd ghdl
make bindir=${PBINDIR} GHDL1_GCC_BIN="--GHDL1=${PBINDIR}/ghdl1" ghdllib
popd

%install
# install mcode on x86
%if %{with mcode}
pushd ghdl-mcode
make DESTDIR=%{buildroot} install
mv %{buildroot}/%{_bindir}/ghdl %{buildroot}/%{_bindir}/ghdl-mcode
popd
%endif

# install llvm
%if %{with llvm}
pushd ghdl-llvm
%make_install
mv %{buildroot}/%{_bindir}/ghdl %{buildroot}/%{_bindir}/ghdl-llvm
popd
%endif

# install gcc
%make_install -C obj-%{gcc_target_platform}

pushd ghdl
%make_install
popd

# Remove files not to be packaged
pushd %{buildroot}
rm -f \
        .%{_bindir}/{cpp,gcc,gccbug,gcov,gcov-dump,gcov-tool,lto-dump} \
        .%{_bindir}/%{gcc_target_platform}-gcc{,-%{gcc_major}} \
        .%{_bindir}/{,%{gcc_target_platform}-}gcc-{ar,nm,ranlib} \
        .%{_includedir}/mf-runtime.h \
        .%{_libdir}/lib{atomic,cc1,gcc_s,gomp,quadmath,ssp}* \
        .%{_infodir}/dir \
        .%{_infodir}/{cpp,cppinternals,gcc,gccinstall,gccint}.info* \
        .%{_infodir}/{libgomp,libquadmath}.info* \
        .%{_datadir}/locale/*/LC_MESSAGES/{gcc,cpplib}.mo \
        .%{_mandir}/man1/{cpp,gcc,gcov,gcov-dump,gcov-tool,lto-dump}.1* \
        .%{_mandir}/man7/{fsf-funding,gfdl,gpl}.7* \
        .%{_prefix}/lib/libgcc_s.* \
        .%{_prefix}/lib/libmudflap.* \
        .%{_prefix}/lib/libmudflapth.* \
        .%{_prefix}/lib/lib{atomic,gomp,quadmath,ssp}* \
        .%{_libdir}/32/libiberty.a

# Remove crt/libgcc, as ghdl invokes the native gcc to perform the linking
rm -f \
        .%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/*crt* \
        .%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/libgc* \
        .%{_libexecdir}/gcc/%{gcc_target_platform}/%{gcc_major}/{cc1,collect2} \
        .%{_libexecdir}/gcc/%{gcc_target_platform}/%{gcc_major}/*lto*

# Remove directory hierarchies not to be packaged
rm -rf \
        .%{_prefix}/lib/gcc/%{gcc_target_platform}/%{gcc_major}/{include,include-fixed,plugin,install-tools} \
        .%{_libexecdir}/gcc/%{gcc_target_platform}/%{gcc_major}/install-tools \
        .%{_libexecdir}/gcc/%{gcc_target_platform}/%{gcc_major}/plugin \

popd

%if "%{_lib}" != "lib"
mv %{buildroot}/usr/lib/libghdlvpi.so %{buildroot}%{_libdir}/
mv %{buildroot}/usr/lib/libghdl-*.so %{buildroot}%{_libdir}/
mv %{buildroot}/usr/lib/libghw.so %{buildroot}%{_libdir}/
%endif
# remove static libghdl
rm %{buildroot}/usr/lib/libghdl.{a,link}

%files
%{_bindir}/ghdl
%{_bindir}/ghwdump
%{_infodir}/ghdl.info.*
# Need to own directory %%{_libexecdir}/gcc even though we only want the
# %%{gcc_target_platform}/%%{gcc_version} subdirectory
%{_libexecdir}/gcc/
%{_mandir}/man1/*
%{_includedir}/ghdl/
%{_libdir}/libghdl-*.so
%{_libdir}/libghdlvpi.so
%{_libdir}/libghw.so

%files grt
# Need to own directory %%{_libdir}/gcc even though we only want the
# %%{gcc_target_platform}/%%{gcc_version} subdirectory
%{_prefix}/lib/gcc/
%{_prefix}/lib/ghdl/
%if %{with llvm}
%exclude %{_prefix}/lib/ghdl/llvm
%endif
%if %{with mcode}
%exclude %{_prefix}/lib/ghdl/mcode
%endif

%if %{with mcode}
%files mcode
%{_bindir}/ghdl-mcode

%files mcode-grt
#%%dir %%{_libdir}/ghdl
%{_prefix}/lib/ghdl/mcode
%endif

%if %{with llvm}
%files llvm
%{_bindir}/ghdl-llvm
%{_bindir}/ghdl1-llvm

%files llvm-grt
#%%dir %%{_libdir}/ghdl
%{_prefix}/lib/ghdl/llvm
%endif

%changelog
%autochangelog
