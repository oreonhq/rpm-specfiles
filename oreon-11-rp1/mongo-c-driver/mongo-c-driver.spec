%global source0_hash a3fc6ebf73e7a26482a5c0f86e4011e4c1f1d8f5bd16ca9ae7c732a8e6965490
%global gh_owner     mongodb
%global gh_project   mongo-c-driver
%global libname      libmongoc
%global soname       2
%global up_version   2.3.1
%bcond_with          tests
%bcond_without       manpages
%bcond_without       libmongocrypt
%bcond_without       libutf8proc
Name:      mongo-c-driver
Summary:        Client library written in C for MongoDB
Version:   %{up_version}%{?up_prever:~%{up_prever}}
Release:        1%{?dist}
License:   Apache-2.0 AND ISC AND MIT AND Zlib
URL:       https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{name}/archive/refs/tags/%{version}.tar.gz
%if %{with libutf8proc}
%endif
%if %{with tests}
%endif
%if %{with libmongocrypt}
%endif
%if %{with manpages}
%endif
Requires:   %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:  %{name}-tools         < 1.3.0
Provides:   %{name}-tools         = %{version}
Provides:   %{name}-tools%{?_isa} = %{version}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(mongocrypt)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  mongodb-server
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(snappy)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3
BuildRequires:  python3-sphinx
# /oreon:deps
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
%oreon_autofiles libbson usr/*/lib*.so.*
%oreon_autofiles libbson-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

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
make check || ret=1
: Cleanup
[ -s server.pid ] && kill $(cat server.pid)
%endif
exit $ret
%files -f %{oreon_filedir}/main.list
%files -n mongo-c-driver-libs -f %{oreon_filedir}/mongo-c-driver-libs.list
%files -n mongo-c-driver-devel -f %{oreon_filedir}/mongo-c-driver-devel.list
%files -n libbson -f %{oreon_filedir}/libbson.list
%files -n libbson-devel -f %{oreon_filedir}/libbson-devel.list

%changelog

%autochangelog

