Name: libasyncns
Version: 0.8
Release: 32%{?dist}
Summary: Asynchronous Name Service Library
Source0: http://0pointer.de/lennart/projects/libasyncns/libasyncns-%{version}.tar.gz
License: LGPL-2.1-or-later
Url: http://0pointer.de/lennart/projects/libasyncns/

BuildRequires:  gcc
BuildRequires: make
%description
A small and lightweight library that implements easy to use asynchronous
wrappers around the libc NSS functions getaddrinfo(), res_query() and related.

%package devel
Summary: Development Files for libasyncns Client Development
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
Development Files for libasyncns Client Development

%ldconfig_scriptlets

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT \( -name *.a -o -name *.la \) -exec rm {} \;
rm -rf $RPM_BUILD_ROOT/usr/share/doc/libasyncns/

%files
%doc README LICENSE
%{_libdir}/libasyncns.so.*

%files devel
%{_includedir}/asyncns.h
%{_libdir}/libasyncns.so
%{_libdir}/pkgconfig/libasyncns.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8-32
- Prepare for Oreon 11 (RP1)
