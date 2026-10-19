%global source0_hash 105f02079b0b50034c759db34b473ecb5704ffa20a5486b60a8b7698128bfc69
Summary:        Library of Optimized Inner Loops, CPU optimized functions
Name: liboil
Version: 0.3.17
Release:        1%{?dist}
License: LicenseRef-Callaway-BSD
URL: http://liboil.freedesktop.org/
Source0:        http://liboil.freedesktop.org/download/%{name}-%{version}.tar.gz
Patch4: liboil-0.3.13-disable-ppc64-opts.patch
Patch5: liboil-configure-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
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

%define _lto_cflags -flto=auto -ffat-lto-objects
%configure
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n liboil-devel -f %{oreon_filedir}/liboil-devel.list

%changelog

%autochangelog
