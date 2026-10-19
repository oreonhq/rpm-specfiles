%global source0_hash b177a1c033bd907ea341db7e46eeee181acb73225bf58ada1966e7b4d50f657f
Name:		libgcroots
Version:	0.3.2
Release:        1%{?dist}
License:	Boehm-GC
URL:		https://github.com/uim/libgcroots
Source0:        https://github.com/uim/libgcroots/releases/download/%{version}/%{name}-%{version}.tar.bz2
Summary:        Roots acquisition library for Garbage Collector
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
libgcroots abstracts architecture-dependent part of garbage collector
roots acquisition such as register windows of SPARC and register stack
backing store of IA-64.
This library encourages to have own GC such as for small-footprint,
some application-specific optimizations, just learning or to test
experimental ideas.

%package devel
Summary:	Development files for libgcroots
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig
%description devel
libgcroots abstracts architecture-dependent part of garbage collector
roots acquisition such as register windows of SPARC and register stack
backing store of IA-64.

This package contains a header file and development library to help you
to develop any own GC.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm $RPM_BUILD_ROOT%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libgcroots-devel -f %{oreon_filedir}/libgcroots-devel.list

%changelog

%autochangelog
