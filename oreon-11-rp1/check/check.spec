%global source0_hash 998d355294bb94072f40584272cf4424571c396c631620ce463f6ea97aa67d2e
%bcond mingw %[0%{?fedora}]
%bcond bootstrap 0
Name:           check
Version:        0.15.2
Release:        21%{?dist}
Summary:        A unit test framework for C
License:        LGPL-2.1-or-later
URL:            https://libcheck.github.io/check/
VCS:            git:https://github.com/libcheck/check.git
Source0:        https://github.com/libcheck/check/archive/refs/tags/0.15.2.tar.gz#/check-0.15.2.tar.gz
Patch0:         %{name}-0.11.0-info-in-builddir.patch
Patch1:         %{name}-0.15.2-texinfo.patch
Patch2:         %{name}-0.11.0-fp.patch
%if %{without bootstrap}
%endif
%if %{with mingw}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  patchutils
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsubunit)
BuildRequires:  texinfo
# /oreon:deps
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

mkdir autotools_build
cd autotools_build
%global _configure ../configure
%configure \
%if %{with bootstrap}
  --disable-build-docs \
%endif
  --disable-timeout-tests
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
%oreon_autofiles check-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles check-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles check-checkmk usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-check usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-check usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

cd autotools_build
export LD_LIBRARY_PATH=$PWD/src/.libs
%ifnarch s390x
make check
%endif
rm -rf checkmk/test/check_checkmk*
rm -rf checkmk/test/empty_input
cd -
%files -f %{oreon_filedir}/main.list
%files -n check-devel -f %{oreon_filedir}/check-devel.list
%files -n check-static -f %{oreon_filedir}/check-static.list
%files -n check-checkmk -f %{oreon_filedir}/check-checkmk.list
%files -n mingw32-check -f %{oreon_filedir}/mingw32-check.list
%files -n mingw64-check -f %{oreon_filedir}/mingw64-check.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.15.2-21
- Prepare for Oreon 11 (RP1)
