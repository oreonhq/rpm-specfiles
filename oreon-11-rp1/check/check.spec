%global source0_hash 998d355294bb94072f40584272cf4424571c396c631620ce463f6ea97aa67d2e

%bcond mingw %[0%{?fedora}]

# Build without documentation for bootstrapping purposes
%bcond bootstrap 0

Name:           check
Version:        0.15.2
Release:        21%{?dist}
Summary:        A unit test framework for C
License:        LGPL-2.1-or-later
URL:            https://libcheck.github.io/check/
VCS:            git:https://github.com/libcheck/check.git
# The upstream tarball includes an index.html and the web/ folder with files
# licensed CC-BY-NC.  This license is not allowed in Fedora
# Our tarball are the same sources with index.html and web/ removed.
# Easiest way to verify: unpack both tarballs and run
#    diff -r check-0.15.2 upstream-check-0.15.2
# Source:       https://github.com/libcheck/check/archive/{version}/{name}-{version}.tar.gz
Source:        https://github.com/libcheck/check/archive/refs/tags/0.15.2/check-0.15.2.tar.gz
# Only needed for autotools in Fedora
Patch0:         %{name}-0.11.0-info-in-builddir.patch
# Fix a texinfo error due to a missing @end verbatim
# https://github.com/libcheck/check/issues/360
# https://github.com/libcheck/check/pull/361
Patch1:         %{name}-0.15.2-texinfo.patch
# Fix test failures due to varying floating point behavior across platforms
Patch2:         %{name}-0.11.0-fp.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  patchutils
BuildRequires:  pkgconfig
%if ! 0%{?rhel}
BuildRequires:  pkgconfig(libsubunit)
%endif
%if %{without bootstrap}
BuildRequires:  texinfo
%endif

%if %{with mingw}
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
%endif

%description
Check is a unit test framework for C. It features a simple interface for
defining unit tests, putting little in the way of the developer.  Tests are
run in a separate address space, so Check can catch both assertion failures
and code errors that cause segmentation faults or other signals.  The output
from unit tests can be used within source code editors and IDEs.

%package devel
Summary:        Libraries and headers for developing programs with check
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-static%{?_isa} = %{version}-%{release}

%description devel
Libraries and headers for developing programs with check

%package static
Summary:        Static libraries of check

%description static
Static libraries of check.

%package checkmk
Summary:        Translate concise versions of test suites into C programs
License:        checkmk
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description checkmk
The checkmk binary translates concise versions of test suites into C programs
suitable for use with the Check unit test framework.

%if %{with mingw}
%package -n mingw32-check
Summary:        Libraries and headers for developing programs with check
BuildArch: noarch

%description -n mingw32-check
MinGW libraries and headers for developing programs with check

%package -n mingw64-check
Summary:        Libraries and headers for developing programs with check
BuildArch: noarch

%description -n mingw64-check
MinGW libraries and headers for developing programs with check

%{?mingw_debug_package}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -N
rm -f index.html
rm -rf web
%if 0%{?fedora}
%patch -P0 -p1 -b .info-in-builddir
%endif
%if %{without bootstrap}
%patch -P1 -p1
%endif
%autopatch -m2 -p1

%conf
# Fix detection of various time-related function declarations
sed -e '/DECLS(\[a/s|)|,,,[AC_INCLUDES_DEFAULT\n[#include <time.h>\n #include <sys/time.h>]]&|' \
    -i configure.ac

# Avoid an obsolescence warning
sed -i 's/fgrep/grep -F/' Makefile.am

# Get rid of version control files
find . -name .cvsignore -delete

# Regenerate configure due to patch 0
autoreconf -ivf

# Fix libdir for the cmake build
sed -i 's,set(libdir .*),set(libdir "%{_libdir}"),' CMakeLists.txt

%build
# The autotools build does not create the cmake files.
# The cmake build does not create the info or aclocal files.
# Therefore we build with both and combine the results to get everything.
mkdir autotools_build
cd autotools_build
%global _configure ../configure
%configure \
%if %{with bootstrap}
  --disable-build-docs \
%endif
  --disable-timeout-tests

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build
cd -

%cmake -DCHECK_ENABLE_TIMEOUT_TESTS:BOOL=OFF
%cmake_build

%if %{with mingw}
%mingw_configure \
%if %{with bootstrap}
  --disable-build-docs
%endif
%mingw_make %{?_smp_mflags}
%endif

%install
cd autotools_build
%make_install
rm -rf %{buildroot}%{_libdir}
rm -rf %{buildroot}%{_infodir}/dir
rm -rf %{buildroot}%{_docdir}/%{name}
cd -

%cmake_install

# The library does not really depend on -pthread
sed -i 's/ -pthread//' %{buildroot}%{_libdir}/pkgconfig/check.pc

%if %{with mingw}
%mingw_make_install
%mingw_debug_install_post

rm -rf $RPM_BUILD_ROOT%{mingw32_bindir}/checkmk
rm -rf $RPM_BUILD_ROOT%{mingw64_bindir}/checkmk
rm -rf $RPM_BUILD_ROOT%{mingw32_infodir}/
rm -rf $RPM_BUILD_ROOT%{mingw64_infodir}/
rm -f $RPM_BUILD_ROOT%{mingw32_mandir}/man1/checkmk.1*
rm -f $RPM_BUILD_ROOT%{mingw64_mandir}/man1/checkmk.1*

%endif

%check
cd autotools_build
export LD_LIBRARY_PATH=$PWD/src/.libs
%ifnarch s390x
make check
%endif
# Don't need to package the sh, log or trs files
# when we scoop the other checkmk/test files for doc
rm -rf checkmk/test/check_checkmk*
# these files are empty
rm -rf checkmk/test/empty_input
cd -

%files
%doc AUTHORS NEWS
%license COPYING.LESSER
%{_libdir}/libcheck.so.0{,.*}
%if %{without bootstrap}
%{_infodir}/check*
%endif

%files devel
%doc doc/example
%{_includedir}/check.h
%{_includedir}/check_stdint.h
%{_libdir}/cmake/check/
%{_libdir}/libcheck.so
%{_libdir}/pkgconfig/check.pc
%{_datadir}/aclocal/check.m4

#check used to be static only, hence this.
%files static
%license COPYING.LESSER
%{_libdir}/libcheck.a

%files checkmk
%doc checkmk/README checkmk/examples
%doc checkmk/test
%{_bindir}/checkmk
%{_mandir}/man1/checkmk.1*

%if %{with mingw}
%files -n mingw32-check
%license COPYING.LESSER
%{mingw32_bindir}/libcheck-0.dll
%{mingw32_includedir}/check.h
%{mingw32_includedir}/check_stdint.h
%{mingw32_libdir}/libcheck.a
%{mingw32_libdir}/libcheck.dll.a
%{mingw32_libdir}/pkgconfig/check.pc
%{mingw32_datadir}/aclocal/check.m4
%{mingw32_docdir}

%files -n mingw64-check
%license COPYING.LESSER
%{mingw64_bindir}/libcheck-0.dll
%{mingw64_includedir}/check.h
%{mingw64_includedir}/check_stdint.h
%{mingw64_libdir}/libcheck.a
%{mingw64_libdir}/libcheck.dll.a
%{mingw64_libdir}/pkgconfig/check.pc
%{mingw64_datadir}/aclocal/check.m4
%{mingw64_docdir}
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.15.2-21
- Prepare for Oreon 11 (RP1)
