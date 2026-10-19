%global source1_hash 9672b3b53faf734ec5c0198d5d349bc6a30ecb119c02f48d2947b5082682546a
%global source0_hash e05cb1388eaca3830aded4ccf20044b6e1ac1a61411dcca11b0437c4285c8bc2
%global with_http3 0
%global with_mingw 0
Summary:        Experimental HTTP/2 client, server and proxy
Name: nghttp2
Version: 1.70.0
Release:        1%{?dist}
License: MIT
URL: https://nghttp2.org/
Source0:        https://github.com/tatsuhiro-t/nghttp2/releases/download/v%{version}/nghttp2-%{version}.tar.xz
Source1:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2: tatsuhiro-t.pgp
Requires: libnghttp2%{?_isa} = %{version}-%{release}
%{?systemd_requires}
# oreon:deps
BuildRequires:  CUnit-devel
BuildRequires:  c-ares-devel
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  libev-devel
BuildRequires:  libnghttp3-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-c-ares
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw32-openssl
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-c-ares
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw64-openssl
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-zlib
BuildRequires:  ngtcp2-crypto-ossl-devel
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
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

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
    --enable-http3                          \
    --with-libxml2
sed -i libtool                              \
    -e 's/^runpath_var=.*/runpath_var=/'    \
    -e 's/^hardcode_libdir_flag_spec=".*"$/hardcode_libdir_flag_spec=""/'
%make_build
popd
%mingw_configure --disable-hpack-tools --disable-static
%mingw_make_build
%install
pushd build
%make_install
install -D -m0444 -p contrib/nghttpx.service \
    "$RPM_BUILD_ROOT%{_unitdir}/nghttpx.service"
popd
rm -f "$RPM_BUILD_ROOT%{_libdir}/libnghttp2.la"
rm -f "$RPM_BUILD_ROOT%{_datadir}/doc/nghttp2/README.rst"
%ldconfig_scriptlets -n libnghttp2
%mingw_make_install
%mingw_debug_install_post
rm -f "${buildroot}%{mingw32_libdir}/libnghttp2.la"
rm -f "${buildroot}%{mingw64_libdir}/libnghttp2.la"
rm -f "%{buildroot}%{mingw32_datadir}/doc/nghttp2/README.rst"
rm -f "%{buildroot}%{mingw64_datadir}/doc/nghttp2/README.rst"
rm -r "%{buildroot}%{mingw32_mandir}/man1"
rm -r "%{buildroot}%{mingw64_mandir}/man1"
%oreon_autofiles libnghttp2 usr/*/lib*.so.*
%oreon_autofiles libnghttp2-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles mingw32-libnghttp2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libnghttp2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post nghttpx.service
%postun

%systemd_postun nghttpx.service
%check

export "LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}:$LD_LIBRARY_PATH"
pushd build
%make_build check
popd
%files -f %{oreon_filedir}/main.list
%files -n libnghttp2 -f %{oreon_filedir}/libnghttp2.list
%files -n libnghttp2-devel -f %{oreon_filedir}/libnghttp2-devel.list
%files -n mingw32-libnghttp2 -f %{oreon_filedir}/mingw32-libnghttp2.list
%files -n mingw64-libnghttp2 -f %{oreon_filedir}/mingw64-libnghttp2.list

%changelog

%autochangelog
