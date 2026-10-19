%global source0_hash b6ade658f4af3a823d0dc806ae5ef0623f0f4f5e2aeb895a0f77c4783840c30e
%bcond_without libuv
Name:           libwebsockets
Version:        4.5.8
Release:        1%{?dist}
Summary:        Lightweight C library for Websockets
License:        LicenseRef-Callaway-LGPLv2 AND LicenseRef-Callaway-Public-Domain AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT AND Zlib
URL:            http://libwebsockets.org
Source0:        https://github.com/warmcat/libwebsockets/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{with libuv}
%endif
Provides:       bundled(sha1-hollerbach)
Provides:       bundled(base64-decode)
Provides:       bundled(ssl-http2)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-g++
BuildRequires:  glib2-devel
BuildRequires:  libev-devel
BuildRequires:  libuv-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
This is the libwebsockets C library for lightweight websocket clients and
servers.

%package devel
Summary:        Headers for developing programs that will use %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if %{with libuv}
Requires:       libuv-devel
%endif
Requires:       libev-devel
Requires:       openssl-devel
%description devel
This package contains the header files needed for developing
%{name} applications.

%prep
%oreon_prep
%build

CFLAGS="$RPM_OPT_FLAGS -Wno-discarded-qualifiers"
%cmake \
    -D LWS_WITH_HTTP2=ON \
    -D LWS_IPV6=ON \
    -D LWS_WITH_ZIP_FOPS=ON \
    -D LWS_WITH_SOCKS5=ON \
    -D LWS_WITH_RANGES=ON \
    -D LWS_WITH_ACME=ON \
    -D LWS_WITH_GLIB=ON \
%if %{with libuv}
    -D LWS_WITH_LIBUV=ON \
%endif
    -D LWS_BUILD_HASH=no_hash \
    -D LWS_LINK_TESTAPPS_DYNAMIC=ON \
    -D LWS_UNIX_SOCK=ON \
    -D LWS_USE_BUNDLED_ZLIB=OFF \
    -D LWS_WITH_DISKCACHE=ON \
    -D LWS_WITH_EXTERNAL_POLL=ON \
    -D LWS_WITH_FTS=ON \
    -D LWS_WITH_HTTP_PROXY=ON \
    -D LWS_WITH_LIBEV=ON \
    -D LWS_WITH_LIBEVENT=OFF \
    -D LWS_WITH_LWSAC=ON \
    -D LWS_WITH_STATIC=OFF \
    -D LWS_WITH_THREADPOOL=ON \
    -D LWS_WITHOUT_BUILTIN_GETIFADDRS=ON \
    -D LWS_WITHOUT_BUILTIN_SHA1=ON \
    -D LWS_WITHOUT_CLIENT=OFF \
    -D LWS_WITHOUT_SERVER=OFF \
    -D LWS_WITHOUT_TEST_CLIENT=ON \
    -D LWS_WITHOUT_TEST_PING=ON \
    -D LWS_WITHOUT_TEST_SERVER_EXTPOLL=ON \
    -D LWS_WITHOUT_TEST_SERVER=ON \
    -D LWS_WITHOUT_TESTAPPS=ON \
    %nil
%cmake_build
%install
%cmake_install
find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete
find %{buildroot} -name '*_static.pc' -delete
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libwebsockets-devel -f %{oreon_filedir}/libwebsockets-devel.list

%changelog

%autochangelog
