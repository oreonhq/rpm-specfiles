%global source0_hash 4f1a66e746cbe54ff3c2fbada5843df4fbbbe7481d80be003e8d11161935ab74

Name: libasyncns
Version: 0.8
Release: 32%{?dist}
Summary: Asynchronous Name Service Library
Source0:        http://0pointer.de/lennart/projects/libasyncns/libasyncns-%{version}.tar.gz
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
