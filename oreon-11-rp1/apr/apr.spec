%global source0_hash 49030d92d2575da735791b496dc322f3ce5cff9494779ba8cc28c7f46c5deb32

%define aprver 1

%bcond tests 1

# Arches on which the multilib apr.h hack is needed:
%define multilib_arches %{ix86} ia64 ppc ppc64 s390 s390x x86_64

# Similar issue to https://bugzilla.redhat.com/show_bug.cgi?id=2043092
%undefine _package_note_flags

# Disable .la file removal since the .la file is exported via apr-config.
%global __brp_remove_la_files %nil

Summary: Apache Portable Runtime library
Name: apr
Version: 1.7.6
Release: 5%{?dist}
# Apache-2.0: everything
# ISC: network_io/apr-1.4.6/network_io/unix/inet_?to?.c
# BSD-4-Clause-UC:  strings/apr_snprintf.c, strings/apr_fnmatch.c,
#                   include/apr_fnmatch.h, misc/unix/getopt.c,
#                   file_io/unix/mktemp.c, strings/apr_strings.c
# Zlib: strings/apr_strnatcmp.c, include/apr_strings.h
# Caldera-no-preamble: strings/apr_snprintf.c
License: Apache-2.0 AND (BSD-4-Clause-UC AND ISC AND Zlib AND Caldera-no-preamble)
URL: https://apr.apache.org/
Source0: https://www.apache.org/dist/apr/%{name}-%{version}.tar.bz2
Source1: apr-wrapper.h
Patch1: apr-1.7.2-libdir.patch
Patch2: apr-1.2.7-pkgconf.patch
Patch3: apr-1.7.0-deepbind.patch
Patch4: apr-1.7.6-autoconf.patch
BuildRequires: gcc, autoconf, libtool, libuuid-devel, python3
BuildRequires: make
BuildRequires: libxcrypt-devel

%description
The mission of the Apache Portable Runtime (APR) is to provide a
free library of C data structures and routines, forming a system
portability layer to as many operating systems as possible,
including Unices, MS Win32, BeOS and OS/2.

%package devel
Summary: APR library development kit
Conflicts: subversion-devel < 0.20.1-2
Requires: apr = %{version}-%{release}, pkgconfig

%description devel
This package provides the support files which can be used to 
build applications using the APR library.  The mission of the
Apache Portable Runtime (APR) is to provide a free library of 
C data structures and routines.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -S gendiff

%build
# regenerate configure script etc.
./buildconf

%configure \
        --includedir=%{_includedir}/apr-%{aprver} \
        --with-installbuilddir=%{_libdir}/apr-%{aprver}/build \
        --with-devrandom=/dev/urandom \
        --disable-static \
        --disable-sctp

# Sanity tests to catch subtle configure script failures:
#
# 1. Fail if apr_strtoi64() is not using libc strtol/strtoll
strfn=`echo XXX APR_INT64_STRFN | cpp -I./include -I./include/arch/unix -include include/arch/unix/apr_private.h \
            | sed -n '/^XXX/{s/XXX //;p;}'`
: APR_INT64_STRFN detected as $strfn
if test "x$strfn" = "x"; then
    cat config.log
    : configure failed to detect working strtol, bailing.
fi

# 2. Fail if LFS support isn't present in a 32-bit build, since this
# breaks ABI and the soname doesn't change: see #254241
if grep 'define SIZEOF_VOIDP 4' include/apr.h \
   && ! grep off64_t include/apr.h; then
    cat config.log
    : LFS support not present in 32-bit build
    exit 1
fi

%{make_build}

%install
rm -rf $RPM_BUILD_ROOT
%{make_install}

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/aclocal
for f in find_apr.m4 apr_common.m4; do
 install -p -m 644 build/$f $RPM_BUILD_ROOT/%{_datadir}/aclocal
done

# Trim exported dependecies
sed -ri '/^dependency_libs/{s,-l(uuid|crypt) ,,g}' \
      $RPM_BUILD_ROOT%{_libdir}/libapr*.la
sed -ri '/^LIBS=/{s,-l(uuid|crypt) ,,g;s/  */ /g}' \
      $RPM_BUILD_ROOT%{_bindir}/apr-%{aprver}-config
sed -ri '/^Libs/{s,-l(uuid|crypt) ,,g}' \
      $RPM_BUILD_ROOT%{_libdir}/pkgconfig/apr-%{aprver}.pc

%ifarch %{multilib_arches}
# Ugly hack to allow parallel installation of 32-bit and 64-bit apr-devel 
# packages:
mv $RPM_BUILD_ROOT%{_includedir}/apr-%{aprver}/apr.h \
   $RPM_BUILD_ROOT%{_includedir}/apr-%{aprver}/apr-%{_arch}.h
install -c -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_includedir}/apr-%{aprver}/apr.h
%endif

# Unpackaged files:
rm -f $RPM_BUILD_ROOT%{_libdir}/apr.exp \
      $RPM_BUILD_ROOT%{_libdir}/libapr-*.a

# Additionally packaged (see https://bugzilla.redhat.com/1669589) --
sed -i '1s,/.*,/usr/bin/python3,' build/gen-build.py
for f in build/gen-build.py build/install.sh build/config.*; do
    install -c -m755 $f $RPM_BUILD_ROOT%{_libdir}/apr-%{aprver}/build
done

%check
grep ^cross_compiling=no $RPM_BUILD_ROOT%{_bindir}/apr-%{aprver}-config

%if %{with tests}
pushd test
  make %{?_smp_mflags}
  ./testall -v -q
popd
%endif

%ldconfig_scriptlets

%files
%doc CHANGES LICENSE NOTICE README*
%{_libdir}/libapr-%{aprver}.so.*

%files devel
%doc docs/APRDesign.html docs/canonical_filenames.html
%doc docs/incomplete_types docs/non_apr_programs
%{_bindir}/apr-%{aprver}-config
%{_libdir}/libapr-%{aprver}.la
%{_libdir}/libapr-%{aprver}.so
%{_libdir}/pkgconfig/*.pc
%dir %{_libdir}/apr-%{aprver}
%dir %{_libdir}/apr-%{aprver}/build
%{_libdir}/apr-%{aprver}/build/*
%dir %{_includedir}/apr-%{aprver}
%{_includedir}/apr-%{aprver}/*.h
%{_datadir}/aclocal/*.m4

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7.6-5
- Prepare for Oreon 11 (RP1)
