%global source0_hash 6abd7ab0a7f1580d5914457cb3c85eb80455657ee5119206edbd7f848c14f0b2

%global with_http3 0
%global with_mingw 0

%if 0%{?fedora} >= 43
# Enable HTTP/3 support in nghttpx and h2load
%global with_http3 1
%endif

%if 0%{?fedora}
%global with_mingw 1
%endif

Summary: Experimental HTTP/2 client, server and proxy
Name: nghttp2
Version: 1.68.1
Release: 1%{?dist}

# Parts of ruby bindings are additionally under GPL-2.0-or-later, MIT and
# HPND-Kevlin-Henney but they are NOT shipped.
License: MIT

URL: https://nghttp2.org/
Source0:        https://github.com/tatsuhiro-t/nghttp2/releases/download/v1.68.1/nghttp2-1.68.1.tar.xz
Source1:        https://github.com/nghttp2/nghttp2/releases/download/v1.68.1/nghttp2-1.68.1.tar.xz.asc
Source2: tatsuhiro-t.pgp

BuildRequires: CUnit-devel
BuildRequires: c-ares-devel
BuildRequires: gcc-c++
BuildRequires: libev-devel
BuildRequires: libxml2-devel
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: python3-devel
BuildRequires: systemd-rpm-macros
BuildRequires: zlib-devel

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
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

# not needed on Fedora/RHEL
rm -f "$RPM_BUILD_ROOT%{_libdir}/libnghttp2.la"

# will be installed via %%doc
rm -f "$RPM_BUILD_ROOT%{_datadir}/doc/nghttp2/README.rst"

%ldconfig_scriptlets -n libnghttp2

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


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.68.0-3
- Prepare for Oreon 11 (RP1)
