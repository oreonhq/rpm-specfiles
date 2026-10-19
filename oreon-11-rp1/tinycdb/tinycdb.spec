%global source0_hash 469de2d445bf54880f652f4b6dc95c7cdf6f5502c35524a45b2122d70d47ebc2
Name:		tinycdb
Summary:        Utility and library for manipulating constant databases
Version:	0.81
Release:        1%{?dist}
License:	LicenseRef-Fedora-Public-Domain
URL:		http://www.corpit.ru/mjt/tinycdb.html
Source0:        http://www.corpit.ru/mjt/%{name}/%{name}-%{version}.tar.gz
Source1:	libcdb.pc
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
tinycdb is a small, fast and reliable utility and subroutine library for
creating and reading constant databases. The database structure is tuned
for fast reading.

This package contains tinycdb utility and shared library.

%package devel
Summary:	Development files for tinycdb
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
tinycdb is a small, fast and reliable utility set and subroutine
library for creating and reading constant databases.

This package contains tinycdb development library and header file for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
cp %{SOURCE1} .
# Fix libdir pathing in pkgconfig file.
sed -i -e 's\/lib\/%{_lib}\g' libcdb.pc

%build

make %{?_smp_mflags} staticlib sharedlib cdb-shared CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}"
%install
mkdir -p %{buildroot}%{_libdir}
make DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{_libdir} mandir=%{_mandir} \
	install install-sharedlib INSTALLPROG=cdb-shared CP="cp -p"
chmod +x %{buildroot}%{_libdir}/*.so.*
rm -f %{buildroot}%{_libdir}/lib*.a
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cp -p libcdb.pc %{buildroot}%{_libdir}/pkgconfig/libcdb.pc
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n tinycdb-devel -f %{oreon_filedir}/tinycdb-devel.list

%changelog

%autochangelog
