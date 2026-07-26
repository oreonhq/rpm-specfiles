%global source0_hash 1d3be708604eae0e42d578ba93b390c2a145f17743a744d8f3f8c2ad5855a38a

%{?mingw_package_header}

%global name1 mpfr

Summary:        MinGW C library for multiple-precision floating-point computations
Name:           mingw-%{name1}
Version:        4.0.2
Release:        16%{?dist}
URL:            http://www.mpfr.org/
Source0:        http://www.mpfr.org/mpfr-%{version}/%{name1}-%{version}.tar.xz

# https://gforge.inria.fr/scm/viewvc.php/mpfr?revision=13499&view=revision
# https://www.mpfr.org/mpfr-4.0.2/patch01
Patch0: %{name1}-include-float.patch

# https://gforge.inria.fr/scm/viewvc.php/mpfr?revision=13828&view=revision
# https://www.mpfr.org/mpfr-4.0.2/patch02
Patch1: %{name1}-int-overflow.patch

# https://gforge.inria.fr/scm/viewvc.php/mpfr?revision=13836&view=revision
# https://gforge.inria.fr/scm/viewvc.php/mpfr?revision=13838&view=revision
# https://www.mpfr.org/mpfr-4.0.2/patch03
Patch2: %{name1}-set-int.patch

# https://gforge.inria.fr/scm/viewvc.php/mpfr?revision=13697&view=revision
# https://gforge.inria.fr/scm/viewvc.php/mpfr?revision=13837&view=revision
# https://gforge.inria.fr/scm/viewvc.php/mpfr?revision=13841&view=revision
# https://www.mpfr.org/mpfr-4.0.2/patch04
Patch3: %{name1}-sub1-ubf.patch

# https://gforge.inria.fr/scm/viewvc.php/mpfr?revision=13516&view=revision
# https://gforge.inria.fr/scm/viewvc.php/mpfr?revision=13520&view=revision
# https://www.mpfr.org/mpfr-4.0.2/patch05
Patch4: %{name1}-const.patch

# https://gforge.inria.fr/scm/viewvc.php/mpfr?revision=13518&view=revision
# https://www.mpfr.org/mpfr-4.0.2/patch06
Patch5: %{name1}-array-length.patch

# https://gforge.inria.fr/scm/viewvc.php/mpfr?revision=13869&view=revision
# https://www.mpfr.org/mpfr-4.0.2/patch07
Patch6: %{name1}-sub1-ubftest.patch

# GFDL  (mpfr.texi, mpfr.info and fdl.texi)
# Automatically converted from old format: LGPLv3+ and GPLv3+ and GFDL - review is highly recommended.
License:        LGPL-3.0-or-later AND GPL-3.0-or-later AND LicenseRef-Callaway-GFDL
BuildRequires: make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gmp
BuildRequires:  mingw64-gmp
BuildArch:      noarch

%description
The MPFR library is a C library for multiple-precision floating-point
computations with "correct rounding". The MPFR is efficient and 
also has a well-defined semantics. It copies the good ideas from the 
ANSI/IEEE-754 standard for double-precision floating-point arithmetic 
(53-bit mantissa). MPFR is based on the GMP multiple-precision library.

# Mingw32
%package -n mingw32-%{name1}
Summary:        %{summary}

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
Summary:        %{summary}

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

%files -n mingw32-%{name1}
%doc COPYING COPYING.LESSER NEWS README
%{mingw32_bindir}/libmpfr-6.dll
%{mingw32_libdir}/libmpfr.dll.a
%{mingw32_includedir}/*.h
%{mingw32_libdir}/pkgconfig/mpfr.pc

%files -n mingw64-%{name1}
%doc COPYING COPYING.LESSER NEWS README
%{mingw64_bindir}/libmpfr-6.dll
%{mingw64_libdir}/libmpfr.dll.a
%{mingw64_includedir}/*.h
%{mingw64_libdir}/pkgconfig/mpfr.pc

%changelog
%autochangelog
