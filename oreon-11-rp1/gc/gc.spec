%global source0_hash none

Summary: Garbage collector for C and C++
Name:    gc
Version: 8.2.6
Release: 6%{?dist}

# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL:     https://www.hboehm.info/gc/
Source0:        https://github.com/ivmai/bdwgc/releases/download/v8.2.6/gc-8.2.6%{?pre}.tar.gz

## upstreamable patches

## downstream patches

BuildRequires: automake libtool
BuildRequires: gcc-c++
## https://www.hboehm.info/gc/ says: "Starting with 8.0, libatomic_ops is only required if the compiler does not understand C atomics."
#BuildRequires: pkgconfig(atomic_ops) >= 7.4
BuildRequires: pkgconfig
BuildRequires: make

# rpmforge compatibility
Obsoletes: libgc < %{version}-%{release}
Provides:  libgc = %{version}-%{release}

%description
The Boehm-Demers-Weiser conservative garbage collector can be
used as a garbage collecting replacement for C malloc or C++ new.

%package devel
Summary: Libraries and header files for %{name} development
Requires: %{name}%{?_isa} = %{version}-%{release}
Obsoletes: libgc-devel < %{version}-%{release}
Provides:  libgc-devel = %{version}-%{release}
%description devel
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n gc-%{version}%{?pre} -p1


%build
# refresh auto*/libtool to purge rpaths
rm -f libtool libtool.m4
autoreconf -i -f

# see https://bugzilla.redhat.com/689877
CPPFLAGS="-DUSE_GET_STACKBASE_FOR_MAIN $CPPFLAGS"
# https://github.com/ivmai/bdwgc/commit/3ea130ae326d02e224921017d3ee9c287fd4e670
# WAS https://bugzilla.redhat.com/show_bug.cgi?id=1551671
CPPFLAGS="-DDONT_UNDEF_EXCEPTIONS $CPPFLAGS"
export CPPFLAGS

%configure \
  --disable-docs \
  --enable-cplusplus \
  --enable-large-config \
  --enable-threads=posix

%make_build


%install
%make_install

install -p -D -m644 doc/gc.man  %{buildroot}%{_mandir}/man3/gc.3

## Unpackaged files
rm -rfv %{buildroot}%{_datadir}/gc/
rm -fv  %{buildroot}%{_libdir}/lib*.la


%check
%ifarch %{arm}
## cordtest segfaults
%global arch_ignore ||:
%endif
## cordtest segfaults or hangs on ix86
## gctest sometimes(?) hangs on armv7hl, aarch64, ppc64le
%ifnarch %{arm} aarch64 %{ix86} ppc64le
make check %{?arch_ignore}
%endif


%ldconfig_scriptlets

%files
%{_libdir}/libcord.so.1*
%{_libdir}/libgc.so.1*
%{_libdir}/libgccpp.so.1*
%{_libdir}/libgctba.so.1*

%files devel
%doc doc/README.environment doc/README.linux
%doc doc/*.md
%{_includedir}/gc.h
%{_includedir}/gc_cpp.h
%{_includedir}/gc/
%{_libdir}/libcord.so
%{_libdir}/libgc.so
%{_libdir}/libgccpp.so
%{_libdir}/libgctba.so
%{_libdir}/pkgconfig/bdw-gc.pc
%{_mandir}/man3/gc.3*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.2.6-6
- Prepare for Oreon 11 (RP1)
