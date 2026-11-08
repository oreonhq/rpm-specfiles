# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1fb324b6ec2c56f6bde0658f4139ffd8209fa9e77ce98fd7a5f63af8d0e508ad

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global with_http3 0
%global with_mingw 0

# Enable HTTP/3 support in nghttpx and h2load
%global with_http3 1

%global with_mingw 1

Summary: Experimental HTTP/2 client, server and proxy
Name: nghttp2
Version:        1.69.0
Release:        1%{?dist}

# Parts of ruby bindings are additionally under GPL-2.0-or-later, MIT and
# HPND-Kevlin-Henney but they are NOT shipped.
License: MIT

URL: https://nghttp2.org/
Source0:        https://github.com/tatsuhiro-t/nghttp2/releases/download/v%{version}/nghttp2-%{version}.tar.xz
Source1:        nghttp2-1.69.0.tar.xz.asc
Source2: tatsuhiro-t.pgp

# fix HTTP Request/Response Smuggling and Response-Queue Poisoning via ambiguous HTTP/1.1 Upgrade requests (CVE-2026-58055)
Patch001:        0001-nghttp2-1.69.0-CVE-2026-58055.patch

BuildRequires: CUnit-devel
BuildRequires: c-ares-devel
BuildRequires: gcc-c++
BuildRequires: libev-devel
BuildRequires: libxml2-devel
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: python3-devel
BuildRequires: systemd-rpm-macros
BuildRequires: systemd-devel
BuildRequires: zlib-devel
BuildRequires: oreon-rpm-macros

# For gpg verification of source tarball
BuildRequires: gnupg2

Requires: libnghttp2%{?_isa} = %{version}-%{release}
%{?systemd_requires}

%if %{with_http3}
BuildRequires: libnghttp3-devel
BuildRequires: ngtcp2-crypto-ossl-devel
%endif

%if %{with_mingw}
BuildRequires: mingw32-filesystem >= 107
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-binutils
BuildRequires: mingw32-c-ares
BuildRequires: mingw32-libxml2
BuildRequires: mingw32-openssl
BuildRequires: mingw32-python3
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem >= 107
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-binutils
BuildRequires: mingw64-c-ares
BuildRequires: mingw64-libxml2
BuildRequires: mingw64-openssl
BuildRequires: mingw64-python3
BuildRequires: mingw64-zlib
%endif

%description
This package contains the HTTP/2 client, server and proxy programs.


%package -n libnghttp2
Summary: A library implementing the HTTP/2 protocol

%description -n libnghttp2
libnghttp2 is a library implementing the Hypertext Transfer Protocol
version 2 (HTTP/2) protocol in C.


%package -n libnghttp2-devel
Summary: Files needed for building applications with libnghttp2
Requires: libnghttp2%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description -n libnghttp2-devel
The libnghttp2-devel package includes libraries and header files needed
for building applications with libnghttp2.

%if %{with_mingw}
%package -n mingw32-libnghttp2
Summary: A library implementing the HTTP/2 protocol

%description -n mingw32-libnghttp2
libnghttp2 is a library implementing the Hypertext Transfer Protocol
version 2 (HTTP/2) protocol in C.

This is the MinGW cross-compiled Windows library.

%package -n mingw64-libnghttp2
Summary: A library implementing the HTTP/2 protocol

%description -n mingw64-libnghttp2
libnghttp2 is a library implementing the Hypertext Transfer Protocol
version 2 (HTTP/2) protocol in C.

This is the MinGW cross-compiled Windows library.

%{?mingw_debug_package}
%endif

%prep
%oreon_sha256

%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1

%build
mkdir build
pushd build
%define _configure ../configure
%configure PYTHON=%{__python3}              \
    --disable-hpack-tools                   \
    --disable-python-bindings               \
    --disable-static                        \
%if %{with_http3}
    --enable-http3                          \
%endif
    --with-libxml2

# avoid using rpath
sed -i libtool                              \
    -e 's/^runpath_var=.*/runpath_var=/'    \
    -e 's/^hardcode_libdir_flag_spec=".*"$/hardcode_libdir_flag_spec=""/'

%make_build
popd

%if %{with_mingw}
%mingw_configure --disable-hpack-tools --disable-static
%mingw_make_build
%endif


%install
pushd build
%make_install
install -D -m0444 -p contrib/nghttpx.service \
    "$RPM_BUILD_ROOT%{_unitdir}/nghttpx.service"
popd
install -D -m0644 -p nghttpx.conf.sample \
    "$RPM_BUILD_ROOT%{_sysconfdir}/nghttpx/nghttpx.conf"

rm -f "$RPM_BUILD_ROOT%{_libdir}/libnghttp2.la"

# will be installed via %%doc
rm -f "$RPM_BUILD_ROOT%{_datadir}/doc/nghttp2/README.rst"

%if %{with_mingw}
%mingw_make_install
%mingw_debug_install_post

rm -f "${buildroot}%{mingw32_libdir}/libnghttp2.la"
rm -f "${buildroot}%{mingw64_libdir}/libnghttp2.la"
rm -f "%{buildroot}%{mingw32_datadir}/doc/nghttp2/README.rst"
rm -f "%{buildroot}%{mingw64_datadir}/doc/nghttp2/README.rst"
rm -r "%{buildroot}%{mingw32_mandir}/man1"
rm -r "%{buildroot}%{mingw64_mandir}/man1"
%endif

%ldconfig_scriptlets -n libnghttp2

%post
%systemd_post nghttpx.service

%postun
%systemd_postun nghttpx.service


%check
# test the just built library instead of the system one, without using rpath
export "LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}:$LD_LIBRARY_PATH"
pushd build
%make_build check
popd

%files
%{_bindir}/h2load
%{_bindir}/nghttp
%{_bindir}/nghttpd
%{_bindir}/nghttpx
%{_mandir}/man1/h2load.1*
%{_mandir}/man1/nghttp.1*
%{_mandir}/man1/nghttpd.1*
%{_mandir}/man1/nghttpx.1*
%{_unitdir}/nghttpx.service
%dir %{_sysconfdir}/nghttpx
%config(noreplace) %{_sysconfdir}/nghttpx/nghttpx.conf

%files -n libnghttp2
%{_libdir}/libnghttp2.so.*
%{!?_licensedir:%global license %%doc}
%license COPYING

%files -n libnghttp2-devel
%{_includedir}/nghttp2
%{_libdir}/pkgconfig/libnghttp2.pc
%{_libdir}/libnghttp2.so
%doc README.rst

%if %{with_mingw}
%files -n mingw32-libnghttp2
%license COPYING
%doc README.rst
%{mingw32_bindir}/libnghttp2-14.dll
%{mingw32_libdir}/libnghttp2.dll.a
%{mingw32_libdir}/pkgconfig/libnghttp2.pc
%{mingw32_includedir}/nghttp2/

%files -n mingw64-libnghttp2
%license COPYING
%doc README.rst
%{mingw64_bindir}/libnghttp2-14.dll
%{mingw64_libdir}/libnghttp2.dll.a
%{mingw64_libdir}/pkgconfig/libnghttp2.pc
%{mingw64_includedir}/nghttp2/
%endif


