%global source0_hash 1d3be708604eae0e42d578ba93b390c2a145f17743a744d8f3f8c2ad5855a38a
%{?mingw_package_header}
%global name1 mpfr
Summary:        MinGW C library for multiple-precision floating-point computations
Name:           mingw-%{name1}
Version:        4.0.2
Release:        1%{?dist}
URL:            http://www.mpfr.org/
Source0:        http://www.%{name1}.org/%{name1}-%{version}/%{name1}-%{version}.tar.xz
Patch0: %{name1}-include-float.patch
Patch1: %{name1}-int-overflow.patch
Patch2: %{name1}-set-int.patch
Patch3: %{name1}-sub1-ubf.patch
Patch4: %{name1}-const.patch
Patch5: %{name1}-array-length.patch
Patch6: %{name1}-sub1-ubftest.patch
License:        LGPL-3.0-or-later AND GPL-3.0-or-later AND LicenseRef-Callaway-GFDL
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gmp
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gmp
# /oreon:deps
%description
The MPFR library is a C library for multiple-precision floating-point
computations with "correct rounding". The MPFR is efficient and 
also has a well-defined semantics. It copies the good ideas from the 
ANSI/IEEE-754 standard for double-precision floating-point arithmetic 
(53-bit mantissa). MPFR is based on the GMP multiple-precision library.

# Mingw32
%package -n mingw32-%{name1}
Summary:        MinGW C library for multiple-precision floating-point computations
%description -n mingw32-%{name1}
The MPFR library is a C library for multiple-precision floating-point
computations with "correct rounding". The MPFR is efficient and 
also has a well-defined semantics. It copies the good ideas from the 
ANSI/IEEE-754 standard for double-precision floating-point arithmetic 
(53-bit mantissa). MPFR is based on the GMP multiple-precision library.

This package contains cross-compiled libraries and development tools
for Windows.

# Mingw64
%package -n mingw64-%{name1}
Summary:        MinGW C library for multiple-precision floating-point computations
%description -n mingw64-%{name1}
The MPFR library is a C library for multiple-precision floating-point
computations with "correct rounding". The MPFR is efficient and 
also has a well-defined semantics. It copies the good ideas from the 
ANSI/IEEE-754 standard for double-precision floating-point arithmetic 
(53-bit mantissa). MPFR is based on the GMP multiple-precision library.

This package contains cross-compiled libraries and development tools
for Windows.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name1}-%{version}

%build

%mingw_configure --disable-assert --disable-static --enable-shared
%mingw_make %{?_smp_mflags}
%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}
rm -rf $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{mingw64_libdir}/*.la
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-mpfr -f %{oreon_filedir}/mingw32-mpfr.list
%files -n mingw64-mpfr -f %{oreon_filedir}/mingw64-mpfr.list

%changelog

%autochangelog
