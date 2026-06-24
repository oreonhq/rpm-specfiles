%global source0_hash none

# remirepo/fedora spec file for mongo-c-driver
#
# SPDX-FileCopyrightText:  Copyright 2015-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%global gh_owner     mongodb
%global gh_project   mongo-c-driver
%global libname      libmongoc
%global soname       2
%global up_version   2.3.1
#global up_prever    rc0
# disabled as require a MongoDB server
%bcond_with          tests

# enable/disable man pages
%bcond_without       manpages

# disable for bootstrap (libmongocrypt needs libbson)
%bcond_without       libmongocrypt

%if 0%{?rhel} == 8
%bcond_with          libutf8proc
%else
%bcond_without       libutf8proc
%endif

Name:      mongo-c-driver
Summary:   Client library written in C for MongoDB
Version:   %{up_version}%{?up_prever:~%{up_prever}}
Release:   2%{?dist}
# See THIRD_PARTY_NOTICES
License:   Apache-2.0 AND ISC AND MIT AND Zlib
URL:       https://github.com/%{gh_owner}/%{gh_project}

Source0:   https://github.com/%{gh_owner}/%{gh_project}/archive/refs/tags/%{up_version}%{?up_prever:-%{up_prever}}.tar.gz

BuildRequires: cmake >= 3.15
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
# pkg-config may pull compat-openssl10
BuildRequires: openssl-devel
BuildRequires: pkgconfig(libsasl2)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(snappy)
%if %{with libutf8proc}
BuildRequires: pkgconfig(libutf8proc)
%endif
BuildRequires: pkgconfig(libzstd) >= 0.8.0
%if %{with tests}
BuildRequires: mongodb-server
BuildRequires: openssl
%endif
%if %{with libmongocrypt}
# grep VERSION_LESS src/*/CMakeLists.txt
# use 1.17 to ensure libbson2 is used
BuildRequires: cmake(mongocrypt) >= 1.17
%endif
BuildRequires: perl-interpreter
# From man pages
%if %{with manpages}
BuildRequires: python3
BuildRequires: python3-sphinx >= 5.0
%endif

Requires:   %{name}-libs%{?_isa} = %{version}-%{release}
# Sub package removed
Obsoletes:  %{name}-tools         < 1.3.0
Provides:   %{name}-tools         = %{version}
Provides:   %{name}-tools%{?_isa} = %{version}


%description
%{name} is a client library written in C for MongoDB.


%package libs
Summary:    Shared libraries for %{name}
%if %{without libutf8proc}
Provides:   bundled(libutf8proc) = 2.8.0
%endif
Provides:   bundled(uthash) = 2.3.0

%description libs
This package contains the shared libraries for %{name}.


%package devel
Summary:    Header files and development libraries for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   pkgconfig
Requires:   cmake-filesystem
Requires:   pkgconfig(libzstd)
Requires:   cmake(bson) = %{version}
%if %{with libmongocrypt}
Requires:   cmake(mongocrypt)
%endif
Requires:   openssl-devel
Requires:   pkgconfig(libsasl2)
%if %{with libutf8proc}
Requires:   pkgconfig(libutf8proc)
%endif

%description devel
This package contains the header files and development libraries
for %{name}.

Documentation: http://mongoc.org/libmongoc/%{version}/


%package -n libbson
Summary:    Building, parsing, and iterating BSON documents
# Modified (with bson allocator and some warning fixes and huge indentation
# refactoring) jsonsl is bundled <https://github.com/mnunberg/jsonsl>.
# jsonsl upstream likes copylib approach and does not plan a release
# <https://github.com/mnunberg/jsonsl/issues/14>.
Provides:   bundled(jsonsl)

%description -n libbson
This is a library providing useful routines related to building, parsing,
and iterating BSON documents <http://bsonspec.org/>.


%package -n libbson-devel
Summary:    Development files for %{name}
Requires:   libbson%{?_isa} = %{version}-%{release}
Requires:   pkgconfig
Requires:   cmake-filesystem

%description -n libbson-devel
This package contains libraries and header files needed for developing
applications that use %{name}.

Documentation: http://mongoc.org/libbson/%{version}/


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{up_version}%{?up_prever:-%{up_prever}}


