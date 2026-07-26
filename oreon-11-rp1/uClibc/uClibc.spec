%global source0_hash 62333167b79afb0b25a843513288c67b59547acf653e8fbe62ee64e71ebd1587

Name: uClibc
Version: 0.9.33.2
Release: 34%{?dist}
Summary: C library for embedded Linux

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2
URL: http://www.uclibc.org/
Source0: http://www.uclibc.org/downloads/%{name}-%{version}.tar.xz
Source1: uClibc.config
Patch1: uClibc-0.9.33.2_kernel_long.patch
Patch2: CVE-2016-6264.patch

BuildRequires: make
BuildRequires: gcc

# This package only contains a static library
%global debug_package %{nil}

# uclibc only supports those
ExclusiveArch: %{arm} %{ix86} x86_64 %{mips}

%description
uClibc is a C library for developing embedded Linux systems.
It is much smaller than the GNU C Library, but nearly all applications
supported by glibc also work perfectly with uClibc.

%package devel
Summary: Header files and libraries for uClibc library
Provides: uClibc-static = %{version}-%{release}

%description devel
uClibc is a C library for developing embedded Linux systems.
It is much smaller than the GNU C Library, but nearly all applications
supported by glibc also work perfectly with uClibc.
This package contains the header files and libraries
needed for uClibc package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
%patch -P1 -b .kernel_long -p1
%patch -P2 -b .CVE-2016-6264 -p1

cat %{SOURCE1} >.config1
iconv -f windows-1252 -t utf-8 README >README.pom
mv README.pom README

%build
mkdir kernel-include
cp -a /usr/include/asm kernel-include
cp -a /usr/include/asm-generic kernel-include
cp -a /usr/include/linux kernel-include

arch=`uname -m | sed -e 's/i.86/i386/' -e 's/ppc/powerpc/' -e 's/armv7l/arm/' -e 's/armv5tel/arm/'`
echo "TARGET_$arch=y" >.config
echo "TARGET_ARCH=\"$arch\"" >>.config
%ifarch %{arm}
echo "CONFIG_ARM_EABI=y" >>.config
echo "ARCH_ANY_ENDIAN=n" >>.config
echo "ARCH_LITTLE_ENDIAN=y" >>.config
echo "ARCH_WANTS_LITTLE_ENDIAN=y" >>.config
%endif
%ifarch mips mipsel
echo "CONFIG_MIPS_ISA_MIPS32R2=y" >>.config
%ifarch mipsel
echo "ARCH_WANTS_LITTLE_ENDIAN=y" >>.config
%endif
%endif
%ifarch mips64 mips64el
echo "CONFIG_MIPS_ISA_MIPS64=y" >>.config
echo "CONFIG_MIPS_N64_ABI=y" >>.config
%ifarch mips64el
echo "ARCH_WANTS_LITTLE_ENDIAN=y" >>.config
%endif
%endif
cat .config1 >>.config

yes "" | make oldconfig %{?_smp_mflags}
make V=1 %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT/lib
make install PREFIX="$RPM_BUILD_ROOT/"
make install_headers PREFIX="$RPM_BUILD_ROOT/" DEVEL_PREFIX=""
cp -a kernel-include/* $RPM_BUILD_ROOT/include/

# move libraries to proper subdirectory
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/uClibc
mv  $RPM_BUILD_ROOT/lib/*  $RPM_BUILD_ROOT/%{_libdir}/uClibc/
rm -rf  $RPM_BUILD_ROOT/lib/

# move the header files to /usr subdirectory
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/uClibc
mv  $RPM_BUILD_ROOT/include/*  $RPM_BUILD_ROOT/%{_includedir}/uClibc
rm -rf  $RPM_BUILD_ROOT/include/

%files devel
%doc README docs/Glibc_vs_uClibc_Differences.txt docs/threads.txt docs/uClibc_vs_SuSv3.txt
%doc TODO DEDICATION.mjn3 MAINTAINERS
%doc docs/PORTING COPYING.LIB
%{_includedir}/uClibc
%{_libdir}/uClibc

%changelog
%autochangelog
