%global source0_hash a3c2b80201b89e68616f4ad30bc66aee4927c3ce50e33929ca819d5c43538898
%{?mingw_package_header}
Name:       mingw-gmp
Version:    6.3.0
Release:        1%{?dist}
Summary:        Cross-compiled GNU arbitrary precision library
License:    LGPL-3.0-or-later OR GPL-2.0-or-later
URL:        http://gmplib.org/
Source0:        https://ftp.gnu.org/pub/gnu/gmp/gmp-%{version}.tar.xz
Patch0: gmp-6.3.0-c23.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  git
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
# /oreon:deps
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
%global oreon_srcdir gmp-%{version}
%oreon_prep
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
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/lib{gmp,mp,gmpxx}.la
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/lib{gmp,mp,gmpxx}.la
rm -r $RPM_BUILD_ROOT/%{mingw32_prefix}/share
rm -r $RPM_BUILD_ROOT/%{mingw64_prefix}/share
%oreon_autofiles mingw32-gmp usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-gmp usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-gmp -f %{oreon_filedir}/mingw32-gmp.list
%files -n mingw64-gmp -f %{oreon_filedir}/mingw64-gmp.list

%changelog

%autochangelog
