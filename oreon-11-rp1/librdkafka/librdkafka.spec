%global source0_hash 23c8575c7d1ced07246cb9cf200c11325b72201fd4134a02414ca869fbdd8ed3
%bcond optional_tests %{undefined rhel}
Name:		librdkafka
Version:	2.15.1
Release:        1%{?dist}
Summary:        The Apache Kafka C library
License:	Apache-2.0
URL:		https://github.com/edenhill/librdkafka
Source0:        https://github.com/edenhill/librdkafka/archive/refs/tags/v2.15.1.tar.gz#/librdkafka-2.15.1.tar.gz
%if %{with optional_tests}
%endif
Patch1: disable-ssl-engine.patch
Patch2: include-ossl-rand.patch
# oreon:deps
BuildRequires:  cyrus-sasl-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  python3
BuildRequires:  rapidjson-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Librdkafka is a C/C++ library implementation of the Apache Kafka protocol,
containing both Producer and Consumer support.
It was designed with message delivery reliability and high performance in mind,
current figures exceed 800000 messages/second for the producer and 3 million
messages/second for the consumer.

%package	devel
Summary:	The Apache Kafka C library (Development Environment)
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	devel
librdkafka is a C/C++ library implementation of the Apache Kafka protocol,
containing both Producer and Consumer support.
This package contains headers and libraries required to build applications
using librdkafka.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%define _lto_cflags -flto=auto -ffat-lto-objects
%configure \
    --enable-zlib \
    --enable-zstd \
    --enable-lz4 \
    --enable-lz4-ext \
    --enable-ssl \
    --enable-gssapi \
    --enable-sasl \
    --disable-ssl-engine
%make_build
%check

make check
%install
%make_install
find %{buildroot} -name '*.a' -delete -print
find %{buildroot} -name '*-static.pc' -delete -print
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n librdkafka-devel -f %{oreon_filedir}/librdkafka-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.12.1-2
- Prepare for Oreon 11 (RP1)
