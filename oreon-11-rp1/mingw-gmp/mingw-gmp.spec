%global source0_hash a3c2b80201b89e68616f4ad30bc66aee4927c3ce50e33929ca819d5c43538898

%{?mingw_package_header}

Name:       mingw-gmp
Version:    6.3.0
Release:    5%{?dist}

Summary:    Cross-compiled GNU arbitrary precision library
# Automatically converted from old format: LGPLv3+ or GPLv2+ - review is highly recommended.
License:    LGPL-3.0-or-later OR GPL-2.0-or-later
URL:        http://gmplib.org/
Source0:    ftp://ftp.gnu.org/pub/gnu/gmp/gmp-%{version}.tar.xz
# https://gmplib.org/repo/gmp/rev/8e7bb4ae7a18
Patch0: gmp-6.3.0-c23.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++

BuildRequires:  git
BuildRequires:  libtool

%description
The gmp package contains GNU MP, a library for arbitrary precision
arithmetic, signed integers operations, rational numbers and floating
point numbers. GNU MP is designed for speed, for both small and very
large operands. GNU MP is fast because it uses fullwords as the basic
arithmetic type, it uses fast algorithms, it carefully optimizes
assembly code for many CPUs' most common inner loops, and it generally
emphasizes speed over simplicity/elegance in its operations.

Install the gmp package if you need a fast arbitrary precision
library.

# Mingw32
%package -n mingw32-gmp
Summary: Cross-compiled GNU arbitrary precision library

%description -n mingw32-gmp
The gmp package contains GNU MP, a library for arbitrary precision
arithmetic, signed integers operations, rational numbers and floating
point numbers. GNU MP is designed for speed, for both small and very
large operands. GNU MP is fast because it uses fullwords as the basic
arithmetic type, it uses fast algorithms, it carefully optimizes
assembly code for many CPUs' most common inner loops, and it generally
emphasizes speed over simplicity/elegance in its operations.

Install the gmp package if you need a fast arbitrary precision
library.

# Mingw64
%package -n mingw64-gmp
Summary: Cross-compiled GNU arbitrary precision library

%description -n mingw64-gmp
The gmp package contains GNU MP, a library for arbitrary precision
arithmetic, signed integers operations, rational numbers and floating
point numbers. GNU MP is designed for speed, for both small and very
large operands. GNU MP is fast because it uses fullwords as the basic
arithmetic type, it uses fast algorithms, it carefully optimizes
assembly code for many CPUs' most common inner loops, and it generally
emphasizes speed over simplicity/elegance in its operations.

Install the gmp package if you need a fast arbitrary precision
library.

%?mingw_debug_package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git -n gmp-%{version}

%build
autoreconf -ifv
%mingw_configure \
    --enable-shared \
    --disable-static \
    --enable-cxx \
    --enable-fat
export LD_LIBRARY_PATH=`pwd`/.libs
%mingw_make %{?_smp_mflags}

%install
export LD_LIBRARY_PATH=`pwd`/.libs
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/lib{gmp,mp,gmpxx}.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/lib{gmp,mp,gmpxx}.la

# Remove documentation which duplicates that found in the native package.
rm -r $RPM_BUILD_ROOT/%{mingw32_prefix}/share
rm -r $RPM_BUILD_ROOT/%{mingw64_prefix}/share

# Win32
%files -n mingw32-gmp
%license COPYING COPYING.LESSERv3 COPYINGv2 COPYINGv3
%doc NEWS README
%{mingw32_bindir}/libgmp-10.dll
%{mingw32_bindir}/libgmpxx-4.dll
%{mingw32_libdir}/libgmp.dll.a
%{mingw32_libdir}/libgmpxx.dll.a
%{mingw32_libdir}/pkgconfig/gmp.pc
%{mingw32_libdir}/pkgconfig/gmpxx.pc
%{mingw32_includedir}/gmp.h
%{mingw32_includedir}/gmpxx.h

# Win64
%files -n mingw64-gmp
%license COPYING COPYING.LESSERv3 COPYINGv2 COPYINGv3
%doc NEWS README
%{mingw64_bindir}/libgmp-10.dll
%{mingw64_bindir}/libgmpxx-4.dll
%{mingw64_libdir}/libgmp.dll.a
%{mingw64_libdir}/libgmpxx.dll.a
%{mingw64_libdir}/pkgconfig/gmp.pc
%{mingw64_libdir}/pkgconfig/gmpxx.pc
%{mingw64_includedir}/gmp.h
%{mingw64_includedir}/gmpxx.h

%changelog
%autochangelog
