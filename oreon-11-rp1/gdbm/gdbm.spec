%global source0_hash 6a24504a14de4a744103dcb936be976df6fbe88ccff26065e54c1c47946f4a5e
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: gdbm
Version: 1.26
Release: 1%{?dist}
Summary: GNU database routines
License: GPL-3.0-or-later
URL: https://www.gnu.org.ua/software/gdbm/
Source0: https://ftp.gnu.org/gnu/gdbm/gdbm-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
BuildRequires: readline-devel
%endif

%description
GNU dbm is a library of database functions that use extensible hashing and work similarly to the standard UNIX dbm functions.

%package devel
Summary: GNU database routines
Requires: gdbm%{?_isa} = %{version}-%{release}
Provides: pkgconfig(gdbm)

%description devel
GNU dbm is a library of database functions that use extensible hashing and work similarly to the standard UNIX dbm functions.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_configure --disable-static --disable-nls --enable-libgdbm-compat
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_infodir}

%files
%license COPYING
%{_bindir}/gdbm_dump
%{_bindir}/gdbm_load
%{_bindir}/gdbmtool
%{_libdir}/libgdbm.so.6
%{_libdir}/libgdbm.so.6.*
%{_libdir}/libgdbm_compat.so.4
%{_libdir}/libgdbm_compat.so.4.*
%{_mandir}/man1/gdbm_dump.1*
%{_mandir}/man1/gdbm_load.1*
%{_mandir}/man1/gdbmtool.1*
%{_mandir}/man3/gdbm.3*

%files devel
%{_includedir}/gdbm.h
%{_includedir}/dbm.h
%{_includedir}/ndbm.h
%{_libdir}/libgdbm.so
%{_libdir}/libgdbm_compat.so
%{_libdir}/pkgconfig/gdbm.pc
