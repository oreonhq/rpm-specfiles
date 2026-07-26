%global source0_hash 009115b0fc888dfe28903fecfe806707c544ccad6554ebabdeb3a1d88ec1e9d1

Summary: Library of Optimized Inner Loops, CPU optimized functions
Name: liboil
Version: 0.3.16
Release: 38%{?dist}
# See COPYING which details everything, various BSD licenses apply
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL: http://liboil.freedesktop.org/
Source: http://liboil.freedesktop.org/download/%{name}-%{version}.tar.gz

# https://bugzilla.redhat.com/show_bug.cgi?id=435771
Patch4: liboil-0.3.13-disable-ppc64-opts.patch
Patch5: liboil-configure-c99.patch

BuildRequires:  gcc
BuildRequires: glib2-devel, pkgconfig
BuildRequires: make

%description
Liboil is a library of simple functions that are optimized for various CPUs.
These functions are generally loops implementing simple algorithms, such as
converting an array of N integers to floating-poing numbers or multiplying
and summing an array of N numbers. Clearly such functions are candidates for
significant optimization using various techniques, especially by using
extended instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).

%package devel
Summary: Development files and static library for %{name}
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig, gtk-doc

%description devel
Liboil is a library of simple functions that are optimized for various CPUs.
These functions are generally loops implementing simple algorithms, such as
converting an array of N integers to floating-poing numbers or multiplying
and summing an array of N numbers. Clearly such functions are candidates for
significant optimization using various techniques, especially by using
extended instructions provided by modern CPUs (Altivec, MMX, SSE, etc.).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P4 -p0 -b .disable-ppc64-opts
%patch -P5 -p1

%build
# configure tests try to compile code containing ASMs to a .o file
# In an LTO world, that always works as compilation does not happen until
# link time.  As a result we get the wrong results from configure.
# This can be fixed by using -ffat-lto-objects
# -ffat-lto-objects forces compilation even with LTO.  It is the default
# for F33, but not expected to be enabled by default for F34
%define _lto_cflags -flto=auto -ffat-lto-objects

%configure
# Remove standard rpath from oil-bugreport
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/*.a

%ldconfig_post
%ldconfig_postun

%files
%doc AUTHORS COPYING BUG-REPORTING NEWS README
%{_libdir}/*.so.*

%files devel
%doc HACKING
%{_bindir}/oil-bugreport
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%doc %{_datadir}/gtk-doc/html/%{name}/

%changelog
%autochangelog
