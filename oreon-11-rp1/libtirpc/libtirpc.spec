%global source0_hash 8839959bfcc7a0f4c609d8e4f53f1c67ae33de23775ec35beb39ff15adf11920
%define _root_libdir    /%{_lib}
Name:			libtirpc
Version:		1.3.8
Release:        1%{?dist}
Summary:        Transport Independent RPC Library
License:		SISSL AND BSD-3-Clause
URL:  			http://git.linux-nfs.org/?p=steved/libtirpc.git;a=summary
Source0:        https://downloads.sourceforge.net/libtirpc/libtirpc-%{version}.tar.bz2
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  krb5-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
# /oreon:deps
%description
This package contains SunLib's implementation of transport-independent
RPC (TI-RPC) documentation.  This library forms a piece of the base of 
Open Network Computing (ONC), and is derived directly from the 
Solaris 2.3 source.

TI-RPC is an enhanced version of TS-RPC that requires the UNIX System V 
Transport Layer Interface (TLI) or an equivalent X/Open Transport Interface 
(XTI).  TI-RPC is on-the-wire compatible with the TS-RPC, which is supported 
by almost 70 vendors on all major operating systems.  TS-RPC source code 
(RPCSRC 4.0) remains available from several internet sites.

%package devel
Summary:		Development files for the libtirpc library
Requires:		%{name}%{?_isa} = %{version}-%{release}
Requires:		pkgconfig
%description devel
This package includes header files and libraries necessary for
developing programs which use the tirpc library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# Remove .orig files
find . -name "*.orig" | xargs rm -f

%build

sh autogen.sh
autoreconf -fisv
%configure
make all
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc
mkdir -p %{buildroot}%{_root_libdir}
mkdir -p %{buildroot}%{_libdir}/pkgconfig
make install DESTDIR=%{buildroot} \
	libdir=%{_root_libdir} pkgconfigdir=%{_libdir}/pkgconfig
rm -f %{buildroot}%{_root_libdir}/*.{a,la}
mv %{buildroot}%{_mandir}/man3 %{buildroot}%{_mandir}/man3t
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libtirpc-devel -f %{oreon_filedir}/libtirpc-devel.list

%changelog

%autochangelog
