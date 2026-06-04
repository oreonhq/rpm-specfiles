%global source0_hash none

# Fedora spec file for libmemcached-awesome from
#
# remirepo spec file for libmemcached-awesome
#
# Copyright (c) 2009-2023 Remi Collet
# License: CC-BY-SA-4.0
# https://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without               tests

%global libname              libmemcached

%global gh_commit            92d18858b417309f6bdee6bce464a4f3d6a375fd
%global gh_short             %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner             awesomized
%global gh_project           libmemcached

%global upstream_version     1.1.4
#global upstream_prever      beta3

Name:      %{libname}-awesome
Summary:   Client library and command line tools for memcached server
Version:   %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:   9%{?dist}
# SPDX:
License:   BSD-3-Clause
URL:       https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/refs/tags/%{gh_commit}.tar.gz#/%{gh_project}-%{version}-%{gh_short}.tar.gz

# Fix test with memcached 1.6.40
Patch0:    162.patch

BuildRequires: cmake >= 3.9
# Cannot use Ninja generator because of "multiple rules generate docs/man"
%global _cmake_generator "Unix Makefiles"
BuildRequires: make
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: python3-sphinx
BuildRequires: cyrus-sasl-devel
BuildRequires: flex
BuildRequires: bison
BuildRequires: memcached
BuildRequires: systemtap-sdt-devel
BuildRequires: libevent-devel > 2
BuildRequires: openssl-devel

Provides:      bundled(bobjenkins-hash)
# package rename
Obsoletes:     %{libname}-libs         < 1.1
Provides:      %{libname}-libs         = %{version}-%{release}
Provides:      %{libname}-libs%{?_isa} = %{version}-%{release}


%description
%{name} is a C/C++ client library and tools for the memcached
server (https://memcached.org/). It has been designed to be light
on memory usage, and provide full access to server side methods.

This is a resurrection of the original work from Brian Aker at libmemcached.org.


%package devel
Summary:    Header files and development libraries for %{name}

Requires:   cyrus-sasl-devel%{?_isa}
Requires:   %{name}%{?_isa} = %{version}-%{release}
# package rename
Obsoletes:  %{libname}-devel         < 1.1
Provides:   %{libname}-devel         = %{version}-%{release}
Provides:   %{libname}-devel%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and development libraries
for %{name}. If you like to develop programs using %{name}, 
you will need to install %{name}-devel.

Documentation: https://awesomized.github.io/libmemcached


%package tools
Summary:    %{name} tools

Requires:   %{name}%{?_isa} = %{version}-%{release}
# package rename
Obsoletes:  %{libname}         < 1.1
Provides:   %{libname}         = %{version}-%{release}
Provides:   %{libname}%{?_isa} = %{version}-%{release}

%description tools
This package contains the %{libname}-awesome command line tools:

memaslap    Load testing and benchmarking a server
memcapable  Checking a Memcached server capibilities and compatibility
memcat      Copy the value of a key to standard output
memcp       Copy data to a server
memdump     Dumping your server
memerror    Translate an error code to a string
memexist    Check for the existance of a key
memflush    Flush the contents of your servers
memparse    Parse an option string
memping     Test to see if a server is available.
memrm       Remove a key(s) from the server
memslap     Generate testing loads on a memcached cluster
memstat     Dump the stats of your servers to standard output
memtouch    Touches a key


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{gh_project}-%{gh_commit}

# drop test hanging in mock
# and requiring some memcached build options
rm test/tests/memcached/sasl.cpp
rm test/tests/memcached/regression/lp_001-630-615.cpp
# temporarily ignore with erratic failure
rm test/tests/memcached/udp.cpp
rm test/tests/memcached/regression/lp_000-583-031.cpp
rm test/tests/memcached/regression/gh-php-memcached_0531.cpp

%patch -P0 -p1


%build
%cmake \
  -DBUILD_TESTING:BOOL=ON \
  -DBUILD_DOCS_MAN:BOOL=ON \
  -DBUILD_DOCS_MANGZ:BOOL=OFF \
  -DENABLE_SASL:BOOL=ON \
  -DENABLE_DTRACE:BOOL=ON \
  -DENABLE_OPENSSL_CRYPTO:BOOL=ON \
  -DENABLE_HASH_HSIEH:BOOL=ON \
  -DENABLE_HASH_FNV64:BOOL=ON \
  -DENABLE_HASH_MURMUR:BOOL=ON \
  -DENABLE_MEMASLAP:BOOL=ON

%cmake_build


%install
%cmake_install

mv %{buildroot}%{_datadir}/%{name}/example.cnf support

rm -r %{buildroot}%{_datadir}/doc/%{name}/


%check
%if %{with tests}
: Run test suite
%ctest
%else
: Skip test suite
%endif


%files tools
%{_bindir}/mem*
%{_mandir}/man1/mem*

%files
%license LICENSE
%{_libdir}/libhashkit.so.2*
%{_libdir}/libmemcached.so.11*
%{_libdir}/libmemcachedprotocol.so.0*
%{_libdir}/libmemcachedutil.so.2*
%exclude %{_libdir}/libp9y.a

%files devel
%doc example
%doc *.md
%doc AUTHORS
%doc support/example.cnf
%{_includedir}/libmemcached
%{_includedir}/libmemcached-1.0
%{_includedir}/libhashkit
%{_includedir}/libhashkit-1.0
%{_includedir}/libmemcachedprotocol-0.0
%{_includedir}/libmemcachedutil-1.0
%{_libdir}/libhashkit.so
%{_libdir}/libmemcached.so
%{_libdir}/libmemcachedprotocol.so
%{_libdir}/libmemcachedutil.so
%{_libdir}/pkgconfig/libmemcached.pc
%{_datadir}/aclocal/ax_libmemcached.m4
%{_mandir}/man3/libmemcached*
%{_mandir}/man3/libhashkit*
%{_mandir}/man3/memcached*
%{_mandir}/man3/hashkit*
%dir     %{_libdir}/cmake/%{name}
         %{_libdir}/cmake/%{name}/lib*
%exclude %{_libdir}/cmake/%{name}/p9y*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{upstream_version}%{?upstream_prever:~%{upstream_prever}}-9
- Prepare for Oreon 11 (RP1)
