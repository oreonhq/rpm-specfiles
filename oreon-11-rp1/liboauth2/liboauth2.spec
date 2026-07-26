%global source0_hash 7225b9c4c732eae8716143ef910c67b39bd364a3547b32e5dd70d539d4eacd67

Name: liboauth2
Version: 2.2.0
Release: 2%{?dist}
Summary: Generic library to build OAuth 2.x and OpenID Connect servers and clients in C
License: Apache-2.0
URL: https://github.com/OpenIDC/liboauth2
Source0: https://github.com/OpenIDC/liboauth2/archive/v%{version}/%{name}-%{version}.tar.gz
# Upstream PR: https://github.com/OpenIDC/liboauth2/pull/65
Patch0: 0001-Fix-use-of-strchr-with-new-GCC.patch
# Upstream PR: https://github.com/OpenIDC/liboauth2/pull/66
Patch1: 0001-Few-more-fixes-for-discarded-qualifiers-in-tests.patch

BuildRequires: automake
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: httpd-devel
BuildRequires: libtool
BuildRequires: make
BuildRequires: check
BuildRequires: pkgconfig(check)
BuildRequires: pkgconfig(cjose)
BuildRequires: pkgconfig(jansson)
BuildRequires: pkgconfig(libcurl)
BuildRequires: openldap-devel
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: gdb-minimal
BuildRequires: libxcrypt-devel

%description
liboauth2 library provides primitives to create OAuth 2.x and OpenID Connect
servers and clients

%package devel
Summary: Library to build OAuth 2.x and OpenID Connect servers and clients in C
License: Apache-2.0
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
liboauth2 library provides primitives to create OAuth 2.x and OpenID Connect
servers and clients.

%package apache
Summary: OAuth 2.x and OpenID Connect library integration to Apache
License: Apache-2.0
Requires: %{name}%{?_isa} = %{version}-%{release}

%description apache
OAuth 2.x and OpenID Connect library integration to Apache web server

%package apache-devel
Summary: Development components to build Apache module with liboauth2 library
License: Apache-2.0
Requires: %{name}-apache%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description apache-devel
Development components to build Apache module with liboauth2 library

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n liboauth2-%{version}

%build
autoreconf -ivf
%configure --with-apache --without-redis --without-memcache
%make_build

%check
%make_build check

%install
%make_install
# Don't install static libraries and .la files
rm -vf %{buildroot}%{_libdir}/*.la %{buildroot}%{_libdir}/*.a
find %{buildroot}%{_includedir}/oauth2 -name '*.h' | grep -v apache | sed 's@%{buildroot}@@g' > file.headers

%files devel -f file.headers
%dir %{_includedir}/oauth2
%{_libdir}/pkgconfig/liboauth2.pc
%{_libdir}/liboauth2.so

%files
%{_libdir}/liboauth2.so.0
%{_libdir}/liboauth2.so.0.0.0
%license LICENSE
%doc README.md

%files apache
%{_libdir}/liboauth2_apache.so.0
%{_libdir}/liboauth2_apache.so.0.0.0

%files apache-devel
%{_includedir}/oauth2/apache.h
%{_libdir}/pkgconfig/liboauth2_apache.pc
%{_libdir}/liboauth2_apache.so

%changelog
%autochangelog
