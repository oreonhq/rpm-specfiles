%bcond optional_tests %{undefined rhel}

Name:		librdkafka
Version:	2.12.1
Release:	2%{?dist}
Summary:	The Apache Kafka C library

License:	Apache-2.0
URL:		https://github.com/edenhill/librdkafka
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	python3
BuildRequires:	libzstd-devel
BuildRequires:	lz4-devel
BuildRequires:	openssl-devel
BuildRequires:	cyrus-sasl-devel
BuildRequires:	zlib-devel
%if %{with optional_tests}
BuildRequires:	rapidjson-devel
%endif

Patch1: disable-ssl-engine.patch
Patch2: include-ossl-rand.patch

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
%autosetup -p1

%build
# This package has a configure test which uses ASMs, but does not link the
# resultant .o files.  As such the ASM test is always successful, even on
# architectures were the ASM is not valid when compiling with LTO.
#
# -ffat-lto-objects is sufficient to address this issue.  It is the default
# for F33, but is expected to only be enabled for packages that need it in
# F34, so we use it here explicitly
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

%files
%{_libdir}/librdkafka.so.*
%{_libdir}/librdkafka++.so.*
%doc README.md CONFIGURATION.md INTRODUCTION.md LICENSE LICENSES.txt STATISTICS.md CHANGELOG.md
%license LICENSE LICENSE.pycrc LICENSE.snappy

%files devel
%dir %{_includedir}/librdkafka
%{_includedir}/librdkafka/*
%{_libdir}/librdkafka.so
%{_libdir}/librdkafka++.so
%{_libdir}/pkgconfig/rdkafka.pc
%{_libdir}/pkgconfig/rdkafka++.pc


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.12.1-2
- Prepare for Oreon 11 (RP1)
