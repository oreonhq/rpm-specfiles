%global source0_hash 4f7f217f057ce655ff22559ad221a0fd8ef84ad1fc5fcb6990cecc333aa1635d
%{?mingw_package_header}
%global run_tests 0
%global   libltdl_major  7
%global   patchlevel  %{nil}
Summary:        Runtime libraries for GNU Libtool Dynamic Module Loader
Name:     mingw-libltdl
Version:  2.4.7
Release:        1%{?dist}
License:  LicenseRef-Callaway-LGPLv2+
Source0:        http://ftp.gnu.org/gnu/libtool/libtool-%{version}.tar.xz
URL:      http://www.gnu.org/software/libtool/
%if %run_tests
%endif
BuildArch:      noarch
%{?mingw_debug_package}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description
The mingw-libltdl package contains the GNU Libtool Dynamic Module Loader, a
library that provides a consistent, portable interface which simplifies the
process of using dynamic modules, for the mingw cross compilation
environment.

These runtime libraries are needed by programs that link directly to the
system-installed ltdl libraries; they are not needed by software built using
the rest of the GNU Autotools (including GNU Autoconf and GNU Automake).

%package -n mingw32-libltdl
Summary:        Runtime libraries for GNU Libtool Dynamic Module Loader
%description -n mingw32-libltdl
The mingw32-libltdl package contains the GNU Libtool Dynamic Module Loader, a
library that provides a consistent, portable interface which simplifies the
process of using dynamic modules, for the mingw32 cross compilation
environment.

These runtime libraries are needed by programs that link directly to the
system-installed ltdl libraries; they are not needed by software built using
the rest of the GNU Autotools (including GNU Autoconf and GNU Automake).

%package -n mingw64-libltdl
Summary:        Runtime libraries for GNU Libtool Dynamic Module Loader
%description -n mingw64-libltdl
The mingw64-libltdl package contains the GNU Libtool Dynamic Module Loader, a
library that provides a consistent, portable interface which simplifies the
process of using dynamic modules, for the mingw64 cross compilation
environment.

These runtime libraries are needed by programs that link directly to the
system-installed ltdl libraries; they are not needed by software built using
the rest of the GNU Autotools (including GNU Autoconf and GNU Automake).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n libtool-%{version}%{?patchlevel} -q

%build

cd libltdl
export CXX=false
export F77=false
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%{mingw_configure} --enable-shared --enable-ltdl-install
%{mingw_make} #%{?_smp_mflags}
%check

%if %run_tests
cd libltdl
make check VERBOSE=yes > make_check.log 2>&1 || (cat make_check.log && false)
%endif
%install
cd libltdl
%mingw_make_install DESTDIR=%{buildroot}
rm -f %{buildroot}%{mingw32_libdir}/libltdl.a
rm -f %{buildroot}%{mingw64_libdir}/libltdl.a
find $RPM_BUILD_ROOT -name "*.la" -delete
%oreon_autofiles mingw32-libltdl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libltdl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libltdl -f %{oreon_filedir}/mingw32-libltdl.list
%files -n mingw64-libltdl -f %{oreon_filedir}/mingw64-libltdl.list

%changelog

%autochangelog
