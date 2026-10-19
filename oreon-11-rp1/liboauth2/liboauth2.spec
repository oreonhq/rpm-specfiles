%global source0_hash 0ebc027aaad9cb0f955ac7d9cf91045056b33bcc5e80e3b4cd2d66eddc903104
Name: liboauth2
Version: 2.4.0
Release:        1%{?dist}
Summary:        Generic library to build OAuth 2.x and OpenID Connect servers and clients in C
License: Apache-2.0
URL: https://github.com/OpenIDC/liboauth2
Source0:        https://github.com/OpenIDC/liboauth2/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: 0001-Fix-use-of-strchr-with-new-GCC.patch
Patch1: 0001-Few-more-fixes-for-discarded-qualifiers-in-tests.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  check
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gdb-minimal
BuildRequires:  httpd-devel
BuildRequires:  libtool
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  openldap-devel
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(cjose)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(openssl)
# /oreon:deps
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
%global oreon_srcdir liboauth2-%{version}
%oreon_prep
%build

autoreconf -ivf
%configure --with-apache --without-redis --without-memcache
%make_build
%check

%make_build check
%install
%make_install
rm -vf %{buildroot}%{_libdir}/*.la %{buildroot}%{_libdir}/*.a
find %{buildroot}%{_includedir}/oauth2 -name '*.h' | grep -v apache | sed 's@%{buildroot}@@g' > file.headers
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n liboauth2-devel -f %{oreon_filedir}/liboauth2-devel.list
%files -n liboauth2-apache -f %{oreon_filedir}/liboauth2-apache.list
%files -n liboauth2-apache-devel -f %{oreon_filedir}/liboauth2-apache-devel.list

%changelog

%autochangelog