%build
%cmake \
    -DBUILD_VERSION=%{up_version}%{?up_prever:-%{up_prever}} \
    -DENABLE_MONGOC:BOOL=ON \
    -DENABLE_SHM_COUNTERS:BOOL=ON \
    -DENABLE_SSL:STRING=OPENSSL \
    -DENABLE_SASL:STRING=CYRUS \
    -DENABLE_MONGODB_AWS_AUTH:STRING=ON \
    -DENABLE_CRYPTO_SYSTEM_PROFILE:BOOL=ON \
%if %{with manpages}
    -DENABLE_MAN_PAGES:BOOL=ON \
%else
    -DENABLE_MAN_PAGES:BOOL=OFF \
%endif
    -DENABLE_HTML_DOCS:BOOL=OFF \
    -DENABLE_SHARED:BOOL=ON \
    -DENABLE_STATIC:STRING=OFF \
    -DENABLE_ZLIB:STRING=SYSTEM \
    -DENABLE_ZSTD:STRING=ON \
    -DENABLE_SNAPPY:STRING=ON \
%if %{with tests}
    -DENABLE_TESTS:BOOL=ON \
%else
    -DENABLE_TESTS:BOOL=OFF \
%endif
    -DENABLE_EXAMPLES:BOOL=OFF \
    -DENABLE_UNINSTALL:BOOL=OFF \
%if %{with libmongocrypt}
    -DENABLE_CLIENT_SIDE_ENCRYPTION:BOOL=ON \
%else
    -DENABLE_CLIENT_SIDE_ENCRYPTION:BOOL=OFF \
%endif
    -DCMAKE_SKIP_RPATH:BOOL=ON \
%if %{with libutf8proc}
    -DUSE_BUNDLED_UTF8PROC:BOOL=OFF \
%else
    -DUSE_BUNDLED_UTF8PROC:BOOL=ON \
%endif
    -DENABLE_SRV:BOOL=ON \
    -DENABLE_MONGODB_AWS_AUTH:STRING=ON \
    -S .

%if 0%{?cmake_build:1}
%cmake_build
%else
make %{?_smp_mflags}
%endif


%install
%if 0%{?cmake_install:1}
%cmake_install
%else
make install DESTDIR=%{buildroot}
%endif

: Static library
rm -f  %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_libdir}/cmake/*static*
rm -rf %{buildroot}%{_libdir}/pkgconfig/*static*
: Documentation
rm -rf %{buildroot}%{_datadir}/%{name}


%check
ret=0

%if %{with tests}
: Run a server
mkdir dbtest
mongod \
  --journal \
  --ipv6 \
  --unixSocketPrefix /tmp \
  --logpath     $PWD/server.log \
  --pidfilepath $PWD/server.pid \
  --dbpath      $PWD/dbtest \
  --fork

: Run the test suite
export MONGOC_TEST_OFFLINE=on
export MONGOC_TEST_SKIP_MOCK=on
#export MONGOC_TEST_SKIP_SLOW=on

make check || ret=1

: Cleanup
[ -s server.pid ] && kill $(cat server.pid)
%endif

exit $ret



%files
%{_bindir}/mongoc2-stat

%files libs
%license COPYING
%license THIRD_PARTY_NOTICES
%{_libdir}/%{libname}2.so.%{soname}
%{_libdir}/%{libname}2.so.%{soname}.*

%files devel
%doc src/%{libname}/examples
%doc NEWS
%{_includedir}/mongoc-%{version}
%{_libdir}/%{libname}2.so
%{_libdir}/pkgconfig/mongoc2.pc
%{_libdir}/cmake/mongoc-%{version}
%if %{with manpages}
%{_mandir}/man3/mongoc*
%endif

%files -n libbson
%license COPYING
%license THIRD_PARTY_NOTICES
%{_libdir}/libbson2.so.%{soname}
%{_libdir}/libbson2.so.%{soname}.*

%files -n libbson-devel
%doc src/libbson/examples
%doc src/libbson/NEWS
%{_includedir}/bson-%{version}
%{_libdir}/libbson*.so
%{_libdir}/cmake/bson-%{version}
%{_libdir}/pkgconfig/bson2.pc
%if %{with manpages}
%{_mandir}/man3/bson*
%{_mandir}/man3/libbson*
%endif


%changelog
%autochangelog

