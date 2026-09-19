%global source0_hash 73bc2f51b90d2a780e6d266d43e487b3dbd78945dd0b04b14ca5980fe28d2f53

%{?mingw_package_header}

Name:           mingw-gsl
Version:        1.16
Release:        26%{?dist}
Summary:        MinGW Windows port of the GNU Scientific Library

# info part of this package is under GFDL license
# eigen/nonsymmv.c and eigen/schur.c
# contains rutiens which are part of LAPACK - under BSD style license
# Automatically converted from old format: GPLv3 and GFDL and BSD - review is highly recommended.
License:        GPL-3.0-only AND LicenseRef-Callaway-GFDL AND LicenseRef-Callaway-BSD
URL:            http://www.gnu.org/software/gsl/
Source0:        ftp://ftp.gnu.org/gnu/gsl/gsl-%{version}.tar.gz
Patch0:         gsl-1.15-lib64.patch

BuildArch: noarch

BuildRequires: make
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils

%description
The GNU Scientific Library (GSL) is a collection of routines for
numerical analysis, written in C.

# Mingw32
%package -n mingw32-gsl
Summary: MinGW Windows port of the GNU Scientific Library for the win32 target

%description -n mingw32-gsl
The GNU Scientific Library (GSL) is a collection of routines for
numerical analysis, written in C.

%package -n mingw32-gsl-static
Summary: Static version of MinGW Windows port of the GNU Scientific Library
Requires: mingw32-gsl = %{version}-%{release}

%description -n mingw32-gsl-static
Static version of MinGW Windows port of the GNU Scientific Library
for the win32 target.

# Mingw64
%package -n mingw64-gsl
Summary: MinGW Windows port of the GNU Scientific Library for the win64 target

%description -n mingw64-gsl
The GNU Scientific Library (GSL) is a collection of routines for
numerical analysis, written in C.

%package -n mingw64-gsl-static
Summary: Static version of MinGW Windows port of the GNU Scientific Library
Requires: mingw64-gsl = %{version}-%{release}

%description -n mingw64-gsl-static
Static version of MinGW Windows port of the GNU Scientific Library
for the win32 target.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gsl-%{version}
%patch -P0 -p1 -b .lib64
iconv -f windows-1252 -t utf-8 THANKS > THANKS.aux
touch -r THANKS THANKS.aux
mv THANKS.aux THANKS

%build
# Native package has:
#   configure ... CFLAGS="$CFLAGS -fgnu89-inline"
# but that destroys the original CFLAGS setting.
%mingw_configure

%mingw_make %{?_smp_mflags}

%install
%mingw_make install "DESTDIR=$RPM_BUILD_ROOT"

# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete

# Remove info files and man pages which duplicate native package.
rm -r $RPM_BUILD_ROOT%{mingw32_mandir}
rm -r $RPM_BUILD_ROOT%{mingw32_infodir}
rm -r $RPM_BUILD_ROOT%{mingw64_mandir}
rm -r $RPM_BUILD_ROOT%{mingw64_infodir}

# Mingw32
%files -n mingw32-gsl
%doc COPYING AUTHORS BUGS ChangeLog NEWS README THANKS TODO
%{mingw32_bindir}/libgslcblas-0.dll
%{mingw32_bindir}/libgsl-0.dll
%{mingw32_bindir}/gsl-config
%{mingw32_bindir}/gsl-histogram.exe
%{mingw32_bindir}/gsl-randist.exe
%{mingw32_libdir}/libgslcblas.dll.a
%{mingw32_libdir}/libgsl.dll.a
%{mingw32_libdir}/pkgconfig/gsl.pc
%{mingw32_datadir}/aclocal/gsl.m4
%{mingw32_includedir}/gsl

%files -n mingw32-gsl-static
%{mingw32_libdir}/libgslcblas.a
%{mingw32_libdir}/libgsl.a

# Mingw64
%files -n mingw64-gsl
%doc COPYING AUTHORS BUGS ChangeLog NEWS README THANKS TODO
%{mingw64_bindir}/libgslcblas-0.dll
%{mingw64_bindir}/libgsl-0.dll
%{mingw64_bindir}/gsl-config
%{mingw64_bindir}/gsl-histogram.exe
%{mingw64_bindir}/gsl-randist.exe
%{mingw64_libdir}/libgslcblas.dll.a
%{mingw64_libdir}/libgsl.dll.a
%{mingw64_libdir}/pkgconfig/gsl.pc
%{mingw64_datadir}/aclocal/gsl.m4
%{mingw64_includedir}/gsl

%files -n mingw64-gsl-static
%{mingw64_libdir}/libgslcblas.a
%{mingw64_libdir}/libgsl.a

%changelog
%autochangelog
