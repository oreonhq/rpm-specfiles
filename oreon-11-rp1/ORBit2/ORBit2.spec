%global source0_hash 55c900a905482992730f575f3eef34d50bda717c197c97c08fa5a6eafd857550
%define libidl_version 0.8.2-1
%define glib2_version 2.2.0
Summary:        A high-performance CORBA Object Request Broker
Name: ORBit2
Version: 2.14.19
Release:        1%{?dist}
Source0:        http://download.gnome.org/sources/ORBit2/2.14/%{name}-%{version}.tar.bz2
License: LGPL-2.0-or-later AND GPL-2.0-or-later
URL: http://www.gnome.org/projects/ORBit2
Patch0: ORBit2-2.14.3-multilib.patch
Patch1: ORBit2-2.14.3-ref-leaks.patch
Patch2: ORBit2-make-j-safety.patch
Patch3: ORBit2-allow-deprecated.patch
Patch4: ORBit2-configure-c99.patch
Patch5: pointer-type.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  glib2-devel
BuildRequires:  gtk-doc
BuildRequires:  libIDL-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
ORBit is a high-performance CORBA (Common Object Request Broker
Architecture) ORB (object request broker). It allows programs to
send requests and receive replies from other programs, regardless
of the locations of the two programs. CORBA is an architecture that
enables communication between program objects, regardless of the
programming language they're written in or the operating system they
run on.

You will need to install this package and ORBit-devel if you want to
write programs that use CORBA technology.

%package devel
Summary: Development libraries, header files and utilities for ORBit
Requires: %{name} = %{version}-%{release}
Requires: indent
Requires: libIDL-devel >= %{libidl_version}
Requires: glib2-devel >= %{glib2_version}
Requires: pkgconfig
Requires: automake
Conflicts: ORBit-devel <= 1:0.5.8
%description devel
ORBit is a high-performance CORBA (Common Object Request Broker
Architecture) ORB (object request broker) with support for the
C language.

This package contains the header files, libraries and utilities
necessary to write programs that use CORBA technology. If you want to
write such programs, you'll also need to install the ORBIT package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p1 -b .multilib
%patch -P 1 -p1 -b .ref-leaks
%patch -P 2 -p1 -b .make-j
%patch -P 3 -p1 -b .deprecated
%patch -P 4 -p1
%patch -P 5 -p0

%build

%configure --disable-gtk-doc --enable-purify --disable-static --disable-rpath
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/ORBit-2.0/*.*a
rm -f $RPM_BUILD_ROOT%{_libdir}/orbit-2.0/*.*a
%define wordsize %{__isa_bits}
mv $RPM_BUILD_ROOT%{_includedir}/orbit-2.0/orbit/orbit-config.h \
   $RPM_BUILD_ROOT%{_includedir}/orbit-2.0/orbit/orbit-config-%{wordsize}.h
cat >$RPM_BUILD_ROOT%{_includedir}/orbit-2.0/orbit/orbit-config.h <<EOF
EOF
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libORBitCosNaming-2.so.0.1.0
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/libORBit-imodule-2.so.0.0.0
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/orbit-2.0/Everything_module.so
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/ior-decode-2
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/typelib-dump
%ldconfig_scriptlets
%oreon_autofiles ORBit2-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ORBit2-devel -f %{oreon_filedir}/ORBit2-devel.list

%changelog

%autochangelog
