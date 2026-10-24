%global source0_hash 80304b9c306ea799327f01d9a7549bdb28317789182631f1b54f4511b4206dd6
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libxcrypt
Version: 4.4.38
Release: 1%{?dist}
Summary: Extended crypt library
License: LGPL-2.1-or-later
URL: https://github.com/besser82/libxcrypt
Source0: https://github.com/besser82/libxcrypt/releases/download/v%{version}/libxcrypt-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: perl
%endif

%description
libxcrypt is a modern library for one-way hashing of passwords.

%package devel
Summary: Extended crypt library
Requires: libxcrypt%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libxcrypt)

%description devel
libxcrypt is a modern library for one-way hashing of passwords.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_configure --disable-static --enable-obsolete-api=glibc --enable-hashes=strong,glibc
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la

%files
%license COPYING.LIB
%{_libdir}/libcrypt.so.1
%{_libdir}/libcrypt.so.1.*
%{_libdir}/libcrypt.so.2
%{_libdir}/libcrypt.so.2.*
%{_mandir}/man5/crypt.5*

%files devel
%{_includedir}/crypt.h
%{_libdir}/libcrypt.so
%{_libdir}/pkgconfig/libxcrypt.pc
%{_mandir}/man3/crypt.3*
%{_mandir}/man3/crypt_r.3*
%{_mandir}/man3/crypt_ra.3*
%{_mandir}/man3/crypt_rn.3*
