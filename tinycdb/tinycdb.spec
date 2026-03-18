Name:		tinycdb
Summary:	Utility and library for manipulating constant databases
Version:	0.80
Release:	6%{?dist}
License:	LicenseRef-Fedora-Public-Domain
URL:		http://www.corpit.ru/mjt/tinycdb.html
Source0:	http://www.corpit.ru/mjt/%{name}/%{name}-%{version}.tar.gz
# taken from the 0.77 tarball
Source1:	libcdb.pc

BuildRequires:	make
BuildRequires:	gcc
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

%files
%doc NEWS
%{_bindir}/cdb
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_libdir}/*.so.*

%files devel
%{_includedir}/*.h
%{_mandir}/man3/*.3*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.80-6
- Prepare for Oreon 11 (RP1)
