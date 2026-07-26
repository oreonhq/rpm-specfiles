%global source0_hash 4f7f217f057ce655ff22559ad221a0fd8ef84ad1fc5fcb6990cecc333aa1635d

%{?mingw_package_header}

# Define this to run tests (requires Wine, and won't work inside mock or Koji).
# Note: As of libtool-1.5.26, libltdl does not contain any tests at all.
%global run_tests 0

# Major soname, or the number in libltdl-N.dll
%global   libltdl_major  7

# Tarball patchlevel (a, b, etc. or nothing at all)
#global   patchlevel  b
%global   patchlevel  %{nil}

Summary:  Runtime libraries for GNU Libtool Dynamic Module Loader
Name:     mingw-libltdl
Version:  2.4.7
Release:  10%{?dist}
# Even though the source package contains files under
# "GPLv2+ and LGPLv2+ and GFDL", the binary RPM only ships LGPLv2+ code.
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:  LicenseRef-Callaway-LGPLv2+

Source:   http://ftp.gnu.org/gnu/libtool/libtool-%{version}%{?patchlevel}.tar.xz
URL:      http://www.gnu.org/software/libtool/

BuildRequires: make
BuildRequires:  autoconf
BuildRequires:  automake

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gcc

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gcc

%if %run_tests
BuildRequires:  wine
%endif

BuildArch:      noarch

# Use a ? to expand to nothing if undefined, enabling F13 mock builds on F11.
# This avoids the trick of hiding the macro in %%description which in turn
# confuses the koji webinterface.
%{?mingw_debug_package}

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
# export PATH=%%{mingw32_bindir}:$PATH

#./bootstrap

cd libltdl
export CXX=false
export F77=false
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
# dumb redhat-rpm-config replaces config.{sub,guess} with ancient ones in %%configure, use ./configure instead:
# %%mingw32_configure does not make that error :)
%{mingw_configure} --enable-shared --enable-ltdl-install
# build not smp safe:
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

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

%files -n mingw32-libltdl
%doc AUTHORS NEWS THANKS TODO ChangeLog
%doc libltdl/COPYING.LIB libltdl/README
%{mingw32_bindir}/libltdl-%{libltdl_major}.dll
%dir %{mingw32_includedir}/libltdl
%{mingw32_includedir}/libltdl/lt_dlloader.h
%{mingw32_includedir}/libltdl/lt_error.h
%{mingw32_includedir}/libltdl/lt_system.h
%{mingw32_includedir}/ltdl.h
%{mingw32_libdir}/libltdl.dll.a

%files -n mingw64-libltdl
%doc AUTHORS NEWS THANKS TODO ChangeLog
%doc libltdl/COPYING.LIB libltdl/README
%{mingw64_bindir}/libltdl-%{libltdl_major}.dll
%dir %{mingw64_includedir}/libltdl
%{mingw64_includedir}/libltdl/lt_dlloader.h
%{mingw64_includedir}/libltdl/lt_error.h
%{mingw64_includedir}/libltdl/lt_system.h
%{mingw64_includedir}/ltdl.h
%{mingw64_libdir}/libltdl.dll.a

%changelog
%autochangelog
